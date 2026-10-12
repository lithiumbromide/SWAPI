---
title: "Align Text with Line Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Align_Text_with_Line_Eample_VB.htm"
---

# Align Text with Line Example (VBA)

This example shows how to align text with a selected line.

```vb
'---------------------------------------
' Preconditions: A model document is open.
'
' Postconditions: A sketch containing a line is
'                 created on the Front plane and
'                 the word TEST is aligned with
'                 and created with that line.
'----------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSketchMgr As SldWorks.SketchManager
Dim boolstatus As Boolean

Sub main()
```

```vb
Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swSelMgr = swModel.SelectionManager
Set swModelDocExt = swModel.Extension
Set swSketchMgr = swModel.SketchManager

' Select the Front plane
boolstatus = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
' Open a sketch
swSketchMgr.InsertSketch True
swModel.ClearSelection2 True

' Create a line
swModel.CreateLine2 -0.04180198735321, 0.03305974480578, 0, 0.03898839205059, -0.02461895889792, 0
swModel.ClearSelection2 True

' Rebuild and close the sketch
swSketchMgr.InsertSketch True
swModel.ClearSelection2 True

' Select the Front plane
boolstatus = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
' Open a sketch
swSketchMgr.InsertSketch True
swModel.ClearSelection2 True

' Select the previously created line
boolstatus = swModelDocExt.SelectByID2("Line1@Sketch1", "EXTSKETCHSEGMENT", -0.01503940368923, -0.008275270054597, 0, False, 1, Nothing, 0)
' Align and insert the word TEST on the selected line
swModel.InsertSketchText 0, 0, 0, "TEST", 0, 0, 0, 100, 100
swModel.ClearSelection2 True
```

```vb
End Sub
```
