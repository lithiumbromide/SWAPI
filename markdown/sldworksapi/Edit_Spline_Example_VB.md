---
title: "Edit Spline Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Edit_Spline_Example_VB.htm"
---

# Edit Spline Example (VBA)

This example shows how to modify the control points and knots of a spline.

'----------------------------------------------------------------------------
' Preconditions:
' 1. Ensure the specified template exists.
' 2. Open an Immediate window.
'
' Postconditions:
' 1. Creates a spline sketch.
' 2. Gets its B-curve parameters.
' 3. Modifies a control point in the spline.
' 4. Modifies a knot in the spline.
' 5. When the macro stops, select the spline in the graphics area and press F5.
' 6. Gets the edited B-curve parameters.
' 7. Inspect the Immediate window.
'
'----------------------------------------------------------------------------

```vb
Option Explicit
 Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim swPart As PartDoc
 Dim skSegment As SldWorks.SketchSegment
 Dim swSkSpl As SldWorks.SketchSpline
 Dim swSketch As SldWorks.Sketch
 Dim swSkMan As SldWorks.SketchManager
 Dim swSplineParamData As SldWorks.SplineParamData
 Dim swCurve As SldWorks.Curve
 Dim boolstatus As Boolean
 Dim vSketchSeg As Variant
 Dim i As Integer, j As Integer, k As Integer
 Dim swSheetWidth As Double
 Dim swSheetHeight As Double
 Dim pointArray As Variant
 Dim points() As Double
 Dim varCtrlPoints As Variant
 Dim varKnotPoints As Variant
 Dim weights As Variant

Sub main()
    Set swApp = Application.SldWorks
    swSheetWidth = 0
     swSheetHeight = 0
     Set Part = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2018\templates\Part.prtdot", 0, swSheetWidth, swSheetHeight)

    Set swPart = Part
     Set Part = swApp.ActiveDoc

    ReDim points(0 To 17) As Double
     points(0) = -0.112591397899791
     points(1) = -4.57086601325614E-02
     points(2) = 0
     points(3) = -7.86518975119748E-02
     points(4) = 2.83840071788291E-02
     points(5) = 0
     points(6) = -2.75869611486428E-02
     points(7) = 0
     points(8) = 0
     points(9) = 6.83154803141974E-02
     points(10) = 3.93969983009583E-02
     points(11) = 0
     points(12) = 0.10350046695487
     points(13) = 0.105807158470839
     points(14) = 0
     points(15) = 0.131212536078806
     points(16) = 0.121288640266982
     points(17) = 0
     pointArray = points

    Set skSegment = Part.SketchManager.CreateSpline((pointArray))
     Part.ClearSelection2 True
     Part.SketchManager.InsertSketch True

    Set swSkMan = Part.SketchManager
     Set swSketch = skSegment.GetSketch
     vSketchSeg = swSketch.GetSketchSegments

    Part.ClearSelection2 True

    For i = 0 To UBound(vSketchSeg)

        Set skSegment = vSketchSeg(i)

        Set swCurve = skSegment.GetCurve
         Set swSkSpl = skSegment

        Debug.Print ""
         Debug.Print "B-spline"
         Debug.Print "Is a rational curve? " & swSkSpl.IsRationalCurve

        If swSkSpl.IsRationalCurve Then
             weights = swSkSpl.GetControlVertexWeights
             For k = 0 To UBound(weights)
                 Debug.Print weights(k)
                 Debug.Print ""
             Next
         End If

        Set swSplineParamData = swCurve.GetBCurveParams5(False, False, False, False)

        Debug.Print "The dimension is: " & swSplineParamData.Dimension
         Debug.Print "The order is: " & swSplineParamData.Order
         Debug.Print "The periodicity is: " & swSplineParamData.Periodic
         Debug.Print "The control point count is: " & swSplineParamData.ControlPointsCount

        Debug.Print "The knot point count is: " & swSplineParamData.KnotPointsCount
         boolstatus = swSplineParamData.GetControlPoints(varCtrlPoints)
         Debug.Print "Control Points:"
         For j = 0 To UBound(varCtrlPoints)
             Debug.Print varCtrlPoints(j)
         Next j

        Debug.Print "The knot point count is: " & swSplineParamData.KnotPointsCount
         boolstatus = swSplineParamData.GetKnotPoints(varKnotPoints)
         Debug.Print "Knot Points:"
         For j = 0 To UBound(varKnotPoints)
             Debug.Print varKnotPoints(j)
         Next j

        ' Modify a control point
         boolstatus = swSkSpl.ModifyControlPoint(3, -9.06980622069201E-02, 5.69034826745842E-02, 0#)
         Debug.Print "Modified control point #3."
         Part.ForceRebuild3 True

        ' Modify a knot
         boolstatus = swSkSpl.ModifyKnot(6, 0.41)
         Debug.Print "Modified knot #6."
         Part.ForceRebuild3 True

        swSkMan.InsertSketch True

    Next i
     Debug.Print "Select the sketch in the graphics area and press F5"
     Stop  ' Select the sketch in the graphics area

    Set swSketch = swSkMan.ActiveSketch
     vSketchSeg = swSketch.GetSketchSegments

    If (IsEmpty(vSketchSeg)) Then
         Debug.Print "Periodic B-spline not created"
     Else

        Part.ClearSelection2 True

        For i = 0 To UBound(vSketchSeg)

            Set skSegment = vSketchSeg(i)
             Set swCurve = skSegment.GetCurve

            Debug.Print ""
             Debug.Print "Edited B-spline"
             Debug.Print ""

            Set swSplineParamData = swCurve.GetBCurveParams5(False, False, False, False)

            Debug.Print "The dimension is: " & swSplineParamData.Dimension
             Debug.Print "The order is: " & swSplineParamData.Order
             Debug.Print "The periodicity is: " & swSplineParamData.Periodic
             Debug.Print "The control point count is: " & swSplineParamData.ControlPointsCount

            Debug.Print "The knot point count is: " & swSplineParamData.KnotPointsCount
             boolstatus = swSplineParamData.GetControlPoints(varCtrlPoints)
             Debug.Print "Control Points:"
             For j = 0 To UBound(varCtrlPoints)
                 Debug.Print varCtrlPoints(j)
             Next j

            Debug.Print "The knot point count is: " & swSplineParamData.KnotPointsCount
             boolstatus = swSplineParamData.GetKnotPoints(varKnotPoints)
             Debug.Print "Knot Points:"
             For j = 0 To UBound(varKnotPoints)
                 Debug.Print varKnotPoints(j)
             Next j

        Next i

    End If

End Sub
```
