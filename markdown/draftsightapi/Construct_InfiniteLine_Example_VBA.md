---
title: "Construct InfiniteLine Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Construct_InfiniteLine_Example_VBA.htm"
---

# Construct InfiniteLine Example (VBA)

This example shows how to construct an InfiniteLine.

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
' Postconditions: A message box pops up when an InfiniteLine is
' constructed in the drawing document.
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
    Dim dsInfiniteLine As DraftSight.InfiniteLine
    Dim x1, y1, z1, x2, y2, z2 As Double
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
        'InfiniteLine parameters
        x1 = 0#
        y1 = 0#
        z1 = 0#
        x2 = 1#
        y2 = 5#
        z2 = 0#
```

```
        'Draw an InfiniteLine
        Set dsInfiniteLine = dsSketchManager.InsertInfiniteLine(x1, y1, z1, x2, y2, z2)
```

```
        If Not dsInfiniteLine Is Nothing Then
            MsgBox "InfiniteLine was added to drawing."
        End If
```

```
    Else
```

```
        MsgBox "There are no open documents in DraftSight"
```

```
    End If
```

```
End Sub
```
