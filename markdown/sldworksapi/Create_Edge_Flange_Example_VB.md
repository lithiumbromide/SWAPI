---
title: "Create Edge Flange Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Edge_Flange_Example_VB.htm"
---

# Create Edge Flange Example (VBA)

This example shows how to create an edge flange.

```vb
'-----------------------------------------------
'
' Precconditions: Sheet metal part is open and
'                contains an edge flange. Flat pattern is suppressed.
'
' Postcontitions: Another edge flange is created.
'
'-----------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swEntity As SldWorks.Entity
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swFeat As SldWorks.Feature
Dim swEdgeFlange As SldWorks.EdgeFlangeFeatureData
Dim pNewEdge(0) As Object
Dim boolstatus As Boolean
Dim bRet As Boolean

Sub main()

    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swModelDocExt = swModel.Extension

    ' Select the edge for the new flange
    boolstatus = swModelDocExt.SelectByID2("", "EDGE", 0.06071758265887, -0.03627116313436, 0.05999086611155, False, 0, Nothing, 0)
    Set pNewEdge(0) = swSelMgr.GetSelectedObject6(1, 0)

    ' Select the sketch for the new flange
    boolstatus = swModelDocExt.SelectByID2("Sketch8", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
    Set swEntity = swSelMgr.GetSelectedObject6(1, 0)

    ' Select the existing edge flange to get the edge flange feature
    boolstatus = swModelDocExt.SelectByID2("Edge-Flange1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
    Set swFeat = swSelMgr.GetSelectedObject6(1, 0)
    swModel.ClearSelection2 True
    Set swEdgeFlange = swFeat.GetDefinition

   ' Roll back the model to modify it
    swEdgeFlange.AccessSelections swModel, Nothing

    swEntity.Select4 True, Nothing

    Dim vEdges As Variant
    vEdges = pNewEdge
    ' Create the new flange
    swEdgeFlange.Edges = vEdges

    ' Roll forward the model with the new flange
    swFeat.ModifyDefinition swEdgeFlange, swModel, Nothing

End Sub
```
