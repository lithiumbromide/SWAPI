---
title: "Set Override Option for Auto Relief Default Parameters Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Override_Option_for_Auto_Relief_Default_Parameters_Example_CSharp.htm"
---

# Set Override Option for Auto Relief Default Parameters Example (C#)

This example shows how to set the override option for the auto relief default parameters of a sheet metal feature in a multibody sheet metal part.

```
//---------------------------------------------------
// Preconditions:
// 1. Open a multibody sheet metal part that contains
//    a Sheet-Metal3 feature in the Sheet-Metal folder.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Gets whether the default parameters are overridden
//    for Sheet-Metal3.
// 2. Sets the override option for the auto relief default
//    parameters of Sheet-Metal3.
// 3. Examine the Immediate window.
//
// NOTE: Because the part is used elsewhere, do not
// save changes.
//----------------------------------------------------
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
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            Feature swFeature = default(Feature);
            SheetMetalFeatureData swSheetMetalFeatureData = default(SheetMetalFeatureData);
            int errors = 0;
            bool status = false;
            bool overridden = false;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("Sheet-Metal3", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swFeature = (Feature)swSelectionMgr.GetSelectedObject6(1, -1);
            swSheetMetalFeatureData = (SheetMetalFeatureData)swFeature.GetDefinition();
            Debug.Print("Get override parameter values for Sheet-Metal3:");
            errors = swSheetMetalFeatureData.GetOverrideDefaultParameter2((int)swSheetMetalOverrideDefaultParameters_e.swSheetMetalOverrideDefaultParameters_BendParameters, out overridden);
            Debug.Print("  Bend parameters: " + overridden);
            errors = swSheetMetalFeatureData.GetOverrideDefaultParameter2((int)swSheetMetalOverrideDefaultParameters_e.swSheetMetalOverrideDefaultParameters_BendAllowance, out overridden);
            Debug.Print("  Bend allowance: " + overridden);
            errors = swSheetMetalFeatureData.GetOverrideDefaultParameter2((int)swSheetMetalOverrideDefaultParameters_e.swSheetMetalOverrideDefaultParameters_AutoRelief, out overridden);
            Debug.Print("  Auto relief: " + overridden);
            swSheetMetalFeatureData.AccessSelections(swModel, null);
            if (overridden)
            {
                errors = swSheetMetalFeatureData.SetOverrideDefaultParameter2((int)swSheetMetalOverrideDefaultParameters_e.swSheetMetalOverrideDefaultParameters_AutoRelief, false);
            }
            else
            {
                errors = swSheetMetalFeatureData.SetOverrideDefaultParameter2((int)swSheetMetalOverrideDefaultParameters_e.swSheetMetalOverrideDefaultParameters_AutoRelief, true);
            }
            swFeature.ModifyDefinition(swSheetMetalFeatureData, swModel, null);
            errors = swSheetMetalFeatureData.GetOverrideDefaultParameter2((int)swSheetMetalOverrideDefaultParameters_e.swSheetMetalOverrideDefaultParameters_AutoRelief, out overridden);
            Debug.Print("Override auto relief default parameters for Sheet-Metal3?  " + overridden);
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
