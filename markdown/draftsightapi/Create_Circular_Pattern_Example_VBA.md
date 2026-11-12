---
title: "Create Circular Pattern Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_Circular_Pattern_Example_VBA.htm"
---

# Create Circular Pattern Example (VBA)

This example shows how to construct a circular pattern of Circles in a DraftSight drawing.

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
' Postconditions:
' 1. Constructs three Circles.
' 2. Creates a circular pattern of the Circles.
' 3. Zooms the drawing to fit.
' 4. Examine the drawing.
'----------------------------------------------------------------
Option Explicit

Sub main()

    Dim dsApp As DraftSight.Application
    Dim dsDoc As DraftSight.Document
    Dim dsModel As DraftSight.Model
    Dim dsSketchManager As DraftSight.SketchManager
    Dim dsCircle1 As DraftSight.Circle
    Dim dsCircle2 As DraftSight.Circle
    Dim dsCircle3 As DraftSight.Circle
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
        'Circle parameters
        Dim center1X As Double, center2X As Double, center3X As Double
        center1X = 30#
        center2X = 60#
        center3X = 90#
```

```
        Dim center1Y As Double, center2Y As Double, center3Y As Double
        center1Y = 30#
        center2Y = 60#
        center3Y = 90#
```

```
        Dim center1Z As Double, center2Z As Double, center3Z As Double
        center1Z = 0#
        center2Z = 0#
        center3Z = 0#
```

```
        Dim radius1 As Double, radius2 As Double, radius3 As Double
        radius1 = 10#
        radius2 = 10#
        radius3 = 10#
```

```
        'Draw the Circles
        Set dsCircle1 = dsSketchManager.InsertCircle(center1X, center1Y, center1Z, radius1)
        Set dsCircle2 = dsSketchManager.InsertCircle(center2X, center2Y, center2Z, radius2)
        Set dsCircle3 = dsSketchManager.InsertCircle(center3X, center3Y, center3Z, radius3)
```

```
        'Circular pattern parameters
        Dim angleBetween As Double
        angleBetween = 3.14159265358979 / 2  '90 degrees in radians
```

```
        Dim fillAngle As Double
        fillAngle = 4.71238898  '270 degrees in radians
```

```
        Dim totalNumber As Long
        totalNumber = 4
```

```
        Dim elementBasePointX As Double
        Dim elementBasePointY As Double
        Dim axisPointX As Double
        Dim axisPointY As Double
        elementBasePointX = 0#
        elementBasePointY = 0#
        axisPointX = 0#
        axisPointY = 0#
```

```
        Dim orientElementsAboutAxis As Boolean
        orientElementsAboutAxis = True
```

```
        'Prepare list of entity types
        Dim dsEntityTypes(0 To 2) As Long
        dsEntityTypes(0) = dsObjectType_e.dsCircleType
        dsEntityTypes(1) = dsObjectType_e.dsCircleType
        dsEntityTypes(2) = dsObjectType_e.dsCircleType
```

```
        'Prepare list of entities
        Dim dsEntities(0 To 2) As Object
        Set dsEntities(0) = dsCircle1
        Set dsEntities(1) = dsCircle2
        Set dsEntities(2) = dsCircle3
```

```
        'Create circular pattern
        dsSketchManager.PatternCircular dsBasePatternOn_AngleBetweenAndElementsNumber, angleBetween, fillAngle, totalNumber, elementBasePointX, elementBasePointY, axisPointX, axisPointY, orientElementsAboutAxis, dsEntityTypes, dsEntities
```

```
        'Zoom to fit
        dsApp.Zoom dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing
```

```
    Else
```

```
        MsgBox "There are no open documents in DraftSight."
```

```
    End If

End Sub
```
