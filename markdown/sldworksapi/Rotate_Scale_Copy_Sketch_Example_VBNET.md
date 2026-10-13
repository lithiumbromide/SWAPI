---
title: "Rotate, Scale, and Copy Sketch Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Rotate_Scale_Copy_Sketch_Example_VBNET.htm"
---

# Rotate, Scale, and Copy Sketch Example (VB.NET)

This example shows how to rotate a sketch; scale, copy, and rotate selected entities of the sketch; and scale the entire sketch.

```
'------------------------------------------------------
' Preconditions: Verify that the specified part document
' template exists.
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
'------------------------------------------------------
```

```
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swSketchMgr As SketchManager
        Dim swModelDocExt As ModelDocExtension
        Dim sketchLines As Object
        Dim status As Boolean

        ' Open a new part document
        swModel = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2015\templates\Part.prtdot", 0, 0, 0)
        swModelDocExt = swModel.Extension

        ' Create sketch of rectangle on the Front plane
        swSketchMgr = swModel.SketchManager
        status = swModelDocExt.SelectByID2("Front Plane", "PLANE", -0.0212975109505464, 0.121561074451165, 0.100935818984055, False, 0, Nothing, 0)
        swModel.ClearSelection2(True)
        swSketchMgr.InsertSketch(True)
        swModel.ClearSelection2(True)
        sketchLines = swSketchMgr.CreateCornerRectangle(0, 0, 0, -0.0822154876580373, 0.063635716435882, 0)
        swModel.ClearSelection2(True)

        ' Rotate the sketch about the specified point
        swModel.SketchModifyRotate(1, 1, 1)

        swModel.ClearSelection2(True)

        ' Make a copy of the selected lines and scale them by a factor of 2
        status = swModelDocExt.SelectByID2("Line3", "SKETCHSEGMENT", -0.0630770706086407, 0.0172671115438625, 0.0215538897292735, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Line2", "SKETCHSEGMENT", -0.0360136822942443, 0.0250170683049161, 0.00200770232274633, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", -0.00735948431462766, -0.0130061570540028, 0.0127196907180518, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Line4", "SKETCHSEGMENT", -0.0501900457103943, -0.0224514168565368, 0.0417377643321936, True, 0, Nothing, 0)
        swModelDocExt.ScaleOrCopy(True, 2, 0, 0.063635716435882, 0, 2)

        ' Rotate selected Line3
        status = swModel.DeSelectByID("Line2", "SKETCHSEGMENT", 0.00159286151716137, 0.0438212483979034, 0.00200770232274633)
        status = swModel.DeSelectByID("Line1", "SKETCHSEGMENT", -0.0149206501299916, -0.00083446413285288, 0.0127196907180518)
        status = swModel.DeSelectByID("Line4", "SKETCHSEGMENT", -0.046010013281556, 0.0301029148938852, 0.0417377643321936)
        swModelDocExt.RotateOrCopy(False, 2, False, -0.164430975316075, 0.063635716435882, 0, 0, 0, 1, 0.78539816339745)
        swModel.ClearSelection2(True)

        ' Zoom to fit
        swModel.ViewZoomtofit2()

        ' Scale the sketch by a factor of 3
        status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
        status = swModel.SketchModifyScale(3)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
