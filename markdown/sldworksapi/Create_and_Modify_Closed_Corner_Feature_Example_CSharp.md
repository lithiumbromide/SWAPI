---
title: "Create and Modify Closed Corner Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_and_Modify_Closed_Corner_Feature_Example_CSharp.htm"
---

# Create and Modify Closed Corner Feature Example (C#)

This example shows how to create and modify a closed corner feature in a sheet metal part.

```
//------------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified sheet metal part document to
//    open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified sheet metal part document.
// 2. Selects two faces.
// 3. Inserts a closed corner feature.
// 4. Modifies properties of the closed corner feature.
// 5. Examine the graphics area and Immediate window.
//
// NOTE: Because this part document is used elsewhere,
// do not save changes.
//--------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace ClosedCornerFeatureDataCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            Feature swFeature = default(Feature);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            ClosedCornerFeatureData swClosedCornerFeatureData = default(ClosedCornerFeatureData);
            bool status = false;
            int errors = 0;
            int warnings = 0;
            string fileName = null;
            object[] faces = null;
            Face2 swFace = default(Face2);
            int i = 0;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\sheetmetal\\formtools\\cover.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;

            //Select the faces for the closed corner feature
            status = swModelDocExt.SelectByID2("", "FACE", 0.0110595835492404, 0.0280018934407167, 0.0497348782814129, true, 1, null, 0);
            status = swModelDocExt.SelectByID2("", "FACE", 0.0181424245698736, 0.0110595835492404, 0.0495671179450028, true, 1073741824, null, 0);

            //Insert the closed corner feature
            swModel.InsertSheetMetalClosedCorner();

            //Select the closed corner feature
            status = swModelDocExt.SelectByID2("Closed Corner1", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            swFeature = (Feature)swSelectionMgr.GetSelectedObject6(1, -1);
            swClosedCornerFeatureData = (ClosedCornerFeatureData)swFeature.GetDefinition();

            //Access closed corner feature
            status = swClosedCornerFeatureData.AccessSelections(swModel, null);
            Debug.Print("Original properties: ");
            Debug.Print("  Corner type: " + swClosedCornerFeatureData.CornerType);
            Debug.Print("  Gap distance: " + swClosedCornerFeatureData.GapDistance);
            Debug.Print("  Open bend region? " + swClosedCornerFeatureData.OpenBendRegion);
            Debug.Print("  Overlap/underlap ratio: " + swClosedCornerFeatureData.OverlapUnderlapRatio);
            faces = (object[])swClosedCornerFeatureData.Faces;
            for (i = 0; i < faces.Length; i++)
            {
                swFace = (Face2)faces[i];
                Debug.Print("  Area of face " + i + ": " + swFace.GetArea() * 1000 + " mm");
            }
            Debug.Print("Modified properties: ");
            swClosedCornerFeatureData.CornerType = (int)swClosedCornerTypes_e.swClosedCornerTypeUnderlap;
            swClosedCornerFeatureData.GapDistance = 0.005;
            swClosedCornerFeatureData.OpenBendRegion = true;
            swClosedCornerFeatureData.OverlapUnderlapRatio = 0.5;
            Debug.Print("  Corner type: " + swClosedCornerFeatureData.CornerType);
            Debug.Print("  Gap distance: " + swClosedCornerFeatureData.GapDistance);
            Debug.Print("  Open bend region? " + swClosedCornerFeatureData.OpenBendRegion);
            Debug.Print("  Overlap/underlap ratio: " + swClosedCornerFeatureData.OverlapUnderlapRatio);

            status = swFeature.ModifyDefinition(swClosedCornerFeatureData, swModel, null);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
