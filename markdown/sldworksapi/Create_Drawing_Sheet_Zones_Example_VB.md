---
title: "Create Drawing Sheet Zones Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Drawing_Sheet_Zones_Example_VB.htm"
---

# Create Drawing Sheet Zones Example (VBA)

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
Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swDraw As SldWorks.DrawingDoc
 Dim currentsheet As SldWorks.Sheet
 Dim swModel As SldWorks.ModelDoc2
 Dim revTableAnno As SldWorks.RevisionTableAnnotation
 Dim boolstatus As Boolean
 Dim longstatus As Long, longwarnings As Long
Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\assem20.slddrw", 3, 0, "", longstatus, longwarnings)
     swApp.ActivateDoc2 "assem20 - Sheet1", False, longstatus
     Set swModel = swApp.ActiveDoc
     Set swDraw = swModel

    boolstatus = swModel.Extension.SetUserPreferenceToggle(swUserPreferenceToggle_e.swShowZoneLines, 0, True)
     boolstatus = swModel.Extension.SetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swRevisionTableMultipleSheetStyle, 0, swRevisionTableMultipleSheetStyle_e.swRevisionTable_Independent)

    If (swDraw Is Nothing) Then
         MsgBox " Please open a drawing document. "
         End
     End If

    Set currentsheet = swDraw.GetCurrentSheet
     swDraw.ActivateSheet (currentsheet.GetName)

    ' Create sheet, Test, with 4 zones
     boolstatus = swDraw.NewSheet4("Test", swDwgPaperAsize, swDwgTemplateAsize, 1, 1, True, "", 0, 0, "", 0.5, 0.5, 0.5, 0.5, 2, 2)

    Stop

    boolstatus = swModel.Extension.SelectByID2("Sheet Format2", "SHEET", 0, 0, 0, False, 0, Nothing, 0)
     swModel.EditTemplate
     swModel.EditSketch
     swModel.ClearSelection2 True
     boolstatus = swModel.Extension.SelectByID2("Sheet Format2", "SHEET", 8.12585524728589E-02, 0.139959974668275, 0, False, 0, Nothing, 0)

    ' Modify Test to have 9 zones
     boolstatus = swDraw.SetupSheet6("Test", swDwgPapersUserDefined, swDwgTemplateCustom, 1, 1, True, "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\sheetformat\a - landscape.slddrt", 0.2794, 0.2159, "Default", False, 0.5, 0.5, 0.5, 0.5, 3, 3)

     swModel.EditSheet
     swModel.EditSketch
     swModel.ForceRebuild3 True

    Set currentsheet = swDraw.GetCurrentSheet
     swDraw.ActivateSheet (currentsheet.GetName)

    ' Insert a revision table and add a revision row
     Set revTableAnno = currentsheet.InsertRevisionTable2(True, 0#, 0#, swBOMConfigurationAnchor_TopLeft, "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\English\standard revision block.sldrevtbt", swRevisionTable_CircleSymbol, True)
     Debug.Print "Revision table annotation"
     Debug.Print "  New revision: " & revTableAnno.AddRevision("A")
     Debug.Print "  Current revision: " & revTableAnno.CurrentRevision

    Dim revTableFeat As SldWorks.RevisionTableFeature
     Set revTableFeat = revTableAnno.RevisionTableFeature
     Debug.Print "Revision table feature"
     Debug.Print "  Number of revision table annotations: " & revTableFeat.GetTableAnnotationCount

    Dim feat As SldWorks.Feature
     Set feat = revTableFeat.GetFeature
     Debug.Print "Feature: " & feat.Name

End Sub
```
