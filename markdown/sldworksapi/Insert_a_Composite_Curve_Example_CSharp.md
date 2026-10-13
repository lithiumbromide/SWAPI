---
title: "Insert a Composite Curve Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_a_Composite_Curve_Example_CSharp.htm"
---

# Insert a Composite Curve Example (C#)

This example shows how to insert a composite curve using two sketches of splines.

```
//--------------------------------------------------------
// Preconditions:
// 1. Verify that the part document template exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens a new part document.
// 2. Creates a sketch of a spline.
// 3. Creates another sketch of a spline.
// 4. Inserts a composite curve using the sketches created
//    in steps 2 and 3.
// 5. Prints the number of joined entities in the composite
//    curve to the Immediate window.
// 6. Examine the Immediate window.
//---------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace CompositeCurveCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            SketchSegment swSketchSegment = default(SketchSegment);
            SketchManager swSketchManager = default(SketchManager);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            CompositeCurveFeatureData swCompositeCurveFeatureData = default(CompositeCurveFeatureData);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            Feature swFeature = default(Feature);
            object pointArray = null;
            double[] points = null;
            bool status = false;
            int nbrEntities = 0;

            swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SolidWorks 2015\\templates\\Part.prtdot", 0, 0, 0);

            //Create sketch containing a spline
            swSketchManager = (SketchManager)swModel.SketchManager;
            swSketchManager.InsertSketch(true);
            Array.Resize(ref points, 12);
            points[0] = -0.0509020857536935;
            points[1] = 0.0116459784886342;
            points[2] = 0;
            points[3] = -0.0404337904830111;
            points[4] = 0.0249930549587544;
            points[5] = 0;
            points[6] = 0.0396486683377099;
            points[7] = -0.0166184187422084;
            points[8] = 0;
            points[9] = 0.0166184187422084;
            points[10] = -0.0399103757194769;
            points[11] = 0;
            pointArray = points;
            swSketchSegment = swSketchManager.CreateSpline2((pointArray), true);
            swModel.ClearSelection2(true);

            //Create another sketch containing a spline
            swSketchManager.InsertSketch(true);
            Array.Resize(ref points, 12);
            points[0] = -0.0509020857536935;
            points[1] = 0.0116459784886342;
            points[2] = 0;
            points[3] = -0.0370315945200393;
            points[4] = -0.00850548990742951;
            points[5] = 0;
            points[6] = 0.00562670870799184;
            points[7] = -0.014786467069839;
            points[8] = 0;
            points[9] = 0.0166184187422084;
            points[10] = -0.0399103757194769;
            points[11] = 0;
            pointArray = points;
            swSketchSegment = (SketchSegment)swSketchManager.CreateSpline2((pointArray), true);
            swSketchManager.InsertSketch(true);
            swModel.ClearSelection2(true);

            //Insert a composite curve using both sketches
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, false, 1, null, 0);
            status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, true, 1, null, 0);
            swModel.InsertCompositeCurve();

            //Get the number of joined entities in the composite curve
            status = swModelDocExt.SelectByID2("CompCurve1", "REFERENCECURVES", 0, 0, 0, false, 0, null, 0);
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swFeature = (Feature)swSelectionMgr.GetSelectedObject6(1, -1);
            swCompositeCurveFeatureData = (CompositeCurveFeatureData)swFeature.GetDefinition();
            nbrEntities = swCompositeCurveFeatureData.GetEntitiesToJoinCount();
            Debug.Print("Number of joined entities: " + nbrEntities.ToString());

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
