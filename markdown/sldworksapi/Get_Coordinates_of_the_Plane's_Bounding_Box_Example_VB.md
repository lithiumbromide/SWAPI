---
title: "Get Coordinates of the Plane's Bounding Box Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Coordinates_of_the_Plane's_Bounding_Box_Example_VB.htm"
---

# Get Coordinates of the Plane's Bounding Box Example (VBA)

This example shows how to get top-left and bottom-right coordinates for a reference plane's bounding box.

```
'-----------------------------------------------------
' Preconditions:
' 1. Verify that the specified part document template
'    exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens a new part document.
' 2. Inserts a reference plane.
' 3. Gets the top-left and bottom-right coordinates
'    of the reference plane's bounding box.
' 4. Examine the Immediate window.
'------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swFeatureMgr As SldWorks.FeatureManager
Dim swRefPlane As SldWorks.RefPlane
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim status As Boolean
Dim mathPoints As Variant
Dim arrData As Variant
Dim i As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    'Create reference plane
    Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2015\templates\Part.prtdot", 0, 0, 0)
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, True, 0, Nothing, 0)
    Set swFeatureMgr = swModel.FeatureManager
    Set swRefPlane = swFeatureMgr.InsertRefPlane(8, 0.0889, 0, 0, 0, 0)
```

```
    'Get top-left and bottom-right coordinates
    'of the reference plane's bounding box
    mathPoints = swRefPlane.BoundingBox 'Two (2) MathPoint objects are always returned
    For i = 0 To UBound(mathPoints)
        arrData = mathPoints(i).arrayData
        Debug.Print " Points x, y, z = " & arrData(0) & ", " & arrData(1) & ", " & arrData(2)
    Next i
```

```
End Sub
```
