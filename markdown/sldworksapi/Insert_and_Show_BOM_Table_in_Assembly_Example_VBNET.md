---
title: "Insert and Show BOM Table in Assembly Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_and_Show_BOM_Table_in_Assembly_Example_VBNET.htm"
---

# Insert and Show BOM Table in Assembly Example (VB.NET)

This example shows how to insert and show a BOM table in an assembly document.

```
'------------------------------------------------
' Preconditions:
' 1. Verify that the specified file and template exist.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Inserts an indented BOM table.
' 2. Inserts a split-circle stacked balloon, which uses the
'    BOM table item number for its upper text,
'    at the selected face.
' 3. Examine the BOM table, stacked balloon, and Immediate
'    window.
'
' NOTE: Because this assembly document is used elsewhere,
' do not save changes.
'-------------------------------------------------

Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Sub Main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swBOMAnnotation As BomTableAnnotation
        Dim swBOMFeature As BomFeature
        Dim StackedBalloonParams As StackedBalloonOptions
        Dim swNote As Note
        Dim boolstatus As Boolean
        Dim BomType As Integer
        Dim nbrType as Integer
        Dim Configuration As String
        Dim TemplateName As String
        Dim nErrors As Integer
        Dim nWarnings As Integer

        ' Open assembly document
        swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\arm2.sldasm", swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", nErrors, nWarnings)
        swModelDocExt = swModel.Extension

        ' Insert BOM table
        TemplateName = "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\bom-standard.sldbomtbt"
        BomType = swBomType_e.swBomType_Indented
        Configuration = "Default"
        nbrType = swNumberingType_e.swNumberingType_Detailed

        swBOMAnnotation = swModelDocExt.InsertBomTable4(TemplateName, 0, 0, BomType, Configuration, False, nbrType, True, True)
        swBOMFeature = swBOMAnnotation.BomFeature

        ' Print the name of the configuration used for the BOM table
        Debug.Print("Name of configuration used for BOM table: " & swBOMFeature.Configuration)

        ' Insert BOM balloon for the selected face
        boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.091853347996107, -0.0104709589619745, 0.00174830255600256, False, 0, Nothing, 0)

        StackedBalloonParams =swModelDocExt.CreateStackedBalloonOptions()
        StackedBalloonParams.BalloonsPerLine = 10
        StackedBalloonParams.StackDirection = swStackedBalloonDirection_e.swStackedBalloonDir_Right
        StackedBalloonParams.Style = swBalloonStyle_e.swBS_SplitCirc
        StackedBalloonParams.LowerTextContent = swBalloonTextContent_e.swBalloonTextCustom
        StackedBalloonParams.LowerText = "Lower Text"
        StackedBalloonParams.ShowQuantity = True
        StackedBalloonParams.Size = swBalloonFit_e.swBF_Tightest
        StackedBalloonParams.QuantityPlacement = swBalloonQuantityPlacement_e.swBalloonQuantityPlacement_Top
        StackedBalloonParams.QuantityDenotationText = "Denotation Text"
        StackedBalloonParams.QuantityOverride = False
        StackedBalloonParams.ItemNumberStart = 1
        StackedBalloonParams.ItemNumberIncrement = 1
        StackedBalloonParams.ItemOrder = swBalloonItemNumbersOrder_e.swBalloonItemNumbers_DoNotChangeItemNumbers

        swNote = swModelDocExt.InsertStackedBalloon2(StackedBalloonParams)

        swModel.ViewZoomtofit2()

        ' Get whether balloon is a stacked balloon;
        ' if so, print the name of the balloon
        If swNote.IsStackedBalloon Then

            Debug.Print("Name of stacked balloon: " & swNote.GetName)

        End If

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
