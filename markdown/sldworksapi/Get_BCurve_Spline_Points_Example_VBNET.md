---
title: "Get BCurve Spline Points Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_BCurve_Spline_Points_Example_VBNET.htm"
---

# Get BCurve Spline Points Example (VB.NET)

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

	Imports SolidWorks.Interop.sldworks

	Imports SolidWorks.Interop.swconst

	Imports System

	Imports System.Diagnostics

	Partial Class SolidWorksMacro

	    Sub main()

	        Dim Part As ModelDoc2

	        Part = swApp.ActiveDoc

	        Dim swSelectMgr As SelectionMgr

	        swSelectMgr = Part.SelectionManager

	        Dim swSketchSeg As Edge

	        swSketchSeg =
	swSelectMgr.GetSelectedObject6(1, -1)

	        Dim swCurveIn As Curve

	        Dim swSplineParaData As SplineParamData

	        Dim varCtrlPoints As Object = Nothing

	        Dim varKnotPoints As Object = Nothing

	        Dim boolStatus As Boolean

	        Dim i As Long

	        swCurveIn = swSketchSeg.GetCurve

	        Debug.Print("")

	        Debug.Print("B-spline")

	        Debug.Print("")

	        swSplineParaData = swCurveIn.GetBCurveParams5(False, False, True, True)

	        Debug.Print("The dimension is: " & swSplineParaData.Dimension)

	        Debug.Print("The order is: " & swSplineParaData.Order)

	        Debug.Print("The periodicity is:
	" & swSplineParaData.Periodic)

	        Debug.Print("The control point
	count is: " & swSplineParaData.ControlPointsCount)

	        Debug.Print("The knot point count
	is: " & swSplineParaData.KnotPointsCount)

	        Debug.Print("COLORREF of spline:
	" & swSplineParaData.Color)

	        Debug.Print("Layer of spline: " & swSplineParaData.Layer)

	        Debug.Print("Style overrides as
	defined in swLayerOverride_e: " & swSplineParaData.LayerOverride)

	        Debug.Print("Line style as
	defined in swLineStyles_e:: " & swSplineParaData.LineStyle)

	        Debug.Print("Line weight at
	defined in swLineWeights_e: " & swSplineParaData.LineWidth)

	    End Sub

	    Public swApp As SldWorks

	End Class
```
