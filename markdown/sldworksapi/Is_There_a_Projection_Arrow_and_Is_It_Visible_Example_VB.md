---
title: "Is There a Projection Arrow and Is It Visible Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Is_There_a_Projection_Arrow_and_Is_It_Visible_Example_VB.htm"
---

# Is There a Projection Arrow and Is It Visible Example (VBA)

This example shows how to find out if:

- the selected drawing view is a projected view
- a projection arrow exists in the projected view
- the projected arrow is visible

```
'--------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\advdrawings\foodprocessor.slddrw.
' 2. Double-click the projected view (i.e., the upper-right drawing view).
' 3. In the PropertyManager page, click the Arrow check box and
'    type a label for the projection arrow.
' 4. Click OK to close the PropertyManager page.
'
' Postconditions:
' 1. Creates a visible projection arrow for Drawing View2, which is
'    a projected view.
' 2. Examine the graphics area and Immediate window.
'
' NOTE: Because this drawing document is used elsewhere, do not save
' changes.
'--------------------------------------------------------------------------
```

```vb
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swDrawing As SldWorks.DrawingDoc
Dim swView As SldWorks.View
Dim swProjectionArrow As SldWorks.ProjectionArrow
Dim typeDrawingView As Long
Dim boolstatus As Boolean
Sub main()
```

```vb
Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swDrawing = swModel

Set swModelDocExt = swModel.Extension
boolstatus = swDrawing.ActivateView("Drawing View2")
boolstatus = swModelDocExt.SelectByID2("Drawing View2", "DRAWINGVIEW", 0.4426278247583, 0.3837831481976, 0, False, 0, Nothing, 0)

Set swView = swDrawing.ActiveDrawingView
typeDrawingView = swView.Type
If typeDrawingView = 4 Then
    Debug.Print "Type of selected drawing view is projected."
Else
    Debug.Print "Type of selected drawing view is not projected. Exiting macro."
    Exit Sub
End If

Set swProjectionArrow = swView.GetProjectionArrow
If Not swProjectionArrow Is Nothing Then
    Debug.Print "Projection arrow visible: " & swProjectionArrow.Visible
Else
    Debug.Print "No projection arrow in projected view."
End If
```

```vb
End Sub
```
