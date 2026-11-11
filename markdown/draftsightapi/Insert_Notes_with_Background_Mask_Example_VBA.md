---
title: "Insert Notes with Background Mask Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_Notes_with_Background_Mask_Example_VBA.htm"
---

# Insert Notes with Background Mask Example (VBA)

This example shows how to insert Notes with a background Mask in a drawing document.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to the DraftSight type library,
'    install_dir\bin\dsAutomation.dll.
' 4. Press F5.
'
' Postconditions:
' 1. Inserts two Notes with a blue background Mask in the drawing.
' 2. Zooms to fit the two Notes in the drawing.
' 3. Examine the drawing.
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
    Dim dsNote As DraftSight.Note
    Dim x1, y1, z1, x2, y2, z2 As Double
    Dim strArray(0 To 1) As String
```

```
    'Connect to DraftSight
    Set dsApp = GetObject(, "DraftSight.Application")
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
        'Note parameters
        x1 = 10#
        y1 = 10#
        z1 = 0#
        x2 = 60#
        y2 = 20#
        z2 = 0#
        strArray(0) = "First Note's text line."
        strArray(1) = "Second Note's text line."

        'Add a Note
        Set dsNote = dsSketchManager.InsertNote(x1, y1, z1, x2, y2, z2, strArray)
```

```
        'Change height of Note text
        dsNote.TextHeight = 2
```

```
        'Change Note to use blue background Mask
        dsNote.UseDrawingBackgroundColor = False
        dsNote.BackgroundMask = True
        dsNote.BackgroundBorderOffsetFactor = 4
        Dim dsColor As DraftSight.Color
        Set dsColor = dsNote.Color
        dsColor.SetNamedColor dsNamedColor_Blue
        dsNote.BackgroundFillColor = dsColor
```

```
        'Zoom to fit the Note
        dsApp.Zoom dsZoomRange_Fit, Null, Null
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
