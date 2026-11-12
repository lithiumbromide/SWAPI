---
title: "Create and Transform Mathematical Elliptical ArcExample (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_and_Transform_Mathematical_Elliptical_Arc_Example_VBA.htm"
---

# Create and Transform Mathematical Elliptical ArcExample (VBA)

## Create and Transform Mathematical Elliptical Arc Example (VBA)

This example shows how to create and transform a mathematical elliptical Arc.

```
'-----------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this code into the Visual Basic IDE.
' 3. Add a reference to the DraftSight type library,
'    install_dir\bin\dsAutomation.dll.
' 4. Open the Immediate window.
' 5. Start DraftSight.
' 6. Press F5.
'
' Postconditions:
' 1. Connects to DraftSight.
' 2. Gets the active document.
' 3. Creates a mathematical elliptical Arc.
' 4. Gets various mathematical elliptical Arc values.
' 5. Gets the intersection points of the mathematical elliptical
'    Arc with a mathematical linear object and plane.
' 6. Sets various values to use to transform the
'    mathematical elliptical Arc.
' 7. Applies a mathematical transformation to the
'    mathematical elliptical Arc.
' 8. Examine the Immediate window.
'---------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim dsApp As DraftSight.Application
```

```
    'Connects to DraftSight
    Set dsApp = GetObject(, "DraftSight.Application")
```

```
    'Aborts any command currently running in DraftSight
    'to avoid nested commands
    dsApp.AbortRunningCommand
```

```
    'Gets active document
    Dim dsDoc As DraftSight.Document
    Set dsDoc = dsApp.GetActiveDocument
    If dsDoc Is Nothing Then
        MsgBox "There are no open documents in DraftSight."
        Exit Sub
    End If
```

```
    'Creates a mathematical elliptical Arc
    Dim dsMathUtility As DraftSight.MathUtility
    Set dsMathUtility = dsApp.GetMathUtility
    Dim Center As DraftSight.MathPoint
    Set Center = dsMathUtility.CreatePoint(3#, 7#, 0#)
    Dim MinorAxis1 As DraftSight.MathVector
    Set MinorAxis1 = dsMathUtility.CreateVector(1#, 1#, 0#)
    Dim MajorAxis2 As DraftSight.MathVector
    Set MajorAxis2 = dsMathUtility.CreateVector(3#, 1#, 0#)
    Dim majorRadius As Double
    majorRadius = 3#
    Dim minorRadius As Double
    minorRadius = 2#
    Dim startAngle As Double
    startAngle = 2.1
    Dim endAngle As Double
    endAngle = 1#
```

```
    Dim dsMathEllipArc As DraftSight.MathEllipArc
    Set dsMathEllipArc = dsMathUtility.CreateEllipArc(Center, MajorAxis2, MinorAxis1, majorRadius, minorRadius, startAngle, endAngle)
    If dsMathEllipArc Is Nothing Then
        Debug.Print ("Mathematical elliptical Arc not created.")
    Else
        Debug.Print ("Mathematical elliptical Arc created.")
    End If
```

```
    'Gets length of mathematical elliptical Arc
    Dim mathEllipArcLength As Double
    mathEllipArcLength = dsMathEllipArc.GetLength
```

```
    'Gets normal of mathematical elliptical Arc
    Dim dsNormal As DraftSight.MathVector
    Set dsNormal = dsMathEllipArc.GetNormal
```

```
    'Gets major and minor axes of mathematical elliptical Arc
    Dim dsMajorAxis As DraftSight.MathVector
    Set dsMajorAxis = dsMathEllipArc.GetMajorAxis
    Dim dsMinorAxis As DraftSight.MathVector
    Set dsMinorAxis = dsMathEllipArc.GetMinorAxis
```

```
    'Gets plane of mathematical elliptical Arc
    Dim dsPlane As DraftSight.MathPlane
    Set dsPlane = dsMathEllipArc.GetPlane
```

```
    'Gets intersection point of mathematical
    'elliptical Arc with a mathematical linear
    'object
    Dim dsLinearObject As DraftSight.MathLine
    Set dsLinearObject = dsMathUtility.CreateLine(1#, 1#, 0#, 0#, 10#, 12#, dsMathLineType_e.dsMathLineType_Infinite)
    Dim intersectionPoint1 As DraftSight.MathPoint
    Dim intersectionPoint2 As DraftSight.MathPoint
    Dim result As Long
    result = dsMathEllipArc.IntersectWithLinearObject(dsLinearObject, intersectionPoint1, intersectionPoint2)
    If result = 0 Then
        Debug.Print "Mathematical elliptical Arc and linear object do not intersect."
    Else
        Debug.Print "Mathematical elliptical Arc and linear object do intersect."
    End If

    'Gets intersection point of mathematical elliptical Arc with
    'a mathematical plane
    Dim dsPlaneObject As DraftSight.MathPlane
    Set dsPlaneObject = dsMathUtility.CreateXYPlane
    result = dsMathEllipArc.IntersectWithPlane(dsPlaneObject, intersectionPoint1, intersectionPoint2)
    If result = 0 Then
        Debug.Print "Mathematical elliptical Arc and plane do not intersect."
    Else
        Debug.Print "Mathematical elliptical Arc and plane do intersect."
    End If
```

```
    'Changes major and minor radii
    dsMathEllipArc.majorRadius = 4#
    dsMathEllipArc.minorRadius = 3#
```

```
    'Sets axes of mathematical elliptical Arc
    Dim MinorAxis3 As DraftSight.MathVector
    Set MinorAxis3 = dsMathUtility.CreateVector(2#, 2#, 0#)
    Dim MajorAxis4 As DraftSight.MathVector
    Set MajorAxis4 = dsMathUtility.CreateVector(3.5, 2.3, 0#)
    dsMathEllipArc.SetAxes MajorAxis4, MinorAxis3
```

```
    'Sets start angle
    dsMathEllipArc.startAngle = 3#
```

```
    'Applies a mathematical transformation to the
    'mathematical elliptical Arc
    Dim dsProjectionPlane As DraftSight.MathPlane
    Set dsProjectionPlane = dsMathUtility.CreateYZPlane
    Dim dsProjectionDirection As DraftSight.MathVector
    Set dsProjectionDirection = dsMathUtility.CreateVector(1, 0, 0)
    Dim dsProjectionTransformation As DraftSight.MathTransform
    Set dsProjectionTransformation = dsMathUtility.CreateTransformProjection(dsProjectionPlane, dsProjectionDirection)
    dsMathEllipArc.TransformBy dsProjectionTransformation
    Debug.Print ("Mathematical transformation applied to mathematical elliptical Arc.")
```

```
End Sub
```
