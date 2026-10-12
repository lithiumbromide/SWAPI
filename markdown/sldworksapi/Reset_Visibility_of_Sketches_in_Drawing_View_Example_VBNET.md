---
title: "Reset Visibility of Sketches in Drawing View Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Reset_Visibility_of_Sketches_in_Drawing_View_Example_VBNET.htm"
---

# Reset Visibility of Sketches in Drawing View Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System

	Partial Class SolidWorksMacro

	    Public Sub Main()

	        Dim swModel As ModelDoc2
	        Dim swDrawing As DrawingDoc
	        Dim swModelDocExt As ModelDocExtension
	        Dim swSelMgr As SelectionMgr
	        Dim swView As View
	        Dim fileName As String
	        Dim boolstatus As Boolean
	        Dim errors As Integer
	        Dim warnings As Integer

	        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\resetsketchvisibility.SLDDRW"

	        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
	        swDrawing = swModel
	        swModelDocExt = swModel.Extension
	        swSelMgr = swModel.SelectionManager

	        Stop ' Examine the drawing, then press F5
```

```
	        ' Select a drawing view where to hide a sketch
	        boolstatus = swDrawing.ActivateView("Drawing View1")

	        ' Hide the selected sketch
	        boolstatus = swModelDocExt.SelectByID2("Sketch1@resetsketchvisibility-7@Drawing View1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
	        swModel.BlankSketch()

	        Stop ' Examine the drawing to verify that selected sketch is hidden, then press F5

	        ' Select the drawing view with the hidden sketch
	        boolstatus = swModelDocExt.SelectByID2("Drawing View1", "DRAWINGVIEW", 0, 0, 0, False, 0, Nothing, 0)
	        swView = swSelMgr.GetSelectedObject6(1, -1)

	        ' Reset the visibility of sketches in the selected
	        ' drawing view so that the drawing view reflects the model
	        swView.ResetSketchVisibility()

	End Sub

	''' <summary>
	''' The SldWorks swApp variable is pre-assigned for you.
	''' </summary>
	Public swApp As SldWorks

End Class
```
