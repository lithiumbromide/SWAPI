---
title: "Get All Sketch Relations and Their Types Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_All_Sketch_Relations_and_Their_Types_Example_VB.htm"
---

# Get All Sketch Relations and Their Types Example (VBA)

This example shows how to get all of the sketch relations and their types for the selected sketch.

```
'----------------------------------------------------------------
' Preconditions:
' 1. Open a part document.
' 2. Select a sketch.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets the sketch relations for the selected sketch.
' 2. Examine the Immediate window.
'----------------------------------------------------------------
Option Explicit
```

```
Public Enum swSketchRelationFilterType_e
    swAll = 0
    swDangling = 1
    swOverDefining = 2
    swExternal = 3
    swDefinedInContext = 4
    swLocked = 5
    swBroken = 6
    swSelectedEntities = 7
End Enum
```

```
Public Enum swConstraintType_e
    swConstraintType_INVALIDCTYPE = 0
    swConstraintType_DISTANCE = 1
    swConstraintType_ANGLE = 2
    swConstraintType_RADIUS = 3
    swConstraintType_HORIZONTAL = 4
    swConstraintType_VERTICAL = 5
    swConstraintType_TANGENT = 6
    swConstraintType_PARALLEL = 7
    swConstraintType_PERPENDICULAR = 8
    swConstraintType_COINCIDENT = 9
    swConstraintType_CONCENTRIC = 10
    swConstraintType_SYMMETRIC = 11
    swConstraintType_ATMIDDLE = 12
    swConstraintType_ATINTERSECT = 13
    swConstraintType_SAMELENGTH = 14
    swConstraintType_DIAMETER = 15
    swConstraintType_OFFSETEDGE = 16
    swConstraintType_FIXED = 17
    swConstraintType_ARCANG90 = 18
    swConstraintType_ARCANG180 = 19
    swConstraintType_ARCANG270 = 20
    swConstraintType_ARCANGTOP = 21
    swConstraintType_ARCANGBOTTOM = 22
    swConstraintType_ARCANGLEFT = 23
    swConstraintType_ARCANGRIGHT = 24
    swConstraintType_HORIZPOINTS = 25
    swConstraintType_VERTPOINTS = 26
    swConstraintType_COLINEAR = 27
    swConstraintType_CORADIAL = 28
    swConstraintType_SNAPGRID = 29
    swConstraintType_SNAPLENGTH = 30
    swConstraintType_SNAPANGLE = 31
    swConstraintType_USEEDGE = 32
    swConstraintType_ELLIPSEANG90 = 33
    swConstraintType_ELLIPSEANG180 = 34
    swConstraintType_ELLIPSEANG270 = 35
    swConstraintType_ELLIPSEANGTOP = 36
    swConstraintType_ELLIPSEANGBOTTOM = 37
    swConstraintType_ELLIPSEANGLEFT = 38
    swConstraintType_ELLIPSEANGRIGHT = 39
    swConstraintType_ATPIERCE = 40
    swConstraintType_DOUBLEDISTANCE = 41
    swConstraintType_MERGEPOINTS = 42
    swConstraintType_ANGLE3P = 43
    swConstraintType_ARCLENGTH = 44
    swConstraintType_NORMAL = 45
    swConstraintType_NORMALPOINTS = 46
    swConstraintType_SKETCHOFFSET = 47
    swConstraintType_ALONGX = 48
    swConstraintType_ALONGY = 49
    swConstraintType_ALONGZ = 50
    swConstraintType_ALONGXPOINTS = 51
    swConstraintType_ALONGYPOINTS = 52
    swConstraintType_ALONGZPOINTS = 53
    swConstraintType_PARALLELYZ = 54
    swConstraintType_PARALLELZX = 55
    swConstraintType_INTERSECTION = 56
    swConstraintType_PATTERNED = 57
    swConstraintType_ISOBYPOINT = 58
    swConstraintType_SAMEISOPARAM = 59
    swConstraintType_FITSPLINE = 60
End Enum
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swFeat As SldWorks.Feature
    Dim swSketch As SldWorks.Sketch
    Dim swSkRelMgr As SldWorks.SketchRelationManager
    Dim vSkRelArr As Variant
    Dim swSkRel As SldWorks.SketchRelation
    Dim relType As Long
    Dim i As Long
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFeat = swSelMgr.GetSelectedObject5(1)
    Set swSketch = swFeat.GetSpecificFeature2
    Set swSkRelMgr = swSketch.RelationManager
```

```
    vSkRelArr = swSkRelMgr.GetRelations(swAll)
```

```
    For i = 0 To UBound(vSkRelArr)
        Set swSkRel = vSkRelArr(i)
        relType = swSkRel.GetRelationType
        Debug.Print relType
    Next i
```

```
End Sub
```
