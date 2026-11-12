---
title: "Translate Move Face Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Translate_Move_Face_Feature_Example_VBNET.htm"
---

# Translate Move Face Feature Example (VB.NET)

This example shows how to translate a Move Face feature.

```
'---------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified document to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Creates Move Face1 in the FeatureManager design tree.
' 2. Modifies the translation parameters of Move Face1.
' 3. Gets the type of end condition and offset distance of Move Face1.
' 4. Examine the Immediate window.
'
' NOTE: Because the model document is used elsewhere,
' do not save changes.
'---------------------------------------------------------------------------
Imports System.Collections
Imports System.Collections.Generic
Imports System.Data
Imports System.Diagnostics
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices

Partial Class SolidWorksMacro

    Dim swModel As ModelDoc2
    Dim swModelDocExt As ModelDocExtension
    Dim swFeatMgr As FeatureManager
    Dim swFeat As Feature
    Dim swMoveFaceFeat As MoveFaceFeatureData
    Dim transParams As Object
    Dim boolstatus As Boolean
    Dim triadParams As Double() = New Double(2) {}
    Dim fileerror As Integer
    Dim filewarning As Integer

    Public Sub Main()
        ' Open the document
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
        boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.04239074672171, 0.01587499999999, 0.3283508339712, True, 1, Nothing, 0)

        ' Create the Move Face feature by
        ' translating the selected face
        swFeat = swFeatMgr.InsertMoveFace3(swMoveFaceType_e.swMoveFaceTypeTranslate, False, 0, 0, transParams, Nothing, swEndConditions_e.swEndCondBlind, 0)

        ' Modify the Move Face feature
        swMoveFaceFeat = swFeat.GetDefinition

        ' Roll back the Move Face feature
        swMoveFaceFeat.AccessSelections(swModel, Nothing)

        triadParams(0) = 0
        triadParams(1) = 0.1
        triadParams(2) = 0

        transParams = triadParams

        swMoveFaceFeat.TriadTranslationParameters = (transParams)

        ' Get type of end condition and offset distance from which the Move Face feature is translated
        Debug.Print("Type of end condition to which the Move Face feature is translated: " & swMoveFaceFeat.EndCondition)

        If swMoveFaceFeat.EndCondition = 5 Then
            Debug.Print("Offset distance of the Move Face feature: " & (swMoveFaceFeat.OffsetDistance * 39.37) & " inches")
        Else
            Debug.Print("Offset distance of the Move Face feature: " & (swMoveFaceFeat.Distance * 39.37) & " inches")
        End If

        ' Roll back the part with the modified Move Face feature
        swFeat.ModifyDefinition(swMoveFaceFeat, swModel, Nothing)

    End Sub

    Public swApp As SldWorks

End Class
```
