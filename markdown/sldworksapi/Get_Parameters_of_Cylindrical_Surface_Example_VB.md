---
title: "Get Parameters of Cylindrical Surface Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Parameters_of_Cylindrical_Surface_Example_VB.htm"
---

# Get Parameters of Cylindrical Surface Example (VBA)

This example shows how to get the origin, axis, and radius for the selected cylindrical surface.

```
'-----------------------------------------------------
' Preconditions:
' 1. Open a part that contains a cylindrical surface.
' 2. Select the cylindrical surface.
' 3. Open the Immediate window.
'
' Postconditions: Examine the Immediate window.
'----------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swFace As SldWorks.Face2
    Dim swSurf As SldWorks.Surface
    Dim vCylinder As Variant

    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFace = swSelMgr.GetSelectedObject5(1)
    Set swSurf = swFace.GetSurface
```

```
    If swSurf.IsCylinder Then
        vCylinder = swSurf.CylinderParams
        Debug.Print "Origin         = (" & vCylinder(0) * 1000# & ", " & vCylinder(1) * 1000# & ", " & vCylinder(2) * 1000# & ") mm"
        Debug.Print "Axis           = (" & vCylinder(3) & ", " & vCylinder(4) & ", " & vCylinder(5) & ")"
        Debug.Print "Radius         = " & vCylinder(6) * 1000# & " mm"
    End If
```

```
End Sub
```
