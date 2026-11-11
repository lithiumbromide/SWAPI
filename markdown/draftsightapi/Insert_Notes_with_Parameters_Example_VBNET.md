---
title: "Insert Notes with Parameters Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_Notes_with_Parameters_Example_VBNET.htm"
---

# Insert Notes with Parameters Example (VB.NET)

This example shows how to insert Notes with parameters in a drawing document.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VB.NET Windows console project.
' 2. Copy and paste this example into the VB.NET IDE.
' 3. Add a reference to:
'    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
' 4. Start DraftSight and open a document.
' 5. Start debugging the project.
'
' Postconditions: A message box pops up when the Notes with
' parameters are inserted in the drawing document.
'----------------------------------------------------------------
```

```
Imports DraftSight.Interop.dsAutomation
Module Module1
```

```
    Sub Main()
```

```
        Dim dsApp As Application
        Dim dsDoc As Document
        Dim dsModel As Model
        Dim dsSketchManager As SketchManager
        Dim dsNote As Note
        Dim x1, y1, z1, x2, y2, z2 As Double
        Dim strArray(0 To 1) As String
        Dim angle, height, lineSpaceDistance, width As Double
        Dim justify As dsNoteJustification_e
        Dim lineSpacingStyle As dsNoteLineSpacingStyle_e
        Dim textStyle As String
```

```
        'Connect to DraftSight
        dsApp = GetObject(, "DraftSight.Application")
	dsApp.AbortRunningCommand() ' abort any command currently running in DraftSight to avoid nested commands
```

```
        'Get active document
        dsDoc = dsApp.GetActiveDocument()
        If Not dsDoc Is Nothing Then
```

```
            'Get model space
            dsModel = dsDoc.GetModel()
```

```
            'Get Sketch Manager
            dsSketchManager = dsModel.GetSketchManager()
```

```
            'Note parameters
            x1 = 10.0#
            y1 = 10.0#
            z1 = 0.0#
            x2 = 60.0#
            y2 = 20.0#
            z2 = 0.0#
            strArray(0) = "First Note's text line."
            strArray(1) = "Second Note's text line."
            angle = 0.0#
            height = 1.0#
            justify = dsNoteJustification_e.dsNoteJustification_BottomCenter
            lineSpacingStyle = dsNoteLineSpacingStyle_e.dsNoteLineSpacingStyle_AtLeast
            lineSpaceDistance = 1.5
            textStyle = "Standard"
            width = 25.0#
```

```
            'Add Notes with parameters
            dsNote = dsSketchManager.InsertNoteWithParameters(x1, y1, z1, x2, y2, z2, strArray, angle, height, justify, lineSpacingStyle, lineSpaceDistance, textStyle, width)
```

```
            If Not dsNote Is Nothing Then
                MsgBox("Notes with parameters were inserted in the drawing.")
            End If
```

```
        Else
```

```
            MsgBox("There are no open documents in DraftSight.")
```

```
        End If
```

```
    End Sub
```

```
End Module
```
