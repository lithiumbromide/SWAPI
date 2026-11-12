---
title: "Extend Sketch Entity Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Extend_Sketch_Entity_Example_VB.htm"
---

# Extend Sketch Entity Example (VBA)

This example shows how to extend a selected sketch entity (e.g., line, segment, or arc) to meet another sketch entity.

```
'-------------------------------------------------------------------
' Preconditions: Open a new part document.
'
' Postconditions:
' 1. Inserts a new sketch is inserted.
' 2. Creates two non-parallel lines.
' 3. Extends the first line to meet the second line.
' 4. Examine the graphics area.
'-------------------------------------------------------------------
Option Explicit
```

```vb
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swModelDocExt As SldWorks.ModelDocExtension
 Dim swSketchMgr As SldWorks.SketchManager
 Dim boolstatus As Boolean
Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swModelDocExt = swModel.Extension
     Set swSketchMgr = swModel.SketchManager

    swSketchMgr.InsertSketch False
    ' Create two non-parallel lines
     swSketchMgr.CreateLine -0.5, 0.88, 0#, -0.21, -0.13, 0#
     swSketchMgr.CreateLine -0.75, -1.128, 0#, 0.41, -1.128, 0#

    swModel.ViewZoomtofit2
    ' Set the selection mode to default
     swModel.SetPickMode
    ' Select the sketch line to extend
     boolstatus = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", 0#, 0#, 0#, False, 0, Nothing, 0)
    ' Extend the selected sketch line to meet the second line
     boolstatus = swSketchMgr.SketchExtend(0#, 0#, 0#)

    swSketchMgr.InsertSketch True

End Sub
```
