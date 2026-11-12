---
title: "Get Labels of Datum Origin Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Labels_of_Datum_Origin_Example_VB.htm"
---

# Get Labels of Datum Origin Example (VBA)

This example shows how to insert a hole table annotation and get some of its properties.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Verify that the specified files exist:
 '    * part document
 '    * drawing document template
 '    * hole table template
 ' 2. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Opens the specified part document.
 ' 2. Creates a drawing of the part document.
 ' 3. Inserts a hole table annotation at the specified vertex.
 ' 4. Prints to the Immediate window:
 '    * the hole table's datum origin x and y labels
 '    * whether to display hole sizes using ANSI inch letters
 '      and drill numbers
 ' 5. Examine the Immediate window and drawing.
 '
  ' NOTE: Because the model is used elsewhere, do not save changes.
 '----------------------------------------------------------------------------
 Option Explicit
 Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swDrawingDoc As SldWorks.DrawingDoc
 Dim swView As SldWorks.View
 Dim swModelView As SldWorks.ModelView
 Dim swModelDocExt As SldWorks.ModelDocExtension
 Dim swSelectionMgr As SldWorks.SelectionMgr
 Dim swHoleTableAnnotation As SldWorks.HoleTableAnnotation
 Dim swHoleTable As SldWorks.HoleTable
 Dim swDatumOrigin As SldWorks.DatumOrigin
 Dim fileName As String
 Dim drawingDocTemplate As String
 Dim holeTableTemplate As String
 Dim status As Boolean
 Dim errors As Long
 Dim warnings As Long
 Sub main()
     Set swApp = Application.SldWorks
     'Open part document and create drawing document
     fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\tolanalyst\minimum_clearance\top_plate.sldprt"
     Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
     drawingDocTemplate = "C:\ProgramData\SolidWorks\SolidWorks 2016\templates\Drawing.drwdot"
     Set swDrawingDoc = swApp.NewDocument(drawingDocTemplate, swDwgPaperSizes_e.swDwgPaperBsize, 0.2794, 0.4318)
     Set swView = swDrawingDoc.CreateDrawViewFromModelView3(fileName, "*Front", 0.193046827497194, 0.155595183164983, 0)
     'Insert hole table annotation
     Set swModel = swApp.ActiveDoc
     Set swDrawingDoc = swModel
     Set swModelView = swModel.ActiveView
     Set swModelDocExt = swModel.Extension
     status = swDrawingDoc.ActivateView("Drawing View1")
     status = swModelDocExt.SelectByID2("", "VERTEX", 0.216278249046016, 0.198389907070707, 8.0000000000382E-03, False, 0, Nothing, 0)
     status = swModelDocExt.SelectByID2("", "FACE", 0.228097744219978, 0.151927063973064, 4.0000000000191E-03, False, 0, Nothing, 0)
     swModel.ClearSelection2 True
     status = swModelDocExt.SelectByID2("", "VERTEX", 0.216278249046016, 0.198389907070707, 8.0000000000382E-03, True, 1, Nothing, 0)
     status = swModelDocExt.SelectByID2("", "FACE", 0.228097744219978, 0.151927063973064, 4.0000000000191E-03, True, 2, Nothing, 0)
     Set swSelectionMgr = swModel.SelectionManager
     Set swView = swSelectionMgr.GetSelectedObjectsDrawingView2(1, -1)
     holeTableTemplate = "C:\Program Files\SolidWorks Corp\SolidWorks\lang\english\standard hole table--letters.sldholtbt"
     Set swHoleTableAnnotation = swView.InsertHoleTable2(False, 5.40658670033671E-02, 0.253819263748597, 1, "A", holeTableTemplate)
     swModel.ClearSelection2 True
     'Get hole table and its datum origin
     Set swHoleTable = swHoleTableAnnotation.HoleTable
     Set swDatumOrigin = swHoleTable.DatumOrigin
     'Get datum origin's x and y labels
     Debug.Print "Datum origin:"
     Debug.Print ("  X label: " & swDatumOrigin.XLabel)
     Debug.Print ("  Y label: " & swDatumOrigin.YLabel)
     'Get whether to display hole sizes using ANSI inch letters and drill numbers
     Debug.Print "Display ANSI inch letter and drill number sizes in hole table? " & swHoleTable.ShowANSIInchLetterNumberDrillSizes

End Sub
```
