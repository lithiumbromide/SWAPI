---
title: "Save Current View to PDF Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Save_Current_View_to_PDF_Example_VBA.htm"
---

# Save Current View to PDF Example (VBA)

This example shows how to export the current view of the drawing to a PDF file.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to the DraftSight type library,
'    install_dir\bin\dsAutomation.dll.
' 4. Open the Immediate window.
' 5. Start DraftSight.
' 6. Ensure the specified document to open exists.
' 7. Run the macro.
'
' Postconditions:
' 1. Specified document is opened.
' 2. The current view of the drawing is exported to the specified PDF file.
'---------------------------------------------------------------------------
Option Explicit
```

```vb
Sub main()
         Dim dsApp As DraftSight.Application
         'Connect to DraftSight application
         Set dsApp = GetObject(, "DraftSight.Application")
         'Abort any command currently running in DraftSight
         'to avoid nested commands
         dsApp.AbortRunningCommand
         'Open document
         Dim dsDoc As DraftSight.Document
         Dim docName As String
         docName = "c:\ProgramData\Dassault Systemes\DraftSight\Examples\B-44563.DWG"
         Set dsDoc = dsApp.OpenDocument2(docName, dsDocumentOpenOption_e.dsDocumentOpen_Default, dsEncoding_e.dsEncoding_Default)
         If dsDoc Is Nothing Then
             MsgBox ("Specified document did not open. Check path and file name.")
             Return
         End If
         'Export current view of drawing to a PDF
         Dim dsExportDocument As DraftSight.DocumentExporter
         Dim exportFileName As String
         Dim ExportSettings As DraftSight.ExportSettings
         Dim status As Boolean

         'Export all sheets
        Dim sheetsList As Variant
        sheetsList = dsDoc.GetSheets2()
        ReDim sheetArray(UBound(sheetsList)) As String
        Dim i As Long
        Dim sheet As DraftSight.sheet
        For i = 0 To UBound(sheetsList)
            Set sheet = sheetsList(i)
            sheetArray(i) = sheet.Name
        Next

         Set dsExportDocument = dsDoc.GetDocumentExporter()
         Set ExportSettings = dsExportDocument.CreateExportSettings

         ExportSettings.Sheets = sheetArray
         ExportSettings.SetPrintMargins 30, 30, 30, 30
         ExportSettings.PrintStyleTable = "monochrome.ctb"
         ExportSettings.EnableCustomBitmapResolution = True
         ExportSettings.CustomBitmapResolution = 151
         ExportSettings.EnableLayersInPDFFile = True
         ExportSettings.TrueTypeFontsType = dsTrueTypeFontsType_e.dsTrueTypeFontsType_Embedded

         Dim paperSizes(0) As String
         ExportSettings.GetAvailablePaperSizes (paperSizes)
        ExportSettings.PaperSize = paperSizes(0)
         Dim top As Double, bottom As Double, left As Double, right As Double
         ExportSettings.GetPrintMargins top, bottom, left, right
         Debug.Print "Enable custom bitmap resolution? " & ExportSettings.EnableCustomBitmapResolution
         Debug.Print "  Custom bitmap resolution: " & ExportSettings.CustomBitmapResolution
         Debug.Print "Enable Layers in PDF file? " & ExportSettings.EnableLayersInPDFFile
         Debug.Print "PrintStyle table: " & ExportSettings.PrintStyleTable
         Debug.Print "TrueType font as defined in dsTrueTypeFontsType_e: " & ExportSettings.TrueTypeFontsType

        exportFileName = "C:\temp\B-44563.PDF"
         status = dsExportDocument.ExportToPdf2(exportFileName, ExportSettings)
         Debug.Print ""
         If status Then
             Debug.Print "Drawing exported as " & exportFileName & "."
         Else
             Debug.Print "Export of drawing to PDF failed!"
         End If
 End Sub
```
