---
title: "Get Whether Draft Edges Scaled in Printed Drawing Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Whether_Draft_Edges_Scaled_in_Printed_Drawing_Example_CSharp.htm"
---

# Get Whether Draft Edges Scaled in Printed Drawing Example (C#)

This example shows how to get whether draft edges are scaled when printing a drawing in high quality.

```
//------------------------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified drawing exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified drawing.
// 2. Examine the Immediate window.
//------------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace ScaleDraftEdgesCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {

            DrawingDoc swDrawing = default(DrawingDoc);
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            PageSetup swPageSetup = default(PageSetup);
            string fileName = null;
            int errors = 0;
            int warnings = 0;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\foodprocessor.slddrw";
            swDrawing = (DrawingDoc)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocDRAWING, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModel = (ModelDoc2)swDrawing;
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swPageSetup = (PageSetup)swModelDocExt.AppPageSetup;
            if (swPageSetup.HighQuality)
            {
                Debug.Print("Drawing set to print in high quality. Are draft edges scaled? " + swPageSetup.ScaleDraftEdges);
            }
            else
            {
                Debug.Print("Drawing not set to print in high quality. Can only scale draft edges when drawing set to print in high quality.");
            }
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
