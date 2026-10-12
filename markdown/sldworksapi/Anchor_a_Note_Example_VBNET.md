---
title: "Anchor a Note Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Anchor_a_Note_Example_VBNET.htm"
---

# Anchor a Note Example (VB.NET)

This example shows how to:

- insert a note.
- set a note's text to all uppercase and its vertical justification to bottom.
- anchor and position a note.

```
'------------------------------------------------------------------------------------
' Preconditions: Open public_documents\samples\tutorial\advdrawings\foodprocessor.slddrw.
'
' Postconditions:
' 1. Inserts a note.
' 2. Sets the note's text to all uppercase and its vertical justification
'    to bottom.
' 3. Locks the note at the specified position.
' 4. Examine the graphics area.
'
' NOTE: Because the model is used elsewhere, do not save changes.
'------------------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Dim Part As ModelDoc2
    Dim myNote As Note
    Dim myAnnotation As Annotation
    Dim boolstatus As Boolean

    Sub main()

        Part = swApp.ActiveDoc
        myNote = Part.InsertNote("Drawing View1 Note")
        If Not myNote Is Nothing Then
            myNote.AllUpperCase = True
            myNote.SetTextVerticalJustification(swTextAlignmentVertical_e.swTextAlignmentBottom)
            myNote.LockPosition = True
            myAnnotation = myNote.GetAnnotation()
            If Not myAnnotation Is Nothing Then
                boolstatus = myAnnotation.SetPosition(0.2, 0.269, 0)
            End If
        End If
        Part.ClearSelection2(True)
        Part.WindowRedraw()

    End Sub

    Public swApp As SldWorks

End Class
```
