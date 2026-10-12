---
title: "Get Names and Show Model Break Views Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Names_and_Show_Model_Break_Views_Example_VB.htm"
---

# Get Names and Show Model Break Views Example (VBA)

This example shows how to:

- get the names of the Model Break Views in the current configuration of an active model.
- show one of the Model Break Views.

```
'--------------------------------------
' Preconditions:
' 1. Open a part document with multiple
'    hidden Model Break Views.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the number and names of the Model Break
'    Views in the current configuration of the
'    active model.
' 2. Shows one of the Model Break Views.
' 3. Examine the Immediate window and the
'    graphics area.
'----------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim names As Variant
Dim name As String
Dim nbr As Long
Dim i As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
```

```
    'Get and print number and names of Model Break
    'Views in current configuration of the active
    'model
    nbr = swModelDocExt.GetModelBreakViewNames(names)
    ReDim Preserve names(nbr - 1)
    Debug.Print "Model Break Views:"
    Debug.Print "  Number: " & nbr
    Debug.Print "  Names: "
    For i = 0 To nbr - 1
        name = CStr(names(i))
        Debug.Print "    " & name
    Next
```

```
    'Show Model Break View
    swModelDocExt.ShowModelBreakView True, name
```

```
End Sub
```
