---
title: "Get Note Text Formatting Properties Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Note_Text_Formatting_Properties_Example_VB.htm"
---

# Get Note Text Formatting Properties Example (VBA)

This example shows how to get the text formatting out of a note.

```
'------------------------------------------------
' Preconditions:
' 1. Open a part containing a note.
' 2. Select the note.
' 3. Open the Immediate window.
'
' Postconditions: Examine the Immediate window.
'------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim Part As SldWorks.ModelDoc2
    Dim SelMgr As SldWorks.SelectionMgr
    Dim Note As SldWorks.Note
    Dim TextFormat As SldWorks.TextFormat
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set Part = swApp.ActiveDoc
    If Not Part Is Nothing Then
        Set SelMgr = Part.SelectionManager()
        If SelMgr.GetSelectedObjectCount() <> 1 Then
            MsgBox "Please select a note."
        ElseIf SelMgr.GetSelectedObjectType(1) <> swSelNOTES Then
            MsgBox "Please select a note."
        Else
            Set Note = SelMgr.GetSelectedObject2(1)
            Set TextFormat = Note.GetTextFormat
            Debug.Print "Text format:"
            Debug.Print "  Bold: " & TextFormat.Bold
            Debug.Print "  Italic: " & TextFormat.Italic
            Debug.Print "  Underline: " & TextFormat.Underline
            Debug.Print "  Strikeout: " & TextFormat.Strikeout
            Debug.Print "  Typeface: " & TextFormat.TypeFaceName
            If TextFormat.IsHeightSpecifiedInPts() Then
                Debug.Print "  Height in points: " & TextFormat.CharHeightInPts
            End If
        End If
    End If
```

```
End Sub
```
