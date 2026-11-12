---
title: "Create Hidden Undo Object Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Multiple_Undo_Command_Example_VB.htm"
---

# Create Hidden Undo Object Example (VBA)

This example shows how to create an Undo object that is hidden in the SOLIDWORKS Undo list.

```vb
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
Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim swModelDocExt As SldWorks.ModelDocExtension
 Dim boolstatus As Boolean
 Dim longstatus As Long
 Option Explicit
 Sub main()
    Set swApp = Application.SldWorks

    Set Part = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2013\templates\Part.prtdot", 0, 0, 0)
     swApp.ActivateDoc3 "Part2", False, swUserDecision, longstatus
     Set Part = swApp.ActiveDoc

    Set swModelDocExt = Part.Extension
    Dim myModelView As SldWorks.ModelView
     Set myModelView = Part.ActiveView
     myModelView.FrameState = swWindowState_e.swWindowMaximized
     Part.SketchManager.InsertSketch True
     boolstatus = Part.Extension.SelectByID2("Front Plane", "PLANE", -6.92248508634211E-02, 3.92379182115397E-02, 9.87134779060705E-03, False, 0, Nothing, 0)
     Part.ClearSelection2 True
     Dim vSkLines As Variant
     vSkLines = Part.SketchManager.CreateCornerRectangle(-8.91172006155176E-02, 0.0314069429482, 0, -4.25302352423542E-02, 6.01966406507166E-03, 0)
     Part.ClearSelection2 True
     Part.SketchManager.InsertSketch True
     boolstatus = Part.Extension.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
     Part.ClearSelection2 True
     Dim skSegment As SldWorks.SketchSegment
     Set skSegment = Part.SketchManager.CreateCircle(0.009029, 0.03036, 0#, 0.021854, 0.019629, 0#)
     Part.ClearSelection2 True
     Part.SketchManager.InsertSketch True
     boolstatus = Part.Extension.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
     Part.ClearSelection2 True
     Set skSegment = Part.SketchManager.CreateEllipse(3.06284568434307E-02, 6.19756829649987E-03, 0, 3.09763470298606E-02, 9.97419305453208E-03, 0, 2.86971648691861E-02, 6.37547252792807E-03, 0)
     Part.ClearSelection2 True
     Part.SketchManager.InsertSketch True
     boolstatus = Part.Extension.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
     Part.ClearSelection2 True
     Set skSegment = Part.SketchManager.CreateEllipse(2.40620641310443E-02, 1.31240684851264E-02, 0, 7.71974468433887E-02, 7.06711158113391E-02, 0, 8.86560440335415E-04, 3.45228945826079E-02, 0)
     Part.ClearSelection2 True
     Part.SketchManager.InsertSketch True

    boolstatus = Part.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
     Part.ClearSelection2 True
     boolstatus = Part.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 4, Nothing, 0)
     Dim myFeature As SldWorks.Feature
     Set myFeature = Part.FeatureManager.FeatureExtrusion2(True, False, False, 0, 0, 0.00254, 0.00254, False, False, False, False, 1.74532925199433E-02, 1.74532925199433E-02, False, False, False, False, True, True, True, 0, 0, False)
     Part.SelectionManager.EnableContourSelection = False

    ' Start recording the SOLIDWORKS Undo object
     swModelDocExt.StartRecordingUndoObject
    boolstatus = Part.Extension.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, False, 4, Nothing, 0)
     Set myFeature = Part.FeatureManager.FeatureExtrusion2(True, False, False, 0, 0, 0.00254, 0.00254, False, False, False, False, 1.74532925199433E-02, 1.74532925199433E-02, False, False, False, False, True, True, True, 0, 0, False)
     Part.SelectionManager.EnableContourSelection = False
     boolstatus = Part.Extension.SelectByID2("Sketch4", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
     Set myFeature = Part.FeatureManager.FeatureExtrusion2(True, False, False, 0, 0, 0.00254, 0.00254, False, False, False, False, 1.74532925199433E-02, 1.74532925199433E-02, False, False, False, False, True, True, True, 0, 0, False)
     Part.SelectionManager.EnableContourSelection = False

    ' End recording the SOLIDWORKS Undo object with name "API Undo" and hide it in the Undo list
     swModelDocExt.FinishRecordingUndoObject2 "API Undo", True
    Part.ClearSelection2 True
     boolstatus = Part.Extension.SelectByID2("Sketch3", "SKETCH", 0, 0, 0, False, 4, Nothing, 0)
     Set myFeature = Part.FeatureManager.FeatureCut3(True, False, True, 0, 0, 0.00254, 0.00254, False, False, False, False, 1.74532925199433E-02, 1.74532925199433E-02, False, False, False, False, False, True, True, True, True, False, 0, 0, False)
     Part.SelectionManager.EnableContourSelection = False

End Sub
```
