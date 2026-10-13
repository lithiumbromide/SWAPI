---
title: "Move and Copy Body by Setting Transforms Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Move_and_Copy_Body_by_Setting_Transforms_Example_VB.htm"
---

# Move and Copy Body by Setting Transforms Example (VBA)

This example shows how to move and copy bodies by setting transforms.

```vb
'----------------------------------------------------------
'
' Preconditions:
'    (1) Part document is open.
'    (2) Body-Move/Copy1 feature exists.
'
' Postconditions: Body is moved and copied as per transform settings.
'
'-----------------------------------------------------------
Option Explicit

Sub main()
    Dim swApp As SldWorks.SldWorks
    Dim part As SldWorks.PartDoc
    Dim component As SldWorks.Component2
    Dim moveCopyFeat As SldWorks.feature
    Dim moveCopy_featData As SldWorks.MoveCopyBodyFeatureData
    Dim boolstatus As Boolean

    Set swApp = Application.SldWorks
    Set part = swApp.ActiveDoc

    Set moveCopyFeat = part.FeatureByName("Body-Move/Copy1")
    Set moveCopy_featData = moveCopyFeat.GetDefinition
    boolstatus = moveCopy_featData.AccessSelections(part, component)

    moveCopy_featData.TransformType = swTransformType_Translation
    moveCopy_featData.TransformX = 0.02
    moveCopy_featData.TransformY = 0.03
    moveCopy_featData.TransformZ = 0.04

    boolstatus = moveCopyFeat.ModifyDefinition(moveCopy_featData, part, Nothing)
    moveCopy_featData.ReleaseSelectionAccess

End Sub
```
