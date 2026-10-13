---
title: "Constrain Sketch Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Constrain_Sketch_Example_VB.htm"
---

# Constrain Sketch Example (VBA)

This example shows how to fully constrain a sketch.

| Before constraining the sketch | After constraining the sketch |
| --- | --- |
|  |  |

```vb
'----------------------------------------------------------------------------
 ' Preconditions: Before constraining  the sketch sketch exists.
 '
 ' Postconditions: Fully constrains the sketch, which looks like
 ' After constraining the sketch.
 '----------------------------------------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSketchMgr As SldWorks.SketchManager
Dim swSketch As SldWorks.Sketch
Dim swSelMgr As SldWorks.SelectionMgr
Dim swFeat As SldWorks.Feature
Dim nSketchStatus As Long
Dim boolstatus As Boolean

Sub main()
```

```vb
Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc

' Is a model document active?
If swModel Is Nothing Then
    swApp.SendMsgToUser2 "A part document must be open and the active document.", swMbWarning, swMbOk
    Exit Sub
End If

' Is it a part document?
Dim modelType As Long
modelType = swModel.GetType
If modelType <> SwConst.swDocPART Then
    swApp.SendMsgToUser2 "A part document must be open and the active document.", swMbWarning, swMbOk
    Exit Sub
End If

Set swSketchMgr = swModel.SketchManager
Set swSketch = swSketchMgr.ActiveSketch
    If swSketch Is Nothing Then
    swApp.SendMsgToUser2 "No active sketch; thus, a sketch could not be selected.", swMbWarning, swMbOk
    Exit Sub
    End If

' Select the lines and make them colinear and vertical
boolstatus = swModel.Extension.SelectByID2("Line2", "SKETCHSEGMENT", 0.02116924482339, 0.04904427527406, 0, False, 0, Nothing, 0)
boolstatus = swModel.Extension.SelectByID2("Line3", "SKETCHSEGMENT", 0.06508556638246, 0.02563976857491, 0, True, 0, Nothing, 0)
swModel.SketchAddConstraints "sgCOLINEAR"
swModel.SketchAddConstraints "sgVERTICAL2D"
    MsgBox "The lines have been selected, made colinear, and vertically constrained."
swModel.ClearSelection2 True

'Select the center of the circles and constrain them to the origin
boolstatus = swModel.Extension.SelectByID2("Point7", "SKETCHPOINT", 0.1074240560292, 0.006179841656516, 0, False, 0, Nothing, 0)
boolstatus = swModel.Extension.SelectByID2("Point1@Origin", "EXTSKETCHPOINT", 0, 0, 0, True, 0, Nothing, 0)
swModel.SketchAddConstraints "sgCOINCIDENT"
    MsgBox "The center of the circles and the origin were selected and made coincident"
swModel.ClearSelection2 True

' Select a line and the circle and make them tangent
boolstatus = swModel.Extension.SelectByID2("Line2", "SKETCHSEGMENT", 0.005390925700365, 0.009861449451888, 0, False, 0, Nothing, 0)
boolstatus = swModel.Extension.SelectByID2("Arc1", "SKETCHSEGMENT", -0.01222819732034, 0.04720347137637, 0, True, 0, Nothing, 0)
swModel.SketchAddConstraints "sgTANGENT"
    MsgBox "One line and a cirle were selected; both lines are now tangent with the circle."
swModel.ClearSelection2 True

'Select the circles and make them concentric
boolstatus = swModel.Extension.SelectByID2("Arc2", "SKETCHSEGMENT", -0.0290584043849, 0.03116218026797, 0, False, 0, Nothing, 0)
boolstatus = swModel.Extension.SelectByID2("Arc1", "SKETCHSEGMENT", -0.01222819732034, 0.04720347137637, 0, True, 0, Nothing, 0)
swModel.SketchAddConstraints "sgCONCENTRIC"
    MsgBox "The circles have been selected and made concentric."
swModel.ClearSelection2 True

'Select all the sketch entities and fix their positions
MsgBox "All  sketch entities will be selected and made fixed to fully constrain the sketch."
boolstatus = swModel.Extension.SelectByID2("Line2", "SKETCHSEGMENT", 0.02116924482339, 0.04904427527406, 0, False, 0, Nothing, 0)
boolstatus = swModel.Extension.SelectByID2("Line3", "SKETCHSEGMENT", 0.06508556638246, 0.02563976857491, 0, True, 0, Nothing, 0)
boolstatus = swModel.Extension.SelectByID2("Arc2", "SKETCHSEGMENT", -0.0290584043849, 0.03116218026797, 0, False, 0, Nothing, 0)
boolstatus = swModel.Extension.SelectByID2("Arc1", "SKETCHSEGMENT", -0.01222819732034, 0.04720347137637, 0, True, 0, Nothing, 0)
swModel.SketchAddConstraints "sgFIXED"
swModel.ClearSelection2 True
```

```vb
End Sub
```
