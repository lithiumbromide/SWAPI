---
title: "Select Chains of Entities Attached to a Sketch Segment Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Chain_of_Entities_Example_VB.htm"
---

# Select Chains of Entities Attached to a Sketch Segment Example (VBA)

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
Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim SelMgr As SldWorks.SelectionMgr
 Dim sketchSegment As SldWorks.sketchSegment
 Dim SelData As SldWorks.SelectData
 Dim boolstatus As Boolean
Sub main()
    Set swApp = Application.SldWorks
     Set Part = swApp.ActiveDoc
     Set SelMgr = Part.SelectionManager
     Set SelData = SelMgr.CreateSelectData
     boolstatus = Part.Extension.SelectByID2("Line3@Sketch2", "EXTSKETCHSEGMENT", -0.01022262320328, 0.01646364019604, 0, False, 0, Nothing, 0)
     Set sketchSegment = SelMgr.GetSelectedObject6(1, -1)
     boolstatus = sketchSegment.SelectChain(True, SelData)
End Sub
```
