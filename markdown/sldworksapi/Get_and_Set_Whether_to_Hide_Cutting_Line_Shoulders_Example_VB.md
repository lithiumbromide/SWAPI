---
title: "Get and Set Whether to Hide Cutting Line Shoulders Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Whether_to_Hide_Cutting_Line_Shoulders_Example_VB.htm"
---

# Get and Set Whether to Hide Cutting Line Shoulders Example (VBA)

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
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swDrawing As SldWorks.DrawingDoc
Dim swSheet As SldWorks.Sheet
Dim swView As SldWorks.View
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSketchSegment As SldWorks.SketchSegment
Dim swSketchMgr As SldWorks.SketchManager
Dim swSectionView As SldWorks.DrSection
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim fileName As String
Dim swSheetWidth As Double
Dim swSheetHeight As Double
Dim drawingTemplate As String
Dim sheetTemplate As String
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    'Open part
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\cam roller.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
```

```
    'Create drawing of part
    swSheetWidth = 1.189
    swSheetHeight = 0.841
    drawingTemplate = "C:\ProgramData\SolidWorks\SOLIDWORKS 2017\templates\Drawing.drwdot"
    Set swDrawing = swApp.NewDocument(drawingTemplate, swDwgPaperSizes_e.swDwgPapersUserDefined, swSheetWidth, swSheetHeight)
    Set swSheet = swDrawing.GetCurrentSheet()
    swSheet.SetProperties2 swDwgPaperSizes_e.swDwgPapersUserDefined, swDwgTemplates_e.swDwgTemplateCustom, 1, 2, False, swSheetWidth, swSheetHeight, True
    sheetTemplate = "C:\ProgramData\SolidWorks\SOLIDWORKS 2017\lang\english\sheetformat\a0 - iso.slddrt"
    swSheet.SetTemplateName sheetTemplate
    swSheet.ReloadTemplate True
    status = swDrawing.GenerateViewPaletteViews(fileName)
    Set swView = swDrawing.DropDrawingViewFromPalette2("*Left", 0.580930433566434, 0.431525272727273, 0)
```

```
    'Create section view
    Set swDrawing = swApp.ActiveDoc
    status = swDrawing.ActivateView("Drawing View1")
    swModel.ClearSelection2 True
    Set swModel = swDrawing
    Set swSketchMgr = swModel.SketchManager
    Set swSketchSegment = swSketchMgr.CreateLine(0#, 0#, 0#, 0.012168, 0.021283, 0#)
    Set swSketchSegment = swSketchMgr.CreateLine(0#, 0#, 0#, 0.024347, -0.010966, 0#)
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", 0.690604633175108, 0.625483883858213, 0, False, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("Line2", "SKETCHSEGMENT", 0.747211061353527, 0.357889859742052, 0, True, 0, Nothing, 0)
    Set swView = swDrawing.CreateSectionViewAt5(0.676815388637685, 0.116110180826413, 0, "A", swCreateSectionViewAtOptions_e.swCreateSectionView_OffsetSection, Nothing, 0)
    status = swDrawing.ActivateView("Drawing View2")
    swModel.ClearSelection2 True
```

```
    'Get section view and get and set whether to hide cutting line shoulders
    Set swSectionView = swView.GetSection
    If swSectionView.CuttingLineShoulders Then
        Debug.Print "Hide cutting line shoulders = True"
        Debug.Print "Setting hide cutting line shoulders to False"
        swSectionView.CuttingLineShoulders = False
        Debug.Print "  Hide cutting line shoulders = " & swSectionView.CuttingLineShoulders
    Else
        Debug.Print "Hide cutting line shoulders = False"
        Debug.Print "Setting hide cutting line shoulders to True"
        swSectionView.CuttingLineShoulders = True
        Debug.Print "  Hide cutting line shoulders = " & swSectionView.CuttingLineShoulders
    End If
```

```
End Sub
```
