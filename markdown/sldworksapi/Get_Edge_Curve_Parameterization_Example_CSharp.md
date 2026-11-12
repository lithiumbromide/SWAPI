---
title: "Get Edge Curve Parameterization Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Edge_Curve_Parameterization_Example_CSharp.htm"
---

# Get Edge Curve Parameterization Example (C#)

This example shows how to get curve parameterization data for a selected edge.

```vb
 //------------------------------------------------
 // Preconditions:
 // 1. Open a part or assembly.
 // 2. If you opened an assembly, ensure that it is
 //    fully resolved.
 // 3. Select an edge.
 // 4. Open an Immediate Window.
 //
 // Postconditions: Inspect the Immediate window.
 //-----------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;
 namespace GetCurveParams_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {

             ModelDoc2 Part = default(ModelDoc2);

             Part = (ModelDoc2)swApp.ActiveDoc;

             SelectionMgr swSelectMgr = default(SelectionMgr);
             swSelectMgr = (SelectionMgr)Part.SelectionManager;

             Edge swEdge = default(Edge);
             swEdge = (Edge)swSelectMgr.GetSelectedObject5(1);

             Curve swCurve = default(Curve);
             CurveParamData swCurveParaData = default(CurveParamData);
             swCurve = (Curve)swEdge.GetCurve();
             swCurveParaData = (CurveParamData)swEdge.GetCurveParams3();

             Debug.Print("The curve tag is: " + swCurveParaData.CurveTag);
             Debug.Print("The curve type as defined in swCurveType_e is: " + swCurveParaData.CurveType);

             double[] vEndPoint = null;
             vEndPoint = (double[])swCurveParaData.EndPoint;
             double[] EndPoint = new double[3];

             int i = 0;

             for (i = 0; i <= vEndPoint.GetUpperBound(0); i++)
             {
                 EndPoint[i] = vEndPoint[i];
             }

             Debug.Print("The end point x,y,z coordinates are: " + EndPoint[0] + "," + EndPoint[1] + "," + EndPoint[2]);

             double[] vStartPoint = null;
             double[] StartPoint = new double[3];
             vStartPoint = (double[])swCurveParaData.StartPoint;
             for (i = 0; i <= vStartPoint.GetUpperBound(0); i++)
             {
                 StartPoint[i] = vStartPoint[i];
             }

             Debug.Print("The start point x,y,z coordinates are: " + StartPoint[0] + "," + StartPoint[1] + "," + StartPoint[2]);

             Debug.Print("The curve and edge are in the same direction: " + swCurveParaData.Sense);
             Debug.Print("The maximum U parameter value is: " + swCurveParaData.UMaxValue);

             Debug.Print("The minimum U parameter value is: " + swCurveParaData.UMinValue);
         }

         public SldWorks swApp;

     }
 }
```
