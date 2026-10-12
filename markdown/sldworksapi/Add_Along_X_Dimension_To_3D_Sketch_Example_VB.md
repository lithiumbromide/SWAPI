---
title: "Add Along X Dimension to 3D Sketch Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Along_X_Dimension_To_3D_Sketch_Example_VB.htm"
---

# Add Along X Dimension to 3D Sketch Example (VBA)

This example shows how to add a display dimension along the x axis in a 3D sketch.

```
'----------------------------------------------------------------------------
' Preconditions: Verify that the specified part template exists.
'
' Postconditions:
' 1. Opens a new part document.
' 2. Inserts a 3D sketch.
' 3. Click the green check mark in the Modify dimension dialog
'    (If you don't see the dialog, look for it behind other open windows).
' 4. Puts 3DSketch1 in edit mode; 3DSketch1 contains a spline and a
'    corner rectangle.
' 5. Displays the display dimension of 84.46 mm on the x axis while the
'    sketch is in edit mode.
' 6. Examine the graphics area.
'----------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim Part As SldWorks.ModelDoc2
Dim myDisplayDim As SldWorks.DisplayDimension
Dim boolstatus As Boolean
Dim longstatus As Long
Sub main()
```

```
    Set swApp = Application.SldWorks
    longstatus = swApp.ResetUntitledCount(0, 0, 0)
    Set Part = swApp.NewDocument("C:\Documents and Settings\All Users\Application Data\SOLIDWORKS\SOLIDWORKS 2015\templates\Part.prtdot", 0, 0, 0)
    swApp.ActivateDoc2 "Part1", False, longstatus
    Set Part = swApp.ActiveDoc
```

```
    Part.SketchManager.Insert3DSketch True
    Dim vSkLines As Variant
    vSkLines = Part.SketchManager.CreateCornerRectangle(-0.05171778666374, 0.01933785938058, 0.03, 0.08445537697179, -0.04142795937025, -0.03)
    boolstatus = Part.Extension.SelectByID2("Right Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    Part.ClearSelection2 True
```

```
    Dim pointArray As Variant
    Dim points() As Double
    ReDim points(0 To 11) As Double
    points(0) = 0
    points(1) = -0.03591009660795
    points(2) = 0.04608246573503
    points(3) = 0
    points(4) = 0.0147420284178
    points(5) = 0.005170989573514
    points(6) = 0
    points(7) = -0.006478053228363
    points(8) = -0.04282131900055
    points(9) = 0
    points(10) = -0.02294509596464
    points(11) = -0.09396066420243
    pointArray = points
```

```
    Dim skSegment As SldWorks.SketchSegment
    Set skSegment = Part.SketchManager.CreateSpline2((pointArray), True)
    Part.SketchManager.InsertSketch True
```

```
    boolstatus = Part.Extension.SelectByID2("3DSketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
    Part.EditSketch
    boolstatus = Part.Extension.SelectByID2("Point5", "SKETCHPOINT", 0, -0.03591009660795, 0.04608246573503, False, 0, Nothing, 0)
    boolstatus = Part.Extension.SelectByID2("Point4", "SKETCHPOINT", 0.08445537697179, 0.02732744880518, -0.01872625210654, True, 0, Nothing, 0)
    Set myDisplayDim = Part.SketchManager.AddAlongXDimension(0.05, -0.091, 0.001)
    Part.ClearSelection2 True
```

```
    Part.ViewZoomtofit2
```

```
End Sub
```
