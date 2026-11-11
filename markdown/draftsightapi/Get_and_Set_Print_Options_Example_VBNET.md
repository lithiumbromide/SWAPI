---
title: "Get and Set Print Options Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Get_and_Set_Print_Options_Example_VBNET.htm"
---

# Get and Set Print Options Example (VB.NET)

This example shows how to get and set print options and print to a specified device.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1.  Create a VB.NET Windows console project.
 ' 2.  Copy and paste this example into the VB.NET IDE.
 ' 3.  Add a reference to:
 '     install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
 ' 4.  Start DraftSight and open a document that has Sheet1.
  ' 5.  Run the macro to see the available printers in the Immediate window.
 ' 6.  Reset the macro.
 ' 7.  Substitute a valid printer in the PrinterName property. If you specify
 '     PDF, JPG, PNG, or SVG, then you must also provide a full pathname
 '     to print to in IPrintManager::PrintOut at the bottom of this macro.
 ' 8.  Comment out the first Stop.
 ' 9. Save the macro.
  ' 10. Run the macro to see the available paper sizes in the Immediate window.
 ' 11. Reset the macro.
 ' 12. Substitute a valid paper size for the PaperSize property.
 ' 13. Comment out the second Stop.
 ' 14. Save the macro.
  ' 15. Run the macro to see the available print styles in the Immediate window.
 ' 16. Reset the macro.
 ' 17. Substitute a valid print style in the StyleTable property.
 ' 18. Comment out the third Stop.
 ' 19. Save the macro.
 ' 20. Run the macro to completion.
 '
 ' Postconditions: Sheet1 of the open document is printed to the
 ' specified printer on paper of the specified size.
  '----------------------------------------------------------------------------
 Imports DraftSight.Interop.dsAutomation
 Module Module1

     Dim dsDoc As Document
     Sub Main()
         Dim dsApp As Application

         'Connect to DraftSight
         dsApp = GetObject(, "DraftSight.Application")
         'Abort any command currently running in DraftSight
         'to avoid nested commands
         dsApp.AbortRunningCommand()
         'Get active document
         dsDoc = dsApp.GetActiveDocument()
         If Not dsDoc Is Nothing Then
             'Get and set printing options
             GetSetPrintOptions(dsApp)
         End If

     End Sub
     Sub GetSetPrintOptions(dsApp As Application)
         Dim dsPrintMgr As PrintManager
         Dim printerName As String
         Dim dsVarPaperSizes As Object
         Dim dsVarPrinters As Object
         Dim paperLength As Double
         Dim paperWidth As Double
         Dim dsSheet As Sheet
         Dim top As Double
         Dim bottom As Double
         Dim left As Double
         Dim right As Double
         Dim sheetArray(0) As String
         Dim sheetObj As Object

         'Get PrintManager
         dsPrintMgr = dsApp.GetPrintManager
         dsDoc = dsApp.GetActiveDocument
         dsSheet = dsDoc.GetSheet("Sheet1")
         dsSheet.Activate()

         If Not dsPrintMgr Is Nothing Then

             'Get available printers
             dsVarPrinters = dsPrintMgr.GetAvailablePrinters
             Debug.Print("Available printers:")
             Debug.Print(" PDF")
             Debug.Print(" JPG")
             Debug.Print(" PNG")
             Debug.Print(" SVG")
             For i = 0 To UBound(dsVarPrinters)
                 Debug.Print(" " & dsVarPrinters(i))
             Next i

             Stop

             'Set the printer name
             printerName = "JPG"
             dsPrintMgr.Printer = printerName
             If printerName = "" Then
                 MsgBox("Failed to set IPrintManager.Printer property " & printerName & " value.")
             End If

             'Get available paper sizes for printer
             dsVarPaperSizes = dsPrintMgr.AvailablePaperSizes

             If IsArray(dsVarPaperSizes) And UBound(dsVarPaperSizes) = 0 Then
                 MsgBox("List of available paper sizes is empty for " & dsPrintMgr.Printer & " printer.")
             Else
                 Debug.Print("Available paper sizes for " & printerName & ":")
                 For i = 0 To UBound(dsVarPaperSizes)
                     Debug.Print(" " & dsVarPaperSizes(i))
                 Next i
             End If

             Stop

             'Set paper size
             dsPrintMgr.PaperSize = "VGA_(480.00_x_640.00_Pixels)"

             'Get paper size
             dsPrintMgr.GetPaperSize(paperLength, paperWidth)
             Debug.Print("Paper length: " & paperLength)
             Debug.Print("Paper width: " & paperWidth)

             'Get print margins

             dsPrintMgr.GetPrintMargins(top, bottom, left, right)

             Debug.Print("Top margin: " & top)
             Debug.Print("Bottom margin: " & bottom)
             Debug.Print("Left margin: " & left)
             Debug.Print("Right margin: " & right)

             'Set print orientation
             dsPrintMgr.Orientation = dsPrintOrientation_e.dsPrintOrientation_Landscape

             'Set the sheets to print
             sheetArray(0) = "Sheet1"
             dsPrintMgr.SetSheets(sheetArray)
             'Verify the sheets to print
             sheetObj = dsPrintMgr.GetSheets
             If IsNothing(sheetObj) Then
                 MsgBox("Failed to set sheets to print")
             End If
             'Center the printout
             dsPrintMgr.PrintOnCenter = True

             'Set print quality as defined in dsStandardPrintQuality_e
             dsPrintMgr.Quality = dsStandardPrintQuality_e.dsStandardPrintQuality_Normal

             'Scale the line weights
             dsPrintMgr.ScaleLineWeight = True

             'Scale the printout to fit the paper
             dsPrintMgr.ScaleToFit = True

            dsPrintMgr.GetAvailablePrintStyleTables(dsVarPrintStyles)
             Debug.Print("Available print style tables:")
             For i = 0 To UBound(dsVarPrintStyles)
                 Debug.Print(" " & dsVarPrintStyles(i))
             Next i

             Stop

             'Set the print style table
             dsPrintMgr.StyleTable = "default.ctb"

             'Set the printing range
             dsPrintMgr.SetPrintRange(dsPrintRange_e.dsPrintRange_AllGeometry, "", False, 0#, 0#, 0#, 0#)

             'Use the assigned print style
             dsPrintMgr.UseAssignedPrintStyle = True
             dsPrintMgr.PrintOut(1, "c:\temp\printout.jpg") ' If printerName is set to JPG
             'dsPrintMgr.PrintOut (1, "") ' If printerName is a physical device

             dsSheet.Activate()

         Else
             MsgBox("IDocument.GetPrintManager returns Nothing.")
         End If
     End Sub

 End Module
```
