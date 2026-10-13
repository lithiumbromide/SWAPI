---
title: "Calculate Closest Distance Between Faces Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Calculate_Closest_Distance_Between_Faces_Example_VB.htm"
---

# Calculate Closest Distance Between Faces Example (VBA)

This example shows how to calculate the closest distance between two faces.

**NOTE:** The SOLIDWORKS Design user interface can measure the distance between two selected faces. The corresponding method for this functionality is IModelDoc2::ClosestDistance. If any of the faces is cylindrical, then the measurement point is taken from the axis of the cylinder. This is by design and the intended behavior. However, in some circumstances, this measurement might not be appropriate. For example, the minimum amount of material between two holes is normally measured between the cylindrical faces and not between the axes. This sample code shows how to detect such situations and to calculate the distance between faces.

```
'-----------------------------------------------
' Preconditions:
' 1. Open a part or fully resolved assembly.
' 2. Select two faces that do not intersect.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Inserts a 3D sketch using the results from
'    the user-interface Measure tool.
' 2. Inserts a 3D sketch showing closest distance
'    between faces.
' 3. Examine the Immediate window, FeatureManager
'    tree, and graphics area.
'-----------------------------------------------
Option Explicit
```

```
Sub CreateLine(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, vPt1 As Variant, vPt2 As Variant)
    Dim swSketchSeg  As SldWorks.SketchSegment
    Dim bRet As Boolean
```

```
    swModel.SetAddToDB True
    swModel.Insert3DSketch2 False
    Set swSketchSeg = swModel.CreateLine2(vPt1(0), vPt1(1), vPt1(2), vPt2(0), vPt2(1), vPt2(2))
    swModel.SetAddToDB False
    swModel.Insert3DSketch2 True
    bRet = swModel.EditRebuild3
End Sub
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swFace1 As SldWorks.Face2
    Dim swFace2 As SldWorks.Face2
    Dim swSurf1 As SldWorks.Surface
    Dim swSurf2 As SldWorks.Surface
    Dim vPoint1 As Variant
    Dim vPoint2 As Variant
    Dim vClosestPt1 As Variant
    Dim vClosestPt2 As Variant
    Dim nDist As Double
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFace1 = swSelMgr.GetSelectedObject6(1, -1)
    Set swFace2 = swSelMgr.GetSelectedObject6(2, -1)
    Set swSurf1 = swFace1.GetSurface
    Set swSurf2 = swFace2.GetSurface
```

```
    'Get the result of the measure command
    'Need the points returned
    nDist = swModel.ClosestDistance(swFace1, swFace2, vPoint1, vPoint2)
    Debug.Print " ClosestDistance = " & nDist * 1000# & " mm"
```

```
    CreateLine swApp, swModel, vPoint1, vPoint2
```

```
    'Use the points returned by the user-interface Measure tool
    'to get the nearest point actually on the faces in question.
    If swSurf1.IsCylinder Then
        'Measure has returned the center point,
        'so use the point on the other surface
        vClosestPt1 = swFace1.GetClosestPointOn(vPoint2(0), vPoint2(1), vPoint2(2))
    Else
        'Probably on the surface, but just to be sure
        vClosestPt1 = swFace1.GetClosestPointOn(vPoint1(0), vPoint1(1), vPoint1(2))
    End If
```

```
    If swSurf2.IsCylinder Then
        'Measure tool returned the center point, so use
        'the point on the other surface
        vClosestPt2 = swFace2.GetClosestPointOn(vPoint1(0), vPoint1(1), vPoint1(2))
    Else
        'Probably on the surface, but just to be sure
        vClosestPt2 = swFace2.GetClosestPointOn(vPoint2(0), vPoint2(1), vPoint2(2))
    End If
```

```
    nDist = Sqr((vClosestPt1(0) - vClosestPt2(0)) ^ 2 + (vClosestPt1(1) - vClosestPt2(1)) ^ 2 + (vClosestPt1(2) - vClosestPt2(2)) ^ 2)
    Debug.Print " Distance = " & nDist * 1000# & " mm"
```

```
    CreateLine swApp, swModel, vClosestPt1, vClosestPt2
```

```
End Sub
```
