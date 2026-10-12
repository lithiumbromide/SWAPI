---
title: "Insert a Composite Curve Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_a_Composite_Curve_Example_VBNET.htm"
---

# Insert a Composite Curve Example (VB.NET)

This example shows how to insert a composite curve using two sketches of splines.

```
'--------------------------------------------------------
' Preconditions:
' 1. Verify that the part document template exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens a new part document.
' 2. Creates a sketch of a spline.
' 3. Creates another sketch of a spline.
' 4. Inserts a composite curve using the sketches created
'    in steps 2 and 3.
' 5. Prints the number of joined entities in the composite
'    curve to the Immediate window.
' 6. Examine the Immediate window.
'---------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swSketchSegment As SketchSegment
        Dim swSketchManager As SketchManager
        Dim swModelDocExt As ModelDocExtension
        Dim swCompositeCurveFeatureData As CompositeCurveFeatureData
        Dim swSelectionMgr As SelectionMgr
        Dim swFeature As Feature
        Dim pointArray As Object
        Dim points() As Double
        Dim status As Boolean

        swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2015\templates\Part.prtdot", 0, 0, 0)

        'Create sketch containing a spline
        swSketchManager = swModel.SketchManager
        swSketchManager.InsertSketch(True)
        ReDim Preserve points(11)
        points(0) = -0.0509020857536935
        points(1) = 0.0116459784886342
        points(2) = 0
        points(3) = -0.0404337904830111
        points(4) = 0.0249930549587544
        points(5) = 0
        points(6) = 0.0396486683377099
        points(7) = -0.0166184187422084
        points(8) = 0
        points(9) = 0.0166184187422084
        points(10) = -0.0399103757194769
        points(11) = 0
        pointArray = points
        swSketchSegment = swSketchManager.CreateSpline2((pointArray), True)
        swModel.ClearSelection2(True)

        'Create another sketch containing a spline
        swSketchManager.InsertSketch(True)
        ReDim Preserve points(11)
        points(0) = -0.0509020857536935
        points(1) = 0.0116459784886342
        points(2) = 0
        points(3) = -0.0370315945200393
        points(4) = -0.00850548990742951
        points(5) = 0
        points(6) = 0.00562670870799184
        points(7) = -0.014786467069839
        points(8) = 0
        points(9) = 0.0166184187422084
        points(10) = -0.0399103757194769
        points(11) = 0
        pointArray = points
        swSketchSegment = swSketchManager.CreateSpline2((pointArray), True)
        swSketchManager.InsertSketch(True)
        swModel.ClearSelection2(True)

        'Insert a composite curve using both sketches
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, False, 1, Nothing, 0)
        status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, True, 1, Nothing, 0)
        swModel.InsertCompositeCurve()

        'Get the number of joined entities in the composite curve
        status = swModelDocExt.SelectByID2("CompCurve1", "REFERENCECURVES", 0, 0, 0, False, 0, Nothing, 0)
        swSelectionMgr = swModel.SelectionManager
        swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
        swCompositeCurveFeatureData = swFeature.GetDefinition
        Debug.Print("Number of joined entities: " & swCompositeCurveFeatureData.GetEntitiesToJoinCount)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
