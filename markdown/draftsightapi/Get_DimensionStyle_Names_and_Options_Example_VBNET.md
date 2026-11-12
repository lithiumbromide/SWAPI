---
title: "Get DimensionStyle Names and Options Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Get_DimensionStyle_Names_and_Options_Example_VBNET.htm"
---

# Get DimensionStyle Names and Options Example (VB.NET)

This example shows how to get the names and options of the DimensionStyles in a document and how to export the current view of the drawing to a PNG file.

```vb
  '-------------------------------------------------------------
 ' Preconditions:
 ' 1. Create a VB.NET Windows console project.
 ' 2. Copy and paste this project into the VB.NET IDE.
 ' 3. Add a reference to
 '    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dllb.
 ' 4. Open the Immediate window.
 ' 5. Start DraftSight.
 ' 6. Click Start Debugging.
 '
 ' Postconditions:
 ' 1. Specified document is opened.
  ' 2. The document's DimensionStyle names and options are printed to
 '    the Immediate window.
  ' 3. The current view of the drawing is exported to a PNG file.
 ' 4. To verify step 3, open
 '    C:\ProgramData\Dassault Systemes\DraftSight\Examples\B-44563.PNG
 '    using an application like Microsoft Paint.
  '------------------------------------------------------------

 Imports System.IO
 Imports DraftSight.Interop.dsAutomation

 Module Module1

     Dim dsApp As DraftSight.Interop.dsAutomation.Application

     Sub Main()

         'Connect to DraftSight application
         dsApp = GetObject(, "DraftSight.Application")
         'Abort any command currently running in DraftSight
         'to avoid nested commands
         dsApp.AbortRunningCommand()

         'Open document
         Dim dsDoc As Document
         Dim docName As String
         docName = "C:\ProgramData\Dassault Systemes\DraftSight\Examples\B-44563.DWG"
         dsDoc = dsApp.OpenDocument2(docName, dsDocumentOpenOption_e.dsDocumentOpen_Default, dsEncoding_e.dsEncoding_Default)
         If dsDoc Is Nothing Then
             Debug.Print("Specified document did not open. Check path and file name.")
             Return
         End If

         'Get DimensionStyle manager
         Dim dsDimStyleManager As DimensionStyleManager
         dsDimStyleManager = dsDoc.GetDimensionStyleManager()

         'Get DimensionStyles and options for document
         Dim dsDimensionStyles As Object
         dsDimensionStyles = dsDimStyleManager.GetDimensionStyles()
         Dim index As Long
         If IsArray(dsDimensionStyles) Then
             For index = 0 To UBound(dsDimensionStyles) - 1
                 Dim dsDimensionStyle As Object
                 dsDimensionStyle = dsDimensionStyles(index)
                 Debug.Print("")
                 Debug.Print("Name of DimensionStyle: " & dsDimensionStyle.Name)
                 'Print DimensionStyle's options
                 PrintDimensionStyleOptions(dsDimensionStyle)
             Next
         End If

         'Export current view of drawing to PNG
         Dim dsExportDocument As DocumentExporter
         Dim exportFileName As String
         Dim status As Boolean
         dsExportDocument = dsDoc.GetDocumentExporter()
         exportFileName = "C:\ProgramData\Dassault Systemes\DraftSight\Examples\B-44563.PNG"
         dsExportDocument.ExportToPng(exportFileName, status)
         Debug.Print("")
         If status Then
             Debug.Print("Drawing exported as " & exportFileName & ".")
         Else
             Debug.Print("Export of drawing to PNG failed!")
         End If
     End Sub

     Sub PrintDimensionStyleOptions(ByRef dsDimensionStyle As DimensionStyle)
         'Angular DimensionStyle options
         Dim dsDimensionStyleAngularDimensionOptions As DimensionStyleAngularDimensionOptions
         dsDimensionStyleAngularDimensionOptions = dsDimensionStyle.GetDimensionStyleAngularDimensionOptions()
         Debug.Print("  Angular DimensionStyle options:  ")
         Debug.Print("    Precision: " & dsDimensionStyleAngularDimensionOptions.Precision)
         Debug.Print("    Format: " & dsDimensionStyleAngularDimensionOptions.Format)
         Debug.Print("    Hide leading zeroes: " & dsDimensionStyleAngularDimensionOptions.HideLeadingZeroes)
         Debug.Print("    Hide trailing zeroes: " & dsDimensionStyleAngularDimensionOptions.HideTrailingZeroes)

         'Dual DimensionStyle options
         Dim dsDimensionStyleDualDimensionOptions As DimensionStyleDualDimensionOptions
         dsDimensionStyleDualDimensionOptions = dsDimensionStyle.GetDimensionStyleDualDimensionOptions()
         Debug.Print("  Dual DimensionStyle options:  ")
         Debug.Print("    Precision: " & dsDimensionStyleDualDimensionOptions.Precision)
         Debug.Print("    Format: " & dsDimensionStyleDualDimensionOptions.Format)
         Debug.Print("    Hide leading zeroes: " & dsDimensionStyleDualDimensionOptions.HideLeadingZeroes)
         Debug.Print("    Hide trailing zeroes: " & dsDimensionStyleDualDimensionOptions.HideTrailingZeroes)
         'Fit DimensionStyle options

         Dim dsDimensionStyleFitOptions As DimensionStyleFitOptions
         dsDimensionStyleFitOptions = dsDimensionStyle.GetDimensionStyleFitOptions()
         Debug.Print("  Fit DimensionStyle options:  ")
         Debug.Print("    Placement of text: " & dsDimensionStyleFitOptions.FitDimensionText)
         Debug.Print("    Entity to move outside Dimension's extension lines: " & dsDimensionStyleFitOptions.FitGeometry)
         Debug.Print("    Hide arrows: " & dsDimensionStyleFitOptions.HideArrows)
         Dim dimensionScale As dsDimensionScale_e
         Dim scaleFactor As Double
         dsDimensionStyleFitOptions.GetDimensionScale(dimensionScale, scaleFactor)
         Debug.Print("    Scale factor: " & scaleFactor)

         'Linear DimensionStyle options
         Dim dsDimensionStyleLinearDimensionOptions As DimensionStyleLinearDimensionOptions
         dsDimensionStyleLinearDimensionOptions = dsDimensionStyle.GetDimensionStyleLinearDimensionOptions()
         Debug.Print("  Linear DimensionStyle options:  ")
         Debug.Print("    Precision: " & dsDimensionStyleLinearDimensionOptions.Precision)
         Debug.Print("    Format: " & dsDimensionStyleLinearDimensionOptions.Format)
         Debug.Print("    Hide leading zeroes: " & dsDimensionStyleLinearDimensionOptions.HideLeadingZeroes)
         Debug.Print("    Hide trailing zeroes: " & dsDimensionStyleLinearDimensionOptions.HideTrailingZeroes)
         'Tolerance DimensionStyle options

         Dim dsDimensionStyleToleranceOptions As DimensionStyleToleranceOptions
         dsDimensionStyleToleranceOptions = dsDimensionStyle.GetDimensionStyleToleranceOptions()
         Debug.Print("  Tolerance DimensionStyle options:  ")
         Debug.Print("    Precision: " & dsDimensionStyleToleranceOptions.Precision)
         Debug.Print("    Minimum value: " & dsDimensionStyleToleranceOptions.MinimumValue)
         Debug.Print("    Maximum value: " & dsDimensionStyleToleranceOptions.MaximumValue)
         Debug.Print("    Hide leading zeroes: " & dsDimensionStyleToleranceOptions.HideLeadingZeroes)
         Debug.Print("    Hide trailing zeroes: " & dsDimensionStyleToleranceOptions.HideTrailingZeroes)

     End Sub

 End Module
```
