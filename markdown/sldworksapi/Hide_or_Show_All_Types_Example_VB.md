---
title: "Hide or Show All Types Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Hide_or_Show_All_Types_Example_VB.htm"
---

# Hide or Show All Types Example (VBA)

This example shows how to hide or show these types in a the current document:

| planes curves axes sketches temporary axes all annotations (including model dimensions and feature dimensions) | origins points coordinate systems routing points |
| --- | --- |

```vb
'-------------------------------------------
Option Explicit

Public Enum swUserPreferenceToggle_e
    swViewDisplayHideAllTypes = 198
End Enum

Sub main()
    Dim swApp                       As SldWorks.SldWorks
    Dim swModel                     As SldWorks.modelDoc
    Dim bRet                        As Boolean
    Dim bShow                       As Boolean
    Dim nResponse                   As Integer

    nResponse = MsgBox("Hide all types?", vbYesNo)
    If nResponse = vbYes Then
        bShow = True
    Else
        bShow = False
    End If

    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc

    bRet = swModel.SetUserPreferenceToggle(swViewDisplayHideAllTypes, bShow): Debug.Assert bRet
End Sub
'-------------------------------------------
```
