---
title: "Change Bend Radius of Sheet Metal Part Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Bend_Radius_of_Sheet_Metal_Part_Example_VB.htm"
---

# Change Bend Radius of Sheet Metal Part Example (VBA)

This example shows how to change the default bend radius of a sheet metal part.

```
'-----------------------------------------------
' Preconditions:
' 1. Open a sheet metal part.
' 2. Select the Sheet-Metal feature.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Doubles the default bend radius .
' 2. Examine the graphics area and Immediate window.
'-----------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swFeat As SldWorks.Feature
    Dim swSheetMetal As SldWorks.SheetMetalFeatureData
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFeat = swSelMgr.GetSelectedObject5(1)
    Set swSheetMetal = swFeat.GetDefinition
```

```
    Debug.Print "Feature = " & swFeat.Name
    Debug.Print "  Original bend radius = " & swSheetMetal.BendRadius * 1000# & " mm"
```

```
    ' Rollback to change default bend radius
    bRet = swSheetMetal.AccessSelections(swModel, Nothing): Debug.Assert bRet
```

```
    ' Double the default bend radius value
    swSheetMetal.BendRadius = 2# * swSheetMetal.BendRadius
```

```
    ' Apply changes
    bRet = swFeat.ModifyDefinition(swSheetMetal, swModel, Nothing): Debug.Assert bRet
```

```
    Debug.Print "  Modified bend radius = " & swSheetMetal.BendRadius * 1000# & " mm"
```

```
End Sub
```
