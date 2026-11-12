---
title: "Crop Drawing View Using Jagged Outline Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Crop_Drawing_View_Using_Jagged_Outline_Example_VBNET.htm"
---

# Crop Drawing View Using Jagged Outline Example (VB.NET)

This example shows how to crop a drawing view using a jagged outline with the least shape intensity.

```
'----------------------------------------------------------------------------
' Preconditions: Verify that the drawing to open exists.
'
' Postconditions:
' 1. Opens the drawing.
' 2. Selects and activates Drawing View1 on Sheet1.
' 3. Creates a rectangle.
' 4. Crops Drawing View1 around the rectangle.
' 5. Examine the drawing.
'
' NOTE: Because the drawing is used elsewhere, do not save changes.
' ---------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swDrawing As DrawingDoc
        Dim swSelMgr As SelectionMgr
        Dim swView As View
        Dim swSketchMgr As SketchManager
        Dim sketchLines As Object
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer
        Dim fileName As String

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\foodprocessor.slddrw"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExt = swModel.Extension
        swDrawing = swModel
        swSelMgr = swModel.SelectionManager

        'Crop Drawing View1 using a jagged outline
        'with the least shape intensity
        status = swModelDocExt.SelectByID2("Drawing View1", "DRAWINGVIEW", 0, 0, 0, False, 0, Nothing, 0)
        swView = swSelMgr.GetSelectedObject6(1, -1)
        swSketchMgr = swModel.SketchManager
        status = swDrawing.ActivateView("Drawing View1")
        sketchLines = swSketchMgr.CreateCornerRectangle(-0.0574722079408937, 0.0331536511827661, 0, 0.0371399698368841, -0.0373161088172339, 0)
        errors = swView.Crop2(True, False, 5)

        swModel.ClearSelection2(True)

        If swView.CropViewNoOutline Then
            Debug.Print("No outline.")
        Else
            If swView.CropViewJaggedOutline Then
                Debug.Print("Jagged outline with shape intensity (1=most to 5=least): " & swView.CropViewJaggedShapeIntensity)
            End If
        End If

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
