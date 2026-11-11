---
title: "Construct Circle Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Construct_Circle_Example_VBA.htm"
---

# Construct Circle Example (VBA)

This example shows how to construct a Circle.

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
' Postconditions: A message box pops up when a Circle is
' constructed in the drawing document.
'----------------------------------------------------------------
```

```
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
    Dim dsCircle As DraftSight.Circle
    Dim centerX, centerY, centerZ, radius As Double
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
        centerX = 1#
        centerY = 2#
        centerZ = 0#
        radius = 5#
```

```
        'Construct a Circle
        Set dsCircle = dsSketchManager.InsertCircle(centerX, centerY, centerZ, radius)
```

```
        If Not dsCircle Is Nothing Then
            MsgBox "Circle was added to drawing."
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
