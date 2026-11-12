---
title: "Create Drawing Sheet Zones Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Drawing_Sheet_Zones_Example_VBNET.htm"
---

# Create Drawing Sheet Zones Example (VB.NET)

This example shows how to create a drawing sheet with zones, modify the zones in the drawing sheet, and insert a revision table.

```vb
  '-----------------------------------------------------------------------------
 ' Preconditions:
  ' 1. Verify that the specified model document and templates exist.
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Creates a new sheet named Test with four zones.
 ' 2. Inspect the graphics area.
 ' 3. Press F5.
 ' 4. Modifies Test to contain nine zones.
 ' 5. Creates Revision Table1.
 ' 6. Adds a revision row to the table.
 ' 7. Inspect the FeatureManager design tree, the graphics area, and the
 '    Immediate window.
 '
  ' NOTE: Because the model is used elsewhere, do not save changes to it.
  '---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swDraw As DrawingDoc
     Dim currentsheet As Sheet
     Dim swModel As ModelDoc2
     Dim revTableAnno As RevisionTableAnnotation
     Dim boolstatus As Boolean
     Dim longstatus As Integer, longwarnings As Integer

     Sub main()

         swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\assem20.slddrw", 3, 0, "", longstatus, longwarnings)
         swApp.ActivateDoc2("assem20 - Sheet1", False, longstatus)
         swModel = swApp.ActiveDoc
         swDraw = swModel

         boolstatus = swModel.Extension.SetUserPreferenceToggle(swUserPreferenceToggle_e.swShowZoneLines, 0, True)
         boolstatus = swModel.Extension.SetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swRevisionTableMultipleSheetStyle, 0, swRevisionTableMultipleSheetStyle_e.swRevisionTable_Independent)

         If (swDraw Is Nothing) Then
             MsgBox(" Please open a drawing document. ")
         End If

         currentsheet = swDraw.GetCurrentSheet
         swDraw.ActivateSheet(currentsheet.GetName)

         ' Create sheet, Test, with 4 zones
         boolstatus = swDraw.NewSheet4("Test", swDwgPaperSizes_e.swDwgPaperAsize, swDwgTemplates_e.swDwgTemplateAsize, 1, 1, True, "", 0, 0, "", 0.5, 0.5, 0.5, 0.5, 2, 2)

         Stop

         boolstatus = swModel.Extension.SelectByID2("Sheet Format2", "SHEET", 0, 0, 0, False, 0, Nothing, 0)
         swModel.EditTemplate()
         swModel.EditSketch()
         swModel.ClearSelection2(True)
         boolstatus = swModel.Extension.SelectByID2("Sheet Format2", "SHEET", 0.0812585524728589, 0.139959974668275, 0, False, 0, Nothing, 0)

         ' Modify Test to have 9 zones
         boolstatus = swDraw.SetupSheet6("Test", swDwgPaperSizes_e.swDwgPapersUserDefined, swDwgTemplates_e.swDwgTemplateCustom, 1, 1, True, "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\sheetformat\a - landscape.slddrt", 0.2794, 0.2159, "Default", False, 0.5, 0.5, 0.5, 0.5, 3, 3)

         swModel.EditSheet()
         swModel.EditSketch()
         swModel.ForceRebuild3(True)

         currentsheet = swDraw.GetCurrentSheet
         swDraw.ActivateSheet(currentsheet.GetName)

         ' Insert a revision table and add a revision row
         revTableAnno = currentsheet.InsertRevisionTable2(True, 0.0#, 0.0#, swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_TopLeft, "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\English\standard revision block.sldrevtbt", swRevisionTableSymbolShape_e.swRevisionTable_CircleSymbol, True)
         Debug.Print("Revision table annotation")
         Debug.Print("  New revision: " & revTableAnno.AddRevision("A"))
         Debug.Print("  Current revision: " & revTableAnno.CurrentRevision)

         Dim revTableFeat As RevisionTableFeature
         revTableFeat = revTableAnno.RevisionTableFeature
         Debug.Print("Revision table feature")
         Debug.Print("  Number of revision table annotations: " & revTableFeat.GetTableAnnotationCount)

         Dim feat As Feature
         feat = revTableFeat.GetFeature
         Debug.Print("Feature: " & feat.Name)

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
