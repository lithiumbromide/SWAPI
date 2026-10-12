---
title: "Get x,y,z Locations of Points in Sketch Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_x,y,z_Locations_of_Points_in_Sketch_Example_VB.htm"
---

# Get x,y,z Locations of Points in Sketch Example (VBA)

This example shows how to get the x, y, and z locations of the points in the selected sketch.

```
'---------------------------------------------
' Preconditions:
' 1. Open a part.
' 2. Select a sketch.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets the IDs of the sketch points in the
'    sketch and their model and sketch point
'    x, y, and z locations.
' 2. Examine the Immediate window.
'----------------------------------------------
Option Explicit
```

```
Sub ProcessSketchPoint(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swSkPt As SldWorks.SketchPoint)
    Dim vID As Variant
    Dim swSketch As SldWorks.Sketch
    Dim swMathUtil As SldWorks.MathUtility
    Dim swXform As SldWorks.MathTransform
    Dim nPt(2) As Double
    Dim vPt As Variant
    Dim swMathPt As SldWorks.MathPoint
```

```
    Set swSketch = swSkPt.GetSketch
    vID = swSkPt.GetID
    Debug.Print "    ID = [" & vID(0) & "," & vID(1) & "]"
    If swSketch.Is3D Then
        ' Point is already is in model space
        Debug.Print "      Point (model)    = (" & swSkPt.X * 1000# & ", " & swSkPt.Y * 1000# & ", " & swSkPt.Z * 1000# & ") mm"
    Else
        nPt(0) = swSkPt.X:  nPt(1) = swSkPt.Y:  nPt(2) = swSkPt.Z
        vPt = nPt
        Set swXform = swSketch.ModelToSketchTransform
        Set swXform = swXform.Inverse
        Set swMathUtil = swApp.GetMathUtility
        Set swMathPt = swMathUtil.CreatePoint((vPt))
        Set swMathPt = swMathPt.MultiplyTransform(swXform)
        Debug.Print "      Point (model)    = (" & swMathPt.ArrayData(0) * 1000# & ", " & swMathPt.ArrayData(1) * 1000# & ", " & swMathPt.ArrayData(2) * 1000# & ") mm"
        Debug.Print "      Point (sketch)   = (" & swSkPt.X * 1000# & ", " & swSkPt.Y * 1000# & ", " & swSkPt.Z * 1000# & ") mm"
    End If
End Sub
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
    Dim vSkPtArr As Variant
    Dim vSkPt As Variant
    Dim swSkPt As SldWorks.SketchPoint
    Dim i As Long
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFeat = swSelMgr.GetSelectedObject6(1, 0)
    Set swSketch = swFeat.GetSpecificFeature2
    Debug.Print "Feature = " & swFeat.Name
    Debug.Print "  Sketch Points:"
```

```
    vSkPtArr = swSketch.GetSketchPoints2: If IsEmpty(vSkPtArr) Then Exit Sub
    For Each vSkPt In vSkPtArr
        Set swSkPt = vSkPt
        ProcessSketchPoint swApp, swModel, swSkPt
    Next vSkPt
```

```
End Sub
```
