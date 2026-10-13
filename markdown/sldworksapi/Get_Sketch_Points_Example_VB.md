---
title: "Get Sketch Points Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sketch_Points_Example_VB.htm"
---

# Get Sketch Points Example (VBA)

This example shows how to loop through a selected sketch that has one or more sketch points and get the x and y coordinates of every sketch point.

```
'-------------------------------------------------------
' Preconditions:
' 1. Open a model containing a sketch with one or more
'    sketch points.
' 2. Select the sketch.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets the value for each sketch point in the sketch.
' 2. Gets the x and y coordinates of each sketch
'    point in the sketch.
' 3. Examine the Immediate window.
'--------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swSketch As SldWorks.Sketch
    Dim swFeat As SldWorks.Feature
    Dim swSketchPoint As SldWorks.SketchPoint
    Dim sketchPointArray As Variant
    Dim i As Long
    Dim xValue As Double
    Dim yValue As Double
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
    Set swSketch = swFeat.GetSpecificFeature2
    Debug.Print "FeatName = " + swFeat.Name
    Debug.Print " "
```

```
    sketchPointArray = swSketch.GetSketchPoints2
    For i = 0 To UBound(sketchPointArray)
        ' Get value returned by ISketchPoint::GetCoords
        Set swSketchPoint = sketchPointArray(i)
        Debug.Print "Value returned by ISketchPoint::GetCoords: " & swSketchPoint.GetCoords
```

```
        ' Get the x & y coordinates
        xValue = sketchPointArray(i).X
        yValue = sketchPointArray(i).Y
        Debug.Print "Sketch point coordinates: "
        Debug.Print "  x: " & xValue
        Debug.Print "  y: " & yValue
        Debug.Print " "
        ' Do something useful with the data
    Next i
```

```
End Sub
```
