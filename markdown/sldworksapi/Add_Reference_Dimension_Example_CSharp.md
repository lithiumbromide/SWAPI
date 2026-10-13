---
title: "Add Reference Dimension Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Reference_Dimension_Example_CSharp.htm"
---

# Add Reference Dimension Example (C#)

This example shows how to add a reference dimension to a model in a drawing.

```
//---------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified drawing document to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified drawing document.
// 2. Activates a drawing view, selects an edge on the model, and
//    creates a dimension.
// 3. Prints to the Immediate window whether the dimension
//    is a reference dimension.
// 4. Examine the Immediate window.
//
// NOTE: Because the drawing document is used elsewhere, do not
// save any changes.
//---------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace ISReferenceDimCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            DrawingDoc swDrawingDoc = default(DrawingDoc);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            DisplayDimension swDisplayDimension = default(DisplayDimension);
            string fileName = null;
            bool status = false;
            int errors = 0;
            int warnings = 0;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\cylinder20.SLDDRW";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocDRAWING, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swDrawingDoc = (DrawingDoc)swModel;
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            status = swDrawingDoc.ActivateView("Drawing View1");
            status = swModelDocExt.SelectByID2("", "EDGE", 0.512187343878665, 0.498697444621999, 249.953027873291, false, 0, null, 0);
            swDisplayDimension = (DisplayDimension)swModelDocExt.AddDimension(0.698326046410311, 0.699228314873418, 0, (int)swSmartDimensionDirection_e.swSmartDimensionDirection_Up);
            Debug.Print("Is reference dimension? " + swDisplayDimension.IsReferenceDim());

            swModel.ClearSelection2(true);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
