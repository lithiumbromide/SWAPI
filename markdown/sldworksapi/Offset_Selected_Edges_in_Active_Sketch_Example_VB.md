---
title: "Offset Selected Edges in Active Sketch Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Offset_Selected_Edges_in_Active_Sketch_Example_VB.htm"
---

# Offset Selected Edges in Active Sketch Example (VBA)

This example shows how to offset the selected edges to generate geometry in the active sketch.

```
'----------------------------------------------
' Preconditions:
' 1. Open a part.
' 2. Open a new sketch on a plane.
' 3. Select one or more edges in the part coincident
'    to the plane.
'
' Postconditions:
' 1. Offsets the selected edges.
' 2. Examine the sketch in the graphics area.
'----------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSketchMgr As SldWorks.SketchManager
    Dim swSketch As SldWorks.Sketch
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSketchMgr = swModel.SketchManager
    Set swSketch = swModel.GetActiveSketch2
```

```
    bRet = swSketchMgr.SketchUseEdge(False)

End Sub
```
