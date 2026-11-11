---
title: "Save Current View to PDF Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Save_Current_View_to_PDF_Example_CSharp.htm"
---

# Save Current View to PDF Example (C#)

This example shows how to export the current view of the drawing to a PDF file.

```vb
  //-------------------------------------------------------------
 // Preconditions:
 // 1. Create a C# Windows console project.
 // 2. Copy and paste this project into the C# IDE.
 // 3. Add a reference to:
 //    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
 // 4. Open the Immediate window.
 // 5. Start DraftSight.
 // 6. Open c:\ProgramData\Dassault Systemes\DraftSight\Examples\B-44563.DWG.
 // 7. Click Start Debugging.
 //
 // Postconditions:
 // 1. Specified document is opened.
  // 3. The current view of the drawing is exported to a PDF file.
  //------------------------------------------------------------

 using System.IO;
 using DraftSight.Interop.dsAutomation;
 using System.Diagnostics;
 using System.Runtime.InteropServices;

 namespace ExportToPDF_CSharp
 {
     static class Program
     {

         public static void Main()
         {
             DraftSight.Interop.dsAutomation.Application dsApp;
             //Connect to DraftSight application
             dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");
             //Abort any command currently running in DraftSight
             //to avoid nested commands
             dsApp.AbortRunningCommand();

             //OGet active document document
             Document dsDoc = default(Document);
             string docName = null;
             //docName = "C:\\ProgramData\\Dassault Systemes\\DraftSight\\Examples\\B-44563.DWG";
             //dsDoc = dsApp.OpenDocument2(docName, dsDocumentOpenOption_e.dsDocumentOpen_Default, dsEncoding_e.dsEncoding_Default);
            dsDoc = dsApp.GetActiveDocument();
             if (dsDoc == null)
             {
                 Debug.Print("Specified document did not open. Check path and file name.");
                 return;
             }

             //Export current view of drawing to a PDF
             DocumentExporter dsExportDocument = default(DocumentExporter);
             string exportFileName = null;
             ExportSettings ExportSettings = default(ExportSettings);
             bool status = false;
             dsExportDocument = dsDoc.GetDocumentExporter();
             ExportSettings = dsExportDocument.CreateExportSettings();

            //Export all sheets
            object[] sheetsList = (object[])dsDoc.GetSheets2();
            string[] sheetArray = new string[sheetsList.Length];
            int j = 0;
            for (int i = 0; i < sheetsList.Length; i++)
            {
                Sheet sheet = (Sheet)sheetsList[i];
                sheetArray[j] = sheet.Name;
                j++;
            }

             ExportSettings.Sheets = sheetArray;
             ExportSettings.SetPrintMargins(30, 30, 30, 30);
             ExportSettings.PrintStyleTable = "monochrome.ctb";
             ExportSettings.EnableCustomBitmapResolution = true;
             ExportSettings.CustomBitmapResolution = 151;
             ExportSettings.EnableLayersInPDFFile = true;
             ExportSettings.TrueTypeFontsType = dsTrueTypeFontsType_e.dsTrueTypeFontsType_Embedded;

             object paperSizes = null;
            string[] paperSizeArray = new string[1];
             ExportSettings.GetAvailablePaperSizes(out paperSizes);
            paperSizeArray = (string[])paperSizes;
            ExportSettings.PaperSize = paperSizeArray[0];
             double top = 0;
             double bottom = 0;
             double left = 0;
             double right = 0;
             ExportSettings.GetPrintMargins(out top, out bottom, out left, out right);
             Debug.Print("Enable custom bitmap resolution? " + ExportSettings.EnableCustomBitmapResolution);
             Debug.Print("  Custom bitmap resolution: " + ExportSettings.CustomBitmapResolution);
             Debug.Print("Enable Layers in PDF file? " + ExportSettings.EnableLayersInPDFFile);
             Debug.Print("PrintStyle table: " + ExportSettings.PrintStyleTable);
             Debug.Print("TrueType font as defined in dsTrueTypeFontsType_e: " + ExportSettings.TrueTypeFontsType);

             exportFileName = "C:\\temp\\B-44563.PDF";
             status = dsExportDocument.ExportToPdf2(exportFileName, ExportSettings);
             Debug.Print("");
             if (status)
             {
                 Debug.Print("Drawing exported as " + exportFileName + ".");
             }
             else
             {
                 Debug.Print("Export of drawing to PDF failed!");
             }
         }

     }
 }
```
