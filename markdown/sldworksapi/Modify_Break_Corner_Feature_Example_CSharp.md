---
title: "Modify Break Corner Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Modify_Break_Corner_Feature_Example_CSharp.htm"
---

# Modify Break Corner Feature Example (C#)

This example shows how to create and modify a break corner feature in a sheet metal part.

```
//---------------------------------------------------
// Preconditions:
// 1. Verify that the specified part document exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified document.
// 2. Selects a face on Edge-Flange1.
// 3. Creates a break corner feature.
// 4. Unsuppresses the flat pattern feature.
// 5. Accesses the break corner feature and
//    and modifies it.
// 6. Suppresses the flat pattern feature.
// 7. Examine the graphics area and the Immediate window.
//
// NOTE: Because the part document is used elsewhere,
// do not save any changes.
//----------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace BreakCornerFeatureCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            Feature swFeature = default(Feature);
            BreakCornerFeatureData swBreakCornerFeatureData = default(BreakCornerFeatureData);
            string fileName = null;
            bool status = false;
            int errors = 0;
            int warnings = 0;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\sm1-remove-edges.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("", "FACE", -0.111589911985732, 0.0979999999999563, 0.0841212722518208, true, 0, null, 0);
            swModel.InsertSheetMetalBreakCorner((int)swBreakCornerTypes_e.swBreakCornerTypeChamfer, 0.005);

            //Select and unsuppress the flat pattern feature
            status = swModelDocExt.SelectByID2("Flat-Pattern1", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            swModel.EditUnsuppress2();
            swModel.ClearSelection2(true);

            //Select the break corner feature
            //and change some of its properties
            status = swModelDocExt.SelectByID2("Break-Corner1", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swFeature = (Feature)swSelectionMgr.GetSelectedObject6(1, 0);
            swBreakCornerFeatureData = (BreakCornerFeatureData)swFeature.GetDefinition();
            status = swBreakCornerFeatureData.AccessSelections(swModel, null);
            Debug.Print("AccessSelections: " + status);
            Debug.Print("");
            Debug.Print("  -------------Original--------------");
            Debug.Print("    CenteredOnBendLines: " + swBreakCornerFeatureData.CenteredOnBendLines);
            Debug.Print("    InternalCornersOnly: " + swBreakCornerFeatureData.InternalCornersOnly);
            swBreakCornerFeatureData.InternalCornersOnly = true;
            swBreakCornerFeatureData.CenteredOnBendLines = true;
            Debug.Print("");
            Debug.Print("  -------------Modified--------------");
            Debug.Print("    CenteredOnBendLines: " + swBreakCornerFeatureData.CenteredOnBendLines);
            Debug.Print("    InternalCornersOnly: " + swBreakCornerFeatureData.InternalCornersOnly);
            status = swFeature.ModifyDefinition(swBreakCornerFeatureData, swModel, null);
            Debug.Print("");
            Debug.Print("ModifyDefinition: " + status);
            swModel.ClearSelection2(true);

            //Select and suppress the flat pattern feature
            status = swModelDocExt.SelectByID2("Flat-Pattern1", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            swModel.EditSuppress2();
            swModel.ClearSelection2(true);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
