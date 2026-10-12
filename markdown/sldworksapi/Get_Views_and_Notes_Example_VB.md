---
title: "Get Views and Notes(VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Views_and_Notes_Example_VB.htm"
---

# Get Views and Notes(VBA)

## Get Views and Notes (VBA)

This example shows how to get all of the views and notes in a drawing document.

```vb
'--------------------------------------------
' Preconditions: Drawing document is open and at least
'                one view has some notes.
'
' Postconditions: None
'
' NOTE: IDrawingDoc::GetViews returns both sheets and views.
'----------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swDrawDoc As SldWorks.DrawingDoc
Dim swView As SldWorks.View
Dim swNote As SldWorks.Note
Dim sheetCount As Long
Dim viewCount As Long
Dim noteCount As Long
Dim i As Long

Sub main()

Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swDrawDoc = swModel

Dim viewCount As Long
viewCount = swDrawDoc.GetViewCount

Dim ss As Variant
ss = swDrawDoc.GetViews

For sheetCount = LBound(ss) To UBound(ss)
    Dim vv As Variant
    vv = ss(sheetCount)

    For viewCount = LBound(vv) To UBound(vv)
        Debug.Print (vv(viewCount).GetName2())

        Dim vNotes As Variant
        noteCount = vv(viewCount).GetNoteCount

        If noteCount > 0 Then
            vNotes = vv(viewCount).GetNotes
            For i = 0 To noteCount - 1
                Debug.Print "  Note text: " & vNotes(i).GetText
            Next
        End If

    Next viewCount

Next sheetCount

End Sub
```
