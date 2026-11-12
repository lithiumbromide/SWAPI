---
title: "Get Sheet Numbers and Names Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sheet_Numbers_and_Names_Example_VB.htm"
---

# Get Sheet Numbers and Names Example (VBA)

This example shows how to get the sheet numbers and names for multiple sheets in a drawing document.

```
'---------------------------------------------
' Preconditions:
' 1. Open a drawing that has multiple sheets.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the number and names of the sheets.
' 2. Examine the Immediate window.
'---------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swDraw As SldWorks.DrawingDoc
    Dim swSheet As SldWorks.Sheet
    Dim vSheetNames As Variant
    Dim bRet As Boolean
    Dim i As Long
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swDraw = swModel
    Set swSheet = swDraw.GetCurrentSheet
    Debug.Print "FileName = " + swModel.GetPathName
    Debug.Print "  Current sheet = " & swSheet.GetName
    Debug.Print ""
    vSheetNames = swDraw.GetSheetNames
    For i = 0 To UBound(vSheetNames)
        Debug.Print "  SheetName[" & i & "] = " & vSheetNames(i)
    Next i
```

```
End Sub
```
