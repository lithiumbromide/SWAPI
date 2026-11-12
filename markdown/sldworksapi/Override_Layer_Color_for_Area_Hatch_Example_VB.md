---
title: "Override Layer Color for Area Hatch Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Override_Layer_Color_for_Area_Hatch_Example_VB.htm"
---

# Override Layer Color for Area Hatch Example (VBA)

This example shows how to set the color of an area hatch to override the color a layer.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified drawing exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the drawing.
' 2. Hatches a face in the drawing.
' 3. Sets the color of the hatch to override the color the layer.
' 4. Inspect the Immediate window.
' 5. Click outside the drawing view and inspect the hatch.
'
' NOTE: Because the drawing is used elsewhere, do not save changes.
'---------------------------------------------------------------------------
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swView As SldWorks.View
Dim swSketch As SldWorks.Sketch
Dim vSketchHatch As Variant
Dim swSketchHatch As SldWorks.SketchHatch
Dim swFace As SldWorks.Face2
Dim vID As Variant
Dim i As Long
Dim bRet As Boolean
Dim longstatus As Long, longwarnings As Long
```

```
Option Explicit
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    Set swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\box.slddrw", swDocumentTypes_e.swDocDRAWING, 0, "", longstatus, longwarnings)
    swApp.ActivateDoc2 "box - Sheet1", False, longstatus
    Set swModel = swApp.ActiveDoc
```

```
    bRet = swModel.ActivateView("Drawing View1")
```

```
    bRet = swModel.Extension.SelectByID2("", "FACE", 0.246685509728212, 0.236217308689246, 1.49999999999864E-02, True, 0, Nothing, 0)
    swModel.InsertHatchedFace
    swModel.ClearSelection2 True
```

```
    bRet = swModel.Extension.SelectByID2("Drawing View1", "DRAWINGVIEW", 0, 0, 0, False, 0, Nothing, 0)
```

```
    Set swSelMgr = swModel.SelectionManager
    Set swView = swSelMgr.GetSelectedObject6(1, -1)
    Set swSketch = swView.GetSketch
    swModel.EditSketch
```

```
    swModel.ClearSelection2 True
```

```
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  " & swView.Name
```

```
    vSketchHatch = swSketch.GetSketchHatches
```

```
    If Not IsEmpty(vSketchHatch) Then
```

```
        For i = 0 To UBound(vSketchHatch)
```

```
            Set swSketchHatch = vSketchHatch(i)
            Set swFace = swSketchHatch.GetFace
```

```
            bRet = swSketchHatch.Select4(True, Nothing)
            vID = swSketchHatch.GetID
```

```
            Debug.Print "    Hatch ID(" & i & "): [" & vID(0) & "," & vID(1) & "]"
            Debug.Print "      Angle: " & swSketchHatch.Angle
            Debug.Print "      Color: " & swSketchHatch.Color
            Debug.Print "      Layer: " & swSketchHatch.Layer
            Debug.Print "      Layer override (bitmask)? " & swSketchHatch.LayerOverride
            Debug.Print "      Pattern: " & swSketchHatch.Pattern
            Debug.Print "      Scale: " & swSketchHatch.Scale2
            Debug.Print "      Solid fill? " & swSketchHatch.SolidFill
            Debug.Print " "
```

```
            'Override layer color; change to red
            Dim overRide As Long
            swSketchHatch.Color = RGB(255, 0, 0)
            overRide = swSketchHatch.LayerOverride
            ' Extract the first bit and get its value
            If (overRide And 1) Then
                Debug.Print "      Hatch color overrode layer color!"
            Else
                Debug.Print "      Hatch color did not override layer color!"
            End If
```

```
        Next i
```

```
    End If
```

```
End Sub
```
