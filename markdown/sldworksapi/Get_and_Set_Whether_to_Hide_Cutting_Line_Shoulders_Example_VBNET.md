---
title: "Get and Set Whether to Hide Cutting Line Shoulders Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Whether_to_Hide_Cutting_Line_Shoulders_Example_VBNET.htm"
---

# Get and Set Whether to Hide Cutting Line Shoulders Example (VB.NET)

This example shows how to get and set whether to hide cutting line shoulders in a section view.

```
'--------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the part and templates exist.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the part.
' 2. Creates a drawing of the part.
' 3. Creates a section view.
' 4. Gets and sets whether to hide cutting line shoulders in the section
'    view.
' 5. Examine the Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save it or the drawing.
'--------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()
        Dim swModel As ModelDoc2
        Dim swDrawing As DrawingDoc
        Dim swSheet As Sheet
        Dim swView As View
        Dim swModelDocExt As ModelDocExtension
        Dim swSketchSegment As SketchSegment
        Dim swSketchMgr As SketchManager
        Dim swSectionView As DrSection
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer
        Dim fileName As String
        Dim swSheetWidth As Double
        Dim swSheetHeight As Double
        Dim drawingTemplate As String
        Dim sheetTemplate As String

        'Open part
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\cam roller.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

        'Create drawing of part
        swSheetWidth = 1.189
        swSheetHeight = 0.841
        drawingTemplate = "C:\ProgramData\SolidWorks\SOLIDWORKS 2017\templates\Drawing.drwdot"
        swDrawing = swApp.NewDocument(drawingTemplate, swDwgPaperSizes_e.swDwgPapersUserDefined, swSheetWidth, swSheetHeight)
        swSheet = swDrawing.GetCurrentSheet()
        swSheet.SetProperties2(swDwgPaperSizes_e.swDwgPapersUserDefined, swDwgTemplates_e.swDwgTemplateCustom, 1, 2, False, swSheetWidth, swSheetHeight, True)
        sheetTemplate = "C:\ProgramData\SolidWorks\SOLIDWORKS 2017\lang\english\sheetformat\a0 - iso.slddrt"
        swSheet.SetTemplateName(sheetTemplate)
        swSheet.ReloadTemplate(True)
        status = swDrawing.GenerateViewPaletteViews(fileName)
        swView = swDrawing.DropDrawingViewFromPalette2("*Left", 0.580930433566434, 0.431525272727273, 0)

        'Create section view
        swDrawing = swApp.ActiveDoc
        status = swDrawing.ActivateView("Drawing View1")
        swModel.ClearSelection2(True)
        swModel = swDrawing
        swSketchMgr = swModel.SketchManager
        swSketchSegment = swSketchMgr.CreateLine(0.0#, 0.0#, 0.0#, 0.012168, 0.021283, 0.0#)
        swSketchSegment = swSketchMgr.CreateLine(0.0#, 0.0#, 0.0#, 0.024347, -0.010966, 0.0#)
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", 0.690604633175108, 0.625483883858213, 0, False, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Line2", "SKETCHSEGMENT", 0.747211061353527, 0.357889859742052, 0, True, 0, Nothing, 0)
        swView = swDrawing.CreateSectionViewAt5(0.676815388637685, 0.116110180826413, 0, "A", swCreateSectionViewAtOptions_e.swCreateSectionView_OffsetSection, Nothing, 0)
        status = swDrawing.ActivateView("Drawing View2")
        swModel.ClearSelection2(True)

        'Get section view and get and set whether to hide cutting line shoulders
        swSectionView = swView.GetSection
        If swSectionView.CuttingLineShoulders Then
            Debug.Print("Hide cutting line shoulders = True")
            Debug.Print("Setting hide cutting line shoulders to False")
            swSectionView.CuttingLineShoulders = False
            Debug.Print("  Hide cutting line shoulders = " & swSectionView.CuttingLineShoulders)
        Else
            Debug.Print("Hide cutting line shoulders = False")
            Debug.Print("Setting hide cutting line shoulders to True")
            swSectionView.CuttingLineShoulders = True
            Debug.Print("  Hide cutting line shoulders = " & swSectionView.CuttingLineShoulders)
        End If

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
