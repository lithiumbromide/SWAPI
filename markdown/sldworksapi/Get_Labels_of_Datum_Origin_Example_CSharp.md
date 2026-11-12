---
title: "Get Labels of Datum Origin Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Labels_of_Datum_Origin_Example_CSharp.htm"
---

# Get Labels of Datum Origin Example (C#)

This example shows how to insert a hole table annotation and get some of its properties.

```vb
  //--------------------------------------------------------------------------
 // Preconditions:
 // 1. Verify that the specified files exist:
 //    * part document
 //    * drawing document template
 //    * hole table template
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. Opens the specified part document.
 // 2. Creates a drawing of the part document.
  // 3. Inserts a hole table annotation at the specified vertex.
 // 4. Prints to the Immediate window:
 //   * the hole table's datum origin x and y labels
  //   * whether to display hole sizes using ANSI inch letters
 //     and drill numbers
 // 5. Examine the Immediate window and drawing.
  //
 // NOTE: Because the model is used elsewhere, do not save changes.
  //---------------------------------------------------------------------------

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;

 namespace GetLabels_CSharp.csproj
 {
     public partial class SolidWorksMacro
     {

         public void Main()
         {

             ModelDoc2 swModel;
             DrawingDoc swDrawingDoc;
             View swView;
             ModelView swModelView;
             ModelDocExtension swModelDocExt;
             SelectionMgr swSelectionMgr;
             HoleTableAnnotation swHoleTableAnnotation;
             HoleTable swHoleTable;
             DatumOrigin swDatumOrigin;
             string fileName;
             string drawingDocTemplate;
             string holeTableTemplate;
             bool status;
             int errors = 0;
             int warnings = 0;

             //Open part document and create drawing document
             fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\tolanalyst\\minimum_clearance\\top_plate.sldprt";
             swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
             drawingDocTemplate = "C:\\ProgramData\\SolidWorks\\SolidWorks 2016\\templates\\Drawing.drwdot";
             swDrawingDoc = (DrawingDoc)swApp.NewDocument(drawingDocTemplate, (int)swDwgPaperSizes_e.swDwgPaperBsize, 0.2794, 0.4318);
             swView = (View)swDrawingDoc.CreateDrawViewFromModelView3(fileName, "*Front", 0.193046827497194, 0.155595183164983, 0);

             //Insert hole table annotation
             swModel = (ModelDoc2)swApp.ActiveDoc;
             swDrawingDoc = (DrawingDoc)swModel;
             swModelView = (ModelView)swModel.ActiveView;
             swModelDocExt = (ModelDocExtension)swModel.Extension;
             status = swDrawingDoc.ActivateView("Drawing View1");
             status = swModelDocExt.SelectByID2("", "VERTEX", 0.216278249046016, 0.198389907070707, 0.0080000000000382, false, 0, null, 0);
             status = swModelDocExt.SelectByID2("", "FACE", 0.228097744219978, 0.151927063973064, 0.0040000000000191, false, 0, null, 0);
             swModel.ClearSelection2(true);
             status = swModelDocExt.SelectByID2("", "VERTEX", 0.216278249046016, 0.198389907070707, 0.0080000000000382, true, 1, null, 0);
             status = swModelDocExt.SelectByID2("", "FACE", 0.228097744219978, 0.151927063973064, 0.0040000000000191, true, 2, null, 0);
             swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
             swView = (View)swSelectionMgr.GetSelectedObjectsDrawingView2(1, -1);
             holeTableTemplate = "C:\\Program Files\\SolidWorks Corp\\SolidWorks\\lang\\english\\standard hole table--letters.sldholtbt";
             swHoleTableAnnotation = (HoleTableAnnotation)swView.InsertHoleTable2(false, 0.0540658670033671, 0.253819263748597, 1, "A", holeTableTemplate);
             swModel.ClearSelection2(true);

             //Get hole table and its datum origin
             swHoleTable = (HoleTable)swHoleTableAnnotation.HoleTable;
             swDatumOrigin = (DatumOrigin)swHoleTable.DatumOrigin;

             //Get datum origin's x and y labels
             Debug.Print("Datum origin:");
             Debug.Print("  X label: " + swDatumOrigin.XLabel);
             Debug.Print("  Y label: " + swDatumOrigin.YLabel);

             //Get whether to display hole sizes using ANSI inch letters and drill numbers
             Debug.Print("Display ANSI inch letter and drill number sizes in hole table? " + swHoleTable.ShowANSIInchLetterNumberDrillSizes);

         }

         /// <summary>
         ///  The SldWorks swApp variable is pre-assigned for you.
         /// </summary>
         public SldWorks swApp;
     }
 }
```
