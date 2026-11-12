---
title: "Reset Visibility of Sketches in Drawing View Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Reset_Visibility_of_Sketches_in_Drawing_View_Example_CSharp.htm"
---

# Reset Visibility of Sketches in Drawing View Example (C#)

This example shows how to reset the visibility of any hidden sketches in a drawing view so that the drawing view reflects the model.

```vb
 //--------------------------------------------------
 // Preconditions: Verify that the specified drawing
 // document to open exists.
 //
 // Postconditions:
 // 1. Opens the specified drawing document
 // 2. Examine the drawing, then press F5.
 // 3. Activates a drawing view and hides
 //    a sketch in that drawing view .
 // 4. After examining the drawing to verify,
 //    press F5.
 // 5. Selects the drawing view with the hidden sketch
 //    and resets the visibility of all sketches in
 //    that drawing view  so that the drawing view
 //    reflects the model.
 // 6. Examine the drawing to verify that the hidden
 //    sketch is visible.
 //
 // NOTE: Because this drawing is used elsewhere, do
 // not save changes.
 //-------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;

 namespace ResetSketchVisibilityCSharp.csproj
 {

     partial class SolidWorksMacro
     {

         public void Main()
         {

             ModelDoc2 swModel = default(ModelDoc2);
             DrawingDoc swDrawing = default(DrawingDoc);
             ModelDocExtension swModelDocExt =  default(ModelDocExtension);
             SelectionMgr swSelMgr = default(SelectionMgr);
             View swView = default(View);
             string fileName = null;
             bool boolstatus = false;
             int errors = 0;
             int warnings = 0;

             fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\resetsketchvisibility.SLDDRW";

             swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocDRAWING, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
             swDrawing = (DrawingDoc)swModel;
             swModelDocExt = (ModelDocExtension)swModel.Extension;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;

             // Examine the drawing, then press F5
             System.Diagnostics.Debugger.Break();

             // Select a drawing view where to hide a sketch
             boolstatus = swDrawing.ActivateView("Drawing View1");

             // Hide the selected sketch
             boolstatus = swModelDocExt.SelectByID2("Sketch1@resetsketchvisibility-7@Drawing View1",  "SKETCH", 0, 0, 0,  false, 0,  null, 0);
             swModel.BlankSketch();

             // Examine the drawing to verify that selected sketch is hidden, then press F5
             System.Diagnostics.Debugger.Break();

             // Select the drawing view with the hidden sketch
             boolstatus = swModelDocExt.SelectByID2("Drawing View1",  "DRAWINGVIEW", 0, 0, 0,  false, 0,  null, 0);
             swView = (View)swSelMgr.GetSelectedObject6(1, -1);

             // Reset the visibility of sketches in the selected
             // drawing view so that drawing view reflects the model
             swView.ResetSketchVisibility();

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```
