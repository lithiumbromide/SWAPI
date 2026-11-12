---
title: "Create and Transform Mathematical Elliptical Arc Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_and_Transform_Mathematical_Elliptical_Arc_Example_VBNET.htm"
---

# Create and Transform Mathematical Elliptical Arc Example (VB.NET)

This example shows how to create and transform a mathematical elliptical Arc.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VB.NET Windows console project.
' 2. Copy and paste this code into the VB.NET project.
' 3. Add a reference to
'    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
' 4. Add a reference to System.Windows.Forms.
' 5. Open the Immediate window.
' 6. Start DraftSight.
' 7. Press F5.
'
' Postconditions:
' 1. Connects to DraftSight.
' 2. Gets the active document.
' 3. Creates a mathematical elliptical Arc.
' 4. Gets various mathematical elliptical Arc values.
' 5. Gets the intersection points of the mathematical elliptical Arc
'    with a mathematical linear object and plane.
' 6. Sets various values to use to transform the
'    mathematical elliptical Arc.
' 7. Applies a mathematical transformation to the
'    mathematical elliptical Arc.
' 8. Examine the Immediate window.
'---------------------------------------------------------------
Imports System
Imports DraftSight.Interop.dsAutomation
Imports System.Runtime.InteropServices
Imports System.Windows.Forms
Imports System.Diagnostics

Module Module1

    Sub Main()

        Dim dsApp As DraftSight.Interop.dsAutomation.Application

        'Connects to DraftSight application
        dsApp = GetObject(, "DraftSight.Application")
        If dsApp Is Nothing Then
            Return
        End If

        'Gets active document
        Dim dsDoc As Document = dsApp.GetActiveDocument()
        If dsDoc Is Nothing Then
            MessageBox.Show("There are no open documents in DraftSight.")
            Return
        End If

        'Aborts any command currently running in DraftSight
        'to avoid nested commands
        dsApp.AbortRunningCommand()

        'Creates a mathematical elliptical Arc
        Dim dsMathUtility As MathUtility = dsApp.GetMathUtility()

        Dim Center As MathPoint = dsMathUtility.CreatePoint(3.0, 7.0, 0.0)
        Dim minorAxis__1 As MathVector = dsMathUtility.CreateVector(1.0, 1.0, 0.0)
        Dim majorAxis__2 As MathVector = dsMathUtility.CreateVector(3.0, 1.0, 0.0)
        Dim majorRadius As Double = 3.0
        Dim minorRadius As Double = 2.0
        Dim startAngle As Double = 2.1
        Dim endAngle As Double = 1.0

        Dim dsMathEllipArc As MathEllipArc = dsMathUtility.CreateEllipArc(Center, majorAxis__2, minorAxis__1, majorRadius, minorRadius, startAngle, _
         endAngle)
        If dsMathEllipArc Is Nothing Then
            Debug.Print("Mathematical elliptical Arc not created.")
        Else
            Debug.Print("Mathematical elliptical Arc created.")
        End If

        'Gets length of mathematical elliptical Arc
        Dim mathEllipArcLength As Double = dsMathEllipArc.GetLength()

        'Gets normal of mathematical elliptical Arc
        Dim dsNormal As MathVector = dsMathEllipArc.GetNormal()

        'Gets major and minor axes of mathematical elliptical Arc
        Dim dsMajorAxis As MathVector = dsMathEllipArc.GetMajorAxis()
        Dim dsMinorAxis As MathVector = dsMathEllipArc.GetMinorAxis()

        'Gets plane of mathematical elliptical Arc
        Dim dsMathPlane As MathPlane = dsMathEllipArc.GetPlane()

        'Gets start point of mathematical elliptical Arc
        Dim dsStartPoint As MathPoint = dsMathEllipArc.GetStartPoint()

        'Gets intersection point of mathematical
        'elliptical Arc with a mathematical linear object
        Dim dsLinearObject As MathLine = dsMathUtility.CreateLine(1.0, 1.0, 0, 0, 10.0, 12.0, _
         dsMathLineType_e.dsMathLineType_Infinite)
        Dim intersectionPoint1 As MathPoint = Nothing
        Dim intersectionPoint2 As MathPoint = Nothing
        Dim result As Integer = dsMathEllipArc.IntersectWithLinearObject(dsLinearObject, intersectionPoint1, intersectionPoint2)
        If result = 0 Then
            Debug.Print("Mathematical elliptical Arc and linear object do not intersect.")
        Else
            Debug.Print("Mathematical ellipitcal Arc and linear object do intersect.")
        End If

        'Gets intersection point of mathematical elliptical Arc with
        'a mathematical plane
        Dim dsPlaneObject As MathPlane = dsMathUtility.CreateXYPlane()
        result = dsMathEllipArc.IntersectWithPlane(dsPlaneObject, intersectionPoint1, intersectionPoint2)
        If result = 0 Then
            Debug.Print("Mathematical elliptical Arc and plane do not intersect.")
        Else
            Debug.Print("Mathematical ellipitcal Arc and plane do intersect.")
        End If

        'Changes major and minor radii
        dsMathEllipArc.MajorRadius = 4.0
        dsMathEllipArc.MinorRadius = 3.0

        'Sets axes of mathematical elliptical Arc
        Dim MinorAxis__3 As MathVector = dsMathUtility.CreateVector(2.0, 2.0, 0.0)
        Dim MajorAxis__4 As MathVector = dsMathUtility.CreateVector(3.5, 2.3, 0.0)
        dsMathEllipArc.SetAxes(MajorAxis__4, MinorAxis__3)

        'Sets start angle
        dsMathEllipArc.StartAngle = 3.0

        'Applies a mathematical transformation to the
        'mathematical elliptical Arc
        Dim dsProjectionPlane As MathPlane = dsMathUtility.CreateYZPlane()
        Dim dsProjectionDirection As MathVector = dsMathUtility.CreateVector(1, 0, 0)
        Dim dsProjectionTransformation As MathTransform = dsMathUtility.CreateTransformProjection(dsProjectionPlane, dsProjectionDirection)
        dsMathEllipArc.TransformBy(dsProjectionTransformation)
        Debug.Print("Mathematical transformation applied to mathematical elliptical Arc.")

    End Sub

End Module
```
