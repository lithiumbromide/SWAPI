---
title: "Create and Transform Mathematical Elliptical Arc Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_and_Transform_Mathematical_Elliptical_Arc_Example_CSharp.htm"
---

# Create and Transform Mathematical Elliptical Arc Example (C#)

This example shows how to create and transform a mathematical elliptical Arc.

```
//--------------------------------------------------------------
// Preconditions:
// 1. Create a C# Windows console project.
// 2. Copy and paste this code into the C# project.
// 3. Add a reference to
//    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
// 4. Add a reference to System.Windows.Forms.
// 5. Open the Immediate window.
// 6. Start DraftSight.
// 7. Press F5.
//
// Postconditions:
// 1. Connects to DraftSight.
// 2. Gets the active document.
// 3. Creates a mathematical elliptical Arc.
// 4. Gets various mathematical elliptical Arc values.
// 5. Gets the intersection points of the mathematical elliptical Arc
//    with a mathematical linear object and plane.
// 6. Sets various values to use to transform the
//    mathematical elliptical Arc.
// 7. Applies a mathematical transformation to the
//    mathematical elliptical Arc.
// 8. Examine the Immediate window.
//---------------------------------------------------------------
using System;
using DraftSight.Interop.dsAutomation;
using System.Runtime.InteropServices;
using System.Windows.Forms;
using System.Diagnostics;

namespace MathEllipArcCSharp
{
    class Program
    {

        static void Main()
        {
            DraftSight.Interop.dsAutomation.Application dsApp;

            //Connects to DraftSight application
            dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");

            if (null == dsApp)
            {
                return;
            }

            //Gets active document
            Document dsDoc = dsApp.GetActiveDocument();
            if (null == dsDoc)
            {
                MessageBox.Show("There are no open documents in DraftSight.");
                return;
            }

            //Aborts any command currently running in DraftSight
            //to avoid nested commands
            dsApp.AbortRunningCommand();

            //Creates a mathematical elliptical Arc
            MathUtility dsMathUtility = dsApp.GetMathUtility();

            MathPoint Center = dsMathUtility.CreatePoint(3.0, 7.0, 0.0);
            MathVector minorAxis = dsMathUtility.CreateVector(1.0, 1.0, 0.0);
            MathVector majorAxis = dsMathUtility.CreateVector(3.0, 1.0, 0.0);
            double majorRadius = 3.0;
            double minorRadius = 2.0;
            double startAngle = 2.1;
            double endAngle = 1.0;

            MathEllipArc dsMathEllipArc = dsMathUtility.CreateEllipArc(Center, majorAxis, minorAxis, majorRadius, minorRadius, startAngle, endAngle);
            if (dsMathEllipArc != null)
            {
                Debug.Print("Mathematical elliptical Arc created.");
            }
            else
            {
                Debug.Print("Mathematical elliptical Arc not created.");
            }

            //Gets length of mathematical elliptical Arc
            double mathEllipArcLength = dsMathEllipArc.GetLength();

            //Gets normal of mathematical elliptical Arc
            MathVector dsNormal = dsMathEllipArc.GetNormal();

            //Gets major and minor axes of mathematical elliptical Arc
            MathVector dsMajorAxis = dsMathEllipArc.GetMajorAxis();
            MathVector dsMinorAxis = dsMathEllipArc.GetMinorAxis();

            //Gets plane of mathematical elliptical Arc
            MathPlane dsMathPlane = dsMathEllipArc.GetPlane();

            //Gets start point of mathematical elliptical Arc
            MathPoint dsStartPoint = dsMathEllipArc.GetStartPoint();

            //Gets intersection point of mathematical
            //elliptical Arc with a mathematical linear object
            MathLine dsLinearObject = dsMathUtility.CreateLine(1.0, 1.0, 0, 0, 10.0, 12.0, dsMathLineType_e.dsMathLineType_Infinite);
            MathPoint intersectionPoint1, intersectionPoint2;
            int result = dsMathEllipArc.IntersectWithLinearObject(dsLinearObject, out intersectionPoint1, out intersectionPoint2);
            if (result == 0 )
            {
                Debug.Print("Mathematical elliptical Arc and linear object do not intersect.");
            }
            else
            {
                Debug.Print("Mathematical elliptical Arc and linear object do intersect.");
            }

            //Gets intersection point of mathematical elliptical Arc with
            //a mathematical plane
            MathPlane dsPlaneObject = dsMathUtility.CreateXYPlane();
            result = dsMathEllipArc.IntersectWithPlane(dsPlaneObject, out intersectionPoint1, out intersectionPoint2);
            if (result == 0)
            {
                Debug.Print("Mathematical elliptical Arc and plane do not intersect.");
            }
            else
            {
                Debug.Print("Mathematical elliptical Arc and plane do intersect.");
            }

            //Changes major and minor radii
            dsMathEllipArc.MajorRadius = 4.0;
            dsMathEllipArc.MinorRadius = 3.0;

            //Sets axes of mathematical elliptical Arc
            MathVector MinorAxis = dsMathUtility.CreateVector(2.0, 2.0, 0.0);
            MathVector MajorAxis = dsMathUtility.CreateVector(3.5, 2.3, 0.0);
            dsMathEllipArc.SetAxes(MajorAxis, MinorAxis);

            //Sets start angle
            dsMathEllipArc.StartAngle = 3.0;

            //Applies a mathematical transformation to the
            //mathematical elliptical Arc
            MathPlane dsProjectionPlane = dsMathUtility.CreateYZPlane();
            MathVector dsProjectionDirection = dsMathUtility.CreateVector(1.0, 0.0, 0.0);
            MathTransform dsProjectionTransformation = dsMathUtility.CreateTransformProjection(dsProjectionPlane, dsProjectionDirection);
            dsMathEllipArc.TransformBy(dsProjectionTransformation);
            Debug.Print("Mathematical transformation applied to mathematical elliptical Arc.");
        }
    }
}
```
