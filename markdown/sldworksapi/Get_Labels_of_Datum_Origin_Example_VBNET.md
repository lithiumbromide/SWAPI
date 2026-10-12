---
title: "Get Labels of Datum Origin Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Labels_of_Datum_Origin_Example_VBNET.htm"
---

# Get Labels of Datum Origin Example (VB.NET)

This example shows how to insert a hole table annotation and get some of its properties.

```vb
  '---------------------------------------------------------------------------
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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim swDrawingDoc As DrawingDoc
     Dim swView As View
     Dim swModelView As ModelView
     Dim swModelDocExt As ModelDocExtension
     Dim swSelectionMgr As SelectionMgr
     Dim swHoleTableAnnotation As HoleTableAnnotation
     Dim swHoleTable As HoleTable
     Dim swDatumOrigin As DatumOrigin
     Dim fileName As String
     Dim drawingDocTemplate As String
     Dim holeTableTemplate As String
     Dim status As Boolean
     Dim errors As Integer
     Dim warnings As Integer

     Sub main()

         'Open part document and create drawing document
         fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\tolanalyst\minimum_clearance\top_plate.sldprt"
         swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
         drawingDocTemplate = "C:\ProgramData\SolidWorks\SolidWorks 2016\templates\Drawing.drwdot"
         swDrawingDoc = swApp.NewDocument(drawingDocTemplate, swDwgPaperSizes_e.swDwgPaperBsize, 0.2794, 0.4318)
         swView = swDrawingDoc.CreateDrawViewFromModelView3(fileName, "*Front", 0.193046827497194, 0.155595183164983, 0)

         'Insert hole table annotation
         swModel = swApp.ActiveDoc
         swDrawingDoc = swModel
         swModelView = swModel.ActiveView
         swModelDocExt = swModel.Extension
         status = swDrawingDoc.ActivateView("Drawing View1")
         status = swModelDocExt.SelectByID2("", "VERTEX", 0.216278249046016, 0.198389907070707, 0.0080000000000382, False, 0, Nothing, 0)
         status = swModelDocExt.SelectByID2("", "FACE", 0.228097744219978, 0.151927063973064, 0.0040000000000191, False, 0, Nothing, 0)
         swModel.ClearSelection2(True)
         status = swModelDocExt.SelectByID2("", "VERTEX", 0.216278249046016, 0.198389907070707, 0.0080000000000382, True, 1, Nothing, 0)
         status = swModelDocExt.SelectByID2("", "FACE", 0.228097744219978, 0.151927063973064, 0.0040000000000191, True, 2, Nothing, 0)
         swSelectionMgr = swModel.SelectionManager
         swView = swSelectionMgr.GetSelectedObjectsDrawingView2(1, -1)
         holeTableTemplate = "C:\Program Files\SolidWorks Corp\SolidWorks\lang\english\standard hole table--letters.sldholtbt"
         swHoleTableAnnotation = swView.InsertHoleTable2(False, 0.0540658670033671, 0.253819263748597, 1, "A", holeTableTemplate)
         swModel.ClearSelection2(True)

         'Get hole table and its datum origin
         swHoleTable = swHoleTableAnnotation.HoleTable
         swDatumOrigin = swHoleTable.DatumOrigin

         'Get datum origin's x and y labels
         Debug.Print("Datum origin:")
         Debug.Print("  X label: " & swDatumOrigin.XLabel)
         Debug.Print("  Y label: " & swDatumOrigin.YLabel)

         'Get whether to display hole sizes using ANSI inch letters and drill numbers
         Debug.Print("Display ANSI inch letter and drill number sizes in the hole table? " & swHoleTable.ShowANSIInchLetterNumberDrillSizes)

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
