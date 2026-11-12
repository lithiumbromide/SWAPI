---
title: "Is There a Projection Arrow and Is It Visible Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Is_There_a_Projection_Arrow_and_Is_It_Visible_Example_CSharp.htm"
---

# Is There a Projection Arrow and Is It Visible Example (C#)

This example shows how to find out if:

- the selected drawing view is a projected view
- a projection arrow exists in the projected view
- the projected arrow is visible

```
//--------------------------------------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\advdrawings\foodprocessor.slddrw.
// 2. Double-click the projected view (i.e., the upper-right drawing view).
// 3. In the PropertyManager page, click the Arrow check box and
//    type a label for the projection arrow.
// 4. Click OK to close the PropertyManager page.
//
// Postconditions:
// 1. Creates a visible projection arrow for Drawing View2, which is
//    a projected view.
// 2. Examine the graphics area and Immediate window.
//
// NOTE: Because this drawing document is used elsewhere, do not save
// changes.
//--------------------------------------------------------------------------
```

```vb
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;

namespace Visibleprojectionarrowcsharp.csproj
{
    partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel;
            ModelDocExtension swModelDocExt;
            DrawingDoc swDrawing;
            View swView;
            ProjectionArrow swProjectionArrow;
            int typeDrawingView;
            bool boolstatus;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swDrawing = (DrawingDoc)swModel;

            swModelDocExt = (ModelDocExtension)swModel.Extension;
            boolstatus = swDrawing.ActivateView("Drawing View2");
            boolstatus = swModelDocExt.SelectByID2("Drawing View2", "DRAWINGVIEW", 0.4426278247583, 0.3837831481976, 0, false, 0, null, 0);

            swView = (View)swDrawing.ActiveDrawingView;
            typeDrawingView = swView.Type;
            if (typeDrawingView == 4)
            {
                Debug.Print("Type of selected drawing view is projected.");
            }
            else
            {
                Debug.Print("Type of selected drawing view is not projected. Exiting macro.");
                return;
            }

            swProjectionArrow = (ProjectionArrow)swView.GetProjectionArrow();
            if ((swProjectionArrow != null))
            {
                Debug.Print("Projection arrow visible: " + swProjectionArrow.Visible);
            }
            else
            {
                Debug.Print("No projection arrow in projected view.");
            }

        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;

    }
}
```
