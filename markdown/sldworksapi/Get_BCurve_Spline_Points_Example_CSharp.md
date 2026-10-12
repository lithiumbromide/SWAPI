---
title: "Get BCurve Spline Points Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_BCurve_Spline_Points_Example_CSharp.htm"
---

# Get BCurve Spline Points Example (C#)

This example shows how to get B-spline parameter data (knots, control points, etc.) for a selected spline
or curve.

```
//---------------------------------------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\molds\telephone.sldprt.
// 2. Select a curve.
// 3. Open the Immediate Window.
//
// Postconditions: Examine the Immediate window.
//----------------------------------------------------------------------------

	using SolidWorks.Interop.sldworks;

	using SolidWorks.Interop.swconst;

	using System;

	using System.Diagnostics;

	namespace GetBSplineParamData_CSharp.csproj

	{

	    partial class SolidWorksMacro

	    {

	        public void Main()

	        {

	            ModelDoc2 Part = null;

	            Part = (ModelDoc2)swApp.ActiveDoc;

	            SelectionMgr swSelectMgr = null;

	            swSelectMgr = (SelectionMgr)Part.SelectionManager;

	            IEdge swSketchSeg = null;

	            swSketchSeg = (ISketchSegment)swSelectMgr.GetSelectedObject6(1,-1);

	            Curve swCurveIn = null;

	            SplineParamData swSplineParaData = default(SplineParamData);

	            object varCtrlPoints = null;

	            object varKnotPoints = null;

	            bool boolStatus = false;

	            int i = 0;

	            swCurveIn = (Curve)swSketchSeg.GetCurve();

	            Debug.Print("");

	            Debug.Print("B-spline");

	            Debug.Print("");

	            swSplineParaData = (SplineParamData)swCurveIn.GetBCurveParams5(false, false, true, true);

	            Debug.Print("The dimension is: " + swSplineParaData.Dimension);

	            Debug.Print("The order is: " + swSplineParaData.Order);

	            Debug.Print("The periodicity is: " + swSplineParaData.Periodic);

	            Debug.Print("The control point count is: " + swSplineParaData.ControlPointsCount);

	            Debug.Print("The knot point count is: " + swSplineParaData.KnotPointsCount);

	            Debug.Print("COLORREF of spline: " + swSplineParaData.Color);

	            Debug.Print("Layer of spline: " + swSplineParaData.Layer);

	            Debug.Print("Style overrides as defined in swLayerOverride_e: " + swSplineParaData.LayerOverride);

	            Debug.Print("Line style as defined in swLineStyles_e:: " + swSplineParaData.LineStyle);

	            Debug.Print("Line weight at defined in swLineWeights_e: " + swSplineParaData.LineWidth);

	        }

	        public SldWorks swApp;

	    }

	}
```
