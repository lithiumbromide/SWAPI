---
title: "Select Face Using Intersecting Ray Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Face_Using_Intersecting_Ray_Example_CSharp.htm"
---

# Select Face Using Intersecting Ray Example (C#)

This example shows how to select the first face that is intersected by a ray that starts at the specified point and runs parallel to the specified direction vector within the specified radius.

```
//-----------------------------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\api\box.sldrpt.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Selects the first face intersected by a ray that starts
//    at the specified point and runs parallel to the specified
//    direction vector within the specified radius.
// 2. Examine the graphics area and Immediate window.
//-----------------------------------------------------------------
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
            double startPointX = 0;
            double startPointY = 0;
            double startPointZ = 0;
            double rayVecX = 0;
            double rayVecY = 0;
            double rayVecZ = 0;
            double radius = 0;
            bool status = false;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            startPointX = 0.1;
            startPointY = 0.0;
            startPointZ = 0.0;

            rayVecX = -1.0;
            rayVecY = 0.0;
            rayVecZ = 0.0;

            radius = 1.0;

            status = swModelDocExt.SelectByRay(startPointX, startPointY, startPointZ, rayVecX, rayVecY, rayVecZ, radius, (int)swSelectType_e.swSelFACES, false, 0, (int)swSelectOption_e.swSelectOptionDefault);
            Debug.Print("Selection status: " + status);
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
