---
title: "Cut and Paste Sketch Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Cut_and_Paste_Sketch_Example_VBNET.htm"
---

# Cut and Paste Sketch Example (VB.NET)

This example shows how to cut and paste a sketch to and from the Microsoft Windows Clipboard.

```
'----------------------------------------------------------------------
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
'----------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Dim swModel As ModelDoc2
    Dim swModelDocExt As ModelDocExtension
    Dim swSketchManager As SketchManager
    Dim swSketchSegment As SketchSegment
    Dim status As Boolean
    Dim errors As Integer

    Sub Main()

        ' Create a new part document
        swModel = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2015\templates\Part.prtdot", swDwgPaperSizes_e.swDwgPaperAsize, 0, 0)
        swApp.ActivateDoc3("Part1", False, swRebuildOnActivation_e.swRebuildActiveDoc, errors)
        swModelDocExt = swModel.Extension

        ' Create a sketch
        status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, swSelectOption_e.swSelectOptionDefault)
        swSketchManager = swModel.SketchManager
        swSketchManager.InsertSketch(True)
        swModel.ClearSelection2(True)
        swSketchSegment = swSketchManager.CreateLine(-0.066124, 0.011735, 0.0#, -0.039675, 0.011735, 0.0#)
        swSketchSegment = swSketchManager.CreateLine(-0.039675, -0.008754, 0.0#, -0.010245, -0.008754, 0.0#)
        swSketchSegment = swSketchManager.CreateLine(-0.010245, -0.029989, 0.0#, 0.022166, -0.029989, 0.0#)
        swModel.ClearSelection2(True)
        swSketchManager.InsertSketch(True)

        Stop
        ' Examine the graphics area to
        ' verify that the sketch was created

        ' Press F5 to continue executing the
        ' macro

        ' Select the sketch and place it on the Microsoft Windows Clipboard
        status = swModelDocExt.SelectByID2("Line1@Sketch1", "EXTSKETCHSEGMENT", -0.051595524691358, 0.0117347222222222, 0, False, 0, Nothing, 0)
        swModel.EditCut()

        Stop
        ' Examine the graphics area to
        ' verify that the sketch was cut

        ' Press F5 to continue executing the
        ' macro

        ' Paste the contents of the Clipboard into the
        ' part document

        swModel.Paste()
        ' Examine the graphics area to
        ' verify that the sketch was pasted
        ' into the document
    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
