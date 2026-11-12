---
title: "Modify Plane by Changing System Value Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Modify_Plane_by_Changing_System_Value_Example_VB.htm"
---

# Modify Plane by Changing System Value Example (VBA)

This example shows how to modify the offset distance of an offset plane by modifying the system value.

```
'--------------------------------------------
' Preconditions:
' 1. Open a model document that has an offset
'    plane named Plane1.
' 2. Note the location of Plane1.
'
' Postconditions:
' 1. Halves the offset distance of Plane1.
' 2. Examine the graphics area and note the
'    the location of Plane1.
'--------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelMgr As SldWorks.SelectionMgr
Dim swDim As SldWorks.Dimension
Dim dimValue As Variant
Dim boolstatus As Boolean
Dim longstatus As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swModelDocExt = swModel.Extension
    boolstatus = swModelDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, False, 0, Nothing, swSelectOptionDefault)
    Set swDim = swModel.Parameter("D1@Plane1")
    dimValue = swDim.GetSystemValue3(swThisConfiguration, Empty)
    dimValue(0) = dimValue(0) / 2
    longstatus = swDim.SetSystemValue3(dimValue(0), swSetValue_InThisConfiguration, Empty)
```

```
    swModel.EditRebuild3
```

```
End Sub
```
