---
title: "Get Angle Between Plane and Line Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Angle_Between_Plane_and_Line_Example_VB.htm"
---

# Get Angle Between Plane and Line Example (VBA)

This example shows how to get the angle between a selected plane and a selected sketch line.

```
'-----------------------------------------------
' Preconditions:
' 1. Verify that the specified part template exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens a new part.
' 2. Creates a 3D sketch.
' 3. Selects the Top Plane and a sketch line in the
'    3D sketch.
' 4. Gets the normal vector, curve vector, and the angle
'    between the selected plane and sketch line.
' 5. Examine the Immediate window.
'-----------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSketchManager As SldWorks.SketchManager
Dim swMath As SldWorks.MathUtility
Dim swSketchSegment As SldWorks.SketchSegment
Dim swSketch As SldWorks.Sketch
Dim swFeature As SldWorks.Feature
Dim swRefPlane As SldWorks.RefPlane
Dim normVec As MathVector
Dim curveVec As SldWorks.MathVector
Dim swCurve As SldWorks.Curve
Dim dirArr(2) As Double
Dim params As Variant
Dim crossVec As SldWorks.MathVector
Dim dot As Double
Dim vecLen As Double
Dim angle As Double
Dim boolstatus As Boolean
Dim longstatus As Long
```

```
Sub main()
    Set swApp = Application.SldWorks
```

```
    longstatus = swApp.ResetUntitledCount(0, 0, 0)
    Set swModel = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2016\templates\Part.prtdot", 0, 0, 0)
    swApp.ActivateDoc2 "Part1", False, longstatus
    Set swModel = swApp.ActiveDoc
```

```
    ' Insert 3D sketch
    Set swSketchManager = swModel.SketchManager
    swSketchManager.Insert3DSketch True
    Set swSketchSegment = swSketchManager.CreateLine(-0.038076, 0.043671, -0#, -0.01322, 0.054563, -0#)
    Set swSketch = swModel.GetActiveSketch2()
    boolstatus = swSketch.SetWorkingPlaneOrientation(0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0)
    Set swSketchSegment = swSketchManager.CreateLine(-0.01322, 0.054563, -0#, -0.01322, 0.08124, 0.018547)
    Set swSketch = swModel.GetActiveSketch2()
    boolstatus = swSketch.SetWorkingPlaneOrientation(0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0)
    Set swSketchSegment = swSketchManager.CreateLine(-0.01322, 0.08124, 0.018547, 0.000568, 0.08124, 0.004759)
    Set swSketch = swSketchManager.ActiveSketch
    boolstatus = swSketch.SetWorkingPlaneOrientation(0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1)
    swModel.ClearSelection2 True
    swSketchManager.InsertSketch True
```

```
    ' Select Top Plane and a line in the 3D sketch
    Set swMath = swApp.GetMathUtility
    Set swSelMgr = swModel.SelectionManager
    Set swModelDocExt = swModel.Extension
    swModel.ClearSelection2 True
    boolstatus = swModelDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    Set swFeature = swSelMgr.GetSelectedObject6(1, -1)
    boolstatus = swModelDocExt.SelectByID2("Line1@3DSketch1", "EXTSKETCHSEGMENT", -3.42695618142891E-02, 4.53389966494514E-02, 0, True, 0, Nothing, 0)
    Set swSketchSegment = swSelMgr.GetSelectedObject6(2, -1)
    Set swRefPlane = swFeature.GetSpecificFeature2
```

```
    ' Get the normal and curve vectors
    dirArr(0) = 0#
    dirArr(1) = 0#
    dirArr(2) = 1#
```

```
    Set normVec = swMath.CreateVector((dirArr))
    Set normVec = normVec.MultiplyTransform(swRefPlane.Transform)
    Debug.Print "Normal vector: " & normVec.ArrayData(0), normVec.ArrayData(1), normVec.ArrayData(2)
```

```
    Set swCurve = swSketchSegment.GetCurve
    params = swCurve.LineParams
    dirArr(0) = params(3)
    dirArr(1) = params(4)
    dirArr(2) = params(5)
    Set curveVec = swMath.CreateVector((dirArr))
    Debug.Print "Curve vector:  " & curveVec.ArrayData(0), curveVec.ArrayData(1), curveVec.ArrayData(2)
```

```
    Set crossVec = curveVec.Cross(normVec)
```

```
    ' Get the angle between the Top Plane and
    ' selected line in the 3D sketch
    dot = curveVec.dot(normVec)
    vecLen = crossVec.GetLength()
    angle = Atn(dot / vecLen)
    Debug.Print "Angle:         " & angle
```

```
End Sub
```
