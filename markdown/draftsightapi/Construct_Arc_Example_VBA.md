---
title: "Construct Arc Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Construct_Arc_Example_VBA.htm"
---

# Construct Arc Example (VBA)

This example shows how to construct an Arc.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to the DraftSight type library,
'    install_dir\bin\dsAutomation.dll.
' 4. Start DraftSight and open a document.
' 5. Run the macro.
'
' Postconditions: A message box pops up when an Arc is
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
    Dim dsArc As DraftSight.CircleArc
    Dim centerX, centerY, centerZ, radius As Double
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
        'Arc parameters (start and end angle values should be in radians)
        centerX = 0#
        centerY = 0#
        centerZ = 0#
        radius = 4#
        startAngle = 0#
        endAngle = 3.14159265358979 '180 degrees in radians
```

```
        'Construct an Arc
        Set dsArc = dsSketchManager.InsertArc(centerX, centerY, centerZ, radius, startAngle, endAngle)
```

```
        If Not dsArc Is Nothing Then
            MsgBox "An Arc was added to drawing."
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
