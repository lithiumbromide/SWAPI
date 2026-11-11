---
title: "Save Current View to PDF Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Save_Current_View_to_PDF_Example_VBNET.htm"
---

# Save Current View to PDF Example (VB.NET)

This example shows how to export the current view of the drawing to a PDF file.

```vb
  '-------------------------------------------------------------
 ' Preconditions:
 ' 1. Create a VB.NET Windows console project.
 ' 2. Copy and paste this project into the VB.NET IDE.
 ' 3. Add a reference to
 '    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
 ' 4. Open the Immediate window.
 ' 5. Start DraftSight.
 ' 6.   Open c:\ProgramData\Dassault Systemes\DraftSight\Examples\B-44563.DWG.
 ' 7. Click Start Debugging.
 '
 ' Postconditions:
 ' 1. Specified document is opened.
  ' 2. The current view of the drawing is exported to a PDF file.
  '------------------------------------------------------------

 Imports System.IO
 Imports DraftSight.Interop.dsAutomation
 Module Module1

     Sub main()
         Dim dsApp As Application
         'Connect to DraftSight application
         dsApp = CreateObject("DraftSight.Application")
         'Abort any command currently running in DraftSight
         'to avoid nested commands
         dsApp.AbortRunningCommand
         'Get active document
         Dim dsDoc As Document
         'Dim docName As String
         'docName = "c:\ProgramData\Dassault Systemes\DraftSight\Examples\B-44563.DWG"
         'dsDoc = dsApp.OpenDocument2(docName, dsDocumentOpenOption_e.dsDocumentOpen_Default, dsEncoding_e.dsEncoding_Default)
         dsDoc = dsApp.GetActiveDocument
        If dsDoc Is Nothing Then
             MsgBox("Specified document did not open. Check path and file name.")
             Return
         End If
         'Export current view of drawing to a PDF
         Dim dsExportDocument As DocumentExporter
         Dim exportFileName As String
         Dim ExportSettings As ExportSettings
         Dim status As Boolean
         dsExportDocument = dsDoc.GetDocumentExporter()
         ExportSettings = dsExportDocument.CreateExportSettings

         'Export all sheets
        Dim sheetsList As Object() = CType(dsDoc.GetSheets2(), Object())
        Dim sheetArray As String() = New String(sheetsList.Length - 1) {}
        Dim j As Integer = 0

        For i As Integer = 0 To sheetsList.Length - 1
            Dim sheet As Sheet = CType(sheetsList(i), Sheet)
            sheetArray(j) = sheet.Name
            j += 1
        Next

         ExportSettings.Sheets = sheetArray
         ExportSettings.SetPrintMargins(30, 30, 30, 30)
         ExportSettings.PrintStyleTable = "monochrome.ctb"
         ExportSettings.EnableCustomBitmapResolution = True
         ExportSettings.CustomBitmapResolution = 151
         ExportSettings.EnableLayersInPDFFile = True
         ExportSettings.TrueTypeFontsType = dsTrueTypeFontsType_e.dsTrueTypeFontsType_Embedded

         Dim paperSizes As String() = Nothing
         ExportSettings.GetAvailablePaperSizes(paperSizes)
        ExportSettings.PaperSize = paperSizes(0)
         Dim top As Double, bottom As Double, left As Double, right As Double
         ExportSettings.GetPrintMargins(top, bottom, left, right)
         Debug.Print("Enable custom bitmap resolution? " & ExportSettings.EnableCustomBitmapResolution)
         Debug.Print("  Custom bitmap resolution: " & ExportSettings.CustomBitmapResolution)
         Debug.Print("Enable Layers in PDF file? " & ExportSettings.EnableLayersInPDFFile)
         Debug.Print("PrintStyle table: " & ExportSettings.PrintStyleTable)
         Debug.Print("TrueType font as defined in dsTrueTypeFontsType_e: " & ExportSettings.TrueTypeFontsType)

        exportFileName = "C:\temp\B-44563.PDF"
        status = dsExportDocument.ExportToPdf2(exportFileName, ExportSettings)
        Debug.Print("")
        If status Then
            Debug.Print("Drawing exported as " & exportFileName & ".")
        Else
            Debug.Print("Export of drawing to PDF failed!")
        End If
    End Sub

 End Module
```
