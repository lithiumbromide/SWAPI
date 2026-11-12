---
title: "Change Direction Reference of Move Face Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Direction_Reference_of_Move_Face_Feature_Example_VB.htm"
---

# Change Direction Reference of Move Face Feature Example (VBA)

This example shows how to change the reference direction of a Move Face feature.

```vb
'-----------------------------------------------------
'
' Preconditions: Part is open that has a Move Face feature.
'
' Postconditions: The selected edge becomes the new
'                direction reference for the Move Face feature.
'
'-----------------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelMgr As SldWorks.SelectionMgr
Dim swFeat As SldWorks.Feature
Dim swMoveFaceFeat As SldWorks.MoveFaceFeatureData
Dim swEntity As SldWorks.Entity
Dim boolstatus As Boolean
Dim dirType As Long

Sub main()

    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swModelDocExt = swModel.Extension

    ' Get the Move Face feature
    boolstatus = swModelDocExt.SelectByID2("Move Face1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
    Set swFeat = swSelMgr.GetSelectedObject6(1, 0)
    swModel.ClearSelection2 True
    Set swMoveFaceFeat = swFeat.GetDefinition

    ' Roll back the Move Face feature
    swMoveFaceFeat.AccessSelections swModel, Nothing
    ' Get the current direction reference
    Set swEntity = swMoveFaceFeat.GetDirectionReference(dirType)
    swEntity.Select4 False, Nothing
   ' Clear the selection
    swModel.ClearSelection2 True

    ' Select a different edge for the direction reference
    boolstatus = swModelDocExt.SelectByID2("", "EDGE", -0.05047526142499, 0.03085263679878, 0.04047526142483, False, 0, Nothing, 0)
    Set swEntity = swSelMgr.GetSelectedObject6(1, 0)
    swModel.ClearSelection2 True
    ' Set the direction reference to the just-selected edge
    swMoveFaceFeat.SetDirectionReference swEntity

    ' Roll back the part with the modified Move Face feature
    swFeat.ModifyDefinition swMoveFaceFeat, swModel, Nothing

End Sub
```
