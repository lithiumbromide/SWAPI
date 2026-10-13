---
title: "Move Selected Face Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Move_Selected_Face_Example_VB.htm"
---

# Move Selected Face Example (VBA)

This example shows how to move the selected face in a part.

```vb
'-------------------------------------
'
' Preconditions: Part is open.
'
' Postconditions: The selected face is moved.
'
'-------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swFeatMgr As SldWorks.FeatureManager
Dim swFeat As SldWorks.Feature
Dim boolstatus As Boolean

Sub main()

    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
    Set swFeatMgr = swModel.FeatureManager

    ' Select face to move
    boolstatus = swModelDocExt.SelectByID2("", "FACE", -0.06133102397996, 0.0499999999999, 0.02353079473198, False, 1, Nothing, 0)
    ' Select the direction reference
    boolstatus = swModelDocExt.SelectByID2("", "EDGE", -0.05000883624581, 0.02773250193934, 0.04000883624559, True, 2, Nothing, 0)
    ' Move the selected face
    Set swFeat = swFeatMgr.InsertMoveFace(1, False, 0.034907, 0.05)
    swModel.ViewZoomtofit2

End Sub
```
