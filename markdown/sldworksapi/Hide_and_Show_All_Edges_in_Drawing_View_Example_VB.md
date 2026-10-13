---
title: "Hide and Show All Edges in Drawing View (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Hide_and_Show_All_Edges_in_Drawing_View_Example_VB.htm"
---

# Hide and Show All Edges in Drawing View (VBA)

This example shows how to hide and then show all of the edges in the root component in a drawing view.

```
'---------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the drawing document to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified drawing document.
' 2. Hides and then shows all edges in the root component in
'    Drawing View1.
' 3. Examine the drawing and Immediate window.
'----------------------------------------------------------------------------
Option Explicit
```

```vb
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

 Sub main()
    Set swApp = Application.SldWorks

    ' Specify the drawing to open
     Set swDocSpecification = swApp.GetOpenDocSpec("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\foodprocessor.SLDDRW")
     Set swModel = swApp.ActiveDoc

    If swModel Is Nothing Then
         Set swModel = swApp.OpenDoc7(swDocSpecification)
     End If

     Set swModel = swApp.ActiveDoc
     Set swDraw = swModel

    ' Get the current sheet
     Set swSheet = swDraw.GetCurrentSheet
     Debug.Print swSheet.GetName

    ' Select Drawing View1
     bRet = swModel.Extension.SelectByID2("Drawing View1", "DRAWINGVIEW", 0#, 0#, 0#, True, 0, Nothing, swSelectOptionDefault): Debug.Assert bRet
     Set swView = swModel.SelectionManager.GetSelectedObject6(1, -1)

    ' Print the drawing view name and get the component in the drawing view
     Debug.Print swView.GetName2
     Set swDrawingComponent = swView.RootDrawingComponent
     Set swComponent = swDrawingComponent.Component

    ' Get the component's visible entities in the drawing view
     Dim eCount As Long
     eCount = swView.GetVisibleEntityCount2(swComponent, swViewEntityType_Edge)
     vEdges = swView.GetVisibleEntities2(swComponent, swViewEntityType_Edge)
     Debug.Print "Number of edges found: " & eCount

    ' Hide all of the visible edges in the drawing view
     For i = 0 To eCount - 1
         Set swEntity = vEdges(i)
         swEntity.Select4 True, Nothing
         swDraw.HideEdge
     Next i

    ' Clear all selections
     swModel.ClearSelection2 True

    ' Show all hidden edges
     swView.HiddenEdges = vEdges
End Sub
```
