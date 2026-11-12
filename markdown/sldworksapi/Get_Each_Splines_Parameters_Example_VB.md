---
title: "Get Each Spline's Parameters Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Each_Splines_Parameters_Example_VB.htm"
---

# Get Each Spline's Parameters Example (VBA)

This example shows how to get each spline's parameters in a sketch containing multiple splines.

```
'----------------------------------------------------
' Preconditions:
' 1. Verify that the specified part template exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Creates a sketch containing two splines.
' 2. Gets each spline's dimension, order, periodicity,
'    control point, and knot point data.
' 3. Examine the Immediate window.
'-----------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swSketchSegment As SldWorks.SketchSegment
Dim swFeature As SldWorks.Feature
Dim swSketch As SldWorks.Sketch
Dim swSplineParamData As SldWorks.SplineParamData
Dim swSketchMgr As SldWorks.SketchManager
Dim points(11) As Double
Dim pointArray As Variant
Dim varCtrlPoints As Variant
Dim varKnotPoints As Variant
Dim status As Boolean
Dim i As Integer
Dim j As Integer
Dim k As Integer
Dim splineCount As Long
Dim splinePointCount As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2017\templates\Part.prtdot", 0, 0, 0)
```

```
    'Create a sketch with two splines
    'First spline
    points(0) = -0.185955019567672
    points(1) = 4.16208582005027E-02
    points(2) = 0
    points(3) = -8.62492383138544E-02
    points(4) = 4.03922105323034E-02
    points(5) = 0
    points(6) = -6.72740896322921E-02
    points(7) = 5.40598971292923E-02
    points(8) = 0
    points(9) = -1.41436733240425E-02
    points(10) = -5.70437188125084E-03
    points(11) = 0
    pointArray = points
    Set swSketchMgr = swModel.SketchManager
    Set swSketchSegment = swSketchMgr.CreateSpline((pointArray))
    swModel.ClearSelection2 True
    'Second spline
    points(0) = -8.38342193907238E-02
    points(1) = -3.80341664350112E-02
    points(2) = 0
    points(3) = -6.55490761158148E-02
    points(4) = -1.79490921124739E-02
    points(5) = 0
    points(6) = -1.79387030603664E-02
    points(7) = -6.81344637902441E-02
    points(8) = 0
    points(9) = 6.34819349185705E-02
    points(10) = -3.29692207162395E-02
    points(11) = 0
    pointArray = points
    Set swSketchSegment = swSketchMgr.CreateSpline((pointArray))
    swModel.ClearSelection2 True
    'Sketch
    swSketchMgr.InsertSketch (True)
```

```
    'Get each spline's dimension, order, periodicity, control point, and knot data
    status = swModel.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, swSelectOptionDefault)
    Set swSelMgr = swModel.SelectionManager
    Set swFeature = swSelMgr.GetSelectedObject6(1, -1)
    Set swSketch = swFeature.GetSpecificFeature2
    Debug.Print swFeature.Name
    Debug.Print ""
```

```
    splineCount = swSketch.GetSplineCount(splinePointCount)
```

```
    For i = 1 To splineCount
        Debug.Print "Spline " & i & ": "
        Set swSplineParamData = swSketch.GetSplineParams5(True, i - 1)
        Debug.Print "  Dimension: " & swSplineParamData.Dimension
        Debug.Print "  Order: " & swSplineParamData.Order
        Debug.Print "  Periodicity: " & swSplineParamData.Periodic
        Debug.Print "  Number of control points: " & swSplineParamData.ControlPointsCount
        status = swSplineParamData.GetControlPoints(varCtrlPoints)
        Debug.Print "  Control points:"
```

```
        For j = 0 To UBound(varCtrlPoints)
            Debug.Print "      " & varCtrlPoints(j)
        Next j
```

```
        Debug.Print "  Number of knots: " & swSplineParamData.KnotPointsCount
        status = swSplineParamData.GetKnotPoints(varKnotPoints)
        Debug.Print "    Knot points:"
```

```
        For k = 0 To UBound(varKnotPoints)
            Debug.Print "      " & varKnotPoints(k)
        Next k
```

```
    Next i
```

```
End Sub
```
