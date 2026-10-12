---
title: "Create and Access Curve-driven Pattern Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_and_Access_Curve-driven_Pattern_Feature_Example_CSharp.htm"
---

# Create and Access Curve-driven Pattern Feature Example (C#)

This example shows how to create a curve-driven pattern feature and access its data.

```
//--------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified part document to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified part document.
// 2. Creates a cut extrude feature.
// 3. Creates a curve-driven pattern feature using the
//    the cut extrude feature.
// 4. Gets curve-driven pattern feature data.
// 5. Examine the FeatureManager design tree, graphics area,
//    and Immediate window.
//
// NOTE: Because the part is used elsewhere, do not save changes.
//--------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace CurveDrivenPatternFeatureCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SketchManager swSketchMgr = default(SketchManager);
            SketchSegment swSketchSegment = default(SketchSegment);
            FeatureManager swFeatureMgr = default(FeatureManager);
            Feature swFeature = default(Feature);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            CurveDrivenPatternFeatureData swCurveDrivenPatternFeatureData = default(CurveDrivenPatternFeatureData);
            Entity swEntity = default(Entity);
            object patternDirection = null;
            string fileName = null;
            bool status = false;
            int errors = 0;
            int warnings = 0;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2019\\samples\\tutorial\\api\\bagel.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

            //Sketch a circle and create a cut extrude
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("", "FACE", 0.0118560192339032, 0, 0.0566664535234693, false, 0, null, 0);
            swSketchMgr = (SketchManager)swModel.SketchManager;
            swSketchMgr.InsertSketch(true);
            swSketchSegment = (SketchSegment)swSketchMgr.CreateCircle(-0.059172, -0.048012, 0.0, -0.044189, -0.040533, 0.0);
            swSketchMgr.InsertSketch(true);
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("Sketch6", "SKETCH", 0, 0, 0, false, 0, null, 0);
            swFeatureMgr = (FeatureManager)swModel.FeatureManager;
            swFeature = (Feature)swFeatureMgr.FeatureCut3(true, false, false, 1, 0, 0.00254, 0.00254, false, false, false,
            false, 0.0174532925199433, 0.0174532925199433, false, false, false, false, false, true, true,
            true, true, false, 0, 0, false);
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swSelectionMgr.EnableContourSelection = false;
            swModel.ActivateSelectedFeature();
            status = swModelDocExt.SelectByID2("", "EDGE", 0.0115207253109588, -8.89643058599177E-06, 0.0754182969300832, true, 0, null, 0);
            swModel.ClearSelection2(true);

            //Create curve-driven pattern feature
            status = swModelDocExt.SelectByID2("Cut-Extrude2", "BODYFEATURE", 0, 0, 0, false, 4, null, 0);
            status = swModelDocExt.SelectByID2("", "EDGE", 0.0115207253109588, -8.89643058599177E-06, 0.0754182969300832, true, 1, null, 0);
```

```vb
            swCurveDrivenPatternFeatureData = (CurveDrivenPatternFeatureData)swFeatureMgr.CreateDefinition((int)swFeatureNameID_e.swFmCurvePattern);

            swCurveDrivenPatternFeatureData.D1AlignmentMethod = 0;
             swCurveDrivenPatternFeatureData.D1CurveMethod = 0;
             swCurveDrivenPatternFeatureData.D1InstanceCount = 3;
             swCurveDrivenPatternFeatureData.D1IsEqualSpaced = true;
             swCurveDrivenPatternFeatureData.D1ReverseDirection = false;
             swCurveDrivenPatternFeatureData.D1Spacing = 0.0254;

            swFeature = (Feature)swFeatureMgr.CreateFeature(swCurveDrivenPatternFeatureData);
```

```
            //Access the curve-driven pattern feature
            status = swModelDocExt.SelectByID2("CrvPattern1", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            swFeature = (Feature)swSelectionMgr.GetSelectedObject6(1, -1);
            swCurveDrivenPatternFeatureData = (CurveDrivenPatternFeatureData)swFeature.GetDefinition();
            status = swCurveDrivenPatternFeatureData.AccessSelections(swModel, null);
            Debug.Print("Number of pattern instances in Direction 1: " + swCurveDrivenPatternFeatureData.D1InstanceCount);
            Debug.Print("Alignment method of Direction 1: " + swCurveDrivenPatternFeatureData.D1AlignmentMethod);
            Debug.Print("Curve method of Direction 1: " + swCurveDrivenPatternFeatureData.D1CurveMethod);
            patternDirection = swCurveDrivenPatternFeatureData.D1Direction;
            swEntity = (Entity)patternDirection;
            Debug.Print("Pattern direction object type of Direction 1: " + swEntity.GetType());
            Debug.Print("Pattern instances spaced equally in Direction 1? " + swCurveDrivenPatternFeatureData.D1IsEqualSpaced);
            Debug.Print("Pattern direction reversed in Direction 1? " + swCurveDrivenPatternFeatureData.D1ReverseDirection);
            Debug.Print("Number of seed bodies in pattern: " + swCurveDrivenPatternFeatureData.GetPatternBodyCount());
            Debug.Print("Number of seed features in pattern: " + swCurveDrivenPatternFeatureData.GetPatternFeatureCount());
            swCurveDrivenPatternFeatureData.ReleaseSelectionAccess();

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
