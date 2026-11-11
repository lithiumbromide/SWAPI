---
title: "Construct Ellipses and Elliptical Arcs Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Construct_Ellipses_and_Elliptical_Arcs_Example_VBNET.htm"
---

# Construct Ellipses and Elliptical Arcs Example (VB.NET)

This example shows how to construct Ellipses and elliptical Arcs.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VB.NET Windows console project.
' 2. Copy and paste this example into the VB.NET IDE.
' 3. Add a reference to:
'    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
' 4. Start DraftSight and open a document.
' 5. Start debugging the project.
'
' Postconditions: A message box pops up when an Ellipse or
' elliptical Arc is inserted in the drawing document.
'----------------------------------------------------------------
```

```
Imports DraftSight.Interop.dsAutomation
```

```
Module Module1
```

```
    Sub Main()
        Dim dsApp As Application
        Dim dsDoc As Document
        Dim dsModel As Model
        Dim dsSketchManager As SketchManager
        Dim dsEllipseRotation As EllipseArc
        Dim dsEllipseDistance As EllipseArc
        Dim dsEllipseArcDistance As EllipseArc
        Dim dsEllipseArcRotation As EllipseArc
        Dim x1, y1, x2, y2 As Double
        Dim rotation As Double
        Dim distanceToOtherAxis As Double
        Dim startAngle, endAngle As Double
```

```
        'Connect to DraftSight
        dsApp = GetObject(, "DraftSight.Application")
	dsApp.AbortRunningCommand() ' abort any command currently running in DraftSight to avoid nested commands
```

```
        'Get active document
        dsDoc = dsApp.GetActiveDocument()
        If Not dsDoc Is Nothing Then
```

```
            'Get model space
            dsModel = dsDoc.GetModel()
```

```
            'Get Sketch Manager
            dsSketchManager = dsModel.GetSketchManager()
```

```
            'Ellipse rotation parameters (rotation parameter should be in radians)
            x1 = 0.0#
            y1 = 0.0#
            x2 = 10.0#
            y2 = 0.0#
            rotation = 3.14159265358979 / 4 '45 degrees in radians
            'Draw an ellipse
            dsEllipseRotation = dsSketchManager.InsertEllipseRotation(x1, y1, x2, y2, rotation)
```

```
            'Ellipse distance parameters
            x1 = 0.0#
            y1 = 0.0#
            x2 = 10.0#
            y2 = 0.0#
            distanceToOtherAxis = 3.0#
            'Draw an ellipse
            dsEllipseDistance = dsSketchManager.InsertEllipseDistanceToOtherAxis(x1, y1, x2, y2, distanceToOtherAxis)
```

```
            'Elliptical Arc distance parameters (start and end angle parameters should be in radians)
            x1 = 0.0#
            y1 = 0.0#
            x2 = 10.0#
            y2 = 0.0#
            distanceToOtherAxis = 2.0#
            startAngle = 0.0#
            endAngle = 3.14159265358979 '180 degrees in radians
            'Draw an elliptical Arc
            dsEllipseArcDistance = dsSketchManager.InsertEllipseArcDistanceToOtherAxis(x1, y1, x2, y2, distanceToOtherAxis, startAngle, endAngle)
```

```
            'Ellipitcal Arc rotation parameters (rotation, start, and end angle parameters should be in radians)
            x1 = 0.0#
            y1 = 0.0#
            x2 = 10.0#
            y2 = 0.0#
            rotation = 3.14159265358979 / 4 '45 degrees in radians
            startAngle = 0.0#
            endAngle = 3.14159265358979 '180 degrees in radians
            'Draw an elliptical Arc
            dsEllipseArcRotation = dsSketchManager.InsertEllipseArcRotation(x1, y1, x2, y2, rotation, startAngle, endAngle)
```

```
            If Not dsEllipseRotation Is Nothing Then
                MsgBox("An ellipse using the specified axes end points and the angle of rotation was added to drawing.")
            End If
```

```
            If Not dsEllipseDistance Is Nothing Then
                MsgBox("An ellipse using the specified axes end points and radius of the perpendicular axis was added to drawing.")
            End If
```

```
            If Not dsEllipseArcDistance Is Nothing Then
                MsgBox("An elliptical Arc using the specified axes end points and radius of the perpendicular axis was added to drawing.")
            End If
```

```
            If Not dsEllipseArcRotation Is Nothing Then
                MsgBox("An elliptical Arc using the specified axes end points, angle of rotation, and start and end angles was added to drawing.")
            End If
```

```
        Else
```

```
            MsgBox("There are no open documents in DraftSight.")
```

```
        End If
```

```
    End Sub
```

```
End Module
```
