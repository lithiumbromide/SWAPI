---
title: "Get B-Spline Surface Parameterization Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_B-Spline_Surface_Parameterization_Data_Example_CSharp.htm"
---

# Get B-Spline Surface Parameterization Data Example (C#)

This example shows how to get B-spline parameterization data for a selected face or surface.

```
//----------------------------------------------------------------------------
// Preconditions:
// 1.  Open public_documents\samples\tutorial\molds\telephone.sldprt.
// 2.  Select a face.
// 3.  Open the Immediate Window.
//
// Postconditions: Examine the Immediate window.
//----------------------------------------------------------------------------
```

```vb
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;
 namespace MacroBSurf_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {

             ModelDoc2 swModel = default(ModelDoc2);
             SelectionMgr swSelMgr = default(SelectionMgr);
             Face2 swFace = default(Face2);
             Surface swSurf = default(Surface);
             SurfaceParameterizationData swSurfParam = default(SurfaceParameterizationData);
             BSurfParamData swBSurfParam = default(BSurfParamData);
             bool sense = false;
             object UKnots = null;
             object VKnots = null;
             object vCtrlPts = null;
             int i = 0;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swFace = (Face2)swSelMgr.GetSelectedObject5(1);
             swSurf = (Surface)swFace.GetSurface();
             swSurfParam = (SurfaceParameterizationData)swSurf.Parameterization2();
             Debug.Print("File = " + swModel.GetPathName());
             Debug.Print(" Surface:");
             Debug.Print(" U minimum is: " + swSurfParam.UMin);
             Debug.Print(" U minimum bound type is: " + swSurfParam.UMinBoundType);
             Debug.Print(" U maximum is: " + swSurfParam.UMax);
             Debug.Print(" U maximum bound type is: " + swSurfParam.UMaxBoundType);
             Debug.Print(" U property count is: " + swSurfParam.UPropertyNumber);
             object varUProperties = null;
             int[] uProperties;
             varUProperties = swSurfParam.UProperties;
             uProperties = (int[])varUProperties;
             Debug.Print(" U properties: ");
             for (i = 0; i <= uProperties.GetUpperBound(0); i++)
             {
                 Debug.Print(" " + uProperties[i]);
             }

             Debug.Print(" V minimum is: " + swSurfParam.VMin);
             Debug.Print(" V minimum bound type is: " + swSurfParam.VMinBoundType);
             Debug.Print(" V maximum is: " + swSurfParam.VMax);
             Debug.Print(" V maximum bound type is: " + swSurfParam.VMaxBoundType);
             Debug.Print(" V property count is: " + swSurfParam.VPropertyNumber);
             object varVProperties = null;
             int[] vProperties;
             varVProperties = swSurfParam.VProperties;
             vProperties = (int[])varVProperties;
             Debug.Print(" V properties: ");
             for (i = 0; i <= vProperties.GetUpperBound(0); i++)
             {
                 Debug.Print(" " + vProperties[i]);
             }

             swBSurfParam = (BSurfParamData)swSurf.GetBSurfParams3(false, false, swSurfParam, 0.01, out sense);

             Debug.Print("U order is: " + swBSurfParam.UOrder);
             Debug.Print("V order is: " + swBSurfParam.VOrder);
             Debug.Print(" Control point column count is: " + swBSurfParam.ControlPointColumnCount);
             Debug.Print(" Control point row count is: " + swBSurfParam.ControlPointRowCount);
             Debug.Print(" Control point dimension is: " + swBSurfParam.ControlPointDimension);
             Debug.Print(" U periodicity is: " + swBSurfParam.UPeriodicity);
             Debug.Print(" V periodicity is: " + swBSurfParam.VPeriodicity);

             UKnots = swBSurfParam.UKnots;
             double[] uknots;
             uknots = (double[])UKnots;
             Debug.Print("Knot vector in the U direction: ");
             for (i = 0; i <= uknots.GetUpperBound(0); i++)
             {
                 Debug.Print(uknots[i].ToString());
             }
             VKnots = swBSurfParam.VKnots;
             double[] vknots;
             vknots = (double[])VKnots;
             Debug.Print("Knot vector in the V direction: ");
             for (i = 0; i <= vknots.GetUpperBound(0); i++)
             {
                 Debug.Print(vknots[i].ToString());
             }

             // Get control points in row = 2, column = 3 of the control point matrix
             vCtrlPts = swBSurfParam.GetControlPoints(2, 3);
             double[] ctrlpts;
             ctrlpts = (double[])vCtrlPts;
             Debug.Print("Control point at row=2 and column=3: ");
             for (i = 0; i <= ctrlpts.GetUpperBound(0); i++)
             {
                 Debug.Print(ctrlpts[i].ToString());
             }
         }

         public SldWorks swApp;

     }
 }
```
