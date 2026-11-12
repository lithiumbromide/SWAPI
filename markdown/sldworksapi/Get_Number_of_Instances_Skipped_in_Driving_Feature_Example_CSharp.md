---
title: "Get Number of Instances Skipped in Driving Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Number_of_Instances_Skipped_in_Driving_Feature_Example_CSharp.htm"
---

# Get Number of Instances Skipped in Driving Feature Example (C#)

This example shows how to get the number of instances skipped in the driving feature of a derived pattern feature.

```
//--------------------------------------------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\api\PatternDrivenComponentPattern.sldasm.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Adds instances to skip in the local linear pattern feature.
// 2. Inserts a derived pattern feature.
// 3. Gets the number of instances skipped in the driving feature for the
//    derived pattern feature.
// 4. Gets whether visual properties are propagated in the derived pattern
//    feature.
// 5. Examine the FeatureManager design tree, graphics area, and
//    Immediate window.
//
// NOTE: Because the assembly is used elsewhere, do not save changes.
//--------------------------------------------------------------------------------
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
            AssemblyDoc swAssemblyDoc = default(AssemblyDoc);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            Feature swFeature = default(Feature);
            LocalLinearPatternFeatureData swLocalLinearPatternData = default(LocalLinearPatternFeatureData);
            DerivedPatternFeatureData swDerivedPatternFeatureData = default(DerivedPatternFeatureData);
            int[] list = new int[2];
            object instancesSkipData = null;
            int[] instancesSkipData_Derived = new int[2];
            int instancesToSkipCount = 0;
            bool status = false;
            int i = 0;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            //Add instances to skip to local linear pattern feature, LocalLPattern1
            status = swModelDocExt.SelectByID2("LocalLPattern1", "COMPPATTERN", 0, 0, 0, false, 0, null, 0);
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swFeature = (Feature)swSelectionMgr.GetSelectedObject6(1, -1);
            swLocalLinearPatternData = (LocalLinearPatternFeatureData)swFeature.GetDefinition();
            status = swLocalLinearPatternData.AccessSelections(swModel, null);
            list[0] = 11;
            list[1] = 14;
            instancesSkipData = list;
            swLocalLinearPatternData.SkippedItemArray = instancesSkipData;
            status = swFeature.ModifyDefinition(swLocalLinearPatternData, swModel, null);

            //Insert derived pattern feature, LocalCompPattern1
            status = swModelDocExt.SelectByID2("Part2^patterndrivencomponentpattern-1@patterndrivencomponentpattern", "COMPONENT", 0, 0, 0, false, 1, null, 0);
            status = swModelDocExt.SelectByID2("LocalLPattern1", "COMPPATTERN", 0, 0, 0, true, 6, null, 0);
            swAssemblyDoc = (AssemblyDoc)swModel;
            status = swAssemblyDoc.InsertDerivedPattern();

            //Get number of instances skipped in the driving feature, LocalLPattern1,
            //for derived pattern feature, LocalCompPattern1
            status = swModelDocExt.SelectByID2("LocalCompPattern1", "COMPPATTERN", 0, 0, 0, false, 0, null, 0);
            swFeature = (Feature)swSelectionMgr.GetSelectedObject6(1, -1);
            swDerivedPatternFeatureData = (DerivedPatternFeatureData)swFeature.GetDefinition();
            status = swDerivedPatternFeatureData.AccessSelections(swModel, null);
            instancesSkipData_Derived = (int[])swDerivedPatternFeatureData.DrivingFeatureSkippedItemArray;
            instancesToSkipCount = instancesSkipData_Derived.Length;
            Debug.Print("Number of instances skipped in the driving feature of the derived pattern feature: " + instancesToSkipCount);
            for (i = 0; i <= instancesToSkipCount - 1; i++)
            {
                Debug.Print("  Instance skipped: " + instancesSkipData_Derived[i]);
            }

            //Get whether visual properties are propagated in the derived pattern feature
            Debug.Print ("Visual properties propagated in the derived pattern feature? " + swDerivedPatternFeatureData.PropagateVisualProperty);

            swDerivedPatternFeatureData.ReleaseSelectionAccess();

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
