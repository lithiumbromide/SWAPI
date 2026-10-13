---
title: "Create Drawing Sheet Zones Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Drawing_Sheet_Zones_Example_CSharp.htm"
---

# Create Drawing Sheet Zones Example (C#)

This example shows how to create a drawing sheet with zones, modify the zones in the drawing sheet, and insert a revision table.

```vb
  //-----------------------------------------------------------------------------
 // Preconditions:
  // 1. Verify that the specified model document and templates exist.
 // 2. Open an Immediate window.
 //
 // Postconditions:
 // 1. Creates a new sheet named Test with four zones.
 // 2. Inspect the graphics area.
 // 3. Press F5.
 // 4. Modifies Test to contain nine zones.
 // 5. Creates Revision Table1.
 // 6. Adds a revision row to the table.
 // 7. Inspect the FeatureManager design tree, the graphics area, and the
 //    Immediate window.
 //
  // NOTE: Because the model is used elsewhere, do not save changes to it.
  //---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace InsertRevisionTable_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         DrawingDoc swDraw;
         Sheet currentsheet;
         ModelDoc2 swModel;
         RevisionTableAnnotation revTableAnno;
         bool boolstatus;
         int longstatus;
         int longwarnings;

         public void Main()
         {
             swModel = swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\assem20.slddrw", 3, 0, "", ref longstatus, ref longwarnings);
             swApp.ActivateDoc2("assem20 - Sheet1", false, ref longstatus);
             swModel = (ModelDoc2)swApp.ActiveDoc;
             swDraw = (DrawingDoc)swModel;

             boolstatus = swModel.Extension.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swShowZoneLines, 0, true);
             boolstatus = swModel.Extension.SetUserPreferenceInteger((int)swUserPreferenceIntegerValue_e.swRevisionTableMultipleSheetStyle, 0, (int)swRevisionTableMultipleSheetStyle_e.swRevisionTable_Independent);

             if ((swDraw == null))
             {
                 Debug.Print(" Please open a drawing document. ");
             }

             currentsheet = (Sheet)swDraw.GetCurrentSheet();
             swDraw.ActivateSheet(currentsheet.GetName());

             // Create sheet, Test, with 4 zones
             boolstatus = swDraw.NewSheet4("Test", (int)swDwgPaperSizes_e.swDwgPaperAsize, (int)swDwgTemplates_e.swDwgTemplateAsize, 1, 1, true, "", 0, 0, "",
             0.5, 0.5, 0.5, 0.5, 2, 2);

             System.Diagnostics.Debugger.Break();

             boolstatus = swModel.Extension.SelectByID2("Sheet Format2", "SHEET", 0, 0, 0, false, 0, null, 0);
             swDraw.EditTemplate();
             swModel.EditSketch();
             swModel.ClearSelection2(true);
             boolstatus = swModel.Extension.SelectByID2("Sheet Format2", "SHEET", 0.0812585524728589, 0.139959974668275, 0, false, 0, null, 0);

             // Modify Test to have 9 zones
             boolstatus = swDraw.SetupSheet6("Test", (int)swDwgPaperSizes_e.swDwgPapersUserDefined, (int)swDwgTemplates_e.swDwgTemplateCustom, 1, 1, true, "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\\english\\sheetformat\\a - landscape.slddrt", 0.2794, 0.2159, "Default",
             false, 0.5, 0.5, 0.5, 0.5, 3, 3);

             swDraw.EditSheet();
             swModel.EditSketch();
             swModel.ForceRebuild3(true);

             currentsheet = (Sheet)swDraw.GetCurrentSheet();
             swDraw.ActivateSheet(currentsheet.GetName());

             // Insert a revision table and add a revision row
             revTableAnno = currentsheet.InsertRevisionTable2(true, 0.0, 0.0, (int)swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_TopLeft, "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\\English\\standard revision block.sldrevtbt", (int)swRevisionTableSymbolShape_e.swRevisionTable_CircleSymbol, true);
             Debug.Print("Revision table annotation");
             Debug.Print("  New revision: " + revTableAnno.AddRevision("A"));
             Debug.Print("  Current revision: " + revTableAnno.CurrentRevision);

             RevisionTableFeature revTableFeat = default(RevisionTableFeature);
             revTableFeat = revTableAnno.RevisionTableFeature;
             Debug.Print("Revision table feature");
             Debug.Print("  Number of revision table annotations: " + revTableFeat.GetTableAnnotationCount());

             Feature feat = default(Feature);
             feat = (Feature)revTableFeat.GetFeature();
             Debug.Print("Feature: " + feat.Name);

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```
