---
title: "Get Spline's Parameters Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Spline's_Parameters_Example_VBNET.htm"
---

# Get Spline's Parameters Example (VB.NET)

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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim swSelMgr As SelectionMgr
     Dim swFeat As Feature
     Dim swSketch As Sketch
     Dim swSplineParaData As SplineParamData
     Dim varCtrlPoints As Object
     Dim varKnotPoints As Object
     Dim boolStatus As Boolean
     Dim i As  Integer
     Dim swSketchMgr As SketchManager
     Dim arrCtrlPts(17) As Double
     Dim arrKnotPts(9) As Double
     Dim varSeg As Object

     Sub main()

         swModel = swApp.ActiveDoc
         swSketchMgr = swModel.SketchManager
         swSplineParaData = swSketchMgr.CreateSplineParamData

         swSplineParaData.Dimension = 3
         swSplineParaData.Order = 4
         swSplineParaData.Periodic = 0
         swSplineParaData.ControlPointsCount = 6

         arrCtrlPts(0) = -0.0508
         arrCtrlPts(1) = 0.0254
         arrCtrlPts(2) = 0

         arrCtrlPts(3) = -0.0467151082143202
         arrCtrlPts(4) = 0.0102856278912272
         arrCtrlPts(5) = 0

         arrCtrlPts(6) = -0.00128736279059822
         arrCtrlPts(7) = -0.0242718277078294
         arrCtrlPts(8) = 0

         arrCtrlPts(9) = 0.0314466792227059
         arrCtrlPts(10) = 0.0612396847740687
         arrCtrlPts(11) = 0

         arrCtrlPts(12) = 0.060476660388647
         arrCtrlPts(13) = -0.0433198423870343
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

         swSketchMgr.InsertSketch(True)

         boolStatus = swModel.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, swSelectOption_e.swSelectOptionDefault)

         swSelMgr = swModel.SelectionManager
         swFeat = swSelMgr.GetSelectedObject6(1, -1)
         swSketch = swFeat.GetSpecificFeature2
         Debug.Print(swFeat.Name)
         Debug.Print("")

         swSplineParaData = swSketch.GetSplineParams4(True)

         Debug.Print("The dimension is: " & swSplineParaData.Dimension)
         Debug.Print("The order is: " & swSplineParaData.Order)
         Debug.Print("The periodicity is: " & swSplineParaData.Periodic)
         Debug.Print("The control point count is: " & swSplineParaData.ControlPointsCount)
         boolStatus = swSplineParaData.GetControlPoints(varCtrlPoints)
         Debug.Print("Control Points:")
         For i = 0 To UBound(varCtrlPoints)
             Debug.Print(varCtrlPoints(i))

         Next i
         Debug.Print("The knot point count is: " & swSplineParaData.KnotPointsCount)
         boolStatus = swSplineParaData.GetKnotPoints(varKnotPoints)
         Debug.Print("Knot Points:")
         For i = 0 To UBound(varKnotPoints)
             Debug.Print(varKnotPoints(i))

         Next i
         Debug.Print("The color is: " & swSplineParaData.Color)
         Debug.Print("The line style is: " & swSplineParaData.LineStyle)
         Debug.Print("The line width is: " & swSplineParaData.LineWidth)
         Debug.Print("The layer is: " & swSplineParaData.Layer)
         Debug.Print("The layer override is: " & swSplineParaData.LayerOverride)

     End Sub

     Public swApp As SldWorks

 End  Class
```
