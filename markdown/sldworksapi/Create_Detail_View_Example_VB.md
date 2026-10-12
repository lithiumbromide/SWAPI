---
title: "Create Detail View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Detail_View_Example_VB.htm"
---

# Create Detail View Example (VBA)

This example shows how to create a detail view.

A named view is activated and a circle centered about the view's origin is created. A detail view is then created at the origin of the sheet. If you modify the macro to adjust the values to different locations, you can see how the values affect the results.

The 1,1,0 represent 1m,1m,0m in sheet space. Most APIs expect units of meters and radians for length and angle values, respectively.

NOTE: The call to IDrawingDoc::CreateDetailViewAt3 uses the x,y,z coordinates relative to the sheet's origin. The sheet's origin is at the lower-left corner of the sheet. The x,y,z coordinates represent the location on the sheet where to place the origin of the parent view.

```vb
'---------------------------------------------
'
' Preconditions: Drawing document is open and contains a Drawing View1.
'
' Postconditions: A circle is created about the activated view's origin
'                and a detail view is then created at the origin of the sheet.
'
'------------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swDrawingDoc As SldWorks.DrawingDoc
Dim swSelMgr As SldWorks.SelectionMgr
Dim swSketchSegment As SldWorks.SketchSegment

Sub main()

Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swSelMgr = swModel.SelectionManager
Set swDrawingDoc = swModel

swDrawingDoc.ActivateView "Drawing View1"
Set swSketchSegment = swModel.CreateCircle2(0, 0, 0, 0.005, 0, 0)
swDrawingDoc.CreateDetailViewAt3 0, 0, 0, 0, 1#, 1#, "B", 1, 0

End Sub
```
