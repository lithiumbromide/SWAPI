---
title: "Insert and Show BOM Table and BOM Balloon Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_and_Show_BOM_Table_and_BOM_Balloon_Example_VBNET.htm"
---

# Insert and Show BOM Table and BOM Balloon Example (VB.NET)

This example shows how to insert a Bill of Materials (BOM) table and balloon in a
drawing document.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Specified file and template exist.
' 2. Open an Immediate Window.
'
' Postconditions:
' 1. Inserts an indented BOM table.
' 2. Inserts a BOM balloon annotation.
' 3. Inspect the Immediate Window for the BOM feature
'    properties.
'
' NOTE: Because the drawing is used elsewhere, do not
' save any changes.
'---------------------------------------------------------------------------

Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swDrawing As DrawingDoc
        Dim swView As View
        Dim swBOMAnnotation As BomTableAnnotation
        Dim swBOMFeature As BomFeature
        Dim swNote As Note
        Dim BomBalloonParams As BalloonOptions
        Dim boolstatus As Boolean
        Dim AnchorType As Long
        Dim BomType As Integer
        Dim nErrors As Integer
        Dim nWarnings As Integer
        Dim Configuration As String
        Dim TableTemplate As String
        Dim Nbrtype As Integer

        swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\foodprocessor.slddrw", swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", nErrors, nWarnings)
        swDrawing = swModel
        swModelDocExt = swModel.Extension
        boolstatus = swDrawing.ActivateView("Drawing View1")
        swView = swDrawing.ActiveDrawingView

        ' Insert indented BOM table
        AnchorType = swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_TopLeft
        BomType = swBomType_e.swBomType_Indented
        TableTemplate = "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\bom-standard.sldbomtbt"
        Configuration = ""
        Nbrtype = swNumberingType_e.swNumberingType_Detailed
        swBOMAnnotation = swView.InsertBomTable6(False, 0.4, 0.3, AnchorType, BomType, Configuration, TableTemplate, False, NbrType, True, True, True)
        swBOMFeature = swBOMAnnotation.BomFeature

        Debug.Print("Type of BOM table as defined in swBomType_e: " & swBOMFeature.TableType)
        Debug.Print("Numbering type of BOM table as defined in swNumberingType_e: " & swBOMFeature.NumberingTypeOnIndentedBOM)
        Debug.Print("Value to display when a value is 0 as defined in swZeroQuantityDisplay_e: " & swBOMFeature.ZeroQuantityDisplay)
        Debug.Print("Name of configuration used for BOM table: " & swBOMFeature.Configuration)
        Debug.Print("Display as one item? " & swBOMFeature.DisplayAsOneItem)
        Debug.Print("Sequence start number: " & swBOMFeature.SequenceStartNumber)
        Debug.Print("Keep missing items? " & swBOMFeature.KeepMissingItems)
        Debug.Print("  Strikeout missing items? " & swBOMFeature.StrikeoutMissingItems)
        Debug.Print("  Replace missing components as defined in swKeepReplacedCompOption_e: " & swBOMFeature.KeepReplacedCompOption)
        Debug.Print("Keep current item numbers when reordering rows? " & swBOMFeature.KeepCurrentItemNumbers)

        boolstatus = swModelDocExt.SelectByID2("", "EDGE", 0.1205506330468, 0.261655309417, -0.0004000000000133, False, 0, Nothing, 0)

        BomBalloonParams = swModel.Extension.CreateBalloonOptions()
        BomBalloonParams.Style = swBalloonStyle_e.swBS_Circular
        BomBalloonParams.Size = swBalloonFit_e.swBF_2Chars
        BomBalloonParams.UpperTextContent = swBalloonTextContent_e.swBalloonTextItemNumber
        BomBalloonParams.ShowQuantity = True
        BomBalloonParams.QuantityPlacement = swBalloonQuantityPlacement_e.swBalloonQuantityPlacement_Right
        BomBalloonParams.QuantityDenotationText = "PLACES"
        BomBalloonParams.QuantityOverride = False
        BomBalloonParams.QuantityOverrideValue = ""
        BomBalloonParams.ItemNumberStart = 1
        BomBalloonParams.ItemNumberIncrement = 1
        BomBalloonParams.ItemOrder = swBalloonItemNumbersOrder_e.swBalloonItemNumbers_DoNotChangeItemNumbers

        swNote = swModelDocExt.InsertBOMBalloon2(BomBalloonParams)

        ' Get whether balloon is a BOM balloon
        ' If so, print the name of the BOM balloon

        If swNote.IsBomBalloon Then
            Debug.Print("Name of BOM balloon: " & swNote.GetName)
        End If

        swDrawing.ForceRebuild()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
