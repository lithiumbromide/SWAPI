---
title: "Change Angle to Supplementary Angle Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Angle_to_Supplementary_Angle_Example_CSharp.htm"
---

# Change Angle to Supplementary Angle Example (C#)

This example shows how to change the angle in an angular dimension to its supplementary angle.

```
//-----------------------------------------------------------
// Preconditions: Verify that the drawing exists.
//
// Postconditions:
// 1. Opens the drawing.
// 2. Selects the angular dimension.
// 3. Changes the angle to its supplementary angle.
// 4. Examine the graphics area.
//
// NOTE: Because the drawing is used elsewhere, do not save
// changes.
//-----------------------------------------------------------
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
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            DisplayDimension swDisplayDimension = default(DisplayDimension);
            bool status = false;
            int warnings = 0;
            int errors = 0;
            string fileName = null;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\clamp1.slddrw";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocDRAWING, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            //Select angular dimension
            status = swModelDocExt.SelectByID2("RD1@Drawing View1", "DIMENSION", 0.115166498498499, 0.167429477477477, 0, false, 0, null, 0);
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swDisplayDimension = (DisplayDimension)swSelectionMgr.GetSelectedObject6(1, -1);

            //Change angle to supplementary angle
            status = swDisplayDimension.SupplementaryAngle();

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
