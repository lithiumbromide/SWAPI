---
title: "Insert and Show BOM Table in Assembly Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_and_Show_BOM_Table_in_Assembly_Example_VB.htm"
---

# Insert and Show BOM Table in Assembly Example (VBA)

This example shows how to insert and show a BOM table in an assembly document.

```vb
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
Option Explicit

Sub main()

    Dim swApp                   As SldWorks.SldWorks
    Dim swModel                 As SldWorks.ModelDoc2
    Dim swModelDocExt           As SldWorks.ModelDocExtension
    Dim swBOMAnnotation         As SldWorks.BomTableAnnotation
    Dim swBOMFeature            As SldWorks.BomFeature
    Dim swNote                  As SldWorks.Note
    Dim boolstatus              As Boolean
    Dim BomType                 As Long
    Dim Configuration           As String
    Dim TemplateName            As String
    Dim nErrors                 As Long
    Dim nWarnings               As Long

    Set swApp = Application.SldWorks

   ' Open assembly document
    Set swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\arm2.sldasm", swDocASSEMBLY, swOpenDocOptions_Silent, "", nErrors, nWarnings)
    Set swModelDocExt = swModel.Extension

    ' Insert BOM table
    TemplateName = "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\bom-standard.sldbomtbt"
    BomType = swBomType_Indented
    Configuration = "Default"
    Set swBOMAnnotation = swModelDocExt.InsertBomTable4(TemplateName, 0, 1, BomType, Configuration, False, swNumberingType_Detailed, True, True)
    Set swBOMFeature = swBOMAnnotation.BomFeature

    ' Print the name of the configuration used for the BOM table
    Debug.Print "Name of configuration used for BOM table: " & swBOMFeature.Configuration

    ' Insert BOM balloon for the selected face, which
    ' belongs to the part Side
    boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.091853347996107, -1.04709589619745E-02, 1.74830255600256E-03, False, 0, Nothing, 0)

    Dim StackedBalloonParams as SldWorks.StackedBalloonOptions
    Set StackedBalloonParams = swModelDocExt.CreateStackedBalloonOptions()
     StackedBalloonParams.BalloonsPerLine = 10
     StackedBalloonParams.StackDirection = swStackedBalloonDir_Right
     StackedBalloonParams.Style = swBS_SplitCirc
     StackedBalloonParams.Size = swBF_Tightest
     StackedBalloonParams.UpperTextContent = swBalloonTextItemNumber
     StackedBalloonParams.LowerTextContent = swBalloonTextCustom
     StackedBalloonParams.LowerText = "Lower text"
     StackedBalloonParams.ShowQuantity = True
     StackedBalloonParams.QuantityPlacement = swBalloonQuantityPlacement_Top
     StackedBalloonParams.QuantityDenotationText = "PLACES"
     StackedBalloonParams.QuantityOverride = False
     StackedBalloonParams.ItemNumberStart = 1
     StackedBalloonParams.ItemNumberIncrement = 1
     StackedBalloonParams.ItemOrder = swBalloonItemNumbers_DoNotChangeItemNumbers

    Set swNote = swModelDocExt.InsertStackedBalloon2(StackedBalloonParams)
    swModel.ViewZoomtofit2
    ' Get whether balloon is a stacked balloon;
    ' if so, print the name of the balloon
    If swNote.IsStackedBalloon Then
        Debug.Print ("Name of stacked balloon: " & swNote.GetName)
    End If

End Sub
```
