---
title: "Open and Exit Sketch Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Open_and_Exit_Sketch_Example_VB.htm"
---

# Open and Exit Sketch Example (VBA)

This example shows how to open a sketch, sketch a line, and close the sketch.

```
'-----------------------------------------------------------
' Preconditions:
' 1. Open a part.
' 2. Select a planar face or a sketch.
'
' Postconditions:
' 1. Opens a sketch, sketches a line, and closes the sketch.
' 2. Examine the graphics area and FeatureManager design tree.
'-----------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSkSeg As SldWorks.SketchSegment
    Dim swSkLine As SldWorks.SketchLine
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
```

```
    ' Open a sketch on the selected planar face
    ' or the selected sketch
    swModel.InsertSketch2 True
```

```
        ' Sketch a line
        Set swSkSeg = swModel.CreateLine2(0#, 0#, 0#, 0.1, 0.1, 0#)
        Set swSkLine = swSkSeg
```

```
    ' Exit the sketch
    swModel.InsertSketch2 True
```

```
End Sub
```
