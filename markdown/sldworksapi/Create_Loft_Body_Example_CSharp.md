---
title: "Create Loft Body Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Loft_Body_Example_CSharp.htm"
---

# Create Loft Body Example (C#)

This example shows how to create a temporary loft body using [IModeler::CreateLoftBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateLoftBody2.html).

```
//-----------------------------------------------------
// Preconditions:
// 1. Verify that the specified part document template
//    exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens a new part document.
// 2. Creates and selects sketches of two profiles and
//    a guide curve.
// 3. Creates a temporary loft body.
// 4. Examine the Immediate window and graphics area.
//-----------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace CreateLoftCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SketchManager swSketchMgr = default(SketchManager);
            SketchSegment sketchSegment = default(SketchSegment);
            SelectionMgr swSelMgr = default(SelectionMgr);
            SketchPoint sketchPoint = default(SketchPoint);
            FeatureManager swFeatureMgr = default(FeatureManager);
            RefPlane refPlane = default(RefPlane);
            Feature swFeat = default(Feature);
            bool status = false;
            object profiles = null;
            object guides = null;
            Feature[] profile = new Feature[2];
            Feature[] guideCurve = new Feature[1];
            Modeler swModeler = default(Modeler);
            Body2 swBody = default(Body2);
            int count = 0;
            object[] featArr = null;
            int i = 0;

            //Open new part document
            swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SolidWorks 2014\\templates\\Part.prtdot", 0, 0, 0);
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            //Create closed profile
            status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, false, 0, null, 0);
            swSketchMgr = (SketchManager)swModel.SketchManager;
            sketchSegment = (SketchSegment)swSketchMgr.CreateCircle(0.0, 0.0, 0.0, 0.021796, -0.030937, 0.0);
            sketchPoint = (SketchPoint)swSketchMgr.CreatePoint(0.023454, 0.029699, 0.0);
            swModel.ClearSelection2(true);
            swSketchMgr.InsertSketch(true);

            //Create another closed profile
            status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, true, 0, null, 0);
            swFeatureMgr = (FeatureManager)swModel.FeatureManager;
            refPlane = (RefPlane)swFeatureMgr.InsertRefPlane(8, 0.254, 0, 0, 0, 0);
            status = swModelDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, false, 0, null, 0);
            sketchSegment = (SketchSegment)swSketchMgr.CreateCircle(-0.035118, -0.014102, 0.0, -0.025452, -0.02953, 0.0);
            sketchPoint = (SketchPoint)swSketchMgr.CreatePoint(-0.018033, -0.020392, 0.0);
            swModel.ClearSelection2(true);
            swSketchMgr.InsertSketch(true);

            //Create guide curve
            status = swModelDocExt.SelectByID2("Point4@Sketch1", "EXTSKETCHPOINT", 0.0234541440502721, 0.0296993303358475, 0, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("Point5@Sketch2", "EXTSKETCHPOINT", -0.0180330744027628, -0.0203923494843098, 0, true, 0, null, 0);
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("Point4@Sketch1", "EXTSKETCHPOINT", 0.0234541440502721, 0.0296993303358475, 0, false, 1, null, 0);
            status = swModelDocExt.SelectByID2("Point5@Sketch2", "EXTSKETCHPOINT", -0.0180330744027628, -0.0203923494843098, 0, true, 1, null, 0);
            swModel.Insert3DSplineCurve(false);
            swModel.ClearSelection2(true);

            //Select guide curve and profiles for loft feature
            status = swModelDocExt.SelectByID2("Curve1", "REFERENCECURVES", 0, 0, 0, false, 2, null, 0);
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
            Debug.Print("Guide curve name: " + swFeat.Name);
            guideCurve[0] = (Feature)swFeat;
            guides = guideCurve;
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0.00984860021145358, 0.0365397341178567, 0, true, 1, null, 0);
            swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
            Debug.Print("Profile name: " + swFeat.Name);
            profile[0] = (Feature)swFeat;
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", -0.0401969362026636, 0.00338231877308527, 0, true, 1, null, 0);
            swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
            Debug.Print("Profile name: " + swFeat.Name);
            profile[1] = (Feature)swFeat;
            profiles = profile;
            swModel.ClearSelection2(true);

            //Create temporary loft body
            swModeler = (Modeler)swApp.GetModeler();
            swBody = (Body2)swModeler.CreateLoftBody2(swModel, profiles, guides, null, false, 0, 0, 0, true, false,
            true, false, true, 1, 1, 1, true, true, 1, 1,
            false);

            // Test whether the loft body is a temporary body
            status = swBody.IsTemporaryBody();
            Debug.Print("Is the loft body a temporary body?  " + status);
            if (status)
            {
                // Display the temporary loft body
                swBody.Display3(swModel, 256, (int)swTempBodySelectOptions_e.swTempBodySelectOptionNone);
                Debug.Print("Temporary loft body displayed; examine the graphics area.");
            }
            else
            {
                Debug.Print("Temporary loft body was not created.");
            }

            Debug.Print("");

            //Verify that the temporary loft body is not a loft feature
            //by examining the list of features printed to the
            //Immediate window
            count = swFeatureMgr.GetFeatureCount(false);
            featArr = (object[])swFeatureMgr.GetFeatures(false);
            for (i = 0; i < count - 1; i++)
            {
                swFeat = (Feature)featArr[i];
                Debug.Print(swFeat.Name);
            }

            swModel.ViewZoomtofit2();

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
