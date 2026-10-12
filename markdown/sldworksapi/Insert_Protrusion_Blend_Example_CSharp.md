---
title: "Insert Protrusion Blend Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Protrusion_Blend_Example_CSharp.htm"
---

# Insert Protrusion Blend Example (C#)

This example shows how to create a loft using profiles, guide curves, and a centerline.

```
//---------------------------------------------------------------
// Preconditions: Verify that the specified part template exists.
//
// Postconditions:
// 1. Creates a new part.
// 2. Creates a profile sketch.
// 3. Creates a reference plane and another profile sketch on that
//    reference plane.
// 4. Creates five curves: four guide curves and one centerline.
// 5. Selects the profile sketches, four guide curves, and the
//    centerline.
// 6. Creates a loft feature.
// 7. Examine the FeatureManager design tree and graphics area.
//---------------------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SketchSegment swSketchSegment = default(SketchSegment);
            SketchManager swSketchManager = default(SketchManager);
            RefPlane swRefPlane = default(RefPlane);
            FeatureManager swFeatureManager = default(FeatureManager);
            bool status = false;

            //Create new part
            swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SOLIDWORKS 2016\\templates\\Part.prtdot", 0, 0, 0);

            //Create profile sketch
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, false, 0, null, 0);
            swModel.ClearSelection2(true);
            swSketchManager = (SketchManager)swModel.SketchManager;
            swSketchSegment = (SketchSegment)swSketchManager.CreateEllipse(0, 0, 0, 0.0706113079019074, 0, 0, 0, 0.0374944141689373, 0);
            swModel.ClearSelection2(true);
            swSketchManager.InsertSketch(true);

            // Create reference plane and another profile sketch
            // on that reference plane
            status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, true, 0, null, 0);
            swFeatureManager = (FeatureManager)swModel.FeatureManager;
            swRefPlane = (RefPlane)swFeatureManager.InsertRefPlane(8, 0.07, 0, 0, 0, 0);
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, false, 0, null, 0);
            swSketchSegment = (SketchSegment)swSketchManager.CreateEllipse(0, 0, 0, 0.0527205722070845, 0, 0, 0, 0.0154164850136235, 0);
            swModel.ClearSelection2(true);
            swSketchManager.InsertSketch(true);

            // Create guide curves
            status = swModelDocExt.SelectByID2("Point4@Sketch1", "EXTSKETCHPOINT", 0, 0.0374944141689373, 0, false, 1, null, 0);
            status = swModelDocExt.SelectByID2("Point4@Sketch2", "EXTSKETCHPOINT", 0, 0.0154164850136235, 0, true, 1, null, 0);
            swModel.Insert3DSplineCurve(false);

            status = swModelDocExt.SelectByID2("Point5@Sketch2", "EXTSKETCHPOINT", -0.0527205722070845, 0, 0, true, 1, null, 0);
            status = swModelDocExt.SelectByID2("Point5@Sketch1", "EXTSKETCHPOINT", -0.0706113079019074, 0, 0, true, 1, null, 0);
            swModel.Insert3DSplineCurve(false);

            status = swModelDocExt.SelectByID2("Point6@Sketch2", "EXTSKETCHPOINT", 0, -0.0154164850136235, 0, true, 1, null, 0);
            status = swModelDocExt.SelectByID2("Point6@Sketch1", "EXTSKETCHPOINT", 0, -0.0374944141689373, 0, true, 1, null, 0);
            swModel.Insert3DSplineCurve(false);

            status = swModelDocExt.SelectByID2("Point3@Sketch2", "EXTSKETCHPOINT", 0.0527205722070845, 0, 0, true, 1, null, 0);
            status = swModelDocExt.SelectByID2("Point3@Sketch1", "EXTSKETCHPOINT", 0.0706113079019074, 0, 0, true, 1, null, 0);
            swModel.Insert3DSplineCurve(false);

            // Create centerline
            status = swModelDocExt.SelectByID2("Point2@Sketch2", "EXTSKETCHPOINT", 0, 0, 0, true, 1, null, 0);
            status = swModelDocExt.SelectByID2("Point2@Sketch1", "EXTSKETCHPOINT", 0, 0, 0, true, 1, null, 0);
            swModel.Insert3DSplineCurve(false);

            // Create loft
            status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0.0706113079019074, 0, 0, false, 1, null, 0);
            status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 0.0527205722070845, 0, 0.07, true, 1, null, 0);
            status = swModelDocExt.SelectByID2("Curve1", "REFERENCECURVES", 0.0999754519565386, 0.0447609702560072, 0.128010464418594, true, 4098, null, 0);
            status = swModelDocExt.SelectByID2("Curve2", "REFERENCECURVES", 0.037643674311596, 0.0221603475855119, 0.115437869126538, true, 8194, null, 0);
            status = swModelDocExt.SelectByID2("Curve3", "REFERENCECURVES", 0.0999909384372586, -0.000744308680111772, 0.131301605626447, true, 12290, null, 0);
            status = swModelDocExt.SelectByID2("Curve4", "REFERENCECURVES", 0.158600974878482, 0.0218780932746938, 0.129235804629445, true, 16386, null, 0);
            status = swModelDocExt.SelectByID2("Curve5", "REFERENCECURVES", 0.0998735089003162, 0.022159545044488, 0.108064927518626, true, 4, null, 0);
            swFeatureManager.InsertProtrusionBlend2(false, true, false, 1, 0, 0, 1, 1, true, true,
            false, 0, 0, 0, true, true, true, (int)swGuideCurveInfluence_e.swGuideCurveInfluenceNextEdge);
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
