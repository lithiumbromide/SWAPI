---
title: "Insert a Composite Curve Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_a_Composite_Curve_Example_VB.htm"
---

# Insert a Composite Curve Example (VBA)

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
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSketchSegment As SldWorks.SketchSegment
Dim swSketchManager As SldWorks.SketchManager
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swCompositeCurveFeatureData As SldWorks.CompositeCurveFeatureData
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swFeature As SldWorks.Feature
Dim pointArray As Variant
Dim points() As Double
Dim status As Boolean
```

```
Sub main()
```

```
Set swApp = Application.SldWorks
Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2015\templates\Part.prtdot", 0, 0, 0)
```

```
'Create sketch containing a spline
Set swSketchManager = swModel.SketchManager
swSketchManager.InsertSketch True
ReDim points(0 To 11) As Double
points(0) = -5.09020857536935E-02
points(1) = 1.16459784886342E-02
points(2) = 0
points(3) = -4.04337904830111E-02
points(4) = 2.49930549587544E-02
points(5) = 0
points(6) = 3.96486683377099E-02
points(7) = -1.66184187422084E-02
points(8) = 0
points(9) = 1.66184187422084E-02
points(10) = -3.99103757194769E-02
points(11) = 0
pointArray = points
Set swSketchSegment = swSketchManager.CreateSpline2((pointArray), True)
swModel.ClearSelection2 True
```

```
'Create another sketch containing a spline
swSketchManager.InsertSketch True
ReDim points(0 To 11) As Double
points(0) = -5.09020857536935E-02
points(1) = 1.16459784886342E-02
points(2) = 0
points(3) = -3.70315945200393E-02
points(4) = -8.50548990742951E-03
points(5) = 0
points(6) = 5.62670870799184E-03
points(7) = -0.014786467069839
points(8) = 0
points(9) = 1.66184187422084E-02
points(10) = -3.99103757194769E-02
points(11) = 0
pointArray = points
Set swSketchSegment = swSketchManager.CreateSpline2((pointArray), True)
swSketchManager.InsertSketch True
swModel.ClearSelection2 True
```

```
'Insert a composite curve using both sketches
Set swModelDocExt = swModel.Extension
status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, False, 1, Nothing, 0)
status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, True, 1, Nothing, 0)
swModel.InsertCompositeCurve
```

```
'Get the number of joined entities in the composite curve
status = swModelDocExt.SelectByID2("CompCurve1", "REFERENCECURVES", 0, 0, 0, False, 0, Nothing, 0)
Set swSelectionMgr = swModel.SelectionManager
Set swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
Set swCompositeCurveFeatureData = swFeature.GetDefinition
Debug.Print ("Number of joined entities: " & swCompositeCurveFeatureData.GetEntitiesToJoinCount)
```

```
End Sub
```
