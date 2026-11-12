---
title: "Get Each Spline's Parameters Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Each_Splines_Parameters_Example_CSharp.htm"
---

# Get Each Spline's Parameters Example (C#)

This example shows how to get each spline's parameters in a sketch containing multiple splines.

```
//----------------------------------------------------
// Preconditions:
// 1. Verify that the specified part template exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Creates a sketch containing two splines.
// 2. Gets each spline's dimension, order, periodicity,
//    control point, and knot point data.
// 3. Examine the Immediate window.
//-----------------------------------------------------
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
            SelectionMgr swSelMgr = default(SelectionMgr);
            SketchSegment swSketchSegment = default(SketchSegment);
            Feature swFeature = default(Feature);
            Sketch swSketch = default(Sketch);
            SplineParamData swSplineParamData = default(SplineParamData);
            SketchManager swSketchMgr = default(SketchManager);
            double[] points = new double[12];
            object pointArray = null;
            object varCtrlPoints = null;
            double[] ctrlPoints;
            object varKnotPoints = null;
            double[] knotPoints;
            bool status = false;
            int i = 0;
            int j = 0;
            int k = 0;
            int splineCount = 0;
            int splinePointCount = 0;

            swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SOLIDWORKS 2017\\templates\\Part.prtdot", 0, 0, 0);

            //Create a sketch with two splines
            //First spline
            points[0] = -0.185955019567672;
            points[1] = 0.0416208582005027;
            points[2] = 0;
            points[3] = -0.0862492383138544;
            points[4] = 0.0403922105323034;
            points[5] = 0;
            points[6] = -0.0672740896322921;
            points[7] = 0.0540598971292923;
            points[8] = 0;
            points[9] = -0.0141436733240425;
            points[10] = -0.00570437188125084;
            points[11] = 0;
            pointArray = points;
            swSketchMgr = swModel.SketchManager;
            swSketchSegment = swSketchMgr.CreateSpline((pointArray));
            swModel.ClearSelection2(true);
            //Second spline
            points[0] = -0.0838342193907238;
            points[1] = -0.0380341664350112;
            points[2] = 0;
            points[3] = -0.0655490761158148;
            points[4] = -0.0179490921124739;
            points[5] = 0;
            points[6] = -0.0179387030603664;
            points[7] = -0.0681344637902441;
            points[8] = 0;
            points[9] = 0.0634819349185705;
            points[10] = -0.0329692207162395;
            points[11] = 0;
            pointArray = points;
            swSketchSegment = (SketchSegment)swSketchMgr.CreateSpline((pointArray));
            swModel.ClearSelection2(true);
            //Sketch
            swSketchMgr.InsertSketch(true);

            //Get each spline's dimension, order, periodicity, control point, and knot data
            status = swModel.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, false, 0, null, (int)swSelectOption_e.swSelectOptionDefault);
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swFeature = (Feature)swSelMgr.GetSelectedObject6(1, -1);
            swSketch = (Sketch)swFeature.GetSpecificFeature2();
            Debug.Print(swFeature.Name);
            Debug.Print("");
            splineCount = swSketch.GetSplineCount(ref splinePointCount);
            for (i = 1; i <= splineCount; i++)
            {
                Debug.Print("Spline " + i + ": ");
                swSplineParamData = (SplineParamData)swSketch.GetSplineParams5(true, i - 1);
                Debug.Print("  Dimension: " + swSplineParamData.Dimension);
                Debug.Print("  Order: " + swSplineParamData.Order);
                Debug.Print("  Periodicity: " + swSplineParamData.Periodic);
                Debug.Print("  Number of control points: " + swSplineParamData.ControlPointsCount);
                status = swSplineParamData.GetControlPoints(out varCtrlPoints);
                Debug.Print("  Control points:");
                ctrlPoints = (double[])varCtrlPoints;
                for (j = 0; j <= ctrlPoints.GetUpperBound(0); j++)
                {
                    Debug.Print("      " + ctrlPoints[j].ToString());
                }
                Debug.Print("  Number of knots: " + swSplineParamData.KnotPointsCount);
                status = swSplineParamData.GetKnotPoints(out varKnotPoints);
                Debug.Print("    Knot points:");
                knotPoints = (double[])varKnotPoints;
                for (k = 0; k <= knotPoints.GetUpperBound(0); k++)
                {
                    Debug.Print("      " + knotPoints[k].ToString());
                }
            }

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
