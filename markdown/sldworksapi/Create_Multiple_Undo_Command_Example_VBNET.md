---
title: "Create Hidden Undo Object Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Multiple_Undo_Command_Example_VBNET.htm"
---

# Create Hidden Undo Object Example (VB.NET)

This example shows how to create an Undo object that is hidden in the SOLIDWORKS Undo list.

```
'-----------------------------------------------------------------------------
' Preconditions: Ensure the part template path exists.
'
' Postconditions:
' 1. A part with four sketches is created.
' 2. One sketch is extruded.
' 3. A hidden Undo object, API Undo, is created with two extrusions.
' 4. One sketch is cut extruded.
' 5. The following items appear in the SOLIDWORKS Undo list in this order:
'    a. Extruded Cut
'    b. (API Undo, hidden from view)
'    c. Base
'
' NOTE: If you select Base in the SOLIDWORKS Undo list:
' 1. The base boss created before the recording of the hidden API Undo object is undone.
' 2. The two bosses created during the recording of the hidden API Undo object are undone.
' 3. The cut extrusion created after the recording of the hidden API Undo object is undone.
'----------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Dim swModel As ModelDoc2
    Dim swModelDocExt As ModelDocExtension
    Dim swModelview as ModelView
    Dim swSketchManager As SketchManager
    Dim swSketchSegment As SketchSegment
    Dim swFeature As Feature
    Dim swFeatureManager As FeatureManager
    Dim swSelectionManager As SelectionMgr
    Dim status As Boolean
    Dim errors As Integer

    Sub Main()

        swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2013\templates\Part.prtdot", swDwgPaperSizes_e.swDwgPaperAsize, 0, 0)
        swApp.ActivateDoc3("Part2.sldprt", False, swRebuildOnActivation_e.swDontRebuildActiveDoc, errors)
        swModel = swApp.ActiveDoc
```

swModelView = swModel.**ActiveView**

swModelView.**FrameState** = swWindowState_e.swWindowMaximized

```
        swModelDocExt = swModel.Extension
        swSketchManager = swModel.SketchManager

        swSketchManager.InsertSketch(True)
        status = swModelDocExt.SelectByID2("Front Plane", "PLANE", -0.0692248508634211, 0.0392379182115397, 0.00987134779060705, False, 0, Nothing, 0)
        swModel.ClearSelection2(True)

        Dim vSkLines As Object
        vSkLines = swSketchManager.CreateCornerRectangle(-0.0891172006155176, 0.0314069429482, 0, -0.0425302352423542, 0.00601966406507166, 0)
        swModel.ClearSelection2(True)

        swSketchManager.InsertSketch(True)
        status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        swModel.ClearSelection2(True)

        swSketchSegment = swSketchManager.CreateCircle(0.009029, 0.03036, 0.0#, 0.021854, 0.019629, 0.0#)
        swModel.ClearSelection2(True)

        swSketchManager.InsertSketch(True)
        status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)

        swModel.ClearSelection2(True)
        swSketchSegment = swSketchManager.CreateEllipse(0.0306284568434307, 0.00619756829649987, 0, 0.0309763470298606, 0.00997419305453208, 0, 0.0286971648691861, 0.00637547252792807, 0)
        swModel.ClearSelection2(True)

        swSketchManager.InsertSketch(True)
        status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        swModel.ClearSelection2(True)

        swSketchSegment = swSketchManager.CreateEllipse(0.0240620641310443, 0.0131240684851264, 0, 0.0771974468433887, 0.0706711158113391, 0, 0.000886560440335415, 0.0345228945826079, 0)
        swModel.ClearSelection2(True)
        swSketchManager.InsertSketch(True)

        status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 4, Nothing, 0)

        swFeatureManager = swModel.FeatureManager
        swFeature = swFeatureManager.FeatureExtrusion2(True, False, False, 0, 0, 0.00254, 0.00254, False, False, False, False, 0.0174532925199433, 0.0174532925199433, False, False, False, False, True, True, True, 0, 0, False)
        swSelectionManager = swModel.SelectionManager
        swSelectionManager.EnableContourSelection = False

        ' Start recording the SOLIDWORKS Undo object
        swModelDocExt.StartRecordingUndoObject()
        status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, False, 4, Nothing, 0)
        swFeature = swFeatureManager.FeatureExtrusion2(True, False, False, 0, 0, 0.00254, 0.00254, False, False, False, False, 0.0174532925199433, 0.0174532925199433, False, False, False, False, True, True, True, 0, 0, False)
        swSelectionManager.EnableContourSelection = False
        status = swModelDocExt.SelectByID2("Sketch4", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
        swFeature = swFeatureManager.FeatureExtrusion2(True, False, False, 0, 0, 0.00254, 0.00254, False, False, False, False, 0.0174532925199433, 0.0174532925199433, False, False, False, False, True, True, True, 0, 0, False)
        swSelectionManager.EnableContourSelection = False

        ' End recording the SOLIDWORKS Undo object with name "API Undo" and hide it in the Undo list
        swModelDocExt.FinishRecordingUndoObject2("API Undo", True)
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("Sketch3", "SKETCH", 0, 0, 0, False, 4, Nothing, 0)
        swFeature = swFeatureManager.FeatureCut3(True, False, True, 0, 0, 0.00254, 0.00254, False, False, False, False, 0.0174532925199433, 0.0174532925199433, False, False, False, False, False, True, True, True, True, False, 0, 0, False)
        swSelectionManager.EnableContourSelection = False

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
