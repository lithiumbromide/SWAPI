---
title: "Get DimensionStyle Names and Options Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Get_DimensionStyle_Names_and_Options_Example_CSharp.htm"
---

# Get DimensionStyle Names and Options Example (C#)

This example shows how to get the names and options of the DimensionStyles in a document and how to export the current view of the drawing to a PNG file.

```vb
  //-------------------------------------------------------------
 // Preconditions:
 // 1. Create a C# Windows console project.
 // 2. Copy and paste this project into the C# IDE.
 // 3. Add a reference to:
 //    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
 // 4. Open the Immediate window.
 // 5. Start DraftSight.
 // 6. Click Start Debugging.
 //
 // Postconditions:
 // 1. Specified document is opened.
  // 2. The document's DimensionStyle names and options are printed to
 //    the Immediate window.
  // 3. The current view of the drawing is exported to a PNG file.
 // 4. To verify step 3, open
 //    C:\ProgramData\Dassault Systemes\DraftSight\Examples\B-44563.PNG
 //    using an application like Microsoft Paint.
  //------------------------------------------------------------

 using System.IO;
 using DraftSight.Interop.dsAutomation;
 using System.Diagnostics;
 using System.Runtime.InteropServices;

 namespace GetDimensionStylesCSharp
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

 //Open document
 Document dsDoc = default(Document);
 string docName = null;
 docName = "C:\\ProgramData\\Dassault Systemes\\DraftSight\\Examples\\B-44563.DWG";
 dsDoc = dsApp.OpenDocument2(docName, dsDocumentOpenOption_e.dsDocumentOpen_Default, dsEncoding_e.dsEncoding_Default);
 if (dsDoc == null) {
 Debug.Print("Specified document did not open. Check path and file name.");
 return;
 }

 //Get DimensionStyle manager
 DimensionStyleManager dsDimStyleManager = default(DimensionStyleManager);
 dsDimStyleManager = dsDoc.GetDimensionStyleManager();

  //Get DimensionStyles and options for document
 object[] dsDimensionStyles = null;
 dsDimensionStyles = dsDimStyleManager.GetDimensionStyles();
 long index = 0;
 if (dsDimensionStyles != null)
                 {
 for (index = 0; index <= dsDimensionStyles.Length - 1; index++)
                         {
 DimensionStyle dsDimensionStyle = default(DimensionStyle);
 dsDimensionStyle = (DimensionStyle)dsDimensionStyles[index];
 Debug.Print("");
                                 Debug.Print("Name of DimensionStyle: " + dsDimensionStyle.Name);
                                 //Print DimensionStyle's options
 PrintDimensionStyleOptions(dsDimensionStyle);
 }
 }

 //Export current view of drawing to PNG
 DocumentExporter dsExportDocument = default(DocumentExporter);
 string exportFileName = null;
 bool status = false;
 dsExportDocument = dsDoc.GetDocumentExporter();
 exportFileName = "C:\\ProgramData\\Dassault Systemes\\DraftSight\\Examples\\B-44563.PNG";
 dsExportDocument.ExportToPng(exportFileName, out status);
 Debug.Print("");
 if (status) {
 Debug.Print("Drawing exported as " + exportFileName + ".");
 } else {
 Debug.Print("Export of drawing to PNG failed!");
 }
 }

         public static void PrintDimensionStyleOptions(DimensionStyle dsDimensionStyle)
         {
             //Angular DimensionStyle options
             DimensionStyleAngularDimensionOptions dsDimensionStyleAngularDimensionOptions = default(DimensionStyleAngularDimensionOptions);
             dsDimensionStyleAngularDimensionOptions = dsDimensionStyle.GetDimensionStyleAngularDimensionOptions();
             Debug.Print("  Angular DimensionStyle options:  ");
             Debug.Print("    Precision: " + dsDimensionStyleAngularDimensionOptions.Precision);
             Debug.Print("    Format: " + dsDimensionStyleAngularDimensionOptions.Format);
             Debug.Print("    Hide leading zeroes: " + dsDimensionStyleAngularDimensionOptions.HideLeadingZeroes);
             Debug.Print("    Hide trailing zeroes: " + dsDimensionStyleAngularDimensionOptions.HideTrailingZeroes);

             //Dual DimensionStyle options
             DimensionStyleDualDimensionOptions dsDimensionStyleDualDimensionOptions = default(DimensionStyleDualDimensionOptions);
             dsDimensionStyleDualDimensionOptions = dsDimensionStyle.GetDimensionStyleDualDimensionOptions();
             Debug.Print("  Dual DimensionStyle options:  ");
             Debug.Print("    Precision: " + dsDimensionStyleDualDimensionOptions.Precision);
             Debug.Print("    Format: " + dsDimensionStyleDualDimensionOptions.Format);
             Debug.Print("    Hide leading zeroes: " + dsDimensionStyleDualDimensionOptions.HideLeadingZeroes);
             Debug.Print("    Hide trailing zeroes: " + dsDimensionStyleDualDimensionOptions.HideTrailingZeroes);

             //Fit DimensionStyle options
             DimensionStyleFitOptions dsDimensionStyleFitOptions = default(DimensionStyleFitOptions);
             dsDimensionStyleFitOptions = dsDimensionStyle.GetDimensionStyleFitOptions();
             Debug.Print("  Fit DimensionStyle options:  ");
             Debug.Print("    Placement of text: " + dsDimensionStyleFitOptions.FitDimensionText);
             Debug.Print("    Entity to move outside Dimension's extension lines: " + dsDimensionStyleFitOptions.FitGeometry);
             Debug.Print("    Hide arrows: " + dsDimensionStyleFitOptions.HideArrows);
             dsDimensionScale_e dimensionScale = default(dsDimensionScale_e);
             double scaleFactor = 0;
             dsDimensionStyleFitOptions.GetDimensionScale(out dimensionScale, out scaleFactor);
             Debug.Print("    Scale factor: " + scaleFactor);

             //Linear DimensionStyle options
             DimensionStyleLinearDimensionOptions dsDimensionStyleLinearDimensionOptions = default(DimensionStyleLinearDimensionOptions);
             dsDimensionStyleLinearDimensionOptions = dsDimensionStyle.GetDimensionStyleLinearDimensionOptions();
             Debug.Print("  Linear DimensionStyle options:  ");
             Debug.Print("    Precision: " + dsDimensionStyleLinearDimensionOptions.Precision);
             Debug.Print("    Format: " + dsDimensionStyleLinearDimensionOptions.Format);
             Debug.Print("    Hide leading zeroes: " + dsDimensionStyleLinearDimensionOptions.HideLeadingZeroes);
             Debug.Print("    Hide trailing zeroes: " + dsDimensionStyleLinearDimensionOptions.HideTrailingZeroes);

             //Tolerance DimensionStyle options
             DimensionStyleToleranceOptions dsDimensionStyleToleranceOptions = default(DimensionStyleToleranceOptions);
             dsDimensionStyleToleranceOptions = dsDimensionStyle.GetDimensionStyleToleranceOptions();
             Debug.Print("  Tolerance DimensionStyle options:  ");
             Debug.Print("    Precision: " + dsDimensionStyleToleranceOptions.Precision);
             Debug.Print("    Minimum value: " + dsDimensionStyleToleranceOptions.MinimumValue);
             Debug.Print("    Maximum value: " + dsDimensionStyleToleranceOptions.MaximumValue);
             Debug.Print("    Hide leading zeroes: " + dsDimensionStyleToleranceOptions.HideLeadingZeroes);
             Debug.Print("    Hide trailing zeroes: " + dsDimensionStyleToleranceOptions.HideTrailingZeroes);

         }

     }
 }
```
