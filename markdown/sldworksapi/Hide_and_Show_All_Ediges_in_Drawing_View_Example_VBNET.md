---
title: "Hide and Show All Edges in Drawing View (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Hide_and_Show_All_Ediges_in_Drawing_View_Example_VBNET.htm"
---

# Hide and Show All Edges in Drawing View (VB.NET)

This example shows how to hide and then show all of the edges in the root component in a drawing view.

```vb
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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim swDraw As DrawingDoc
     Dim swDocSpecification As DocumentSpecification
     Dim swSheet As Sheet
     Dim swView As View
     Dim swDrawingComponent As DrawingComponent
     Dim swComponent As Component2
     Dim swEntity As Entity
     Dim vEdges As Object
     Dim bRet As Boolean
     Dim i As  Integer

     Sub main()

         ' Specify the drawing to open
         swDocSpecification = swApp.GetOpenDocSpec("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\foodprocessor.SLDDRW")
         swModel = swApp.ActiveDoc

         If swModel Is Nothing Then
             swModel = swApp.OpenDoc7(swDocSpecification)
         End If

         swModel = swApp.ActiveDoc
         swDraw = swModel

         ' Get the current sheet
         swSheet = swDraw.GetCurrentSheet
         Debug.Print(swSheet.GetName)

         ' Select Drawing View1
         bRet = swModel.Extension.SelectByID2("Drawing View1",  "DRAWINGVIEW", 0.0#, 0.0#, 0.0#,  True, 0,  Nothing, swSelectOption_e.swSelectOptionDefault)
         swView = swModel.SelectionManager.GetSelectedObject6(1, -1)

         ' Print the drawing view name and get the component in the drawing view
         Debug.Print(swView.GetName2)
         swDrawingComponent = swView.RootDrawingComponent
         swComponent = swDrawingComponent.Component

         ' Get the component's visible entities in the drawing view
         Dim eCount As Integer
         eCount = swView.GetVisibleEntityCount2(swComponent, swViewEntityType_e.swViewEntityType_Edge)
         vEdges = swView.GetVisibleEntities2(swComponent, swViewEntityType_e.swViewEntityType_Edge)
         Debug.Print("Number of edges found: " & eCount)

         ' Hide all of the visible edges in the drawing view
         For i = 0 To eCount - 1
             swEntity = vEdges(i)
             swEntity.Select4(True, Nothing)
             swDraw.HideEdge()
         Next i

         ' Clear all selections
         swModel.ClearSelection2(True)

         ' Show all hidden edges
         swView.HiddenEdges = vEdges

     End Sub

     Public swApp As SldWorks

 End  Class
```
