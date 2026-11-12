---
title: "Create Full Symmetrical Angular Dimension Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Full_Symmetrical_Angular_Dimension_Example_VB.htm"
---

# Create Full Symmetrical Angular Dimension Example (VBA)

This example shows how to create a full symmetrical angular dimension between a centerline and a line.

```
'---------------------------------------------------------
' Preconditions: Verify that the specified part document template
' exists.
'
' Postconditions:
' 1. Opens a new part document.
' 2. Opens a sketch.
' 3. Creates a centerline and three lines in
'    the open sketch.
' 4. Selects the centerline and one of the lines.
' 5. Suppresses the dimension dialog.
' 6. Creates a full symmetrical angular dimension for
'    the entities selected in step 4.
' 7. Unsuppresses the dimension dialog.
' 8. Examine the graphics area to verify step 6.
'----------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSketchMgr As SldWorks.SketchManager
Dim swSketchSegment As SldWorks.SketchSegment
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swDisplayDimension As SldWorks.DisplayDimension
Dim status As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2015\templates\Part.prtdot", 0, 0, 0)

    'Sketch a centerline and three lines
    Set swSketchMgr = swModel.SketchManager
    swSketchMgr.InsertSketch (True)
    Set swSketchSegment = swSketchMgr.CreateCenterLine(0#, 0.043667, 0#, 0#, -0.050556, 0#)
    Set swSketchSegment = swSketchMgr.CreateLine(-0.102, 0.039667, 0#, -0.086223, 0.011, 0#)
    Set swSketchSegment = swSketchMgr.CreateLine(0.142445, 0.066556, 0#, 0.100889, -0.032333, 0#)
    Set swSketchSegment = swSketchMgr.CreateLine(0.085334, 0.036556, 0#, 0.049658, -0.048341, 0#)
```

```
    'Select the centerline and one of the lines
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", -2.22223294397278E-04, 2.23334410869282E-02, 0, False, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("Line3", "SKETCHSEGMENT", 0.113556103437018, -1.44445141358242E-03, 0, True, 0, Nothing, 0)
    swModel.ClearSelection2 True
```

```
    'Suppress the dimension dialog box
    swApp.SetUserPreferenceToggle swUserPreferenceToggle_e.swInputDimValOnCreate, False
```

```
    'Create a full symmetrical angular dimension
    status = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", -2.22223294397278E-04, 2.23334410869282E-02, 0, False, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("Line3", "SKETCHSEGMENT", 0.113556103437018, -1.44445141358242E-03, 0, True, 0, Nothing, 0)
    Set swDisplayDimension = swModelDocExt.AddSymmetricDimension(8.32913738352659E-02, 0.112403597688285, 0)
    swModel.ClearSelection2 True
```

```
    'Unsuppress the dimension dialog box
    swApp.SetUserPreferenceToggle swUserPreferenceToggle_e.swInputDimValOnCreate, True
```

```
    swModel.ViewZoomtofit2
```

```
End Sub
```
