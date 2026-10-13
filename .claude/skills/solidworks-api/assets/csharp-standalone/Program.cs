using System;
using System.Collections.Generic;
using System.IO;
using System.Runtime.InteropServices;
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
namespace SolidWorksTool
{
    internal static class Program
    {
        [STAThread]
        private static int Main(string[] args)
        {
            if (args.Length != 1 || !Directory.Exists(args[0]))
            {
                Console.Error.WriteLine("usage: SolidWorksTool <folder>");
                return 2;
            }
            bool started;
            ISldWorks swApp = Connect(out started);
            if (swApp == null)
            {
                return 3;
            }
            int failures = 0;
            swApp.CommandInProgress = true;
            try
            {
                foreach (string path in EnumerateFiles(args[0], () => failures++))
                {
                    int type = DocumentType(path);
                    if (type != (int)swDocumentTypes_e.swDocNONE && !ProcessFile(swApp, path, type))
                    {
                        failures++;
                    }
                }
            }
            finally
            {
                swApp.CommandInProgress = false;
                if (started)
                {
                    swApp.ExitApp();
                }
                Marshal.ReleaseComObject(swApp);
            }
            return failures == 0 ? 0 : 1;
        }
        private static ISldWorks Connect(out bool started)
        {
            started = false;
            try
            {
                return (ISldWorks)Marshal.GetActiveObject("SldWorks.Application");
            }
            catch (COMException)
            {
            }
            Type type = Type.GetTypeFromProgID("SldWorks.Application");
            if (type == null)
            {
                Console.Error.WriteLine("SOLIDWORKS is not installed or not registered: ProgID SldWorks.Application was not found.");
                return null;
            }
            try
            {
                ISldWorks app = (ISldWorks)Activator.CreateInstance(type);
                started = true;
                app.Visible = true;
                return app;
            }
            catch (COMException ex)
            {
                Console.Error.WriteLine("SOLIDWORKS could not be started: " + ex.Message);
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
        private static int DocumentType(string path)
        {
            switch (Path.GetExtension(path).ToLowerInvariant())
            {
                case ".sldprt":
                    return (int)swDocumentTypes_e.swDocPART;
                case ".sldasm":
                    return (int)swDocumentTypes_e.swDocASSEMBLY;
                case ".slddrw":
                    return (int)swDocumentTypes_e.swDocDRAWING;
                default:
                    return (int)swDocumentTypes_e.swDocNONE;
            }
        }
        private static bool ProcessFile(ISldWorks swApp, string path, int type)
        {
            ModelDoc2 model = swApp.GetOpenDocumentByName(path) as ModelDoc2;
            bool openedHere = model == null;
            if (openedHere)
            {
                int errors = 0;
                int warnings = 0;
                int options = (int)(swOpenDocOptions_e.swOpenDocOptions_Silent | swOpenDocOptions_e.swOpenDocOptions_ReadOnly);
                model = swApp.OpenDoc6(path, type, options, "", ref errors, ref warnings);
                if (model == null)
                {
                    Console.Error.WriteLine(path + ": swFileLoadError_e " + (swFileLoadError_e)errors);
                    return false;
                }
                if ((warnings & (int)swFileLoadWarning_e.swFileLoadWarning_AlreadyOpen) != 0)
                {
                    openedHere = false;
                }
            }
            ModelDocExtension extension = null;
            CustomPropertyManager properties = null;
            try
            {
                extension = model.Extension;
                properties = extension.get_CustomPropertyManager("");
                string value;
                string resolved;
                bool wasResolved;
                bool linked;
                swCustomInfoGetResult_e result = (swCustomInfoGetResult_e)properties.Get6("Description", false, out value, out resolved, out wasResolved, out linked);
                switch (result)
                {
                    case swCustomInfoGetResult_e.swCustomInfoGetResult_NotPresent:
                        Console.WriteLine(path + "\t\tnot present");
                        break;
                    case swCustomInfoGetResult_e.swCustomInfoGetResult_CachedValue:
                        Console.WriteLine(path + "\t" + resolved + "\tcached");
                        break;
                    default:
                        Console.WriteLine(path + "\t" + resolved + "\tresolved");
                        break;
                }
                return true;
            }
            finally
            {
                if (properties != null)
                {
                    Marshal.ReleaseComObject(properties);
                }
                if (extension != null)
                {
                    Marshal.ReleaseComObject(extension);
                }
                if (openedHere)
                {
                    swApp.CloseDoc(path);
                }
                Marshal.ReleaseComObject(model);
            }
        }
    }
}
