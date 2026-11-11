---
title: "Insert Shapes Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_Shapes_Example_VBA.htm"
---

# Insert Shapes Example (VBA)

This example shows how to load a shape file and insert the shapes in the loaded shape file into a drawing.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to the DraftSight type library,
'    install_dir\bin\dsAutomation.dll.
' 4. Start DraftSight and open a document.
' 5. Start debugging the project.
'
' Postconditions:
' 1. Gets the Shape Manager.
' 2. Loads a shape file.
' 3. Gets the shapes in the loaded shape file.
' 4. Inserts the shapes, with an obliquing angle of 30, in the drawing.
' 5. Examine the drawing.
'----------------------------------------------------------------
```

```
Option Explicit
```

```
    Sub Main()
```

```
        Dim dsApp As DraftSight.Application
```

```
        'Connect to DraftSight application
        Set dsApp = GetObject(, "DraftSight.Application")
```

```
        ' Abort any command currently running in DraftSight to avoid nested commands
        dsApp.AbortRunningCommand
```

```
        If dsApp Is Nothing Then
            Return
        End If
```

```
        'Get active document
        Dim dsDoc As Document
        Set dsDoc = dsApp.GetActiveDocument()
        If dsDoc Is Nothing Then
            MsgBox ("There are no open documents in DraftSight.")
            Return
        End If
```

```
        'Get the Shape Manager
        Dim dsShapeMgr As ShapeManager
        Set dsShapeMgr = dsDoc.GetShapeManager()
```

```
        'Load shape file LTypeShp.shx
        Dim shapeFileName As String
        shapeFileName = "C:\Program Files\Dassault Systemes\DraftSight\Fonts\LTypeShp.shx"
```

```
        dsShapeMgr.Load (shapeFileName)
```

```
        'Get shapes
        Dim shapesStrList As Variant
        shapesStrList = dsShapeMgr.GetAvailableShapes()
        Dim shapesCount As Long
        shapesCount = UBound(shapesStrList)
```

```
        'Get Sketch Manager
        Dim dsModel As DraftSight.Model
        Dim dsSketchMgr As DraftSight.SketchManager
        Set dsModel = dsDoc.GetModel
        Set dsSketchMgr = dsModel.GetSketchManager()
```

```
        'Insert shapes
        Dim PositionX As Double
        PositionX = 0#
        Dim PositionY As Double
        PositionY = 0#
        Dim PositionZ As Double
        PositionZ = 0#
        Dim i As Long
        For i = 0 To shapesCount - 1
            Dim dsShape As DraftSight.Shape
            Set dsShape = dsSketchMgr.InsertShape(shapesStrList(i), PositionX, PositionY, PositionZ, 1, 0#)
```

```
            'Change obliquing property
            Dim angle As Double
            angle = 3.14159265358979
            dsShape.Obliquing = (30 * angle) / 180
```

```
            Dim X1 As Double, Y1 As Double, Z1 As Double, X2 As Double, Y2 As Double, Z2 As Double
            dsShape.GetBoundingBox X1, Y1, Z1, X2, Y2, Z2
```

```
            PositionX = PositionX + (X2 - X1) + 5
```

```
        Next
```

```
    End Sub
```
