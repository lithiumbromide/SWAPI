---
title: "Create Cut-sweep Feature Using Circular Profile Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Cut-sweep_Feature_Using_Circular_Profile_Example_CSharp.htm"
---

# Create Cut-sweep Feature Using Circular Profile Example (C#)

This example shows how to create a cut-sweep feature using a circular profile.

```
//-----------------------------------------------
// Preconditions:
// 1. Verify that the part exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the part.
// 2. Selects an edge on the part.
// 3. Creates a cut-sweep feature using a circular
//    profile.
// 4. Accesses the cut-sweep feature.
// 5. Changes the diameter of the circular profile.
// 6. Examine the Immediate window, FeatureManager
//    design tree, and graphics area.
//
// NOTE: Because the part is used elsewhere, do not
// save changes.
//------------------------------------------------
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
            Feature swFeature = default(Feature);
            FeatureManager swFeatureManager = default(FeatureManager);
            SweepFeatureData swSweepFeatureData = default(SweepFeatureData);
            bool status = false;
            int errors = 0;
            int warnings = 0;

            swModel = (ModelDoc2)swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\block20.sldprt", 1, 0, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            //Select the edge for the cut-sweep feature
            status = swModelDocExt.SelectByID2("", "EDGE", -0.0372983839416747, 0.0393904284381961, 0.0495042874504179, true, 4, null, 0);
            swFeatureManager = (FeatureManager)swModel.FeatureManager;

            //Create the cut-sweep feature using a circular profile
            swFeature = (Feature)swFeatureManager.InsertCutSwept5(false, true, 0, false, false, 0, 0, false, 0, 0,
            0, 0, true, true, 0, true, true, true, false, true,
            0.0254, (int)swSweepDirection_e.swSweepDirection1);

            //Roll back the cut-sweep feature to access and change the diameter of circular profile
            swSweepFeatureData = (SweepFeatureData)swFeature.GetDefinition();
            status = swSweepFeatureData.AccessSelections(swModel, null);
            Debug.Print("Using a circular profile? " + swSweepFeatureData.CircularProfile);
            Debug.Print("Original size of circular profile = " + swSweepFeatureData.CircularProfileDiameter);
            swSweepFeatureData.CircularProfileDiameter = 0.003;
            Debug.Print("Modified size of circular profile = " + swSweepFeatureData.CircularProfileDiameter);
            Debug.Print("Direction of cut-sweep = " + swSweepFeatureData.Direction);

            //Roll forward the cut-sweep feature
            swFeature.ModifyDefinition(swSweepFeatureData, swModel, null);
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
