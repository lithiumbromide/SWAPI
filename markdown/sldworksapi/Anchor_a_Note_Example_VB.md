---
title: "Anchor a Note Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Anchor_a_Note_Example_VB.htm"
---

# Anchor a Note Example (VBA)

This example shows how to:

- insert a note.
- set a note's text to all uppercase and its vertical justification to bottom.
- anchor and position a note.

'----------------------------------------------------------------------------
' Preconditions: Open `public_documents`**\samples\tutorial\advdrawings\foodprocessor.slddrw**.
'
' Postconditions:
' 1. Inserts a note.
' 2. Sets the note's text to all uppercase and its vertical justification
' to bottom.
' 3. Locks the note at the specified position.
' 4. Examine the graphics area.
'
' NOTE: Because the model is used elsewhere, do not save changes.
'---------------------------------------------------------------------------
Option Explicit

```vb
Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim myNote As SldWorks.Note
 Dim myAnnotation As SldWorks.Annotation
 Dim boolstatus As Boolean

 Sub main()
    Set swApp = Application.SldWorks
     Set Part = swApp.ActiveDoc
    Set myNote = Part.InsertNote("Drawing View1 Note")
     If Not myNote Is Nothing Then
        myNote.AllUpperCase = True
        myNote.SetTextVerticalJustification (swTextAlignmentVertical_e.swTextAlignmentBottom)
        myNote.LockPosition = True
        Set myAnnotation = myNote.GetAnnotation()
        If Not myAnnotation Is Nothing Then
           boolstatus = myAnnotation.SetPosition(0.2, 0.269, 0)
        End If
     End If
    Part.ClearSelection2 True
     Part.WindowRedraw
End Sub
```
