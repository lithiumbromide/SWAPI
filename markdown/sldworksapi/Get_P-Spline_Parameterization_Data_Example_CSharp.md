---
title: "Get P-Spline Parameterization Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_P-Spline_Parameterization_Data_Example_CSharp.htm"
---

# Get P-Spline Parameterization Data Example (C#)

This example shows how to get P-spline parameter data for a selected spline or curve.

```vb
 //---------------------------------------------------------------------------
 // Preconditions:
 // 1.  Open public_documents\samples\tutorial\molds\telephone.sldprt.
 // 2.  Select a curved edge of Shell1 in the graphics area.
 // 3.  Open an Immediate Window.
 //
 // Postconditions:
 // 1. Gets the P-spline parameter data for the selected curved edge.
 // 2. Inspect the Immediate window.
 //---------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;
 namespace GetPSplineParamData_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {

             ModelDoc2 Part = null;
             Part = (ModelDoc2)swApp.ActiveDoc;

             SelectionMgr swSelectMgr = null;
             swSelectMgr = (SelectionMgr)Part.SelectionManager;

             Edge swSketchSeg = null;
             swSketchSeg = (Edge)swSelectMgr.GetSelectedObject6(1, -1);

             Curve swCurveIn = null;
             SplineParamData swSplineParaData = default(SplineParamData);
             object varCtrlPoints = null;
             object varKnotPoints = null;
             bool boolStatus = false;
             int i = 0;
             double[] knotPoints;
             double[] ctrlPoints;

             swCurveIn = (Curve)swSketchSeg.GetCurve();
             swSplineParaData = (SplineParamData)swCurveIn.GetPCurveParams2();

             Debug.Print("P-spline");
             Debug.Print("");
             Debug.Print("The dimension is: " + swSplineParaData.Dimension);
             Debug.Print("The order is: " + swSplineParaData.Order);
             Debug.Print("The periodicity is: " + swSplineParaData.Periodic);
             Debug.Print("The knot count is: " + swSplineParaData.KnotPointsCount);
             Debug.Print("Knots: ");
             boolStatus = swSplineParaData.GetKnotPoints(out varKnotPoints);
             knotPoints = (double[])varKnotPoints;
             for (i = 0; i <= knotPoints.GetUpperBound(0); i++)
             {

                 Debug.Print(knotPoints[i].ToString());
             }
             Debug.Print("The segment count is: " + swSplineParaData.SegmentCount);
             boolStatus = swSplineParaData.GetSegments(out varCtrlPoints);
             ctrlPoints = (double[])varCtrlPoints;
             Debug.Print((swSplineParaData.SegmentCount * swSplineParaData.Dimension * swSplineParaData.Order) +  " Coefficients: ");
             for (i = 0; i <= ctrlPoints.GetUpperBound(0); i++)
             {

                 Debug.Print(ctrlPoints[i].ToString());
             }

             Debug.Print("");

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
