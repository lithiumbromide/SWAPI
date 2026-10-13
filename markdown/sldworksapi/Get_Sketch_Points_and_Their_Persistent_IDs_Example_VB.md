---
title: "Get Sketch Points and Sketch Point IDs Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sketch_Points_and_Their_Persistent_IDs_Example_VB.htm"
---

# Get Sketch Points and Sketch Point IDs Example (VBA)

This example shows how to get all of the sketch points in the selected sketch and their IDs.

```
'--------------------------------------------------
' Preconditions:
' 1. Open a part and select a sketch.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the feature name of the selected sketch and
'    each sketch point ID and their coordinates.
' 2. Examine the Immediate window.
'--------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swSelData As SldWorks.SelectData
    Dim swSketch As SldWorks.Sketch
    Dim swSketchPt As SldWorks.SketchPoint
    Dim swFeat As SldWorks.Feature
    Dim vSketchUserPt As Variant
    Dim vSketchPt As Variant
    Dim vSketchPtID As Variant
    Dim i As Long
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swSelData = swSelMgr.CreateSelectData
    Set swFeat = swSelMgr.GetSelectedObject6(1, 0)
    Set swSketch = swFeat.GetSpecificFeature2
```

```
    Debug.Print "Feature name = " + swFeat.Name
```

```
    vSketchUserPt = swSketch.GetUserPoints2
    For i = 0 To UBound(vSketchUserPt) / 3 - 1
        ' Coordinates in sketch space
        Debug.Print "  User point (" & i & ") = (" & vSketchUserPt(3 * i + 0) * 1000# & ", " & vSketchUserPt(3 * i + 1) * 1000# & ", " & vSketchUserPt(3 * i + 2) * 1000# & ") mm"
    Next i
```

```
    vSketchPt = swSketch.GetSketchPoints2
    For i = 0 To UBound(vSketchPt)
        Set swSketchPt = vSketchPt(i)
```

```
        ' Will fail if point has been deleted
        ' or if point references another entity;
        ' for example, point in sketch or vertex
        bRet = swSketchPt.Select4(True, swSelData)
```

```
        ' Dump persistent identifier
        vSketchPtID = swSketchPt.GetID
        Debug.Print "  Sketch point ID (" & i & ") = [" & vSketchPtID(0) & ", " & vSketchPtID(1) & "]"
        Debug.Print "    Sketch point coordinates (" & swSketchPt.X * 1000# & ", " & swSketchPt.Y * 1000# & ", " & swSketchPt.Z * 1000# & ") mm"
    Next i
```

```
End Sub
```
