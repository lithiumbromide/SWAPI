---
title: "Create and Modify Move Face Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_and_Modify_Move_Face_Feature_Example_VBNET.htm"
---

# Create and Modify Move Face Feature Example (VB.NET)

This example shows how to create a Move Face feature by translating a face on a part.

```vb
  '---------------------------------------------------------------------------
 ' Preconditions: Verify that the specified part exists.
 '
 ' Postconditions:
 ' 1. Creates Move Face1 in the FeatureManager design tree.
 ' 2. Modifies the translation parameters of Move Face1.
 '
 ' NOTE: Because the part is used, do not save changes.
  '---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim swModelDocExt As ModelDocExtension
     Dim swFeatMgr As FeatureManager
     Dim swFeat As Feature
     Dim swMoveFaceFeat As MoveFaceFeatureData
     Dim transParams As Object
     Dim boolstatus As Boolean
     Dim triadParams(0 To 2) As Double
     Dim fileerror As Integer
     Dim filewarning As Integer

     Sub main()

         ' Open the SOLIDWORKS Design document
         swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\assemblymates\knee.sldprt", swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", fileerror, filewarning)

         swModel = swApp.ActiveDoc
         swModelDocExt = swModel.Extension
         swFeatMgr = swModel.FeatureManager

         ' Translation parameters
         triadParams(0) = 0
         triadParams(1) = 0.05
         triadParams(2) = 0

         transParams = triadParams

         ' Select face to move
         boolstatus = swModel.Extension.SelectByID2("", "FACE", 0.04239074672171, 0.01587499999999, 0.3283508339712, False, 1, Nothing, 0)

         ' Create the Move Face feature by
         ' translating the selected face
         swFeat = swFeatMgr.InsertMoveFace3(swMoveFaceType_e.swMoveFaceTypeTranslate, False, 0, 0, (transParams), Nothing, swEndConditions_e.swEndCondBlind, 0)

         ' Modify the Move Face feature
         swMoveFaceFeat = swFeat.GetDefinition

         ' Roll back the Move Face feature
         swMoveFaceFeat.AccessSelections(swModel, Nothing)

         triadParams(0) = 0
         triadParams(1) = 0.1
         triadParams(2) = 0

         transParams = triadParams

         swMoveFaceFeat.TriadTranslationParameters = (transParams)

         ' Roll back the part with the modified Move Face feature
         swFeat.ModifyDefinition(swMoveFaceFeat, swModel, Nothing)

     End Sub

     Public swApp As SldWorks

 End Class
```
