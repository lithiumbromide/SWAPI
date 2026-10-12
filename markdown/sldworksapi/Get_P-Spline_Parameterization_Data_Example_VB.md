---
title: "Get P-Spline Parameterization Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_P-Spline_Parameterization_Data_Example_VB.htm"
---

# Get P-Spline Parameterization Data Example (VBA)

This example shows how to get P-spline parameter data for a selected spline or curve.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\molds\telephone.sldprt.
 ' 2. Select a curved edge of Shell1 in the graphics area.
 ' 3. Open the Immediate Window.
 '
 ' Postconditions:
 ' 1. Gets the P-spline parameter data for the selected curved edge.
 ' 2. Inspect the Immediate window.
 '----------------------------------------------------------------------------

Option Explicit
 Sub main()
     Dim swApp As SldWorks.SldWorks
     Dim Part As SldWorks.ModelDoc2

    Set swApp = CreateObject("SldWorks.Application")
     Set Part = swApp.ActiveDoc
    Dim swSelectMgr As Sldworks.SelectionMgr
     Set swSelectMgr = Part.SelectionManager
    Dim swSketchSeg As SldWorks.Edge
     Set swSketchSeg = swSelectMgr.GetSelectedObject6(1, -1)
    Dim swCurveIn As SldWorks.Curve
     Dim swSplineParaData As SldWorks.SplineParamData
     Dim varCtrlPoints As Variant
     Dim varKnotPoints As Variant
     Dim boolStatus As Boolean
     Dim i As Long

    Set swCurveIn = swSketchSeg.GetCurve
     Set swSplineParaData = swCurveIn.GetPCurveParams2

    Debug.Print "P-spline"
     Debug.Print ""
     Debug.Print "The dimension is: " & swSplineParaData.Dimension
     Debug.Print "The order is: " & swSplineParaData.Order
     Debug.Print "The periodicity is: " & swSplineParaData.Periodic
     Debug.Print "The knot count is: " & swSplineParaData.KnotPointsCount
     Debug.Print "Knots: "
     boolStatus = swSplineParaData.GetKnotPoints(varKnotPoints)
     For i = 0 To UBound(varKnotPoints)
         Debug.Print varKnotPoints(i)

    Next i
     Debug.Print "The segment count is: " & swSplineParaData.SegmentCount
     boolStatus = swSplineParaData.GetSegments(varCtrlPoints)
     Debug.Print (swSplineParaData.SegmentCount * swSplineParaData.Dimension * swSplineParaData.Order) & " Coefficients: "
     For i = 0 To UBound(varCtrlPoints)
         Debug.Print varCtrlPoints(i)
    Next i

    Debug.Print ""

    Debug.Print "COLORREF of spline: " & swSplineParaData.Color
     Debug.Print "Layer of spline: " & swSplineParaData.Layer
     Debug.Print "Style overrides as defined in swLayerOverride_e: " & swSplineParaData.LayerOverride
     Debug.Print "Line style as defined in swLineStyles_e:: " & swSplineParaData.LineStyle
     Debug.Print "Line weight at defined in swLineWeights_e: " & swSplineParaData.LineWidth

End Sub
```
