---
title: "Crop Drawing View Using Jagged Outline Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Crop_Drawing_View_Using_Jagged_Outline_Example_CSharp.htm"
---

# Crop Drawing View Using Jagged Outline Example (C#)

This example shows how to crop a drawing view using a jagged outline with the least shape intensity.

```
//----------------------------------------------------------------------------
// Preconditions: Verify that the drawing to open exists.
//
// Postconditions:
// 1. Opens the drawing.
// 2. Selects and activates Drawing View1 on Sheet1.
// 3. Creates a rectangle.
// 4. Crops Drawing View1 around the rectangle.
// 5. Examine the drawing.
//
// NOTE: Because the drawing is used elsewhere, do not save changes.
// ---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            DrawingDoc swDrawing = default(DrawingDoc);
            SelectionMgr swSelMgr = default(SelectionMgr);
            View swView = default(View);
            SketchManager swSketchMgr = default(SketchManager);
            object[] sketchLines = null;
            bool status = false;
            int errors = 0;
            int warnings = 0;
            string fileName = null;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\foodprocessor.slddrw";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocDRAWING, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swDrawing = (DrawingDoc)swModel;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;

            //Crop Drawing View1 using a jagged outline
            //with the least shape intensity
            status = swModelDocExt.SelectByID2("Drawing View1", "DRAWINGVIEW", 0, 0, 0, false, 0, null, 0);
            swView = (View)swSelMgr.GetSelectedObject6(1, -1);
            swSketchMgr = (SketchManager)swModel.SketchManager;
            status = swDrawing.ActivateView("Drawing View1");
            sketchLines = (object[])swSketchMgr.CreateCornerRectangle(-0.0574722079408937, 0.0331536511827661, 0, 0.0371399698368841, -0.0373161088172339, 0);
            errors = swView.Crop2(true, false, 5);

            swModel.ClearSelection2(true);

            if (swView.CropViewNoOutline)
            {
                Debug.Print("No outline.");
            }
            else
            {
                if (swView.CropViewJaggedOutline)
                {
                    Debug.Print("Jagged outline with shape intensity (1=most to 5=least): " + swView.CropViewJaggedShapeIntensity);
                }
            }
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
