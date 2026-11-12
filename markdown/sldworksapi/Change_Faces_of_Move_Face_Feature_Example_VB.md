---
title: "Change Faces of Move Face Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Faces_of_Move_Face_Feature_Example_VB.htm"
---

# Change Faces of Move Face Feature Example (VBA)

This example shows how to modify a Move Face feature by changing the defining faces.

```vb
'-----------------------------------------
'
' Preconditions: Part is open that has a Move Face feature.
'
' Postcondtiions: The selected new face now defines the Move Face
'                feature.
'
'-----------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelMgr As SldWorks.SelectionMgr
Dim swFeat As SldWorks.Feature
Dim swMoveFaceFeat As SldWorks.MoveFaceFeatureData
Dim swEnt As SldWorks.Entity
Dim vFaces As Variant
Dim pFace As Variant
Dim vNewFaces As Variant
Dim pNewFace As Variant
Dim pNewFaceArr(0) As Object
Dim boolstatus As Boolean

Sub main()

    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swModelDocExt = swModel.Extension

    ' Select the Move Face feature
    boolstatus = swModelDocExt.SelectByID2("Move Face1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
    Set swFeat = swSelMgr.GetSelectedObject6(1, 0)
    swModel.ClearSelection2 True
    Set swMoveFaceFeat = swFeat.GetDefinition

    ' Roll back the Move Face feature
    swMoveFaceFeat.AccessSelections swModel, Nothing

    ' Find and clear the faces that define the Move Face feature
    vFaces = swMoveFaceFeat.Faces
    For Each pFace In vFaces
        Set swEnt = pFace
        swEnt.Select4 False, Nothing
        swModel.ClearSelection2 True
    Next

    ' Select a new face for the Move Face feature
    boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.06393265679355, 0.04999999999984, 0.01806458069194, False, 0, Nothing, 0)
    Set pNewFace = swSelMgr.GetSelectedObject6(1, 0)
    swModel.ClearSelection2 True
    Set pNewFaceArr(0) = pNewFace
    vNewFaces = pNewFaceArr
    ' Set the new face for the Move Face feature
    swMoveFaceFeat.Faces = vNewFaces

    ' Modify the Move Face feature and roll back the feature
    swFeat.ModifyDefinition swMoveFaceFeat, swModel, Nothing

End Sub
```
