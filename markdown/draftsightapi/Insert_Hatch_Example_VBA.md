---
title: "Insert Hatch Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_Hatch_Example_VBA.htm"
---

# Insert Hatch Example (VBA)

This example shows how to insert a Hatch in a drawing document.

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
' Postconditions: A Hatch is inserted in the drawing document
' and zoomed to fit.
```

```
'----------------------------------------------------------------
Option Explicit
```

```
    Dim dsApp As DraftSight.Application
    Dim dsDoc As DraftSight.Document
    Dim dsModel As DraftSight.Model
    Dim dsSketchManager As DraftSight.SketchManager
```

```
    Sub main()
    'Connect to DraftSight
    Set dsApp = GetObject(, "DraftSight.Application")
    'Abort any command currently running in DraftSight
    'to avoid nested commands
    dsApp.AbortRunningCommand
```

```
    'Get active document
    Set dsDoc = dsApp.GetActiveDocument
    If dsDoc Is Nothing Then
        MsgBox ("There are no open documents in DraftSight.")
        End
    End If
```

```
    'Get model space
    Set dsModel = dsDoc.GetModel
```

```
    'Get Sketch Manager
    Set dsSketchManager = dsModel.GetSketchManager
```

```
    'Hatch parameters
    Dim boundaryPointCountArray(0) As Long
    boundaryPointCountArray(0) = 4
```

```
    Dim boundaryPoints(0 To 7) As Double
    boundaryPoints(0) = 0: boundaryPoints(1) = 0
    boundaryPoints(2) = 2: boundaryPoints(3) = 0
    boundaryPoints(4) = 2: boundaryPoints(5) = 2
    boundaryPoints(6) = 0: boundaryPoints(7) = 2
```

```
    Dim patternName As String
    patternName = "ANSI31"
```

```
    Dim patternScale As Double
    patternScale = 1#
```

```
    Dim patternAngle As Double
    patternAngle = 3.14159265358979 / 4 'In radians
```

```
    'Insert Hatch
    Dim dsHatch As DraftSight.Hatch
    Set dsHatch = dsSketchManager.InsertHatchByBoundary(boundaryPointCountArray, boundaryPoints, patternName, patternScale, patternAngle)
```

```
    If Not dsHatch Is Nothing Then
        'Change color of Hatch
        Dim dsColor As DraftSight.Color
        Set dsColor = dsHatch.Color
        dsColor.SetNamedColor dsNamedColor_Green
        dsHatch.Color = dsColor
```

```
        'Zoom to fit
        dsApp.Zoom dsZoomRange_Fit, Nothing, Nothing
    Else
        MsgBox ("Hatch entity was not added to the current drawing.")
    End If
End Sub
```
