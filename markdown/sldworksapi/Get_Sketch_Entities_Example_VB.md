---
title: "Get Sketch Entities Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sketch_Entities_Example_VB.htm"
---

# Get Sketch Entities Example (VBA)

This example shows how to get all of the sketch entities (arcs, ellipses, lines, parabolas, splines, and text) in a sketch.

```
'-------------------------------------------------
' 1. Open a part that has a Sketch1 feature that
'    contains sketch text, sketch lines, sketch parabolas,
'    sketch arcs, sketch ellipses, and sketch splines.
' 2. Open the Immediate window.
'
' Postconditions: Examine the Immediate window.
'-------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
```

```
Sub main()
```

```
    Dim swModel As SldWorks.ModelDoc2
    Dim swSketch As SldWorks.Sketch
    Dim swSketchMgr As SldWorks.SketchManager
    Dim vSketchTextSegments As Variant
    Dim vSketchTextSegment As Variant
    Dim swSketchText As SldWorks.SketchText
    Dim vSketchSegments As Variant
    Dim vSketchSegment As Variant
    Dim swSketchSegment As SldWorks.SketchSegment
    Dim bValue As Boolean
```

```
    ' Connect to SOLIDWORKS Design
    Set swApp = Application.SldWorks
```

```
    ' Get active document
    Set swModel = swApp.ActiveDoc
```

```
    ' Get SketchManager
    Set swSketchMgr = swModel.SketchManager
```

```
    ' Clear the selection
    swModel.ClearSelection2 True
```

```
    ' Select the sketch
    bValue = swModel.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
```

```
    ' Activate the sketch
    swSketchMgr.InsertSketch False
```

```
    ' Get the sketch itself
    Set swSketch = swModel.GetActiveSketch2
```

```
    ' Loop over all SketchText instances
```

```
    ' Get SketchText
    vSketchTextSegments = swSketch.GetSketchTextSegments
```

```
    If (Not IsEmpty(vSketchTextSegments)) Then
        For Each vSketchTextSegment In vSketchTextSegments
            Set swSketchText = vSketchTextSegment
            Debug.Print "Text = " & swSketchText.Text
        Next vSketchTextSegment
    End If
```

```
    Debug.Print
```

```
    ' Loop over all sketch segments
```

```
    ' Get sketch segments
    vSketchSegments = swSketch.GetSketchSegments
```

```
    If (Not IsEmpty(vSketchSegments)) Then
        For Each vSketchSegment In vSketchSegments
            Set swSketchSegment = vSketchSegment
```

```
            ' Determine actual type of sketch segment
            Select Case (swSketchSegment.GetType)
```

```
                ' SketchText "is-a" sketch segment
                Case swSketchSegments_e.swSketchText
```

```
                    ' Cast sketch segment to sketch text
                    Set swSketchText = swSketchSegment
```

```
                    ' Get sketch text specific property
                    Debug.Print "Sketch text = " & swSketchText.Text
```

```
                Case swSketchSegments_e.swSketchLINE
                    Debug.Print "Sketch line"
                Case swSketchSegments_e.swSketchELLIPSE
                    Debug.Print "Sketch ellipse"
                Case swSketchSegments_e.swSketchARC
                    Debug.Print "Sketch arc"
                Case swSketchSegments_e.swSketchPARABOLA
                    Debug.Print "Sketch parabola"
                Case swSketchSegments_e.swSketchSPLINE
                    Debug.Print "Sketch spline"
                Case Else
                    Debug.Print "<unknown>"
            End Select
```

```
        Next vSketchSegment
```

```
    End If
```

```
    swSketchMgr.InsertSketch True
```

```
End Sub
```
