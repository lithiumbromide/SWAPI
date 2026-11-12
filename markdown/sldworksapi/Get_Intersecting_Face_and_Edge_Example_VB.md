---
title: "Get Intersecting Face and Edge Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Intersecting_Face_and_Edge_Example_VB.htm"
---

# Get Intersecting Face and Edge Example (VBA)

This example shows how to get the intersection of a face and an edge.

**NOTE:** A face and an edge intersect in a series of points. This example shows how to use some of the geometry- and topology-related methods to get the intersection points.

```
'-------------------------------------------------------
' Preconditions:
' 1. Open a part or a fully resolved assembly.
' 2. Select an intersecting face and edge, in that
'    order, in the graphics area.
'
' Postconditions:
' 1. Inserts a 3D sketch with sketch points located
'    at the intersection of the face and edge.
' 2. Examine the graphics area and FeatureManager design
'    tree.
'-------------------------------------------------------
Option Explicit
```

```
Sub CreatePoints(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, vPtArray As Variant)
    Dim swSketchPt As SldWorks.SketchPoint
    Dim bRet As Boolean
    Dim i As Long
```

```
    swModel.SetAddToDB True
    swModel.Insert3DSketch2 False
```

```
    For i = 0 To UBound(vPtArray) Step 3
        Set swSketchPt = swModel.CreatePoint2(vPtArray(i + 0), vPtArray(i + 1), vPtArray(i + 2))
    Next i
```

```
    swModel.SetAddToDB False
    swModel.Insert3DSketch2 True
```

```
    bRet = swModel.EditRebuild3
```

```
End Sub
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
    Dim swEdge As SldWorks.Edge
    Dim swCurve As SldWorks.Curve
    Dim vPointArray As Variant
    Dim vTArray As Variant
    Dim vUVArray As Variant
    Dim vCurveParam As Variant
    Dim vCurveBounds As Variant
    Dim nCurveBounds(0 To 5) As Double
    Dim i As Long
    Dim bRet As Boolean
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFace = swSelMgr.GetSelectedObject6(1, -1)
    Set swEdge = swSelMgr.GetSelectedObject6(2, -1)
    Set swSurf = swFace.GetSurface
    Set swCurve = swEdge.GetCurve
```

```
    vCurveParam = swEdge.GetCurveParams2
```

```
    For i = 0 To 5
        nCurveBounds(i) = vCurveParam(i)
    Next i
    vCurveBounds = nCurveBounds
```

```
    bRet = swSurf.IntersectCurve(swCurve, (vCurveBounds), vPointArray, vTArray, vUVArray)

    CreatePoints swApp, swModel, vPointArray
```

```
End Sub
```
