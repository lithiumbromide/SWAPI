---
title: "Automatically Insert Center Marks Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Auto_Insert_Center_Marks_Example_CSharp.htm"
---

# Automatically Insert Center Marks Example (C#)

This example shows how to automatically insert center marks in multiple drawing views.

```
//----------------------------------------------------------------------------
// Preconditions: Open public_documents\samples\tutorial\advdrawings\foodprocessor.slddrw.
//
// Postconditions:
// 1. Clears the Tools > Options > Document Properties > Centerlines/Center Marks >
//    Scale by view scale check box.
// 2. Activates Sheet3.
// 3. Suppresses Drawing View9.
// 4. Inserts center marks in Drawing View9 and Drawing View11.
// 5. Unsuppresses Drawing View9.
// 6. Examine the drawing.
//
// NOTE: Because the drawing is used elsewhere, do not save changes.
// ---------------------------------------------------------------------------
using System;
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;

namespace AutoInsertCenterMarks_CSharp.csproj
{
    partial class SolidWorksMacro
    {
        ModelDoc2 Part;
        DrawingDoc Draw;
        ModelDocExtension ModelDocExt;
        View swActiveView;
        bool boolstatus;

        public void Main()
        {
            Part = (ModelDoc2)swApp.ActiveDoc;
            Draw = (DrawingDoc)Part;
            ModelDocExt = (ModelDocExtension)Part.Extension;

            // Clear the Scale by view scale check box to set gap
            ModelDocExt.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swDetailingCenterMarkScaleByViewScale, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified, false);

            Draw.ActivateSheet("Sheet3");

            // Suppress Drawing View9
            boolstatus = ModelDocExt.SelectByID2("Drawing View9", "DRAWINGVIEW", 0, 0, 0, false, 0, null, 0);
            Draw.SuppressView();

            // Insert center marks for all holes, fillets, and slots in the specified view
            boolstatus = Draw.ActivateView("Drawing View9");
            swActiveView = (View)Draw.ActiveDrawingView;
            boolstatus = swActiveView.AutoInsertCenterMarks2(7, 11, true, true, true, 0.0025, 0.0025, true, true, 0);

            boolstatus = Draw.ActivateView("Drawing View11");
            swActiveView = (View)Draw.ActiveDrawingView;
            boolstatus = swActiveView.AutoInsertCenterMarks2(7, 11, true, true, false, 0.005, 0.005, true, false, 0);

            Part.ClearSelection2(true);

            // Unsuppress Drawing View9
            boolstatus = ModelDocExt.SelectByID2("Drawing View9", "DRAWINGVIEW", 0, 0, 0, false, 0, null, 0);
            Draw.UnsuppressView();
        }

        public SldWorks swApp;
    }

}
```
