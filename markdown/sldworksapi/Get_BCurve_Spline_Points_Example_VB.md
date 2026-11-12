---
title: "Get BCurve Spline Points Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_BCurve_Spline_Points_Example_VB.htm"
---

# Get BCurve Spline Points Example (VBA)

This example shows how to get B-spline parameter data (knots, control points, etc.) for a selected spline
or curve.

```
'---------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\molds\telephone.sldprt.
' 2. Select a curve.
' 3. Open the Immediate Window.
'
' Postconditions: Examine the Immediate window.
'----------------------------------------------------------------------------
Option Explicit

Sub main()

    Dim swApp As SldWorks.SldWorks

    Dim Part As SldWorks.ModelDoc2
```

```vb
    Set swApp = CreateObject("SldWorks.Application")
     Set Part = swApp.ActiveDoc
    Dim swSelectMgr As SldWorks.SelectionMgr
     Set swSelectMgr = Part.SelectionManager
    Dim swSketchSeg As SldWorks.Edge
     Set swSketchSeg = swSelectMgr.GetSelectedObject6(1, -1)
    Dim swCurveIn As SldWorks.Curve
     Dim swSplineParaData As SldWorks.SplineParamData

     Dim boolStatus As Boolean
     Dim i As Long

    Set swCurveIn = swSketchSeg.GetCurve

    Debug.Print ""
     Debug.Print "B-spline"
     Debug.Print ""
     Set swSplineParaData = swCurveIn.GetBCurveParams5(False, False, True, True)
     Debug.Print "The dimension is: " & swSplineParaData.Dimension
     Debug.Print "The order is: " & swSplineParaData.Order
     Debug.Print "The periodicity is: " & swSplineParaData.Periodic
     Debug.Print "The control point count is: " & swSplineParaData.ControlPointsCount
    Debug.Print "The knot point count is: " & swSplineParaData.KnotPointsCount

    Debug.Print "COLORREF of spline: " & swSplineParaData.Color
     Debug.Print "Layer of spline: " & swSplineParaData.Layer
     Debug.Print "Style overrides as defined in swLayerOverride_e: " & swSplineParaData.LayerOverride
     Debug.Print "Line style as defined in swLineStyles_e:: " & swSplineParaData.LineStyle
     Debug.Print "Line weight at defined in swLineWeights_e: " & swSplineParaData.LineWidth

End Sub
```
