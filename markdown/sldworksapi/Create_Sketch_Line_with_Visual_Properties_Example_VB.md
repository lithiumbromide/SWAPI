---
title: "Create Sketch Entities with Visual Properties Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Sketch_Line_with_Visual_Properties_Example_VB.htm"
---

# Create Sketch Entities with Visual Properties Example (VBA)

This example shows how to create a drawing and add some sketch entities and change the visual properties of a couple of sketch entities.

```
'------------------------------------------------------------
' Preconditions: None.
'
' Postconditions:
' 1. Opens a new drawing and creates and activates a layer.
' 2. Inserts some sketch entities.
' 3. Examine the drawing, then press F5.
' 4. Changes the visual properties of a couple of sketch entities,
'    which overrides the visual properties of the layer.
' 5. Repaints the graphics area.
' 6. Examine the drawing.
'------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim pDrawing As SldWorks.DrawingDoc
Dim pLayerMgr As SldWorks.LayerMgr
Dim pSketchSegment1, pSketchSegment2, pSketchSegment3 As Object
Dim pSketchSegment4, pSketchSegment5, pSketchPoint1, pSketchPoint2 As Object
Dim res As Long
```

```
Sub main()
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set pDrawing = swApp.NewDrawing2(13, """", 0, 0.2794, 0.2159)
```

```
    ' Get LayerMgr object
    Set pLayerMgr = pDrawing.GetLayerManager
```

```
    ' Create a layer
    res = pLayerMgr.AddLayer("myLayer", "Desc", 1227327, swLineStyles_e.swLineCONTINUOUS, swLineWeights_e.swLW_THIN)
    If (res = False) Then
        swApp.SendMsgToUser "Error creating layer."
    End If
```

```
    ' Activate the layer
    res = pLayerMgr.SetCurrentLayer("myLayer")
    If (res = False) Then
        swApp.SendMsgToUser "Error activating layer."
    End If
```

```
    ' Create some sketch entities on the active layer
    pDrawing.SetAddToDB True
    Set pSketchPoint1 = pDrawing.CreatePoint2(0.1, 0.14, 0)
    Set pSketchPoint2 = pDrawing.CreatePoint2(0.16, 0.14, 0)
    Set pSketchSegment1 = pDrawing.CreateCircle2(0.13, 0.1, 0, 0.2, 0.099, 0)
    Set pSketchSegment2 = pDrawing.CreateLine2(0.13, 0.1, 0, 0.12, 0.1, 0)
    Set pSketchSegment3 = pDrawing.CreateLine2(0.12, 0.1, 0, 0.13, 0.13, 0)
    Set pSketchSegment4 = pDrawing.CreateArc2(0.13, 0.1, 0, 0.09, 0.07, 0, 0.14, 0.051, 0, 1)
    Set pSketchSegment5 = pDrawing.CreateArc2(0.13, 0.1, 0, 0.195, 0.135, 0, 0.065, 0.135, 0, 1)
    pDrawing.SetAddToDB False
```

```
    pDrawing.ClearSelection
```

```
    Stop
    ' Examine the drawing, then press F5
```

```
    ' Change the visual properties of a couple of sketch entities, which
    ' overrides the visual properties of the layer
    pSketchSegment4.Color = 4227327
    pSketchSegment4.Width = swLineWeights_e.swLW_THICK
    pSketchSegment4.Style = swLineStyles_e.swLinePHANTOM
    pSketchSegment5.Color = 0
```

```
    ' Repaint to see the visual changes
    pDrawing.GraphicsRedraw2
```

```
End Sub
```
