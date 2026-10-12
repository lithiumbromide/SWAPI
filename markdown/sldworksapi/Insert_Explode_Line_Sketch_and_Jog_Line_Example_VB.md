---
title: "Insert Explode Line Sketch and Jog Line Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Explode_Line_Sketch_and_Jog_Line_Example_VB.htm"
---

# Insert Explode Line Sketch and Jog Line Example (VBA)

This example shows how to insert a jog line in an explode line sketch, a type of 3D sketch.

```
'--------------------------------------------------------------------------
' Preconditions: Open public_documents\samples\tutorial\floxpress\ball valve\ball_valve.sldasm.
'
' Postconditions:
' 1. Creates an exploded view of the assembly.
' 2. Adds a jog line, which is a type of explode line.
' 3. Examine the graphics area.
' 4. Locate 3DExplode1, the explode line sketch, on the
'    ConfigurationManager tab (click the ConfigurationManager tab and
'    expand default and ExplView1.)
'
' NOTE: Because this assembly is used elsewhere, do not save changes.
'--------------------------------------------------------------------------
Option Explicit
```

```
Dim SwApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swAssembly As SldWorks.AssemblyDoc
Dim swSketchMgr As SldWorks.SketchManager
Dim swSketchSegment As SldWorks.SketchSegment
```

```
Sub main()
```

```
    Set SwApp = Application.SldWorks
    Set swModel = SwApp.ActiveDoc
    Set swAssembly = swModel
    Set swSketchMgr = swModel.SketchManager
```

```
    ' Explode the assembly
    swAssembly.AutoExplode
```

```
    swModel.EditRebuild3
```

```
    swModel.ViewZoomtofit2
```

```
    ' Insert an explode line sketch
    swSketchMgr.InsertExplodeLineSketch
```

```
    'Create a line
    Set swSketchSegment = swSketchMgr.CreateLine(0, 0.1, 0, 0, 0.3, 0)
```

```
    swModel.ViewZoomtofit2
```

```
    ' Create a jog line using the line
    swSketchSegment.JogLine 0, 0.2, 0, 0.04, 0.25, 0
```

```
    ' Close the 3D sketch and rebuild
    swSketchMgr.Insert3DSketch True
```

```
End Sub
```
