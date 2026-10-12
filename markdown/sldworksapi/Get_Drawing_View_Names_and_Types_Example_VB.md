---
title: "Get Drawing View Names and Types Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Drawing_View_Names_and_Types_Example_VB.htm"
---

# Get Drawing View Names and Types Example (VBA)

This example shows how to get the names and types of all of the drawing views on the current sheet.

```
'---------------------------------------------------------------------------
' Preconditions:
' 1. Open a drawing document.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Traverses the views on the current sheet and gets each view's type.
' 2. Inspect the Immediate window.
'---------------------------------------------------------------------------
Option Explicit
```

```vb
Sub main()
    Dim swApp As SldWorks.SldWorks
     Dim swModel As SldWorks.ModelDoc2
     Dim swDraw As SldWorks.DrawingDoc
     Dim swSheet As SldWorks.Sheet
     Dim swView As SldWorks.View
     Dim bRet As Boolean
    Set swApp = CreateObject("SldWorks.Application")
     Set swModel = swApp.ActiveDoc
     Set swDraw = swModel
     Set swSheet = swDraw.GetCurrentSheet
     Set swView = swDraw.GetFirstView
    Debug.Print "File = " & swModel.GetPathName
     Debug.Print "  " & swSheet.GetName
    While Not swView Is Nothing
         Debug.Print "    " & swView.GetName2 & " [" & swView.Type & "]"
         Set swView = swView.GetNextView
     Wend
End Sub
```
