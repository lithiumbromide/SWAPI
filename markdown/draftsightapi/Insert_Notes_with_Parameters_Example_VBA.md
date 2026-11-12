---
title: "Insert Notes with Parameters Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_Notes_with_Parameters_Example_VBA.htm"
---

# Insert Notes with Parameters Example (VBA)

This example shows how to insert Notes with parameters in a drawing document.

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
' Postconditions: A message box pops up when the Notes with
' with parameters are inserted in the drawing document.
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
    Dim angle, height, lineSpaceDistance, width As Double
    Dim justify As DraftSight.dsNoteJustification_e
    Dim lineSpacingStyle As DraftSight.dsNoteLineSpacingStyle_e
    Dim textStyle As String
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
        'Note parameters
        x1 = 10#
        y1 = 10#
        z1 = 0#
        x2 = 60#
        y2 = 20#
        z2 = 0#
        strArray(0) = "First Note's text line."
        strArray(1) = "Second Note's text line."
        angle = 0#
        height = 1#
        justify = dsNoteJustification_BottomCenter
        lineSpacingStyle = dsNoteLineSpacingStyle_AtLeast
        lineSpaceDistance = 1.5
        textStyle = "Standard"
        width = 25#
```

```
        'Add Notes with parameters
        Set dsNote = dsSketchManager.InsertNoteWithParameters(x1, y1, z1, x2, y2, z2, strArray, angle, height, justify, lineSpacingStyle, lineSpaceDistance, textStyle, width)
```

```
        If Not dsNote Is Nothing Then
            MsgBox "Notes with parameters were added to the drawing."
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
