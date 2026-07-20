---
title: "Insert and Show BOM Table and BOM Balloon Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_and_Show_BOM_Table_and_BOM_Balloon_Example_VB.htm"
---

# Insert and Show BOM Table and BOM Balloon Example (VBA)

This example shows how to insert a Bill of Materials (BOM) table andkadov_tag{{</spaces>}}balloon
in a drawing document.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Specified file and template exist.
 ' 2. Open an Immediate Window.
 '
 ' Postconditions:
 ' 1. Inserts an indented BOM table.
 ' 2. Inserts a BOM balloon annotation.
 ' 3. Inspect the Immediate Window for the BOM feature properties.
 '
 ' NOTE: Because the drawing is used elsewhere, do not save any changes.
 '---------------------------------------------------------------------------

Dim swApp                   As SldWorks.SldWorks
 Dim swModel                 As SldWorks.ModelDoc2
 Dim swModelDocExt           As SldWorks.ModelDocExtension
 Dim swDrawing               As SldWorks.DrawingDoc
 Dim swView                  As SldWorks.View
 Dim swBOMAnnotation         As SldWorks.BomTableAnnotation
 Dim swBOMFeature            As SldWorks.BomFeature
 Dim swNote                  As SldWorks.Note
 Dim BomBalloonParams        As SldWorks.BalloonOptions
 Dim boolstatus              As Boolean
 Dim AnchorType              As Long
 Dim BomType                 As Long
 Dim nErrors                 As Long
 Dim nWarnings               As Long
 Dim Configuration           As String
 Dim TableTemplate           As String
Option Explicit
Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\foodprocessor.slddrw", swDocDRAWING, swOpenDocOptions_Silent, "", nErrors, nWarnings)
     Set swDrawing = swModel
     Set swModelDocExt = swModel.Extension
     boolstatus = swDrawing.ActivateView("Drawing View1")
     Set swView = swDrawing.ActiveDrawingView
    ' Insert indented BOM table
     AnchorType = swBOMConfigurationAnchor_TopLeft
     BomType = swBomType_Indented
     TableTemplate = "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\bom-standard.sldbomtbt"
     Configuration = ""
     Set swBOMAnnotation = swView.InsertBOMTable6(False, 0.4, 0.3, AnchorType, BomType, Configuration, TableTemplate, False, swNumberingType_Detailed, True, True, True)
     Set swBOMFeature = swBOMAnnotation.BomFeature
    Debug.Print "Type of BOM table as defined in swBomType_e: " & swBOMFeature.TableType
     Debug.Print "Numbering type of BOM table as defined in swNumberingType_e: " & swBOMFeature.NumberingTypeOnIndentedBOM
     Debug.Print "Value to display when a value is 0 as defined in swZeroQuantityDisplay_e: " & swBOMFeature.ZeroQuantityDisplay
     Debug.Print "Name of configuration used for BOM table: " & swBOMFeature.Configuration
     Debug.Print "Display as one item? " & swBOMFeature.DisplayAsOneItem
     Debug.Print "Sequence start number: " & swBOMFeature.SequenceStartNumber
     Debug.Print "Keep missing items? " & swBOMFeature.KeepMissingItems
     Debug.Print "  Strikeout missing items? " & swBOMFeature.StrikeoutMissingItems
     Debug.Print "  Replace missing components as defined in swKeepReplacedCompOption_e: " & swBOMFeature.KeepReplacedCompOption
     Debug.Print "Keep current item numbers when reordering rows? " & swBOMFeature.KeepCurrentItemNumbers
    boolstatus = swModelDocExt.SelectByID2("", "EDGE", 0.1205506330468, 0.261655309417, -4.000000000133E-04, False, 0, Nothing, 0)

    Set BomBalloonParams = swModel.Extension.CreateBalloonOptions()
     BomBalloonParams.Style = swBS_Circular
     BomBalloonParams.Size = swBF_2Chars
     BomBalloonParams.UpperTextContent = swBalloonTextItemNumber
     BomBalloonParams.ShowQuantity = True
     BomBalloonParams.QuantityPlacement = swBalloonQuantityPlacement_Right
     BomBalloonParams.QuantityDenotationText = "PLACES"
     BomBalloonParams.QuantityOverride = False
     BomBalloonParams.QuantityOverrideValue = ""
     BomBalloonParams.ItemNumberStart = 1
     BomBalloonParams.ItemNumberIncrement = 1
     BomBalloonParams.ItemOrder = swBalloonItemNumbers_DoNotChangeItemNumbers

    Set swNote = swModelDocExt.InsertBOMBalloon2(BomBalloonParams)

    ' Get whether balloon is a BOM balloon
     ' If so, print the name of the BOM balloon
    If swNote.IsBomBalloon Then
         Debug.Print ("Name of BOM balloon: " & swNote.GetName)
     End If
    swDrawing.ForceRebuild
End Sub
```
