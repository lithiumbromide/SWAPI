---
title: "Get Notes from New or Existing Title Block (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Notes_from_New_or_Existing_Title_Block_Example_VB.htm"
---

# Get Notes from New or Existing Title Block (VBA)

This example shows how to create a title block in a drawing, if one does not already exist, and how to get the notes from an existing title block in a drawing.

```vb
'--------------------------------------------------------
' Preconditions: Drawing document is open.
'
' Postconditions: If the drawing contains a title block, then
'                 notes of that block are printed
'                 to the Immediate window. If not, then
'                 a title block is created.
'-------------------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As ModelDoc2
Dim swExt As ModelDocExtension
Dim swSelMgr As SelectionMgr
Dim swView As View
Dim swDraw As DrawingDoc

Sub main()

Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swExt = swModel.Extension
Set swSelMgr = swModel.SelectionManager

Set swDraw = swModel

Dim swSheet As Sheet
Set swSheet = swDraw.GetCurrentSheet

Dim swTitleBlock As TitleBlock
Set swTitleBlock = swSheet.TitleBlock

Dim vNotes As Variant
Dim i As Integer
' Create title block if one doesn't exist
If swTitleBlock Is Nothing Then
    Set swView = swDraw.GetFirstView

    vNotes = swView.GetNotes
    ' Add first two notes to the title block

    Dim notesArray(1) As Object
    Set notesArray(0) = vNotes(0)
    Set notesArray(1) = vNotes(1)

    Set swTitleBlock = swSheet.InsertTitleBlock(notesArray)

End If

vNotes = swTitleBlock.GetNotes

For i = 0 To UBound(vNotes)
    Dim swNote As Note
    Set swNote = vNotes(i)

    Debug.Print "Name: " & swNote.GetName
    Debug.Print "Value: " & swNote.GetText

Next
End Sub
```
