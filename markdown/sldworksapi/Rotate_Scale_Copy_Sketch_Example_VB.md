---
title: "Rotate, Scale, and Copy Sketch Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Rotate_Scale_Copy_Sketch_Example_VB.htm"
---

# Rotate, Scale, and Copy Sketch Example (VBA)

This example shows how to rotate a sketch; scale, copy, and rotate selected entities of the sketch; and scale the entire sketch.

```
'-------------------------------------------------------------------------
' Preconditions: Verify that the specified part document template exists.
'
' Postconditions:
' Step through the macro and observe:
'   1. Creates a sketch of a rectangle.
'   2. Rotates the sketch about the specified points.
'   3. Makes a copy of the selected sketch lines and
'      scales them by a factor of 2.
'   4. Rotates the selected line.
'   5. Zooms to fit the sketch.
'   6. Scales the sketch by a factor or 3.
'-------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim sketchLines As Variant
Dim status As Boolean
```

```
Sub main()
```

```
Set swApp = Application.SldWorks
```

```
    ' Open a new part document
    Set swModel = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2015\templates\Part.prtdot", 0, 0, 0)
    Set swModelDocExt = swModel.Extension
```

```
    ' Create sketch of rectangle on the Front plane
    Set swSketchMgr = swModel.SketchManager
    status = swModelDocExt.SelectByID2("Front Plane", "PLANE", -2.12975109505464E-02, 0.121561074451165, 0.100935818984055, False, 0, Nothing, 0)
    swModel.ClearSelection2 True
    swSketchMgr.InsertSketch True
    swModel.ClearSelection2 True
    sketchLines = swSketchMgr.CreateCornerRectangle(0, 0, 0, -8.22154876580373E-02, 0.063635716435882, 0)
    swModel.ClearSelection2 True
```

```
    ' Rotate the sketch about the specified point
    swModel.SketchModifyRotate 1, 1, 1
```

```
    swModel.ClearSelection2 True
```

```
    ' Make a copy of the selected lines and scale them by a factor of 2
    status = swModelDocExt.SelectByID2("Line3", "SKETCHSEGMENT", -6.30770706086407E-02, 1.72671115438625E-02, 2.15538897292735E-02, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("Line2", "SKETCHSEGMENT", -3.60136822942443E-02, 2.50170683049161E-02, 2.00770232274633E-03, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", -7.35948431462766E-03, -1.30061570540028E-02, 1.27196907180518E-02, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("Line4", "SKETCHSEGMENT", -5.01900457103943E-02, -2.24514168565368E-02, 4.17377643321936E-02, True, 0, Nothing, 0)
    swModelDocExt.ScaleOrCopy True, 2, 0, 0.063635716435882, 0, 2
```

```
    ' Rotate selected Line3
    status = swModel.DeSelectByID("Line2", "SKETCHSEGMENT", 1.59286151716137E-03, 4.38212483979034E-02, 2.00770232274633E-03)
    status = swModel.DeSelectByID("Line1", "SKETCHSEGMENT", -1.49206501299916E-02, -8.3446413285288E-04, 1.27196907180518E-02)
    status = swModel.DeSelectByID("Line4", "SKETCHSEGMENT", -0.046010013281556, 3.01029148938852E-02, 4.17377643321936E-02)
    swModelDocExt.RotateOrCopy False, 2, False, -0.164430975316075, 0.063635716435882, 0, 0, 0, 1, 0.78539816339745

    swModel.ClearSelection2 True
```

```
    ' Zoom to fit
    swModel.ViewZoomtofit2
```

```
    ' Scale the sketch by a factor of 3
    status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
    status = swModel.SketchModifyScale(3)
```

```
End Sub
```
