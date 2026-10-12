---
title: "Get Fixed Face of Sheet Metal Part Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Fixed_Face_of_Sheet_Metal_Part_Example_VB.htm"
---

# Get Fixed Face of Sheet Metal Part Example (VBA)

This example shows how to find and select the fixed face or edge of a sheet metal part.

```
'-----------------------------------------------------------------
' Preconditions:
' 1. Open a sheet metal part.
' 2. Select the sheet metal feature in the FeatureManager design
'    tree.
'
' Postconditions:
' 1. Rolls back the sheet metal feature and selects the fixed face
'    or edge, if either exists.
' 2. Rolls forward the sheet metal part.
'-----------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp                   As SldWorks.SldWorks
    Dim swModel                 As SldWorks.ModelDoc2
    Dim swSelMgr                As SldWorks.SelectionMgr
    Dim swSelData               As SldWorks.SelectData
    Dim swFeat                  As SldWorks.Feature
    Dim swSheetMetal            As SldWorks.SheetMetalFeatureData
    Dim swFixedFaceEnt          As SldWorks.Entity
    Dim bRet                    As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swSelData = swSelMgr.CreateSelectData
    Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
    Set swSheetMetal = swFeat.GetDefinition
```

```
    ' Roll back the model to get access to fixed face
    bRet = swSheetMetal.AccessSelections(swModel, Nothing)
```

```
    Set swFixedFaceEnt = swSheetMetal.FixedReference
```

```
    If Not swFixedFaceEnt Is Nothing Then
        Debug.Print "Got fixed face or fixed edge."
        bRet = swFixedFaceEnt.Select4(False, swSelData)
    Else
        ' Do not have to specify fixed face or fixed edge in
        ' user interface, so not finding either is a valid
        Debug.Print "No fixed face or fixed edge."
    End If
```

```
    Stop
    'Press F5
```

```
    ' Cancel changes and roll back the model
    swSheetMetal.ReleaseSelectionAccess
```

```
End Sub
```
