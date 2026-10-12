using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
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
            SwDMClassFactory factory = new SwDMClassFactory();
            ISwDMApplication application = factory.GetApplication(licenseKey);
            int failures = 0;
            using (StreamWriter csv = new StreamWriter(args[1], false, new UTF8Encoding(true)))
            {
                csv.WriteLine(CsvLine(new[] { "File", "Configuration" }.Concat(PropertyNames)));
                foreach (string path in Directory.EnumerateFiles(args[0], "*.*", SearchOption.AllDirectories))
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
                csv.WriteLine(CsvLine(new[] { path, "" }.Concat(PropertyNames.Select(name => DocumentProperty(document, name)))));
                if (type == SwDmDocumentType.swDmDocumentDrawing)
                {
                    return true;
                }
                ISwDMConfigurationMgr2 configurations = (ISwDMConfigurationMgr2)document.ConfigurationManager;
                SwDMConfigurationError configError;
                object[] names = configurations.GetConfigurationNames2(out configError) as object[];
                if (configError != SwDMConfigurationError.SwDMConfigurationError_None || names == null)
                {
                    Console.Error.WriteLine(path + ": " + configError);
                    return false;
                }
                foreach (string configName in names.Cast<string>())
                {
                    ISwDMConfiguration configuration = configurations.GetConfigurationByName2(configName, out configError);
                    if (configuration == null)
                    {
                        Console.Error.WriteLine(path + " [" + configName + "]: " + configError);
                        continue;
                    }
                    csv.WriteLine(CsvLine(new[] { path, configName }.Concat(PropertyNames.Select(name => ConfigurationProperty(configuration, name)))));
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
        private static string DocumentProperty(ISwDMDocument document, string name)
        {
            string stored = StoredName(document.GetCustomPropertyNames(), name);
            if (stored == null)
            {
                return "";
            }
            SwDmCustomInfoType type;
            return ((ISwDMDocument17)document).GetCustomProperty2(stored, out type);
        }
        private static string ConfigurationProperty(ISwDMConfiguration configuration, string name)
        {
            string stored = StoredName(configuration.GetCustomPropertyNames(), name);
            if (stored == null)
            {
                return "";
            }
            SwDmCustomInfoType type;
            return ((ISwDMConfiguration14)configuration).GetCustomProperty2(stored, out type);
        }
        private static string StoredName(object names, string wanted)
        {
            object[] array = names as object[];
            return array == null ? null : array.Cast<string>().FirstOrDefault(name => string.Equals(name, wanted, StringComparison.OrdinalIgnoreCase));
        }
        private static string CsvLine(IEnumerable<string> fields)
        {
            return string.Join(",", fields.Select(field => "\"" + (field ?? "").Replace("\"", "\"\"") + "\""));
        }
    }
}
