---
title: "Get UV Parameters for XYZ Location Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_UV_Parameters_For_XYZ_Location_Example_CSharp.htm"
---

# Get UV Parameters for XYZ Location Example (C#)

This example shows how to use IFace2 and ICurve interfaces to get the UV parameters from the XYZ location.

```vb
 //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Open  public_documents\samples\tutorial\cosmosxpress\aw_hook.sldprt.
 // 2. Verify that Tools > System Options > Options > FeatureManager > Solid Bodies
 //    drop-down selection is Show.
 // 3. Expand the Solid Bodies folder and select Split Line1.
 // 4. Open the Immediate window or modify the macro to write the output to a file.
 //
 // Postconditions: Observe the output in the Immediate window.
 //----------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;

 namespace ReverseEvalTestMIK_CSharp.csproj
{
    partial class SolidWorksMacro
    {
        ModelDoc2 swModel;
        SelectionMgr swSelMgr;
        Face2 swFace;

        public void Main()
        {
            swModel = (ModelDoc2)swApp.ActiveDoc;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            double[] pntData = new double[3];
            Body2 swBody = default(Body2);
            Body2 procBody = default(Body2);
            swBody = (Body2)swSelMgr.GetSelectedObject6(1, -1);
            procBody = swBody.GetProcessedBody2(0.5, 0.5);
            //Bypass surface split
            swFace = (Face2)procBody.GetFirstFace();
            //Set swFace = swBody.GetFirstFace
            while ((swFace != null))
            {
                double[] uvBnds = null;
                uvBnds = (double[])swFace.GetUVBounds();
                double UminFace = 0;
                double UmaxFace = 0;
                double VminFace = 0;
                double VmaxFace = 0;
                UminFace = uvBnds[0];
                UmaxFace = uvBnds[1];
                VminFace = uvBnds[2];
                VmaxFace = uvBnds[3];
                Surface swSurf = default(Surface);
                swSurf = (Surface)swFace.GetSurface();
                uvBnds = (double[])swSurf.Parameterization();
                double UminSurf = 0;
                double UmaxSurf = 0;
                double VminSurf = 0;
                double VmaxSurf = 0;
                UminSurf = uvBnds[0];
                UmaxSurf = uvBnds[1];
                VminSurf = uvBnds[2];
                VmaxSurf = uvBnds[3];
                object[] vEdges = null;
                vEdges = (object[])swFace.GetEdges();
                int i = 0;
                for (i = 0; i <= vEdges.GetUpperBound(0); i++)
                {
                    Edge swEdge = default(Edge);
                    swEdge = (Edge)vEdges[i];
                    Curve swCurve = default(Curve);
                    swCurve = (Curve)swEdge.GetCurve();
                    double[] vCurveParams = null;
                    vCurveParams = (double[])swEdge.GetCurveParams2();
                    double startParam = 0;
                    double endParam = 0;
                    double incParam = 0;
                    double curParam = 0;
                    startParam = vCurveParams[6];
                    endParam = vCurveParams[7];
                    incParam = (endParam - startParam) / 10.0;
                    curParam = startParam;
                    while (curParam < endParam)
                    {
                        double[] vEdgePnt = null;
                        vEdgePnt = (double[])swEdge.Evaluate(curParam);
                        double[] vUVSurfParams = null;
                        double UEdge = 0;
                        double VEdge = 0;
                        // Get the UV parameters for the point using IFace2::ReverseEvaluate
                        vUVSurfParams = (double[])swFace.ReverseEvaluate(vEdgePnt[0], vEdgePnt[1], vEdgePnt[2]);
                        if ((vUVSurfParams != null))
                        {
                            UEdge = vUVSurfParams[0];
                            VEdge = vUVSurfParams[1];
                            Debug.Print("Edge point: " + " x: " + vEdgePnt[0] + " y: " + vEdgePnt[1] + " z: " + vEdgePnt[2]);
                            Debug.Print("U parameter returned from IFace2::ReverseEvaluate is " + UEdge);
                            if (UEdge > UmaxFace | UEdge < UminFace)
                            {
                                Debug.Print("U param error face");
                            }
                            //Stop
                            Debug.Print("V parameter returned from IFace2::ReverseEvalute is " + VEdge);
                            if (VEdge > VmaxFace | VEdge < VminFace)
                            {
                                Debug.Print("V param error face");
                            }
                            //Stop
                        }
                        else
                        {
                            Debug.Print("Face reverse evaluate fails - empty data");
                        }
                        // Get the UV parameters for the point using ICurve::ReverseEvaluate
                        vUVSurfParams = (double[])swSurf.ReverseEvaluate(vEdgePnt[0], vEdgePnt[1], vEdgePnt[2]);
                        if ((vUVSurfParams != null))
                        {
                            UEdge = vUVSurfParams[0];
                            VEdge = vUVSurfParams[1];
                            Debug.Print("U parameter returned from ICurve::ReverseEvaluate is " + UEdge);
                            if (UEdge > UmaxFace | UEdge < UminFace)
                            {
                                Debug.Print("U param error surface");
                            }
                            //Stop
                            Debug.Print("V parameter returned from ICurve::ReverseEvaluate is " + VEdge);
                            if (VEdge > VmaxFace | VEdge < VminFace)
                            {
                                Debug.Print("V param error surface");
                            }
                            //Stop
                        }
                        curParam = curParam + incParam;
                    }
                }
                swFace = (Face2)swFace.GetNextFace();
            }
            Debug.Print("Complete");
        }
        public SldWorks swApp;
    }
}
```
