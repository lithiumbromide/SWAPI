---
title: "Change Note Text Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Note_Text_Example_VB.htm"
---

# Change Note Text Example (VBA)

This example shows how to change the note on
a drawing template by opening the drawing template for editing and then selecting
the note and using the INote::SetText method to modify the note.

```
'---------------------------------------------------------------------
' Preconditions: Open public_documents\samples\tutorial\api\2012-sm.slddrw.
'
' Postconditions:
' 1. Examine the title block in the drawing.
' 2. Gets the first drawing view, which is the drawing template.
' 3. Iterates all notes in the drawing template, replacing notes
'    matching initString with newString.
' 4. Examine the title block again to verify step 3.
'
' NOTE: Because the drawing is used elsewhere, do not save changes.
'---------------------------------------------------------------------
```

```
Option Explicit
```

```
Const NumStrings As Long = 3
Dim initString(NumStrings) As String
Dim newString(NumStrings) As String
```

```
Private Sub InitStrings()
    ' Initial strings from drawing
    initString(0) = "2012-sm"
    initString(1) = "WEIGHT:"
    initString(2) = "FINISH:"
```

```
    ' Strings to replace initial strings in drawing
    newString(0) = "NEW 2012-sm"
    newString(1) = "NEW WEIGHT:"
    newString(2) = "NEW FINISH:"
End Sub
```

```
Private Sub DoReplaceString(ByRef sNoteText As String)
    Dim i As Long
```

```
    For i = 0 To NumStrings
        sNoteText = Replace(sNoteText, initString(i), newString(i), 1, -1, vbTextCompare)
    Next i
End Sub
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc
    Dim swDraw As SldWorks.DrawingDoc
    Dim swView As SldWorks.View
    Dim swNote As SldWorks.Note
    Dim sNoteText As String
    Dim nTextCount As Long
    Dim i As Long
```

```
    InitStrings
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swDraw = swModel
    Set swView = swDraw.GetFirstView ' This is the drawing template
```

```
    While Not swView Is Nothing
        Set swNote = swView.GetFirstNote2
        While Not swNote Is Nothing
            If swNote.IsCompoundNote Then
                nTextCount = swNote.GetTextCount
                For i = 1 To nTextCount
                    sNoteText = swNote.GetTextAtIndex(i)
                    DoReplaceString sNoteText
                    swNote.SetTextAtIndex i, sNoteText
                Next i
            Else
                sNoteText = swNote.GetText
                DoReplaceString sNoteText
                swNote.SetText sNoteText
            End If
            Set swNote = swNote.GetNext
        Wend
        Set swView = swView.GetNextView
    Wend
```

```
End Sub
```
