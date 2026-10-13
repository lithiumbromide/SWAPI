---
title: "Insert BOM Table and BOM Balloon Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_BOM_Table_and_BOM_Balloon_Example_VB.htm"
---

# Insert BOM Table and BOM Balloon Example (VBA)

## Insert BOM Table and BOM Balloon (VBA)

This example shows how to insert a BOM table and a BOM balloon in a drawing document.

```
'------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\advdrawings\foodprocessor.slddrw.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Inserts a parts-only BOM table.
' 2. Inserts a split-circle BOM balloon, which uses the BOM
'    table item number for its upper text,
'    to the selected edge.
' 3. Zoom to area and examine both the BOM table and BOM
'    balloon to verify.
'
' NOTE: Because this drawing document is used elsewhere,
' do not save any changes.
'-------------------------------------------------
```

```vb
Option Explicit

Sub main()

    Dim swApp                   As SldWorks.SldWorks
    Dim swModel                 As SldWorks.ModelDoc2
    Dim swModelDocExt           As SldWorks.ModelDocExtension
    Dim swDrawing               As SldWorks.DrawingDoc
    Dim swView                  As SldWorks.View
    Dim swBOMAnnotation         As SldWorks.BomTableAnnotation
    Dim swBOMFeature            As SldWorks.BomFeature
    Dim swNote                  As SldWorks.Note
    Dim boolstatus              As Boolean
    Dim AnchorType              As Long
    Dim BomType                 As Long
    Dim Configuration           As String
    Dim TableTemplate           As String

    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swDrawing = swModel
    Set swModelDocExt = swModel.Extension
    boolstatus = swDrawing.ActivateView("Drawing View1")
    Set swView = swDrawing.ActiveDrawingView

    ' Insert parts-only BOM table
    AnchorType = swBOMConfigurationAnchor_TopLeft
    BomType = swBomType_PartsOnly
    Configuration = ""
    TableTemplate = "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\bom-standard.sldbomtbt"
    Set swBOMAnnotation = swView.InsertBomTable2(False, 0.4, 0.3, AnchorType, BomType, Configuration, TableTemplate)
    Set swBOMFeature = swBOMAnnotation.BomFeature

    ' Print the name of the configuration used for the BOM table
    Debug.Print "Name of configuration used for BOM table: " & swBOMFeature.Configuration

    ' Insert BOM balloon for the selected edge
    boolstatus = swModelDocExt.SelectByID2("", "EDGE", 0.1205506330468, 0.261655309417, -4.000000000133E-04, False, 0, Nothing, 0)
    Set swNote = swModelDocExt.InsertBOMBalloon(swBS_SplitCirc, swBF_Tightest, swBalloonTextItemNumber, "", swBalloonTextCustom, "Lower text", swBF_UserDef, True, 2, "Denotation Text")

    ' Get whether balloon is a BOM balloon;
    ' if so, print the name of the BOM balloon
    If swNote.IsBomBalloon Then
        Debug.Print ("Name of BOM balloon: " & swNote.GetName)
    End If

End Sub
```
