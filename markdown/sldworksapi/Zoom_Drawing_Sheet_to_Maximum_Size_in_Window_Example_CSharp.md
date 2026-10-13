---
title: "Zoom Drawing Sheet to Maximum Size in Window Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Zoom_Drawing_Sheet_to_Maximum_Size_in_Window_Example_CSharp.htm"
---

# Zoom Drawing Sheet to Maximum Size in Window Example (C#)

This example shows how to zoom a drawing sheet to its maximum size within the window.

```
//------------------------------------------------------
// Preconditions: Verify that the drawing to open exists.
//
// Postconditions:
// 1. Opens the drawing.
// 2. Zooms the drawing sheet to its maximum size within
//    the window.
// 3. Examine the graphics area.
//
// NOTE: Because the drawing is used elsewhere, do not
// save changes.
//-------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel;
            ModelDocExtension swModelDocExt;
            string fileName;
            int errors = 0;
            int warnings = 0;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\replaceview.slddrw";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocDRAWING, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swModelDocExt.ViewZoomToSheet();

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
