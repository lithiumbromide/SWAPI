using System;
using System.Collections.Generic;
using System.IO;
using System.Runtime.InteropServices;
using DraftSight.Interop.dsAutomation;
namespace DraftSightTool
{
    internal static class Program
    {
        [STAThread]
        private static int Main(string[] args)
        {
            if (args.Length != 2 || !Directory.Exists(args[0]))
            {
                Console.Error.WriteLine("usage: DraftSightTool <folder with DWG files> <output folder>");
                return 2;
            }
            Application dsApp = Connect();
            if (dsApp == null)
            {
                Console.Error.WriteLine("Start DraftSight first; this tool attaches to the running instance.");
                return 3;
            }
            Directory.CreateDirectory(args[1]);
            int failures = 0;
            int done = 0;
            try
            {
                dsApp.AbortRunningCommand();
                foreach (string path in Directory.GetFiles(args[0], "*.dwg"))
                {
                    string pdf = Path.Combine(args[1], Path.GetFileNameWithoutExtension(path) + ".pdf");
                    if (ProcessFile(dsApp, Path.GetFullPath(path), pdf))
                    {
                        done++;
                    }
                    else
                    {
                        failures++;
                    }
                }
            }
            finally
            {
                Marshal.ReleaseComObject(dsApp);
            }
            Console.WriteLine("exported " + done + ", failed " + failures);
            return failures == 0 ? 0 : 1;
        }
        private static Application Connect()
        {
            try
            {
                return (Application)Marshal.GetActiveObject("DraftSight.Application");
            }
            catch (COMException)
            {
                return null;
            }
        }
        private static bool ProcessFile(Application dsApp, string path, string pdf)
        {
            Document dsDoc = FindOpen(dsApp, path);
            bool openedHere = dsDoc == null;
            if (openedHere)
            {
                dsDoc = dsApp.OpenDocument2(path, dsDocumentOpenOption_e.dsDocumentOpen_ReadOnly, dsEncoding_e.dsEncoding_Default);
                if (dsDoc == null)
                {
                    Console.Error.WriteLine("could not open " + path);
                    return false;
                }
            }
            else
            {
                dsDoc.Activate();
            }
            try
            {
                Console.WriteLine(path + ": " + CountModelEntities(dsDoc) + " model-space entities");
                return ExportPdf(dsDoc, pdf);
            }
            catch (COMException ex)
            {
                Console.Error.WriteLine(path + ": " + ex.Message);
                return false;
            }
            finally
            {
                if (openedHere)
                {
                    dsApp.CloseDocument(dsDoc.GetPathName(), false);
                }
                Marshal.ReleaseComObject(dsDoc);
            }
        }
        private static Document FindOpen(Application dsApp, string path)
        {
            object[] docs = dsApp.GetDocuments() as object[];
            if (docs == null)
            {
                return null;
            }
            foreach (object item in docs)
            {
                Document doc = item as Document;
                if (doc != null && string.Equals(doc.GetPathName(), path, StringComparison.OrdinalIgnoreCase))
                {
                    return doc;
                }
            }
            return null;
        }
        private static int CountModelEntities(Document dsDoc)
        {
            SketchManager sketch = dsDoc.GetModel().GetSketchManager();
            object types;
            object entities;
            sketch.GetEntities(null, LayerNames(dsDoc), out types, out entities);
            object[] list = entities as object[];
            return list == null ? 0 : list.Length;
        }
        private static string[] LayerNames(Document dsDoc)
        {
            List<string> names = new List<string>();
            object[] layers = dsDoc.GetLayerManager().GetLayers() as object[];
            if (layers != null)
            {
                foreach (object item in layers)
                {
                    Layer layer = item as Layer;
                    if (layer != null)
                    {
                        names.Add(layer.Name);
                    }
                }
            }
            return names.ToArray();
        }
        private static bool ExportPdf(Document dsDoc, string pdf)
        {
            List<string> sheetNames = new List<string>();
            object[] sheets = dsDoc.GetSheets2() as object[];
            if (sheets != null)
            {
                foreach (object item in sheets)
                {
                    Sheet sheet = item as Sheet;
                    if (sheet != null)
                    {
                        sheetNames.Add(sheet.Name);
                    }
                }
            }
            DocumentExporter exporter = dsDoc.GetDocumentExporter();
            ExportSettings settings = exporter.CreateExportSettings();
            if (sheetNames.Count > 0)
            {
                settings.Sheets = sheetNames.ToArray();
            }
            bool ok = exporter.ExportToPdf2(pdf, settings);
            Console.WriteLine((ok ? "wrote " : "export failed: ") + pdf);
            return ok;
        }
    }
}
