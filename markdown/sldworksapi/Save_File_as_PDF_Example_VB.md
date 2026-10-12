---
title: "Save File as PDF Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Save_File_as_PDF_Example_VB.htm"
---

# Save File as PDF Example (VBA)

This example shows how to export the specified sheet in a drawing document to a PDF file.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Verify that the specified drawing document to open exists.
 ' 2. Verify that c:\test, the folder where to save
 '    the PDF file, exists. If it does not exist,
 '    create it or change the path to a folder that
 '    exists on your system.
 '
 ' Postconditions:
 ' 1. Opens the specified drawing document.
 ' 2. Saves all but the last drawing sheet to an array.
 ' 3. Saves the array of drawing sheets to a PDF file
 '    called foodprocessor.pdf.
 ' 4. Opens foodprocessor.pdf.
 '----------------------------------------------------------------------------
Option Explicit
    Dim swApp               As SldWorks.SldWorks
     Dim swModel             As SldWorks.ModelDoc2
     Dim swModelDocExt       As SldWorks.ModelDocExtension
     Dim swExportPDFData     As SldWorks.ExportPdfData
     Dim boolstatus          As Boolean
     Dim filename            As String
     Dim lErrors             As Long
     Dim lWarnings           As Long
     Dim strSheetName(4)     As String
     Dim varSheetName        As Variant
Sub main()
    ' Path to which to save PDF file of drawing
     filename = "C:\test\foodprocessor.PDF"
    Set swApp = Application.SldWorks
     swApp.Visible = True
    ' Open specified drawing
     Set swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\foodprocessor.slddrw", swDocDRAWING, swOpenDocOptions_Silent, "", lErrors, lWarnings)
     Set swModelDocExt = swModel.Extension
     Set swExportPDFData = swApp.GetExportFileData(1)
    ' Names of the sheets
     strSheetName(0) = "Sheet1"
     strSheetName(1) = "Sheet2"
     strSheetName(2) = "Sheet3"
     ' strSheetName(3) = "Sheet4"
    varSheetName = strSheetName
    If swExportPDFData Is Nothing Then MsgBox "Nothing"
     boolstatus = swExportPDFData.SetSheets(swExportData_ExportSpecifiedSheets, varSheetName)
     swExportPDFData.ViewPdfAfterSaving = True
    boolstatus = swModelDocExt.SaveAs(filename, 0, 0, swExportPDFData, lErrors, lWarnings)

End Sub
```
