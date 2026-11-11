---
title: "Construct Ellipses and Elliptical Arcs Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Construct_Ellipses_and_Elliptical_Arcs_Example_VBA.htm"
---

# Construct Ellipses and Elliptical Arcs Example (VBA)

This example shows how to construct Ellipses and elliptical Arcs.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to the DraftSight type library,
'    install_dir\bin\dsAutomation.dll.
' 4. Start DraftSight and open a drawing document.
' 5. Run the macro.
'
' Postconditions: A message box pops up when an Ellipse or
' elliptical Arc is constructed in the drawing document.
'----------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim dsApp As DraftSight.Application
    Dim dsDoc As DraftSight.Document
    Dim dsModel As DraftSight.Model
    Dim dsSketchManager As DraftSight.SketchManager
    Dim dsEllipseRotation As DraftSight.EllipseArc
    Dim dsEllipseDistance As DraftSight.EllipseArc
    Dim dsEllipseArcDistance As DraftSight.EllipseArc
    Dim dsEllipseArcRotation As DraftSight.EllipseArc
    Dim x1, y1, x2, y2 As Double
    Dim rotation As Double
    Dim distanceToOtherAxis As Double
    Dim startAngle, endAngle As Double
```

```
    'Connect to DraftSight
    Set dsApp = GetObject(, "DraftSight.Application")
    'Abort any command currently running in DraftSight
    'to avoid nested commands
    dsApp.AbortRunningCommand
```

```
    'Get active document
    Set dsDoc = dsApp.GetActiveDocument()
    If Not dsDoc Is Nothing Then
```

```
        'Get model space
        Set dsModel = dsDoc.GetModel()
```

```
        'Get Sketch Manager
        Set dsSketchManager = dsModel.GetSketchManager()
```

```
        'Ellipse rotation parameters (rotation parameter should be in radians)
        x1 = 0#
        y1 = 0#
        x2 = 10#
        y2 = 0#
        rotation = 3.14159265358979 / 4 '45 degrees in radians
        'Draw an ellipse
        Set dsEllipseRotation = dsSketchManager.InsertEllipseRotation(x1, y1, x2, y2, rotation)
```

```
       'Ellipse distance parameters
        x1 = 0#
        y1 = 0#
        x2 = 10#
        y2 = 0#
        distanceToOtherAxis = 3#
        'Draw an ellipse
        Set dsEllipseDistance = dsSketchManager.InsertEllipseDistanceToOtherAxis(x1, y1, x2, y2, distanceToOtherAxis)
```

```
       'Elliptical Arc distance parameters (start and end angle parameters should be in radians)
        x1 = 0#
        y1 = 0#
        x2 = 10#
        y2 = 0#
        distanceToOtherAxis = 2#
        startAngle = 0#
        endAngle = 3.14159265358979 '180 degrees in radians
        'Draw an elliptical Arc
        Set dsEllipseArcDistance = dsSketchManager.InsertEllipseArcDistanceToOtherAxis(x1, y1, x2, y2, distanceToOtherAxis, startAngle, endAngle)
```

```
        'Ellipitcal Arc rotation parameters (rotation, start, and end angle parameters should be in radians)
        x1 = 0#
        y1 = 0#
        x2 = 10#
        y2 = 0#
        rotation = 3.14159265358979 / 4 '45 degrees in radians
        startAngle = 0#
        endAngle = 3.14159265358979 '180 degrees in radians
        'Draw an elliptical Arc
        Set dsEllipseArcRotation = dsSketchManager.InsertEllipseArcRotation(x1, y1, x2, y2, rotation, startAngle, endAngle)
```

```
        If Not dsEllipseRotation Is Nothing Then
            MsgBox "An ellipse using the specified axes end points and the angle of rotation was added to drawing."
        End If
```

```
        If Not dsEllipseDistance Is Nothing Then
            MsgBox "An ellipse using the specified axes end points and radius of the perpendicular axis was added to drawing."
        End If
```

```
        If Not dsEllipseArcDistance Is Nothing Then
            MsgBox "An elliptical Arc using the specified axes end points and radius of the perpendicular axis was added to drawing."
        End If
```

```
        If Not dsEllipseArcRotation Is Nothing Then
            MsgBox "An elliptical Arc using the specified axes end points, angle of rotation, and start and end angles was added to drawing."
        End If
```

```
    Else
```

```
        MsgBox "There are no open documents in DraftSight."
```

```
    End If
```

```
End Sub
```
