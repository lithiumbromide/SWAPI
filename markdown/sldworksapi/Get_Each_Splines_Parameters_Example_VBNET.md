---
title: "Get Each Spline's Parameters Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Each_Splines_Parameters_Example_VBNET.htm"
---

# Get Each Spline's Parameters Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swSelMgr As SelectionMgr
        Dim swSketchSegment As SketchSegment
        Dim swFeature As Feature
        Dim swSketch As Sketch
        Dim swSplineParamData As SplineParamData
        Dim swSketchMgr As SketchManager
        Dim points(11) As Double
        Dim pointArray As Object
        Dim varCtrlPoints As Object = Nothing
        Dim varKnotPoints As Object = Nothing
        Dim status As Boolean
        Dim i As Integer
        Dim j As Integer
        Dim k As Integer
        Dim splineCount As Integer
        Dim splinePointCount As Integer

        swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2017\templates\Part.prtdot", 0, 0, 0)

        'Create a sketch with two splines
        'First spline
        points(0) = -0.185955019567672
        points(1) = 0.0416208582005027
        points(2) = 0
        points(3) = -0.0862492383138544
        points(4) = 0.0403922105323034
        points(5) = 0
        points(6) = -0.0672740896322921
        points(7) = 0.0540598971292923
        points(8) = 0
        points(9) = -0.0141436733240425
        points(10) = -0.00570437188125084
        points(11) = 0
        pointArray = points
        swSketchMgr = swModel.SketchManager
        swSketchSegment = swSketchMgr.CreateSpline((pointArray))
        swModel.ClearSelection2(True)
        'Second spline
        points(0) = -0.0838342193907238
        points(1) = -0.0380341664350112
        points(2) = 0
        points(3) = -0.0655490761158148
        points(4) = -0.0179490921124739
        points(5) = 0
        points(6) = -0.0179387030603664
        points(7) = -0.0681344637902441
        points(8) = 0
        points(9) = 0.0634819349185705
        points(10) = -0.0329692207162395
        points(11) = 0
        pointArray = points
        swSketchSegment = swSketchMgr.CreateSpline((pointArray))
        swModel.ClearSelection2(True)
        'Sketch
        swSketchMgr.InsertSketch(True)

        'Get each spline's dimension, order, periodicity, control point, and knot data
        status = swModel.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, swSelectOption_e.swSelectOptionDefault)
        swSelMgr = swModel.SelectionManager
        swFeature = swSelMgr.GetSelectedObject6(1, -1)
        swSketch = swFeature.GetSpecificFeature2
        Debug.Print(swFeature.Name)
        Debug.Print("")
        splineCount = swSketch.GetSplineCount(splinePointCount)
        For i = 1 To splineCount
            Debug.Print("Spline " & i & ": ")
            swSplineParamData = swSketch.GetSplineParams5(True, i - 1)
            Debug.Print("  Dimension: " & swSplineParamData.Dimension)
            Debug.Print("  Order: " & swSplineParamData.Order)
            Debug.Print("  Periodicity: " & swSplineParamData.Periodic)
            Debug.Print("  Number of control points: " & swSplineParamData.ControlPointsCount)
            status = swSplineParamData.GetControlPoints(varCtrlPoints)
            Debug.Print("  Control points:")
            For j = 0 To UBound(varCtrlPoints)
                Debug.Print("      " & varCtrlPoints(j))
            Next j
            Debug.Print("  Number of knots: " & swSplineParamData.KnotPointsCount)
            status = swSplineParamData.GetKnotPoints(varKnotPoints)
            Debug.Print("    Knot points:")
            For k = 0 To UBound(varKnotPoints)
                Debug.Print("      " & varKnotPoints(k))
            Next k
        Next i

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
