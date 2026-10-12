---
title: "Get and Add Sketch Points in Hole Wizard Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sketch_Points_in_Wizard_Hole_Example_CSharp.htm"
---

# Get and Add Sketch Points in Hole Wizard Feature Example (C#)

This example shows how to get and add the sketch points in a Hole Wizard feature.

```
//------------------------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified part document template exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Creates a new part document.
// 2. Creates Boss-Extrude1 and #0-80 Tapped Hole1 features.
// 3. Selects #8-80 Tapped Hole1; i.e., the Hole Wizard feature.
// 4. Gets the number of sketch points in the Hole Wizard feature.
// 5. Adds two sketch points to the Hole Wizard feature; thus, adds two more
//    holes to the Hole Wizard feature.
// 6. Examine the Immediate window and graphics area.
//-----------------------------------------------------------------------------
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
            SketchManager swSketchMgr = default(SketchManager);
            FeatureManager swFeatureMgr = default(FeatureManager);
            Feature swFeature = default(Feature);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            WizardHoleFeatureData2 swWizardHoleFeatureData = default(WizardHoleFeatureData2);
            SketchPoint swSketchPoint = default(SketchPoint);
            object sketchLines = null;
            bool status = false;
            int count = 0;
            object[] points = null;

            //Create part with Hole Wizard feature
            swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SolidWorks 2015\\templates\\Part.prtdot", 0, 0, 0);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swSketchAddConstToRectEntity, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified, false);
            status = swModelDocExt.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified, true);
            swSketchMgr = (SketchManager)swModel.SketchManager;
            sketchLines = (object[])swSketchMgr.CreateCornerRectangle(0, 0, 0, 0.0968848174375125, -0.0708129015764598, 0);
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, false, 0, null, 0);
            status = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("Line4", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("Line3", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            swFeatureMgr = (FeatureManager)swModel.FeatureManager;
            swFeature = (Feature)swFeatureMgr.FeatureExtrusion2(true, false, false, 0, 0, 0.0254, 0.00254, false, false, false,
            false, 0.0174532925199433, 0.0174532925199433, false, false, false, false, true, true, true,
            0, 0, false);
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swSelectionMgr.EnableContourSelection = false;
            status = swModelDocExt.SelectByID2("", "FACE", 0.0471052662929878, -0.0336338467782298, 0.0253999999998769, false, 0, null, 0);
            swFeature = (Feature)swFeatureMgr.HoleWizard5(4, 0, 27, "#0-80", 1, 0.00119126, 0.0254, 0.020066, 0, 0,
            0, 0, 0, 0, 1, 0, 0, -1, -1, -1,
            "2B", false, true, true, true, true, false);
            swModel.ViewZoomtofit2();
            status = swModelDocExt.SelectByID2("#0-80 Tapped Hole1", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            swFeature = (Feature)swSelectionMgr.GetSelectedObject6(1, -1);
            swModel.ClearSelection2(true);
            swWizardHoleFeatureData = (WizardHoleFeatureData2)swFeature.GetDefinition();
            count = swWizardHoleFeatureData.GetSketchPointCount();
            Debug.Print(" Number of sketch points in original Hole Wizard Feature = " + count);
            points = (object[])swWizardHoleFeatureData.GetSketchPoints();
            foreach (object point in points)
            {
                swSketchPoint = (SketchPoint)point;
                swSketchPoint.Select4(false, null);
            }
            status = swFeature.ModifyDefinition(swWizardHoleFeatureData, swModel, null);
            swModel.ClearSelection2(true);

            //Select sketch point of Hole Wizard feature
            //and add two sketch points to Hole Wizard feature
            status = swModelDocExt.SelectByID2("Sketch3", "SKETCH", 0, 0, 0, false, 0, null, 0);
            swSketchMgr.AddToDB = true;
            swModel.EditSketch();
            swSketchPoint = swSketchMgr.CreatePoint(0.01, -0.04, 0);
            swSketchPoint = swSketchMgr.CreatePoint(0.01, -0.02, 0);
            swSketchMgr.InsertSketch(true);
            swSketchMgr.AddToDB = false;
            swModel.ForceRebuild3(true);

            //Get number of sketch points in modified Hole Wizard feature
            status = swModelDocExt.SelectByID2("#0-80 Tapped Hole1", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            swFeature = (Feature)swSelectionMgr.GetSelectedObject6(1, -1);
            swModel.ClearSelection2(true);
            swWizardHoleFeatureData = (WizardHoleFeatureData2)swFeature.GetDefinition();
            count = swWizardHoleFeatureData.GetSketchPointCount();
            Debug.Print(" Number of sketch points in modified Hole Wizard Feature = " + count);
            points = (object[])swWizardHoleFeatureData.GetSketchPoints();
            foreach (object point in points)
            {
                swSketchPoint = (SketchPoint)point;
                swSketchPoint.Select4(false, null);
            }
            status = swFeature.ModifyDefinition(swWizardHoleFeatureData, swModel, null);
            swModel.ClearSelection2(true);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
