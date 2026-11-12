---
title: "Change Linear Pattern Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Linear_Pattern_Example_CSharp.htm"
---

# Change Linear Pattern Example (C#)

This example shows how to change a linear pattern from a bodies to a features and faces pattern.

```
//-----------------------------------------------------------
// Preconditions:
// 1. Verify that the specified part template exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens a new part.
// 2. Creates three boss extrude features.
// 3. Creates a linear pattern using Boss-Extrude2 as a bodies
//    pattern.
// 4. Examine the graphics area and press F5.
// 5. Changes the linear pattern to use Boss-Extrude3 as a
//    features and faces pattern.
// 6. Examine the Immediate window and graphics area.
//------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System.Diagnostics;

namespace Macro1CSharp.csproj
{
    partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SketchManager swSketchMgr = default(SketchManager);
            FeatureManager swFeatureMgr = default(FeatureManager);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            SketchSegment swSketchSegment = default(SketchSegment);
            Feature swFeature = default(Feature);
            LinearPatternFeatureData swLinearPatternFeatureData = default(LinearPatternFeatureData);
            object[] sketchSegments = null;
            bool status = false;
            Feature obj = null;
            Feature[] patternFeatures = new Feature[1];

            swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SOLIDWORKS 2015\\templates\\Part.prtdot", 0, 0, 0);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swSketchMgr = (SketchManager)swModel.SketchManager;
            swFeatureMgr = (FeatureManager)swModel.FeatureManager;
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;

            //Create boss extrudes
            status = swModelDocExt.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swSketchAddConstToRectEntity, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified, false);
            status = swModelDocExt.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified, true);
            sketchSegments = (object[])swSketchMgr.CreateCornerRectangle(0, 0, 0, -0.113876153512535, -0.101331667625686, 0);
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, false, 0, null, 0);
            status = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("Line4", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("Line3", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            swFeature = (Feature)swFeatureMgr.FeatureExtrusion3(true, false, false, 0, 0, 0.00254, 0.00254, false, false, false,
            false, 0.0174532925199433, 0.0174532925199433, false, false, false, false, true, true, true,
            0, 0, false);
            swSelectionMgr.EnableContourSelection = false;
            status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, false, 0, null, 0);
            swModel.ClearSelection2(true);
            swSketchSegment = (SketchSegment)swSketchMgr.CreateCircle(-0.105874, -0.015731, 0.0, -0.099776, -0.0152, 0.0);
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("Arc1", "SKETCHSEGMENT", 0, 0, 0, false, 0, null, 0);
            swFeature = (Feature)swFeatureMgr.FeatureExtrusion3(true, false, false, 0, 0, 0.01778, 0.00254, false, false, false,
            false, 0.0174532925199433, 0.0174532925199433, false, false, false, false, false, true, true,
            0, 0, false);
            swSelectionMgr.EnableContourSelection = false;
            status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, false, 0, null, 0);
            swModel.ClearSelection2(true);
            status = swModelDocExt.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swSketchAddConstToRectEntity, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified, false);
            status = swModelDocExt.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified, true);
            sketchSegments = (object[])swSketchMgr.CreateCornerRectangle(-0.10892213539114, -0.0783168275860362, 0, -0.0879628279544704, -0.0928855015339991, 0);
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, false, 0, null, 0);
            status = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("Line4", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("Line3", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            swFeature = (Feature)swFeatureMgr.FeatureExtrusion3(true, false, false, 0, 0, 0.01778, 0.01778, false, false, false,
            false, 0.0174532925199433, 0.0174532925199433, false, false, false, false, false, true, true,
            0, 0, false);
            swSelectionMgr.EnableContourSelection = false;

            //Create linear pattern using Boss-Extrude2 as bodies pattern
            status = swModelDocExt.SelectByID2("", "EDGE", -0.091185205959107, -2.85588595829722E-05, 0.00255940246768205, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("Boss-Extrude2", "SOLIDBODY", 0, 0, 0, true, 0, null, 0);
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("", "EDGE", -0.091185205959107, -2.85588595829722E-05, 0.00255940246768205, true, 1, null, 0);
            status = swModelDocExt.SelectByID2("Boss-Extrude2", "SOLIDBODY", 0, 0, 0, true, 256, null, 0);
            swFeature = (Feature)swFeatureMgr.FeatureLinearPattern4(3, 0.0254, 1, 0.00254, true, false, "NULL", "NULL", false, false,
            false, false, false, false, true, true, false, false, 0, 0);

            System.Diagnostics.Debugger.Break();
            //Examine the graphics area
            //Press F5

            //Select LPattern1
            //Get whether LPattern1n is a features and faces pattern or a bodies pattern
            status = swModelDocExt.SelectByID2("LPattern1", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            swFeature = (Feature)swSelectionMgr.GetSelectedObject6(1, -1);
            swLinearPatternFeatureData = (LinearPatternFeatureData)swFeature.GetDefinition();
            swLinearPatternFeatureData.AccessSelections(swModel, null);
            Debug.Print("Original LPattern1 is a features and faces pattern or a bodies pattern (true if a bodies pattern)? " + swLinearPatternFeatureData.BodyPattern);

            //Change LPattern1 to features and faces pattern
            status = swModelDocExt.SelectByID2("Boss-Extrude3", "BODYFEATURE", 0, 0, 0, true, 0, null, 0);
            obj = (Feature)swSelectionMgr.GetSelectedObject6(1, 0);
            patternFeatures[0] = (Feature)obj;
            DispatchWrapper[] patternFeaturesArray = null;
            patternFeaturesArray = (DispatchWrapper[])ObjectArrayToDispatchWrapperArray(patternFeatures);
            swLinearPatternFeatureData.BodyPattern = false;
            swLinearPatternFeatureData.PatternFeatureArray = patternFeaturesArray;

            swFeature.ModifyDefinition(swLinearPatternFeatureData, swModel, null);

            //Get whether LPattern1 is a features and faces pattern or a bodies pattern
            Debug.Print("Modified LPattern1 is a features and faces pattern or a bodies pattern (false if a features and faces pattern)? " + swLinearPatternFeatureData.BodyPattern);

        }

        public DispatchWrapper[] ObjectArrayToDispatchWrapperArray(object[] Objects)
        {
            int ArraySize = 0;
            ArraySize = Objects.GetUpperBound(0);
            DispatchWrapper[] d = new DispatchWrapper[ArraySize + 1];
            int ArrayIndex = 0;
            for (ArrayIndex = 0; ArrayIndex <= ArraySize; ArrayIndex++)
            {
                d[ArrayIndex] = new DispatchWrapper(Objects[ArrayIndex]);
            }
            return d;

        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>

        public SldWorks swApp;

    }
}
```
