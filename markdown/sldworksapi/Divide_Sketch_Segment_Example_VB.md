---
title: "Divide Sketch Segment Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Divide_Sketch_Segment_Example_VB.htm"
---

# Divide Sketch Segment Example (VBA)

This example shows how to divide a sketch segment into equally spaced sketch points.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Ensure that the specified template exists.
 '
 ' Postconditions:
 ' 1. Creates Sketch1.
 ' 2. Divides the sketch's line into 99 equally spaced sketch points.
 ' ---------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim skSegment As SldWorks.SketchSegment
 Dim SkSeg As SketchSegment
 Dim boolstatus As Boolean
 Dim longstatus As Long
 Option Explicit
 Sub main()
    Set swApp = Application.SldWorks
     Set Part = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2015\templates\Part.prtdot", 0, 0, 0)
     swApp.ActivateDoc2 "Part1", False, longstatus
     Set Part = swApp.ActiveDoc
    Part.SketchManager.InsertSketch True
     Set skSegment = Part.SketchManager.CreateLine(-0.067186, 0.00851, 0#, 0.07118, 0.081524, 0#)
     boolstatus = Part.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
    Set Part = swApp.ActiveDoc
     boolstatus = Part.Extension.SelectByID2("Line1", "SKETCHSEGMENT", 5.8451006543539E-03, 0.017433416397686, -1.49283857579217E-02, False, 0, Nothing, 0)

    Set SkSeg = Part.SelectionManager.GetSelectedObject6(1, -1)
     boolstatus = SkSeg.EqualSegment(swSketchSegmentType_e.swSketchSegmentType_sketchpoints, 99)
    Part.ForceRebuild3 True

    boolstatus = Part.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
     Part.EditSketch
     Part.SketchManager.InsertSketch True

End Sub
```
