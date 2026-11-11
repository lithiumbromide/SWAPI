---
title: "Insert Point Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_Point_Example_VBA.htm"
---

# Insert Point Example (VBA)

This example shows how to insert a point in a drawing document.

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
' Postconditions: A message box pops up when a point is
' inserted in the drawing document. A SimpleNote is also
' added to the drawing that identifies where the point was inserted.
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
    Dim dsPoint As DraftSight.Point
    Dim x, y, z As Double
    Dim dsSimpleNote As DraftSight.SimpleNote
    Dim noteValue As String
    Dim angle, height As Double
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
        'Point parameters
        x = 5#
        y = 5#
        z = 0#
```

```
        'Add a point
        Set dsPoint = dsSketchManager.InsertPoint(x, y, z)
```

```
        'SimpleNote parameters (angle value should be passed in radians)
        noteValue = "Sample text"
        angle = 3.14159265358979 / 4 '45 degrees in radians
        height = 1#
        'Add a SimpleNote
        Set dsSimpleNote = dsSketchManager.InsertSimpleNote(x, y, z, height, angle, noteValue)
```

```
        If Not dsPoint Is Nothing Then
            MsgBox "Point was added to drawing where SimpleNote was added."
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
