---
title: "Get View Mode Names for Model Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_View_Mode_Names_for_Model_Example_VB.htm"
---

# Get View Mode Names for Model Example (VBA)

This example shows how to get all of the view mode names for the current part or assembly.

```vb
'-----------------------------------
'
' Preconditions: Part or assembly document is open.
'
' Postconditions: None
'
'-----------------------------------
Option Explicit
Sub main()
    Dim swApp                   As SldWorks.SldWorks
    Dim swModel                 As SldWorks.ModelDoc2
    Dim vModelViewNames         As Variant
    Dim i                       As Long

    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc

    vModelViewNames = swModel.GetModelViewNames

    Debug.Print "FileName = " & swModel.GetPathName
    Debug.Print "  ModelViewCount = " & swModel.GetModelViewCount
    For i = 0 To UBound(vModelViewNames)
        Debug.Print "    " + vModelViewNames(i)
    Next i
End Sub
'------------------------------------------
```
