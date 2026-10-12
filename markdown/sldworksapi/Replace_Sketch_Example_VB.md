---
title: "Replace Sketch Entity Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Replace_Sketch_Example_VB.htm"
---

# Replace Sketch Entity Example (VBA)

This example shows how to replace a sketch entity in a model with another sketch entity.

```
'----------------------------------------------------------------------------
' Preconditions: Verify that the specified template exists.
'
' Postconditions:
' 1. Opens a new part and creates Boss-Extrude1.
' 2. Replaces a sketch line with a sketch arc and modifies
'    Boss-Extrude1.
' 3. Examine the graphics area.
'---------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks

Dim Part As SldWorks.ModelDoc2

Dim myFeature As SldWorks.Feature

Dim skSegment As SldWorks.SketchSegment

Dim boolstatus As Boolean

Option Explicit
```

```vb
Sub main()
    Set swApp = _
     Application.SldWorks

    Set Part = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2022\templates\Part.prtdot", 0, 0, 0)
     Set Part = swApp.ActiveDoc

    boolstatus = Part.Extension.SelectByID2("Front Plane", "PLANE", -0.048646278525398, 2.22864804840025E-02, 1.05288722478765E-02, False, 0, Nothing, 0)
     Dim vSkLines As Variant
     vSkLines = Part.SketchManager.CreateCornerRectangle(-3.38155129850894E-02, 1.67825138518592E-02, 0, 5.51067619016271E-02, -2.45475575743612E-02, 0)
     Part.ClearSelection2 True
     Part.SketchManager.InsertSketch True
     Part.ShowNamedView2 "*Trimetric", 8
     boolstatus = Part.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 4, Nothing, 0)

    Set myFeature = Part.FeatureManager.FeatureExtrusion2(True, False, False, 0, 0, 0.01778, 0.00254, False, False, False, False, 1.74532925199433E-02, 1.74532925199433E-02, False, False, False, False, True, True, True, 0, 0, False)
     Part.SelectionManager.EnableContourSelection = False
     boolstatus = Part.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
     Part.EditSketch
     Part.ClearSelection2 True

    Set skSegment = Part.SketchManager.Create3PointArc(-0.033816, 0.016783, 0#, 0.055107, 0.016783, 0#, 0.016009, 0.025458, 0#)
     Part.ClearSelection2 True
    boolstatus = Part.Extension.SelectByID2("Line1", "SKETCHSEGMENT", 2.02904300411839E-03, 1.19654152286464E-02, -7.09549576220667E-03, True, 0, Nothing, 0)
     boolstatus = Part.Extension.SelectByID2("Arc1", "SKETCHSEGMENT", 5.88878331207997E-03, 1.71023327681304E-02, -1.26221740799126E-02, True, 0, Nothing, 0)
    ' Replace Line1 with Arc1, delete Line1, and make Arc1 a contour
     boolstatus = Part.SketchManager.SketchReplace2(False, True)
    Part.SketchManager.InsertSketch True

End Sub
```
