---
title: "Create and Modify Move Face Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_and_Modify_Move_Face_Feature_Example_VB.htm"
---

# Create and Modify Move Face Feature Example (VBA)

This example shows how to create a Move Face feature by translating a face on a part.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Verify that the specified part exists.
 ' 2. Press F8 repeatedly to step through the macro.
 ' 3. Observe the graphics area while stepping through the macro.
 '
 ' Postconditions:
 ' 1. Creates Move Face1 in the FeatureManager design tree.
 ' 2. Modifies the translation parameters of Move Face1.
 '
 ' NOTE: Because the part is used elsewhere, do not save changes.
 '---------------------------------------------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swModelDocExt As SldWorks.ModelDocExtension
 Dim swFeatMgr As SldWorks.FeatureManager
 Dim swFeat As SldWorks.Feature
 Dim swMoveFaceFeat As SldWorks.MoveFaceFeatureData
 Dim transParams As Variant
 Dim boolstatus As Boolean
 Dim triadParams(0 To 2) As Double
 Dim fileerror As Long
 Dim filewarning As Long
Sub main()
    Set swApp = Application.SldWorks
    ' Open the SOLIDWORKS Design document
     swApp.OpenDoc6 "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\assemblymates\knee.sldprt", swDocPART, swOpenDocOptions_Silent, "", fileerror, filewarning
    Set swModel = swApp.ActiveDoc
     Set swModelDocExt = swModel.Extension
     Set swFeatMgr = swModel.FeatureManager
    ' Translation parameters
     triadParams(0) = 0
     triadParams(1) = 0.05
     triadParams(2) = 0
    transParams = triadParams
    ' Select face to move
     boolstatus = swModel.Extension.SelectByID2("", "FACE", 0.04239074672171, 0.01587499999999, 0.3283508339712, False, 1, Nothing, 0)
    ' Create the Move Face feature by
     ' translating the selected face
     Set swFeat = swFeatMgr.InsertMoveFace3(swMoveFaceTypeTranslate, False, 0, 0, (transParams), Nothing, swEndCondBlind, 0)
    ' Modify the Move Face feature
     Set swMoveFaceFeat = swFeat.GetDefinition
    ' Roll back the Move Face feature
     swMoveFaceFeat.AccessSelections swModel, Nothing
    triadParams(0) = 0
     triadParams(1) = 0.1
     triadParams(2) = 0
    transParams = triadParams
    swMoveFaceFeat.TriadTranslationParameters = (transParams)
    ' Roll back the part with the modified Move Face feature
     swFeat.ModifyDefinition swMoveFaceFeat, swModel, Nothing
End Sub
```
