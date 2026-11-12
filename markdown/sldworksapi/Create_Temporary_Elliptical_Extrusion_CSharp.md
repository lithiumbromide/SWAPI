---
title: "Create Temporary Elliptical Extrusion Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Temporary_Elliptical_Extrusion_CSharp.htm"
---

# Create Temporary Elliptical Extrusion Example (C#)

This example shows how to create a temporary elliptical body.

```vb
 //------------------------------------------------
 // Preconditions:
 // 1. Open a model document in SOLIDWORKS Design.
 // 2. Open an Immediate Window.
 //
 // Postconditions:
 // 1. Creates a temporary elliptical extruded body.
 // 2. Inspect the Immediate Window.
 //------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;

 namespace CreateTempExtrudedBody_CSharp.csproj
 {
     partial class SolidWorksMacro
     {
         public void Main()
         {
             ModelDoc2 swDocument = default(ModelDoc2);
             PartDoc swPart = default(PartDoc);
             Modeler swModeler = default(Modeler);

             Curve[] swCurve = new Curve[1];
             object vCenter = null;
             double dMajorRadius = 0;
             double dMinorRadius = 0;
             object vMajorAxis = null;
             object vMinorAxis = null;
             double[] vEllipseParams = null;
             double[] aCenter = new double[3];
             double[] aMajorAxis = new double[3];
             double[] aMinorAxis = new double[3];
             double dStartParam = 0;
             double dEndParam = 0;
             bool bIsClosed = false;
             bool bIsPeriodic = false;
             bool bStatus = false;

             swDocument = (ModelDoc2)swApp.ActiveDoc;

             if ((swDocument == null))
             {
                 swDocument = (ModelDoc2)swApp.NewPart();
             }

             if ((swDocument.GetType() != (int)swDocumentTypes_e.swDocPART))
             {
                 return;
             }

             swPart = (PartDoc)swDocument;
             swModeler = (Modeler)swApp.GetModeler();

             aCenter[0] = 0.0;
             aCenter[1] = 0.0;
             aCenter[2] = 0.0;

             vCenter = aCenter;

             dMajorRadius = 2.0;

             aMajorAxis[0] = 1.0;
             aMajorAxis[1] = 0.0;
             aMajorAxis[2] = 0.0;

             vMajorAxis = aMajorAxis;

             dMinorRadius = 1.0;

             aMinorAxis[0] = 0.0;
             aMinorAxis[1] = 1.0;
             aMinorAxis[2] = 0.0;

             vMinorAxis = aMinorAxis;

             swCurve[0] = (Curve)swModeler.CreateEllipse(vCenter, dMajorRadius, dMinorRadius, vMajorAxis, vMinorAxis);

             if ((swCurve[0] == null))
             {
                 Debug.Print(" No curve");

             }
             else
             {
                 Debug.Print("Curve:");
                 Debug.Print("  is ellipse  = " + (swCurve[0].IsEllipse() == false ? "False" : "True"));
                 Debug.Print("  type        = " + swCurve[0].Identity());
                 Debug.Print("  is ellipse  = " + (swCurve[0].Identity() == (int)swCurveTypes_e.ELLIPSE_TYPE));
                 Debug.Print("  trimmed     = " + (swCurve[0].IsTrimmedCurve() == false ? "False" : "True"));

                 bStatus = swCurve[0].GetEndParams(out dStartParam, out dEndParam, out bIsClosed, out bIsPeriodic);

                 Debug.Print("  start param = " + dStartParam);
                 Debug.Print("  end   param = " + dEndParam);
                 Debug.Print("  closed      = " + bIsClosed);
                 Debug.Print("  periodic    = " + bIsPeriodic);

                 Debug.Print("  length      = " + swCurve[0].GetLength3(dStartParam, dEndParam));

                 if ((!(swCurve[0].IsEllipse() == false)))
                 {
                     vEllipseParams = (double[])swCurve[0].GetEllipseParams();

                     Debug.Print("  centre       = (" + vEllipseParams[0] +  ", " + vEllipseParams[1] + ", " + vEllipseParams[2] + ")");
                     Debug.Print("  major radius = " + vEllipseParams[3]);
                     Debug.Print("  major axis   = (" + vEllipseParams[4] +  ", " + vEllipseParams[5] + ", " + vEllipseParams[6] + ")");
                     Debug.Print("  minor radius = " + vEllipseParams[7]);
                     Debug.Print("  minor axis   = (" + vEllipseParams[8] +  ", " + vEllipseParams[9] + ", " + vEllipseParams[10] + ")");
                 }

                 Surface planeSurf = default(Surface);
                 MathUtility swMath = default(MathUtility);
                 double slotDepth = 0;
                 slotDepth = 0.01;

                 swMath = (MathUtility)swApp.GetMathUtility();

                 double[] startArr = new double[3];
                 double[] endArr = new double[3];
                 double[] ptArr = new double[3];
                 double[] dirArr = new double[3];

                 ptArr[0] = 0.0;
                 ptArr[1] = 0.0;
                 ptArr[2] = 0.0;
                 dirArr[0] = 0.0;
                 dirArr[1] = 0.0;
                 dirArr[2] = 1.0;
                 startArr[0] = 1.0;
                 startArr[1] = 0.0;
                 startArr[2] = 0.0;

                 planeSurf = (Surface)swModeler.CreatePlanarSurface2((ptArr), (dirArr), (startArr));

                 Body2 profileBody = default(Body2);
                 Body2 extrudedBody = default(Body2);
                 MathVector dirVector = default(MathVector);

                 profileBody = (Body2)planeSurf.CreateTrimmedSheet4((swCurve), true);

                 dirArr[0] = 0.0;
                 dirArr[1] = 0.0;
                 dirArr[2] = -1.0;

                 dirVector = (MathVector)swMath.CreateVector((dirArr));
                 extrudedBody = swModeler.CreateExtrudedBody(profileBody, dirVector, slotDepth);
                 extrudedBody.Display3(swDocument,  Information.RGB(1, 0, 0), 0);

             }
             swDocument.ViewZoomtofit();
         }

         public SldWorks swApp;

     }
 }
```
