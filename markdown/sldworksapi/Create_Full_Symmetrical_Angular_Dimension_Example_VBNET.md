---
title: "Create Full Symmetrical Angular Dimension Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Full_Symmetrical_Angular_Dimension_Example_VBNET.htm"
---

# Create Full Symmetrical Angular Dimension Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swSketchMgr As SketchManager
        Dim swSketchSegment As SketchSegment
        Dim swModelDocExt As ModelDocExtension
        Dim swDisplayDimension As DisplayDimension
        Dim status As Boolean

        swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2015\templates\Part.prtdot", 0, 0, 0)

        'Sketch a centerline and three lines
        swSketchMgr = swModel.SketchManager
        swSketchMgr.InsertSketch(True)
        swSketchSegment = swSketchMgr.CreateCenterLine(0.0#, 0.043667, 0.0#, 0.0#, -0.050556, 0.0#)
        swSketchSegment = swSketchMgr.CreateLine(-0.102, 0.039667, 0.0#, -0.086223, 0.011, 0.0#)
        swSketchSegment = swSketchMgr.CreateLine(0.142445, 0.066556, 0.0#, 0.100889, -0.032333, 0.0#)
        swSketchSegment = swSketchMgr.CreateLine(0.085334, 0.036556, 0.0#, 0.049658, -0.048341, 0.0#)

        'Select the centerline and one of the lines
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", -0.000222223294397278, 0.0223334410869282, 0, False, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Line3", "SKETCHSEGMENT", 0.113556103437018, -0.00144445141358242, 0, True, 0, Nothing, 0)
        swModel.ClearSelection2(True)

        'Suppress the dimension dialog box
        swApp.SetUserPreferenceToggle(swUserPreferenceToggle_e.swInputDimValOnCreate, False)

        'Create a full symmetrical angular dimension
        status = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", -0.000222223294397278, 0.0223334410869282, 0, False, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Line3", "SKETCHSEGMENT", 0.113556103437018, -0.00144445141358242, 0, True, 0, Nothing, 0)
        swDisplayDimension = swModelDocExt.AddSymmetricDimension(0.0832913738352659, 0.112403597688285, 0)
        swModel.ClearSelection2(True)

        'Unsuppress the dimension dialog box
        swApp.SetUserPreferenceToggle(swUserPreferenceToggle_e.swInputDimValOnCreate, True)

        swModel.ViewZoomtofit2()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
