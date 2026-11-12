---
title: "Get Transform for Each Circular Pattern Instance Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Transform_for_Each_Circular_Pattern_Instance_Example_CSharp.htm"
---

# Get Transform for Each Circular Pattern Instance Example (C#)

This example shows how to get the transform for each instance in a circular pattern feature.

```
//-----------------------------------------------
// Preconditions:
// 1. Verify that the specified part exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the part.
// 2. Selects the circular-pattern feature.
// 3. Get the number of instances in the circular-pattern
//    feature.
// 4. Gets the transform for each instance
//    in the circular-pattern feature.
// 5. Examine the Immediate window.
//
// NOTE: Because the part is used elsewhere, do not
// save changes.
//-----------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;

namespace Macro1CSharp.csproj
{
    partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExtension = default(ModelDocExtension);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            Feature swFeature = default(Feature);
            CircularPatternFeatureData swCircularPatternFeatureData = default(CircularPatternFeatureData);
            MathTransform swMathTransform = default(MathTransform);
            bool boolstatus = false;
            int nErrors = 0;
            int nWarnings = 0;
            int NbrInstances = 0;
            int i = 0;

            swModel = (ModelDoc2)swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\introtosw\\pressure_plate.sldprt", (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref nErrors, ref nWarnings);
            swModelDocExtension = (ModelDocExtension)swModel.Extension;

            // Select the circular-pattern feature
            boolstatus = swModelDocExtension.SelectByID2("CirPattern1", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swFeature = (Feature)swSelectionMgr.GetSelectedObject6(1, -1);
            swCircularPatternFeatureData = (CircularPatternFeatureData)swFeature.GetDefinition();

            // Get the number of instances in the circular-pattern feature
            NbrInstances = swCircularPatternFeatureData.TotalInstances;
            Debug.Print("Number of instances: " + NbrInstances);

            // Get the transform for each instance
            // in the circular-pattern feature
            for (i = 0; i < NbrInstances; i++)
            {
                Debug.Print(" Processing instance " + (i + 1) + "...");
                swMathTransform = (MathTransform)swCircularPatternFeatureData.GetTransform(i);
                // TODO: Do something with the transform

            }
        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
