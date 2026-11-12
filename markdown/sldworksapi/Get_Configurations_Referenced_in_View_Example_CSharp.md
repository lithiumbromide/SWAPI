---
title: "Get Configurations Referenced in View Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Configurations_Referenced_in_View_Example_CSharp.htm"
---

# Get Configurations Referenced in View Example (C#)

This example shows how to get the names and persistent reference IDs of the configurations referenced in each drawing view in the first drawing sheet.

```
//---------------------------------------------------
// Preconditions:
// 1. Open a drawing document with multiple
//    drawing views and multiple referenced
//    configurations in the first drawing sheet
//    in the drawing.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Traverses the drawing views in the first
//    drawing sheet and gets each drawing view's:
//    *  name
//    *  referenced model name
//    *  referenced configuration name and
//       persistent reference ID
// 2. Examine the Immediate window.
//---------------------------------------------------
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
            DrawingDoc swDraw = default(DrawingDoc);
            View swView = default(View);

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swDraw = (DrawingDoc)swModel;
            Debug.Print("File = " + swModel.GetPathName());

            // First drawing view is actually the first drawing sheet,
            // so skip getting model name and configuration from
            // the drawing sheet
            swView = (View)swDraw.GetFirstView();
            // Get first drawing view in first drawing sheet
            swView = (View)swView.GetNextView();
            while ((swView != null))
            {
                Debug.Print("  Drawing view = " + swView.Name);
                Debug.Print("    Referenced model name = " + swView.GetReferencedModelName());
                Debug.Print("    Referenced configuration name = " + swView.ReferencedConfiguration);
                Debug.Print("    Referenced configuration persistent reference ID = " + swView.ReferencedConfigurationID);
                //Get next drawing view
                swView = (View)swView.GetNextView();
            }

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
