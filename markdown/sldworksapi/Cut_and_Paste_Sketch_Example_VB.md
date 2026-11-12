---
title: "Cut and Paste Sketch Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Cut_and_Paste_Sketch_Example_VB.htm"
---

# Cut and Paste Sketch Example (VBA)

This example shows how to cut and paste a sketch to and from the Microsoft Windows Clipboard.

```
'--------------------------------------------------------------------------
' Preconditions: Verify that the specified part template exists.
'
' Postconditions:
' 1. Opens a new part document.
' 2. Creates a sketch containing three lines.
' 3. Press F5 to continue.
' 4. Cuts the sketch and places it on the Microsoft
'    Windows Clipboard.
' 5. Press F5 to continue.
' 6. Pastes the sketch from the Clipboard into the part
'    document.
'--------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSketchManager As SldWorks.SketchManager
Dim swSketchSegment As SldWorks.SketchSegment
Dim status As Boolean
Dim errors As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    ' Create a new part document
    Set swModel = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2015\templates\Part.prtdot", swDwgPaperSizes_e.swDwgPaperAsize, 0, 0)
    swApp.ActivateDoc3 "Part1", False, swRebuildOnActivation_e.swRebuildActiveDoc, errors
    Set swModelDocExt = swModel.Extension
```

```
    ' Create a sketch
    status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, swSelectOption_e.swSelectOptionDefault)
    Set swSketchManager = swModel.SketchManager
    swSketchManager.InsertSketch True
    swModel.ClearSelection2 True
    Set swSketchSegment = swSketchManager.CreateLine(-0.066124, 0.011735, 0#, -0.039675, 0.011735, 0#)
    Set swSketchSegment = swSketchManager.CreateLine(-0.039675, -0.008754, 0#, -0.010245, -0.008754, 0#)
    Set swSketchSegment = swSketchManager.CreateLine(-0.010245, -0.029989, 0#, 0.022166, -0.029989, 0#)
    swModel.ClearSelection2 True
    swSketchManager.InsertSketch True
```

```
    Stop
    ' Examine the graphics area to
    ' verify that the sketch was created
```

```
    ' Press F5 to continue executing the
    ' macro
```

```
    ' Select the sketch and place it on the Microsoft Windows Clipboard
    status = swModelDocExt.SelectByID2("Line1@Sketch1", "EXTSKETCHSEGMENT", -0.051595524691358, 1.17347222222222E-02, 0, False, 0, Nothing, 0)
    swModel.EditCut
```

```
    Stop
    ' Examine the graphics area to
    ' verify that the sketch was cut
```

```
    ' Press F5 to continue executing the
    ' macro
```

```
    ' Paste the contents of the Clipboard into the
    ' part document
    swModel.Paste
```

```
    ' Examine the graphics area to
    ' verify that the sketch was pasted
    ' into the document
```

```
End Sub
```
