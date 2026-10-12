---
title: "Get and Add Sketch Points in Hole Wizard Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sketch_Points_in_Wizard_Hole_Example_VBNET.htm"
---

# Get and Add Sketch Points in Hole Wizard Feature Example (VB.NET)

This example shows how to get and add the sketch points in a Hole Wizard feature.

```
'------------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part document template exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Creates a new part document.
' 2. Creates Boss-Extrude1 and #0-80 Tapped Hole1 features.
' 3. Selects #8-80 Tapped Hole1; i.e., the Hole Wizard feature.
' 4. Gets the number of sketch points in the Hole Wizard feature.
' 5. Adds two sketch points to the Hole Wizard feature; thus, adds two more
'    holes to the Hole Wizard feature.
' 6. Examine the Immediate window and graphics area.
'-----------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSketchMgr As SketchManager
        Dim swFeatureMgr As FeatureManager
        Dim swFeature As Feature
        Dim swSelectionMgr As SelectionMgr
        Dim swWizardHoleFeatureData As WizardHoleFeatureData2
        Dim swSketchPoint As SketchPoint
        Dim sketchLines As Object
        Dim status As Boolean
        Dim count As Integer
        Dim points() As Object
        Dim point As Object

        'Create part with Hole Wizard feature
	swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2015\templates\Part.prtdot", 0, 0, 0)
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstToRectEntity, swUserPreferenceOption_e.swDetailingNoOptionSpecified, False)
        status = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, swUserPreferenceOption_e.swDetailingNoOptionSpecified, True)
        swSketchMgr = swModel.SketchManager
        sketchLines = swSketchMgr.CreateCornerRectangle(0, 0, 0, 0.0968848174375125, -0.0708129015764598, 0)
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Line4", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Line3", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
        swFeatureMgr = swModel.FeatureManager
        swFeature = swFeatureMgr.FeatureExtrusion2(True, False, False, 0, 0, 0.0254, 0.00254, False, False, False, False, 0.0174532925199433, 0.0174532925199433, False, False, False, False, True, True, True, 0, 0, False)
        swSelectionMgr = swModel.SelectionManager
        swSelectionMgr.EnableContourSelection = False
        status = swModelDocExt.SelectByID2("", "FACE", 0.0471052662929878, -0.0336338467782298, 0.0253999999998769, False, 0, Nothing, 0)
        swFeature = swFeatureMgr.HoleWizard5(4, 0, 27, "#0-80", 1, 0.00119126, 0.0254, 0.020066, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1, -1, -1, "2B", False, True, True, True, True, False)
        swModel.ViewZoomtofit2()
        status = swModelDocExt.SelectByID2("#0-80 Tapped Hole1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
        swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
        swModel.ClearSelection2(True)
        swWizardHoleFeatureData = swFeature.GetDefinition
        count = swWizardHoleFeatureData.GetSketchPointCount
        Debug.Print(" Number of sketch points in original Hole Wizard Feature = " & count)
        points = swWizardHoleFeatureData.GetSketchPoints
        For Each point In points
            swSketchPoint = point
            swSketchPoint.Select4(False, Nothing)
        Next
        status = swFeature.ModifyDefinition(swWizardHoleFeatureData, swModel, Nothing)
        swModel.ClearSelection2(True)

        'Select sketch point of Hole Wizard feature
        'and add two sketch points to Hole Wizard feature
        status = swModelDocExt.SelectByID2("Sketch3", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
        swSketchMgr.AddToDB = True
        swModel.EditSketch()
        swSketchPoint = swSketchMgr.CreatePoint(0.01, -0.04, 0)
        swSketchPoint = swSketchMgr.CreatePoint(0.01, -0.02, 0)
        swSketchMgr.InsertSketch(True)
        swSketchMgr.AddToDB = False
        swModel.ForceRebuild3(True)

        'Get number of sketch points in modified Hole Wizard feature
        status = swModelDocExt.SelectByID2("#0-80 Tapped Hole1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
        swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
        swModel.ClearSelection2(True)
        swWizardHoleFeatureData = swFeature.GetDefinition
        count = swWizardHoleFeatureData.GetSketchPointCount
        Debug.Print(" Number of sketch points in modified Hole Wizard Feature = " & count)
        points = swWizardHoleFeatureData.GetSketchPoints
        For Each point In points
            swSketchPoint = point
            swSketchPoint.Select4(False, Nothing)
        Next
        status = swFeature.ModifyDefinition(swWizardHoleFeatureData, swModel, Nothing)
        swModel.ClearSelection2(True)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
