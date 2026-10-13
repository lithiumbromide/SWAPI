---
title: "Insert BOM Table and Stacked Balloon Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_BOM_Table_and_Stacked_Balloon_Example_VB.htm"
---

# Insert BOM Table and Stacked Balloon Example (VBA)

This example shows how to insert a bill of materials table and a stacked balloon annotation in an assembly document.

```vb
 '--------------------------------------------------------------------------------
 ' Preconditions: Open public_documents\samples\tutorial\floxpress\ball valve\ball_valve.sldasm.
 '
 ' Postconditions:
 ' 1. Inserts a parts-only BOM table.
 ' 2. Inserts a stacked balloon annotation.
 ' 3. Inspect the Immediate Window for the name of the configuration used to create
 '    the table and the name of the annotation.
 '
 ' NOTE: Because this document is used elsewhere, do not save any changes.
 '-------------------------------------------------
Option Explicit
Sub main()

    Dim swApp                   As SldWorks.SldWorks
     Dim swModel                 As SldWorks.ModelDoc2
     Dim swModelDocExt           As SldWorks.ModelDocExtension
     Dim swBOMAnnotation         As SldWorks.BomTableAnnotation
     Dim swBOMFeature            As SldWorks.BomFeature
     Dim swNote                  As SldWorks.Note
     Dim StackedBalloonParams    As SldWorks.StackedBalloonOptions
     Dim boolstatus              As Boolean
     Dim BomType                 As Long
     Dim Configuration           As String
     Dim TemplateName            As String
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swModelDocExt = swModel.Extension
    ' Insert BOM table
     TemplateName = "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\bom-standard.sldbomtbt"
     BomType = swBomType_PartsOnly
     Configuration = "Default"
     Set swBOMAnnotation = swModelDocExt.InsertBomTable2(TemplateName, 0.4, 0.3, BomType, Configuration, False)
     Set swBOMFeature = swBOMAnnotation.BomFeature
    ' Print the name of the configuration used for the BOM table
     Debug.Print "Name of configuration used for BOM table: " & swBOMFeature.Configuration
    ' Select a face on which to attach the stacked balloons
     boolstatus = swModelDocExt.SelectByID2("", "FACE", -0.02268677135385, 0.0082159933431, 0.01133567172189, False, 0, Nothing, 0)
    Set StackedBalloonParams = swModel.Extension.CreateStackedBalloonOptions()
     StackedBalloonParams.BalloonsPerLine = 10
     StackedBalloonParams.StackDirection = swStackedBalloonDir_Right
     StackedBalloonParams.Style = swBS_Circular
     StackedBalloonParams.Size = swBF_5Chars
     StackedBalloonParams.UpperTextContent = swBalloonTextItemNumber
     StackedBalloonParams.ShowQuantity = True
     StackedBalloonParams.QuantityPlacement = swBalloonQuantityPlacement_Top
     StackedBalloonParams.QuantityDenotationText = "PLACES"
     StackedBalloonParams.QuantityOverride = False
     StackedBalloonParams.ItemNumberStart = 1
     StackedBalloonParams.ItemNumberIncrement = 1
     StackedBalloonParams.ItemOrder = swBalloonItemNumbers_DoNotChangeItemNumbers

    Set swNote = swModel.Extension.InsertStackedBalloon2(StackedBalloonParams)

    boolstatus = swModel.Extension.SelectByID2("", "FACE", -0.01632926202666, 0.05356671136803, 0.008058200827065, False, 0, Nothing, 0)
     boolstatus = swModel.Extension.SelectByID2("", "FACE", 0.02199792044968, 0.00911087426303, 0.01062976811426, False, 0, Nothing, 0)
     boolstatus = swModel.Extension.SelectByID2("", "FACE", -0.01412287126243, 0.003109265420704, -0.003984592306182, False, 0, Nothing, 0)

    swModel.ViewZoomtofit2
    ' Get whether balloon is a stacked balloon;
     ' If so, print the name of the balloon
    If swNote.IsStackedBalloon Then
         Debug.Print ("Name of stacked balloons: note " & swNote.GetName)
     End If
    swModel.ForceRebuild3 True
 End Sub
```
