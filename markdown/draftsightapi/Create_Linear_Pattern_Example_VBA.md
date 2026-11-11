---
title: "Create Linear pattern Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_Linear_Pattern_Example_VBA.htm"
---

# Create Linear pattern Example (VBA)

## Create Linear Pattern Example (VBA)

This example shows how to create a linear pattern.

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
' 1. Draws a Circle.
' 2. Draws a 2D PolyLine.
' 3. Creates a linear pattern using the Circle and 2D PolyLine
'    entities.
' 4. Zooms the drawing to fit.
' 5. Examine the drawing.
'----------------------------------------------------------------
Option Explicit
Sub main()
    Dim dsApp As DraftSight.Application
    Dim dsDoc As DraftSight.Document
    Dim dsModel As DraftSight.Model
    Dim dsSketchManager As DraftSight.SketchManager
    Dim dsCircle As DraftSight.Circle
    Dim dsPolyLine As DraftSight.PolyLine
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
        Dim centerX As Double
        centerX = 5#
```

```
        Dim centerY As Double
        centerY = 5#
```

```
        Dim centerZ As Double
        centerZ = 0#
```

```
        Dim radius As Double
        radius = 3#
```

```
        'Draw a Circle
        Set dsCircle = dsSketchManager.InsertCircle(centerX, centerY, centerZ, radius)
```

```
        'Draw a 2D PolyLine
        Dim coordinates(0 To 7) As Double
        coordinates(0) = 10: coordinates(1) = 4
        coordinates(2) = 10: coordinates(3) = 6
        coordinates(4) = 14: coordinates(5) = 6
        coordinates(6) = 14: coordinates(7) = 4
        Dim Closed As Boolean
        Closed = True
```

```
        'Construct a 2D PolyLine
        Set dsPolyLine = dsSketchManager.InsertPolyline2D(coordinates, Closed)
```

```
        'Linear pattern parameters
        Dim numberElementsOnVerticalAxis As Long
        numberElementsOnVerticalAxis = 4
```

```
        Dim numberElementsOnHorizontalAxis As Double
        numberElementsOnHorizontalAxis = 5
```

```
        Dim spacingonVerticalAxis As Double
        spacingonVerticalAxis = 20
```

```
        Dim spacingOnHorizontalAxis As Double
        spacingOnHorizontalAxis = 40
```

```
        Dim patternAngle As Double
        patternAngle = 3.14159265358979 / 4 'In radians
```

```
        'Prepare list of entity types
        Dim dsEntityTypes(0 To 1) As Long
        dsEntityTypes(0) = dsObjectType_e.dsCircleType
        dsEntityTypes(1) = dsObjectType_e.dsPolyLineType
```

```
        'Prepare list of entities
        Dim dsEntities(0 To 1) As Object
        Set dsEntities(0) = dsCircle
        Set dsEntities(1) = dsPolyLine
```

```
        'Create linear pattern
        dsSketchManager.PatternLinear numberElementsOnVerticalAxis, numberElementsOnHorizontalAxis, spacingonVerticalAxis, spacingOnHorizontalAxis, patternAngle, dsEntityTypes, dsEntities
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
