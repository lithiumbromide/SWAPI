---
title: "Divide Sketch Segment Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Divide_Sketch_Segment_Example_VBNET.htm"
---

# Divide Sketch Segment Example (VB.NET)

This example shows how to divide a sketch segment into equally spaced sketch points.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Ensure that the specified template exists.
 '
 ' Postconditions:
 ' 1. Creates Sketch1.
 ' 2. Divides the sketch's line into 99 equally spaced sketch points.
 ' ---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Dim Part As ModelDoc2
     Dim skSegment As SketchSegment
     Dim SkSeg As SketchSegment
     Dim boolstatus As Boolean
     Dim longstatus As Integer

     Sub main()

         Part = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2015\templates\Part.prtdot", 0, 0, 0)
         swApp.ActivateDoc2("Part1", False, longstatus)
         Part = swApp.ActiveDoc

         Part.SketchManager.InsertSketch(True)
         skSegment = Part.SketchManager.CreateLine(-0.067186, 0.00851, 0.0#, 0.07118, 0.081524, 0.0#)
         boolstatus = Part.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)

         Part = swApp.ActiveDoc
         boolstatus = Part.Extension.SelectByID2("Line1", "SKETCHSEGMENT", 0.0058451006543539, 0.017433416397686, -0.0149283857579217,  False, 0,  Nothing, 0)

         SkSeg = Part.SelectionManager.GetSelectedObject6(1, -1)
         boolstatus = SkSeg.EqualSegment(swSketchSegmentType_e.swSketchSegmentType_sketchpoints, 99)

         Part.ForceRebuild3(True)

         boolstatus = Part.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
         Part.EditSketch()
         Part.SketchManager.InsertSketch(True)

     End Sub

     Public swApp As SldWorks

 End  Class
```
