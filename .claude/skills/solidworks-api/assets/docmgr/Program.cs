using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using SolidWorks.Interop.swdocumentmgr;
namespace DocMgrTool
{
    internal static class Program
    {
        private static readonly string[] PropertyNames = { "Description", "PartNo", "Material" };
        private static int Main(string[] args)
        {
            if (args.Length != 2 || !Directory.Exists(args[0]))
            {
                Console.Error.WriteLine("usage: DocMgrTool <folder> <output.csv>");
                return 2;
            }
            string licenseKey = Environment.GetEnvironmentVariable("SW_DM_LICENSE_KEY");
            if (string.IsNullOrWhiteSpace(licenseKey))
            {
                Console.Error.WriteLine("Set SW_DM_LICENSE_KEY to your SOLIDWORKS Document Manager license key.");
                return 2;
            }
            ISwDMApplication application = Connect(licenseKey);
            if (application == null)
            {
                return 3;
            }
            int failures = 0;
            using (StreamWriter csv = new StreamWriter(args[1], false, new UTF8Encoding(true)))
            {
                csv.WriteLine(CsvLine(new[] { "File", "Configuration" }.Concat(PropertyNames)));
                foreach (string path in EnumerateFiles(args[0], () => failures++))
                {
                    SwDmDocumentType type = DocumentType(path);
                    if (type != SwDmDocumentType.swDmDocumentUnknown && !Export(application, path, type, csv))
                    {
                        failures++;
                    }
                }
            }
            return failures == 0 ? 0 : 1;
        }
        private static ISwDMApplication Connect(string licenseKey)
        {
            try
            {
                SwDMClassFactory factory = new SwDMClassFactory();
                ISwDMApplication application = factory.GetApplication(licenseKey);
                if (application == null)
                {
                    Console.Error.WriteLine("SW_DM_LICENSE_KEY was rejected; request or renew a Document Manager key for this SOLIDWORKS release.");
                }
                return application;
            }
            catch (COMException ex)
            {
                Console.Error.WriteLine("Document Manager is not available or SW_DM_LICENSE_KEY is invalid or expired: " + ex.Message);
                return null;
            }
        }
        private static IEnumerable<string> EnumerateFiles(string root, Action onError)
        {
            Stack<string> pending = new Stack<string>();
            pending.Push(root);
            while (pending.Count > 0)
            {
                string folder = pending.Pop();
                string[] files;
                string[] subfolders;
                try
                {
                    files = Directory.GetFiles(folder);
                    subfolders = Directory.GetDirectories(folder);
                }
                catch (Exception ex) when (ex is IOException || ex is UnauthorizedAccessException)
                {
                    Console.Error.WriteLine(folder + ": " + ex.Message);
                    onError();
                    continue;
                }
                foreach (string subfolder in subfolders)
                {
                    pending.Push(subfolder);
                }
                foreach (string file in files)
                {
                    yield return file;
                }
            }
        }
        private static SwDmDocumentType DocumentType(string path)
        {
            switch (Path.GetExtension(path).ToLowerInvariant())
            {
                case ".sldprt":
                    return SwDmDocumentType.swDmDocumentPart;
                case ".sldasm":
                    return SwDmDocumentType.swDmDocumentAssembly;
                case ".slddrw":
                    return SwDmDocumentType.swDmDocumentDrawing;
                default:
                    return SwDmDocumentType.swDmDocumentUnknown;
            }
        }
        private static bool Export(ISwDMApplication application, string path, SwDmDocumentType type, StreamWriter csv)
        {
            SwDmDocumentOpenError openError;
            ISwDMDocument document = application.GetDocument(path, type, true, out openError);
            if (document == null)
            {
                Console.Error.WriteLine(path + ": " + openError);
                return false;
            }
            if (openError != SwDmDocumentOpenError.swDmDocumentOpenErrorNone)
            {
                Console.Error.WriteLine(path + ": opened with " + openError);
            }
            try
            {
                Dictionary<string, string> fileNames = StoredNames(document.GetCustomPropertyNames());
                csv.WriteLine(CsvLine(new[] { path, "" }.Concat(PropertyNames.Select(name => DocumentProperty(document, fileNames, name)))));
                if (type == SwDmDocumentType.swDmDocumentDrawing)
                {
                    return true;
                }
                ISwDMConfigurationMgr2 configurations = (ISwDMConfigurationMgr2)document.ConfigurationManager;
                SwDMConfigurationError configError;
                object[] configNames = configurations.GetConfigurationNames2(out configError) as object[];
                if (configError != SwDMConfigurationError.SwDMConfigurationError_None || configNames == null)
                {
                    Console.Error.WriteLine(path + ": " + configError);
                    return false;
                }
                foreach (string configName in configNames.Cast<string>())
                {
                    ISwDMConfiguration configuration = configurations.GetConfigurationByName2(configName, out configError);
                    if (configuration == null)
                    {
                        Console.Error.WriteLine(path + " [" + configName + "]: " + configError);
                        continue;
                    }
                    Dictionary<string, string> configPropertyNames = StoredNames(configuration.GetCustomPropertyNames());
                    csv.WriteLine(CsvLine(new[] { path, configName }.Concat(PropertyNames.Select(name => ConfigurationProperty(configuration, configPropertyNames, name)))));
                }
                return true;
            }
            catch (Exception ex)
            {
                Console.Error.WriteLine(path + ": " + ex.Message);
                return false;
            }
            finally
            {
                document.CloseDoc();
            }
        }
        private static Dictionary<string, string> StoredNames(object names)
        {
            Dictionary<string, string> stored = new Dictionary<string, string>(StringComparer.OrdinalIgnoreCase);
            object[] array = names as object[];
            if (array != null)
            {
                foreach (string name in array.Cast<string>())
                {
                    stored[name] = name;
                }
            }
            return stored;
        }
        private static string DocumentProperty(ISwDMDocument document, Dictionary<string, string> storedNames, string name)
        {
            string stored;
            if (!storedNames.TryGetValue(name, out stored))
            {
                return "";
            }
            SwDmCustomInfoType type;
            return ((ISwDMDocument17)document).GetCustomProperty2(stored, out type);
        }
        private static string ConfigurationProperty(ISwDMConfiguration configuration, Dictionary<string, string> storedNames, string name)
        {
            string stored;
            if (!storedNames.TryGetValue(name, out stored))
            {
                return "";
            }
            SwDmCustomInfoType type;
            return ((ISwDMConfiguration14)configuration).GetCustomProperty2(stored, out type);
        }
        private static string CsvLine(IEnumerable<string> fields)
        {
            return string.Join(",", fields.Select(field => "\"" + (field ?? "").Replace("\"", "\"\"") + "\""));
        }
    }
}
