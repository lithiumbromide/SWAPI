---
title: "Hide All Edges in Drawing View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Hide_All_Edges_in_Drawing_View_Example_VB.htm"
---

# Hide All Edges in Drawing View Example (VBA)

This example shows how to hide all of the visible edges in the root component in a drawing view.

```
'------------------------------------------------------------------
' Preconditions:
' 1. Verify that the drawing document to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified drawing document.
' 2. Gets the current sheet and Drawing View1.
' 3. Gets the visible entities in the root component in
'    Drawing View1.
' 4. Hides all of the visible edges in the root component
'    in Drawing View1.
' 5. Examine Drawing View1 and the Immediate window.
'
' NOTE: Because the drawing is used elsewhere, do not save changes.
'------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swDraw As SldWorks.DrawingDoc
Dim swDocSpecification As SldWorks.DocumentSpecification
Dim swSheet As SldWorks.Sheet
Dim swView As SldWorks.View
Dim swDrawingComponent As SldWorks.DrawingComponent
Dim swComponent As SldWorks.Component2
Dim swEntity As SldWorks.Entity
Dim vEdges As Variant
Dim bRet As Boolean
Dim i As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    ' Open the drawing document
    Set swDocSpecification = swApp.GetOpenDocSpec("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\foodprocessor.slddrw")
    Set swModel = swApp.ActiveDoc
```

```
    If swModel Is Nothing Then
        Set swModel = swApp.OpenDoc7(swDocSpecification)
    End If
```

```
    Set swDraw = swModel
```

```
    ' Get the current sheet
    Set swSheet = swDraw.GetCurrentSheet
    Debug.Print swSheet.GetName
```

```
    ' Select Drawing View1
    bRet = swModel.Extension.SelectByID2("Drawing View1", "DRAWINGVIEW", 0#, 0#, 0#, True, 0, Nothing, swSelectOptionDefault): Debug.Assert bRet
    Set swView = swModel.SelectionManager.GetSelectedObject6(1, -1)
```

```
    ' Print the drawing view name and get the component in the drawing view
    Debug.Print swView.GetName2
    Set swDrawingComponent = swView.RootDrawingComponent
    Set swComponent = swDrawingComponent.Component
```

```
    ' Get the component's visible entities in the drawing view
    vEdges = swView.GetVisibleEntities2(swComponent, swViewEntityType_Edge)
```

```
    ' Hide all of the visible edges in the drawing view
        For i = 0 To UBound(vEdges)
            Set swEntity = vEdges(i)
            swEntity.Select4 True, Nothing
            swDraw.HideEdge
        Next i
```

```
    swModel.ClearSelection2 True
```

```
End Sub
```
