---
title: "Update Plane Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Update_Plane_Example_VBNET.htm"
---

# Update Plane Example (VB.NET)

This example shows how to update a reference plane so that it is parallel to the screen.

```
'---------------------------------------------------------------------------
' Preconditions: Verify that the specified part template exists.
'
' Postconditions:
' 1. Creates Boss-Extrude1 and Plane1.
' 2. Rotates Boss-Extrude1.
' 3. Examine Plane1 in the graphics area.
' 4. Press F5.
' 5. Updates Plane1 so that it is parallel to the screen.
' 6. Examine Plane1 in the graphics area.
'---------------------------------------------------------------------------

Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSketchManager As SketchManager
        Dim swSketchSegment As SketchSegment
        Dim swFeatureManager As FeatureManager
        Dim swFeature As Feature
        Dim swSelectionMgr As SelectionMgr
        Dim swRefPlane As RefPlane
        Dim swModelView As ModelView
        Dim swRefPlaneFeatureData As RefPlaneFeatureData
        Dim status As Boolean

        'Create Boss-Extrude1 and Plane1
        swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2016\templates\part.prtdot", 0, 0, 0)
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        swSketchManager = swModel.SketchManager
        swSketchManager.InsertSketch(True)
        swSketchSegment = swSketchManager.CreateLine(-0.049503, 0.030205, 0.0#, -0.049503, 0.0#, 0.0#)
        swSketchSegment = swSketchManager.CreateLine(-0.049503, 0.0#, 0.0#, 0.0#, 0.0#, 0.0#)
        swSketchSegment = swSketchManager.CreateLine(0.0#, 0.0#, 0.0#, 0.0#, 0.019088, 0.0#)
        swSketchSegment = swSketchManager.CreateLine(0.0#, 0.019088, 0.0#, -0.03503, 0.037127, 0.0#)
        swSketchSegment = swSketchManager.CreateLine(-0.03503, 0.037127, 0.0#, -0.049503, 0.030205, 0.0#)
        swSketchManager.InsertSketch(True)
        swFeatureManager = swModel.FeatureManager
        swFeature = swFeatureManager.FeatureExtrusion3(True, False, False, 0, 0, 0.04, 0.01, False, False, False, False, 0.0174532925199433, 0.0174532925199433, False, False, False, False, True, True, True, 0, 0, False)
        swSelectionMgr = swModel.SelectionManager
        swSelectionMgr.EnableContourSelection = False
        status = swModelDocExt.SelectByID2("", "VERTEX", -0.0350298017733792, 0.0371273946939409, 0.04, True, 0, Nothing, 0)
        swRefPlane = swFeatureManager.InsertRefPlane(4096, 0, 0, 0, 0, 0)
        swModel.ClearSelection2(True)

        'Rotate Boss-Extrude1
        status = swModelDocExt.SelectByID2("Boss-Extrude1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
        swModelView = swModel.ActiveView
        swModelView.RotateAboutCenter(0, 0.00828812132228465)
        swModelView = swModel.ActiveView
        swModelView.RotateAboutCenter(0, 0.00828812132228465)
        swModelView = swModel.ActiveView
        swModelView.RotateAboutCenter(0.00576690959137988, 0)
        swModelView = swModel.ActiveView
        swModelView.RotateAboutCenter(0.00576690959137988, 0.0165762426445693)
        swModelView = swModel.ActiveView
        swModelView.RotateAboutCenter(0.00576690959137988, 0.00828812132228465)
        swModelView = swModel.ActiveView
        swModelView.RotateAboutCenter(0, 0.0165762426445693)
        swModelView = swModel.ActiveView
        swModelView.RotateAboutCenter(0.0115338191827598, 0.0248643639668539)
        swModelView = swModel.ActiveView
        swModelView.RotateAboutCenter(0.0115338191827598, 0.0331524852891386)
        swModelView = swModel.ActiveView
        swModelView.RotateAboutCenter(0.00576690959137988, 0.0248643639668539)
        swModelView = swModel.ActiveView
        swModelView.RotateAboutCenter(0.00576690959137988, 0.0165762426445693)
        swModelView = swModel.ActiveView
        swModelView.RotateAboutCenter(0, 0.0248643639668539)
        swModelView = swModel.ActiveView
        swModelView.RotateAboutCenter(0.00576690959137988, 0.0165762426445693)
        swModelView = swModel.ActiveView
        swModelView.RotateAboutCenter(0.00576690959137988, 0.0165762426445693)
        swModelView = swModel.ActiveView
        swModelView.RotateAboutCenter(0.00576690959137988, 0.0414406066114233)
        swModelView = swModel.ActiveView
        swModelView.RotateAboutCenter(0.00576690959137988, 0.0331524852891386)
        swModelView = swModel.ActiveView
        swModelView.RotateAboutCenter(0.00576690959137988, 0.0331524852891386)
        swModelView = swModel.ActiveView
        swModelView.RotateAboutCenter(0.0115338191827598, 0.0580168492559925)
        swModelView = swModel.ActiveView
        swModelView.RotateAboutCenter(0.00576690959137988, 0.0414406066114233)
        swModelView = swModel.ActiveView
        swModelView.RotateAboutCenter(0.00576690959137988, 0.0580168492559925)
        swModelView = swModel.ActiveView
        swModelView.RotateAboutCenter(0, 0.0663049705782772)
        swModelView = swModel.ActiveView
        swModelView.RotateAboutCenter(0.00576690959137988, 0.0663049705782772)
        swModelView = swModel.ActiveView
        swModelView.RotateAboutCenter(0.00576690959137988, 0.1077455771897)
        swModelView = swModel.ActiveView
        swModelView.RotateAboutCenter(0, 0.0994574558674158)
        swModelView = swModel.ActiveView
        swModelView.RotateAboutCenter(0, 0.0745930919005618)
        swModelView = swModel.ActiveView
        swModelView.RotateAboutCenter(0, 0.0911693345451311)
        swModelView = swModel.ActiveView
        swModelView.RotateAboutCenter(0, 0.0828812132228465)
        swModelView = swModel.ActiveView
        swModelView.RotateAboutCenter(0, 0.0745930919005618)
        swModelView = swModel.ActiveView
        swModelView.RotateAboutCenter(0, 0.0580168492559925)
        swModelView = swModel.ActiveView
        swModelView.RotateAboutCenter(0, 0.0248643639668539)
        swModelView = swModel.ActiveView
        swModelView.RotateAboutCenter(0, 0.00828812132228465)
        swModel.ClearSelection2(True)

        Stop
        'Examine Plane1
        'Press F5 to continue

        'Update Plane1 so that it is parallel to the screen
        status = swModelDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
        swRefPlaneFeatureData = swFeature.GetDefinition
        swRefPlaneFeatureData.UpdatePlane = True
        swFeature.ModifyDefinition(swRefPlaneFeatureData, swModel, Nothing)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
