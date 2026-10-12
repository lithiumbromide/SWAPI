---
title: "Align Assembly Component to Assembly Origin and Planes Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Align_Assembly_Component_to_Assembly_Origin_and_Planes_Example_VB.htm"
---

# Align Assembly Component to Assembly Origin and Planes Example (VBA)

This example shows how to align an assembly component to the assembly origin and planes.

```
'----------------------------------------------
' Preconditions:
' 1. Open an assembly document.
' 2. Select an assembly component.
'
' Postconditions:
' 1. Aligns the selected assembly component
'    to the assembly origin and planes.
' 2. Examine the graphics area.
'-----------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swMathUtil As SldWorks.MathUtility
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swComp As SldWorks.Component2
    Dim swXform As SldWorks.MathTransform
    Dim i As Long
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swMathUtil = swApp.GetMathUtility
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swComp = swSelMgr.GetSelectedObjectsComponent3(1, 0)
    ' Create unit transform
    Set swXform = swMathUtil.CreateTransform(Nothing)
    swComp.Transform2 = swXform
```

```
    ' Rebuild to see updated transform
    bRet = swModel.EditRebuild3
```

```
End Sub
```
