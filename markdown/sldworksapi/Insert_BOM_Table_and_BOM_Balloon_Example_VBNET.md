---
title: "Insert BOM Table and BOM Balloon Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_BOM_Table_and_BOM_Balloon_Example_VBNET.htm"
---

# Insert BOM Table and BOM Balloon Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swDrawing As DrawingDoc
        Dim swView As View
        Dim swBOMAnnotation As BomTableAnnotation
        Dim swBOMFeature As BomFeature
        Dim swNote As Note
        Dim boolstatus As Boolean
        Dim AnchorType As Integer
        Dim BomType As Integer
        Dim Configuration As String
        Dim TableTemplate As String

        swModel = swApp.ActiveDoc
        swDrawing = swModel
        swModelDocExt = swModel.Extension
        boolstatus = swDrawing.ActivateView("Drawing View1")
        swView = swDrawing.ActiveDrawingView

        ' Insert parts-only BOM table
        AnchorType = swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_TopLeft
        BomType = swBomType_e.swBomType_PartsOnly
        Configuration = ""
  TableTemplate = "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\bom-standard.sldbomtbt"
        swBOMAnnotation = swView.InsertBomTable2(False, 0.4, 0.3, AnchorType, BomType, Configuration, TableTemplate)
        swBOMFeature = swBOMAnnotation.BomFeature

        ' Print the name of the configuration used for the BOM table
        Debug.Print("Name of configuration used for BOM table: " & swBOMFeature.Configuration)

        ' Insert BOM balloon for the selected edge
        boolstatus = swModelDocExt.SelectByID2("", "EDGE", 0.1205506330468, 0.261655309417, -0.0004000000000133, False, 0, Nothing, 0)
        swNote = swModelDocExt.InsertBOMBalloon(swBalloonStyle_e.swBS_SplitCirc, swBalloonFit_e.swBF_Tightest, swBalloonTextContent_e.swBalloonTextItemNumber, "", swBalloonTextContent_e.swBalloonTextCustom, "Lower text", swBalloonFit_e.swBF_UserDef, True, 2, "Denotation Text")

        ' Get whether balloon is a BOM balloon;
        ' if so, print the name of the BOM balloon
        If swNote.IsBomBalloon Then
            Debug.Print("Name of BOM balloon: " & swNote.GetName)
        End If

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
