---
title: "Get COLORREF Values of Standard User-interface Elements (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_COLORREF_Values_of_Standard_User-interface_Elements_Example_VB.htm"
---

# Get COLORREF Values of Standard User-interface Elements (VBA)

This example shows how to get the COLORREF values of SOLIDWORKS Design standard user-interface elements.

```
'---------------------------------------------------------
' Preconditions: Open the Immediate window.
'
' Postconditions:
' 1. Prints the names of the SOLIDWORKS Design standard
'    user-interface, elements (dimensions, backgrounds,
'    drawing paper, sketch status, annotations, etc.) and
'    their COLORREF values to the Immediate window.
' 2. Examine the Immediate window.
'--------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swColorTable As SldWorks.colortable
Dim standardCount As Long
Dim count As Long
Dim colorName As String
Dim colorRef As Long
```

```
Sub main()
```

```
Set swApp = Application.SldWorks
Set swColorTable = swApp.GetColorTable
```

```
standardCount = swColorTable.GetStandardCount
Debug.Print "SOLIDWORKS Design standard user-interface element and COLORREF value:"
' Iterate through standard colors
For count = 0 To (standardCount - 1)
    ' Get the entry name
    colorName = swColorTable.GetNameAtIndex(count)
    If colorName <> "" Then
        ' Get the entry's COLORREF
        colorRef = swColorTable.GetColorRefAtIndex(count)
        Debug.Print "  " & colorName & " : " & colorRef
    Else
    End If
Next count
```

```
End Sub
```
