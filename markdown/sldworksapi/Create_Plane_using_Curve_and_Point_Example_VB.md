---
title: "Create Plane using Curve and Point Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Plane_using_Curve_and_Point_Example_VB.htm"
---

# Create Plane using Curve and Point Example (VBA)

This example shows how to create a plane using a curve (edge) and a point.

```
'----------------------------------------------------
' Preconditions:
' 1. Open a part or assembly.
' 2. Select an edge and a point.
'
' Postconditions:
' 1. Creates a plane is created using the selected
'    edge and point.
' 2. Examine the graphics area and FeatureManager design
'    tree.
'-----------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swRefPlane As SldWorks.RefPlane
    Dim swFeat As SldWorks.Feature
    Dim vPlaneParam As Variant
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swRefPlane = swModel.CreatePlanePerCurveAndPassPoint3(True, True)
    Set swFeat = swRefPlane
    vPlaneParam = swRefPlane.GetRefPlaneParams
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  Plane name = " + swFeat.Name
    Debug.Print "    Origin  = (" & vPlaneParam(0) * 1000# & ", " & vPlaneParam(1) * 1000# & ", " & vPlaneParam(2) * 1000# & ") mm"
    Debug.Print "    Xvector = (" & vPlaneParam(3) & ", " & vPlaneParam(4) & ", " & vPlaneParam(5) & ")"
    Debug.Print "    Normal  = (" & vPlaneParam(6) & ", " & vPlaneParam(7) & ", " & vPlaneParam(8) & ")"
```

```
    swModel.EditRebuild3
```

```
End Sub
```
