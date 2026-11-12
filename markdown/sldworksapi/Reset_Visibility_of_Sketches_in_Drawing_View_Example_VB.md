---
title: "Reset Visibility of Sketches in Drawing View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Reset_Visibility_of_Sketches_in_Drawing_View_Example_VB.htm"
---

# Reset Visibility of Sketches in Drawing View Example (VBA)

This example shows how to reset the visibility of any hidden sketches in a drawing view so that the drawing view reflects the model.

```
'--------------------------------------------------
' Preconditions: Verify that the specified drawing
' to open document exists.
'
' Postconditions:
' 1. Opens the specified drawing document.
' 2. Examine the drawing, then press F5.
' 3. Activates a drawing view and hides
'    a sketch in that drawing view.
' 4. After examining the drawing to verify,
'    press F5.
' 5. Selects the drawing view with the hidden sketch
'    and resets the visibility of all sketches in
'    that drawing view so that the drawing view reflects
'    the model.
' 6. Examine the drawing to verify that the hidden
'    sketch is visible.
'
' NOTE: Because this drawing is used elsewhere, do
' not save changes.
'-------------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swDrawing As SldWorks.DrawingDoc
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelMgr As SldWorks.SelectionMgr
Dim swView As SldWorks.View
Dim fileName As String
Dim boolstatus As Boolean
Dim errors As Long
Dim warnings As Long
```

```
Sub main()
```

```
fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\resetsketchvisibility.SLDDRW"
```

```
Set swApp = Application.SldWorks
Set swModel = swApp.OpenDoc6(fileName, swDocDRAWING, swOpenDocOptions_Silent, "", errors, warnings)
Set swDrawing = swModel
Set swModelDocExt = swModel.Extension
Set swSelMgr = swModel.SelectionManager
```

```
Stop ' Examine the drawing, then press F%
```

```
' Select a drawing view where to hide a sketch
boolstatus = swDrawing.ActivateView("Drawing View1")
```

```
' Hide the selected sketch
boolstatus = swModelDocExt.SelectByID2("Sketch1@resetsketchvisibility-7@Drawing View1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
swModel.BlankSketch
```

```
Stop ' Examine the drawing to verify that selected sketch is hidden, then press F5
```

```
' Select the drawing view with the hidden sketch
boolstatus = swModelDocExt.SelectByID2("Drawing View1", "DRAWINGVIEW", 0, 0, 0, False, 0, Nothing, 0)
Set swView = swSelMgr.GetSelectedObject6(1, -1)
```

```
' Reset the visibility of sketches in the selected
' drawing view so that the drawing view reflects
' the model
swView.ResetSketchVisibility
```

```
End Sub
```
