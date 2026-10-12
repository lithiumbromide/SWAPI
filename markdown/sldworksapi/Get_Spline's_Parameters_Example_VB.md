---
title: "Get Spline's Parameters Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Spline's_Parameters_Example_VB.htm"
---

# Get Spline's Parameters Example (VBA)

This example shows how to get spline parameterization data for a selected sketch.

```vb
'-----------------------------------------------
 ' Preconditions:
 ' 1. Open a new part document.
 ' 2. Open an Immediate Window.
 '
 ' Postconditions:
 ' 1. Creates and selects a sketch with a spline.
 ' 2. Inspect the Immediate Window to view the spline's parameterization data.
 '-----------------------------------------------
 Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swSelMgr As SldWorks.SelectionMgr
 Dim swFeat As SldWorks.Feature
 Dim swSketch As SldWorks.Sketch
 Dim swSplineParaData As SldWorks.SplineParamData
 Dim varCtrlPoints As Variant
 Dim varKnotPoints As Variant
 Dim boolStatus As Boolean
 Dim i As Integer
 Dim swSketchMgr As SketchManager
 Dim arrCtrlPts(17) As Double
 Dim arrKnotPts(9) As Double
 Dim varSeg As Variant

Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swSketchMgr = swModel.SketchManager
     Set swSplineParaData = swSketchMgr.CreateSplineParamData

    swSplineParaData.Dimension = 3
     swSplineParaData.Order = 4
     swSplineParaData.Periodic = 0
     swSplineParaData.ControlPointsCount = 6

    arrCtrlPts(0) = -0.0508
     arrCtrlPts(1) = 0.0254
     arrCtrlPts(2) = 0

    arrCtrlPts(3) = -4.67151082143202E-02
     arrCtrlPts(4) = 1.02856278912272E-02
     arrCtrlPts(5) = 0

    arrCtrlPts(6) = -1.28736279059822E-03
     arrCtrlPts(7) = -2.42718277078294E-02
     arrCtrlPts(8) = 0

    arrCtrlPts(9) = 3.14466792227059E-02
     arrCtrlPts(10) = 6.12396847740687E-02
     arrCtrlPts(11) = 0

    arrCtrlPts(12) = 0.060476660388647
     arrCtrlPts(13) = -4.33198423870343E-02
     arrCtrlPts(14) = 0

    arrCtrlPts(15) = 0.0762
     arrCtrlPts(16) = 0.0254
     arrCtrlPts(17) = 0

    boolStatus = swSplineParaData.SetControlPoints(arrCtrlPts)

    arrKnotPts(0) = 0
     arrKnotPts(1) = 0
     arrKnotPts(2) = 0
     arrKnotPts(3) = 0
     arrKnotPts(4) = 0.362665828616751
     arrKnotPts(5) = 0.575110552411167
     arrKnotPts(6) = 1
     arrKnotPts(7) = 1
     arrKnotPts(8) = 1
     arrKnotPts(9) = 1
     boolStatus = swSplineParaData.SetKnotPoints(arrKnotPts)
     varSeg = swSketchMgr.CreateSplinesByEqnParams2(swSplineParaData)

    swSketchMgr.InsertSketch (True)

    boolStatus = swModel.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, swSelectOptionDefault)

    Set swSelMgr = swModel.SelectionManager
     Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
     Set swSketch = swFeat.GetSpecificFeature2
     Debug.Print swFeat.Name
     Debug.Print ""

    Set swSplineParaData = swSketch.GetSplineParams4(True)

    Debug.Print "The dimension is: " & swSplineParaData.Dimension
     Debug.Print "The order is: " & swSplineParaData.Order
     Debug.Print "The periodicity is: " & swSplineParaData.Periodic
     Debug.Print "The control point count is: " & swSplineParaData.ControlPointsCount
     boolStatus = swSplineParaData.GetControlPoints(varCtrlPoints)
     Debug.Print "Control Points:"
     For i = 0 To UBound(varCtrlPoints)
         Debug.Print varCtrlPoints(i)

    Next i
     Debug.Print "The knot point count is: " & swSplineParaData.KnotPointsCount
     boolStatus = swSplineParaData.GetKnotPoints(varKnotPoints)
     Debug.Print "Knot Points:"
     For i = 0 To UBound(varKnotPoints)
         Debug.Print varKnotPoints(i)

    Next i
     Debug.Print "The color is: " & swSplineParaData.Color
     Debug.Print "The line style is: " & swSplineParaData.LineStyle
     Debug.Print "The line width is: " & swSplineParaData.LineWidth
     Debug.Print "The layer is: " & swSplineParaData.Layer
     Debug.Print "The layer override is: " & swSplineParaData.LayerOverride
End Sub
```
