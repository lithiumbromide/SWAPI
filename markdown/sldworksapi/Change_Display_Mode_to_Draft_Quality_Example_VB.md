---
title: "Change Display Mode to Draft Quality Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Display_Mode_to_Draft_Quality_Example_VB.htm"
---

# Change Display Mode to Draft Quality Example (VBA)

This example shows how to change all of the display modes of all of the drawing views in a drawing to draft quality.

```
'------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\introsw\bolt_assembly.slddrw.
' 2. Move the cursor around in a drawing view to see the
'    current display mode for that drawing view (a blank
'    rectangle indicates that the display mode is high quality).
'
' Postconditions:
' 1. Changes the display modes of all drawing views to draft quality.
' 2. Move the cursor around in a drawing view to see the current display
'    mode for that drawing view (a square with a lighting bolt indicates
'    that the display mode is draft quality).
'
' NOTE: Because the drawing is used elsewhere, do not save changes.
'------------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swDraw As SldWorks.DrawingDoc
    Dim swSheet As SldWorks.Sheet
    Dim swView As SldWorks.View
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swDraw = swApp.ActiveDoc
    Set swSheet = swDraw.GetCurrentSheet
    Set swView = swDraw.GetFirstView
```

```
    While Not swView Is Nothing
        If swSheet.GetName <> swView.Name Then
            ' Does not work on drawing sheet, which IDrawingDoc::GetFirstView returns
            bRet = swView.SetDisplayMode3(False, swView.GetDisplayMode2, True, True): Debug.Assert bRet
        End If
        Set swView = swView.GetNextView
    Wend
```

```
End Sub
```
