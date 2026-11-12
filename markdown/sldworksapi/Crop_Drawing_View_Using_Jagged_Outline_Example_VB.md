---
title: "Crop Drawing View Using Jagged Outline Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Crop_Drawing_View_Using_Jagged_Outline_Example_VB.htm"
---

# Crop Drawing View Using Jagged Outline Example (VBA)

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
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swDrawing As SldWorks.DrawingDoc
Dim swSelMgr As SldWorks.SelectionMgr
Dim swView As SldWorks.View
Dim swSketchMgr As SldWorks.SketchManager
Dim sketchLines As Variant
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim fileName As String
```

```
Option Explicit
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\foodprocessor.slddrw"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
    Set swDrawing = swModel
    Set swSelMgr = swModel.SelectionManager
```

```
    'Crop Drawing View1 using a jagged outline
    'with the least shape intensity
    status = swModelDocExt.SelectByID2("Drawing View1", "DRAWINGVIEW", 0, 0, 0, False, 0, Nothing, 0)
    Set swView = swSelMgr.GetSelectedObject6(1, -1)
    Set swSketchMgr = swModel.SketchManager
    status = swDrawing.ActivateView("Drawing View1")
    sketchLines = swSketchMgr.CreateCornerRectangle(-5.74722079408937E-02, 3.31536511827661E-02, 0, 3.71399698368841E-02, -3.73161088172339E-02, 0)
    errors = swView.Crop2(True, False, 5)
```

```
    swModel.ClearSelection2 True
```

```
    If swView.CropViewNoOutline Then
        Debug.Print "No outline."
    Else
        If swView.CropViewJaggedOutline Then
            Debug.Print "Jagged outline with shape intensity (1=most to 5=least): " & swView.CropViewJaggedShapeIntensity
        End If
    End If
```

```
End Sub
```
