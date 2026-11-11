---
title: "Insert Notes with Background Mask Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_Notes_with_Background_Mask_Example_VBNET.htm"
---

# Insert Notes with Background Mask Example (VB.NET)

This example shows how to insert Notes with a background Mask in a drawing document.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VB.NET Windows console project.
' 2. Copy and paste this example into the VB.NET IDE.
' 3. Add a reference to:
'    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
' 4. Start DraftSight.
' 5. Press F5.
'
' Postconditions:
' 1. Inserts two Notes with a blue background Mask in the drawing.
' 2. Zooms to fit the two Notes in the drawing.
' 3. Examine the drawing.
'----------------------------------------------------------------

Imports DraftSight.Interop.dsAutomation
Module Module1

    Sub Main()

        Dim dsApp As Application
        Dim dsDoc As Document
        Dim dsModel As Model
        Dim dsSketchManager As SketchManager
        Dim dsNote As Note
        Dim dsColor As Color
        Dim x1, y1, z1, x2, y2, z2 As Double
        Dim strArray(0 To 1) As String

        'Connect to DraftSight
        dsApp = GetObject(, "DraftSight.Application")

        'Get active document
        dsDoc = dsApp.GetActiveDocument()

        If Not dsDoc Is Nothing Then

            'Get model space
            dsModel = dsDoc.GetModel()

            'Get Sketch Manager
            dsSketchManager = dsModel.GetSketchManager()

            'Note parameters
            x1 = 10.0#
            y1 = 10.0#
            z1 = 0.0#
            x2 = 60.0#
            y2 = 20.0#
            z2 = 0.0#
            strArray(0) = "First Note's text line."
            strArray(1) = "Second Note's text line."

            'Add a note
            dsNote = dsSketchManager.InsertNote(x1, y1, z1, x2, y2, z2, strArray)

            'Change height of Note text
            dsNote.TextHeight = 2

            'Change Note to use blue background Mask
            dsNote.UseDrawingBackgroundColor = False
            dsNote.BackgroundMask = True
            dsColor = dsNote.Color
            dsColor.SetNamedColor(dsNamedColor_e.dsNamedColor_Blue)
            dsNote.BackgroundFillColor = dsColor

            'Zoom to fit the Note
            dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing)

        Else

            MsgBox("There are no open documents in DraftSight.")

        End If

    End Sub

End Module
```
