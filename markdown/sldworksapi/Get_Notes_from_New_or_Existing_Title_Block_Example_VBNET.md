---
title: "Get Notes from New or Existing Title Block (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Notes_from_New_or_Existing_Title_Block_Example_VBNET.htm"
---

# Get Notes from New or Existing Title Block (VB.NET)

This example shows how to create a title block in a drawing, if one does not already exist, and how to get the notes from an existing title block in a drawing.

```vb
'--------------------------------------------------------
' Preconditions: Drawing document is open.
'
' Postconditions: If the drawing contains a title block, then
'                 notes of that block are printed
'                 to the Immediate window. If not, the a
'                 title block is created.
'-------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics
Imports System.Runtime.InteropServices

Partial Class SolidWorksMacro

    Dim swModel As ModelDoc2
    Dim swExt As ModelDocExtension
    Dim swSelMgr As SelectionMgr
    Dim swView As View
    Dim swDraw As DrawingDoc

    Public Sub main()

        swModel = swApp.ActiveDoc
        swExt = swModel.Extension
        swSelMgr = swModel.SelectionManager

        swDraw = swModel

        Dim swSheet As Sheet
        swSheet = swDraw.GetCurrentSheet

        Dim swTitleBlock As TitleBlock
        swTitleBlock = swSheet.TitleBlock

        Dim vNotes As Object
        Dim i As Integer
        ' Create title block if one doesn't exist
        If swTitleBlock Is Nothing Then
            swView = swDraw.GetFirstView
            vNotes = swView.GetNotes
            ' Add first two notes to the title block
            Dim notesArray(1) As DispatchWrapper
            notesArray(0) = New DispatchWrapper(vNotes(0))
            notesArray(1) = New DispatchWrapper(vNotes(1))
            swTitleBlock = swSheet.InsertTitleBlock(notesArray)
        End If

        vNotes = swTitleBlock.GetNotes

        For i = 0 To UBound(vNotes)
            Dim swNote As Note
            swNote = vNotes(i)
            Debug.Print("Name: " & swNote.GetName)
            Debug.Print("Value: " & swNote.GetText)
        Next

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks
End Class
```
