---
title: "Create Mathematical Circular Arcs Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_Mathemetical_Circular_Arcs_Example_CSharp.htm"
---

# Create Mathematical Circular Arcs Example (C#)

This example shows how to create mathematical circular Arcs.

```
//--------------------------------------------------------------
// Preconditions:
// 1. Create a C# Windows console project.
// 2. Copy and paste this example into the C# IDE.
// 3. Add a reference to:
//    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
// 4. Add a reference to System.Windows.Forms.
// 5. Start DraftSight.
// 6. Press F5.
//
// Postconditions:
// 1. Connects to DraftSight.
// 2. Gets the active document.
// 3. Creates a mathematical circular Arc.
// 4. Gets the point on the mathematical circular Arc
//    closest to a mathematical point. Click OK to close
//    the message box.
// 5. Sets the radius for the mathematical circular Arc.
// 6. Creates another mathematical circular Arc.
// 7. Sets the radius for the mathematical circular Arc.
//----------------------------------------------------------------

using System;
using DraftSight.Interop.dsAutomation;
using System.Runtime.InteropServices;
using System.Windows.Forms;

namespace MathCircArcCSharp
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

            //Aborts any command currently running in DraftSight
            //to avoid nested commands
            dsApp.AbortRunningCommand();

            //Gets active document
            Document dsDoc = dsApp.GetActiveDocument();
            if (null == dsDoc)
            {
                MessageBox.Show("There are no open documents in DraftSight.");
                return;
            }

            MathUtility dsMathUtility = dsApp.GetMathUtility();

            //Creates mathematical circular Arc
            MathPoint dsCenter = dsMathUtility.CreatePoint(3.0, 7.0, 0.0);
            MathVector dsNormal = dsMathUtility.CreateVector(1.0, 0.0, 0.0);
            double dsRadius = 2;
            MathVector RefVector = dsMathUtility.CreateVector(1.0, 0.0, 0.0);
            MathCircArc dsMathCircArc = dsMathUtility.CreateCircArc(dsCenter, dsNormal, RefVector, dsRadius, 20, 45);
            //Gets point on mathematical circular Arc
            //closest to this point
            MathPoint point = dsMathUtility.CreatePoint(3.0, 7.0, 0.0);
            MathPoint closestPoint = dsMathCircArc.GetClosestPointTo(point);
            double X, Y, Z;
            closestPoint.GetPosition(out X, out Y, out Z);
            MessageBox.Show("Closest point of (3, 7, 0) is (" + X + ", " + Y + ", " + Z + ")");
            //Sets radius of mathematical circular Arc
            dsMathCircArc.Radius = 6.4;

            //Creates a mathematical circular Arc defining a Circle
            //with the specified center, normal, and radius
            MathPoint center = dsMathUtility.CreatePoint(2.0, 3.1, 0.0);
            MathVector normal = dsMathUtility.CreateVector(1.0, 0.0, 0.0);
            double radius = 3.0;
            MathCircArc circle = dsMathUtility.CreateCircle(center, normal, radius);

        }
    }
}
```
