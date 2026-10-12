---
title: "Insert Reference Plane Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Reference_Plane_Example_VB.htm"
---

# Insert Reference Plane Example (VBA)

This example shows how to create a constraint-based angle reference plane.

```
'-----------------------------------------------------------
' 1. Verify that the specified part exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Creates a constraint-based reference plane.
' 2. Examine the Immediate window.
'
' NOTE: Because the part is used elsewhere, do not
' save changes.
'-----------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swFeatureManager As SldWorks.FeatureManager
Dim swFeature As SldWorks.Feature
Dim swRefPlane As SldWorks.RefPlane
Dim swSelMgr As SldWorks.SelectionMgr
Dim swRefPlaneFeatureData As SldWorks.RefPlaneFeatureData
Dim fileerror As Long
Dim filewarning As Long
Dim boolstatus As Boolean
Dim planeType As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    swApp.OpenDoc6 "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\plate.sldprt", swDocPART, swOpenDocOptions_Silent, "", fileerror, filewarning
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
    Set swFeatureManager = swModel.FeatureManager
    Set swSelMgr = swModel.SelectionManager
```

```
    ' Create a constraint-based reference plane
    boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.028424218552, 0.07057725774359, 0, True, 0, Nothing, 0)
    boolstatus = swModelDocExt.SelectByID2("", "EDGE", 0.05976462601598, 0.0718389621656, 1.242036435087E-04, True, 1, Nothing, 0)
    Set swRefPlane = swFeatureManager.InsertRefPlane(16, 0.7853981633975, 4, 0, 0, 0)
```

```
    ' Get type of the just-created reference plane
    boolstatus = swModelDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, False, 0, Nothing, swSelectOptionDefault)
    Set swFeature = swSelMgr.GetSelectedObject6(1, -1)
    Set swRefPlaneFeatureData = swFeature.GetDefinition
    planeType = swRefPlaneFeatureData.Type2
    Debug.Print "Type of reference plane using IRefPlaneFeatureData::Type2: "
    Select Case planeType
        Case 0
            Debug.Print "  Invalid"
        Case 1
            Debug.Print "  Undefined"
        Case 2
            Debug.Print "  Line Point"
        Case 3
            Debug.Print "  Three Points"
        Case 4
            Debug.Print "  Line Line"
        Case 5
            Debug.Print "  Distance"
        Case 6
            Debug.Print "  Parallel"
        Case 7
            Debug.Print "  Angle"
        Case 8
            Debug.Print "  Normal"
        Case 9
            Debug.Print "  On Surface"
        Case 10
            Debug.Print "  Standard"
        Case 11
            Debug.Print "  Constraint-based"
        End Select
            Debug.Print ""

    planeType = swRefPlaneFeatureData.Type
    Debug.Print "Type of reference plane using IRefPlaneFeatureData::Type: "
    Select Case planeType
        Case 0
            Debug.Print "  Invalid"
        Case 1
            Debug.Print "  Undefined"
        Case 2
            Debug.Print "  Line Point"
        Case 3
            Debug.Print "  Three Points"
        Case 4
            Debug.Print "  Line Line"
        Case 5
            Debug.Print "  Distance"
        Case 6
            Debug.Print "  Parallel"
        Case 7
            Debug.Print "  Angle"
        Case 8
            Debug.Print "  Normal"
        Case 9
            Debug.Print "  On Surface"
        Case 10
            Debug.Print "  Standard"
        Case 11
            Debug.Print "  Constraint-based"
        End Select
            Debug.Print ""
```

```
    swModel.ClearSelection2 True
```

```
End Sub
```
