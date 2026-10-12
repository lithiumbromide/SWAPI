using System;
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
            int failures = 0;
            swApp.CommandInProgress = true;
            try
            {
                foreach (string path in Directory.EnumerateFiles(args[0], "*.*", SearchOption.AllDirectories))
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
            try
            {
                started = false;
                return (ISldWorks)Marshal.GetActiveObject("SldWorks.Application");
            }
            catch (COMException)
            {
                started = true;
                ISldWorks app = (ISldWorks)Activator.CreateInstance(Type.GetTypeFromProgID("SldWorks.Application"));
                app.Visible = true;
                return app;
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
            int errors = 0;
            int warnings = 0;
            int options = (int)(swOpenDocOptions_e.swOpenDocOptions_Silent | swOpenDocOptions_e.swOpenDocOptions_ReadOnly);
            ModelDoc2 model = swApp.OpenDoc6(path, type, options, "", ref errors, ref warnings);
            if (model == null)
            {
                Console.Error.WriteLine(path + ": swFileLoadError_e " + (swFileLoadError_e)errors);
                return false;
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
                properties.Get6("Description", false, out value, out resolved, out wasResolved, out linked);
                Console.WriteLine(path + "\t" + resolved);
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
                swApp.CloseDoc(path);
                Marshal.ReleaseComObject(model);
            }
        }
    }
}
