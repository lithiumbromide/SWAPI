---
title: "Select Chains of Entities Attached to a Sketch Segment Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Chain_of_Entities_Example_VBNET.htm"
---

# Select Chains of Entities Attached to a Sketch Segment Example (VB.NET)

This example shows how to select chains of entities attached to a sketch segment.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a part that contains a sketch of a rectangle.
 ' 2. Select one sketch segment of the rectangle.
 '
 ' Postconditions:
 ' 1. Selects all of the sketch segments of the rectangle.
 ' 2. Examine the graphics area.
 ' ---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System

 Partial Class SolidWorksMacro

     Dim Part As ModelDoc2
     Dim SelMgr As SelectionMgr
     Dim sketchSegment As SketchSegment
     Dim SelData As SelectData
     Dim boolstatus As Boolean

     Sub main()

         Part = swApp.ActiveDoc
         SelMgr = Part.SelectionManager
         SelData = SelMgr.CreateSelectData
         boolstatus = Part.Extension.SelectByID2("Line3@Sketch2", "EXTSKETCHSEGMENT", -0.01022262320328, 0.01646364019604, 0,  False, 0,  Nothing, 0)
         sketchSegment = SelMgr.GetSelectedObject6(1, -1)
         boolstatus = sketchSegment.SelectChain(True, SelData)

     End Sub

     Public swApp As SldWorks

 End  Class
```
