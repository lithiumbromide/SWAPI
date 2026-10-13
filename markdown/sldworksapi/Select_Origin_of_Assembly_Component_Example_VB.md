---
title: "Select Origin of Assembly Component Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Origin_of_Assembly_Component_Example_VB.htm"
---

# Select Origin of Assembly Component Example (VBA)

This example shows how to get the origin of an assembly component.

```
'-------------------------------------------------
' Preconditions:
' 1. Open an assembly that is fully resolved.
' 2. Select a component.
'
' Postconditions:
' 1. Selects the origin of the selected component.
' 2. Examine the graphics area.
'--------------------------------------------------
Option Explicit
```

```vb
Sub main()
    Dim swApp                       As SldWorks.SldWorks
    Dim swModel                     As SldWorks.ModelDoc2
    Dim swSelMgr                    As SldWorks.SelectionMgr
    Dim swSelComp                   As SldWorks.Component2
    Dim swCompModel                 As SldWorks.ModelDoc2
    Dim swFeat                      As SldWorks.Feature
    Dim bRet                        As Boolean

    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swSelComp = swSelMgr.GetSelectedObjectsComponent(1)
    Set swCompModel = swSelComp.GetModelDoc

    swModel.ClearSelection2 True

    Set swFeat = swSelComp.FirstFeature
    Do While Not swFeat Is Nothing
        If "OriginProfileFeature" = swFeat.GetTypeName Then
            bRet = swFeat.Select2(False, 0)
            Exit Do
        End If

        Set swFeat = swFeat.GetNextFeature
    Loop
End Sub
```
