---
title: "Get and Add Sketch Points in Hole Wizard Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sketch_Points_in_Wizard_Hole_Example_VB.htm"
---

# Get and Add Sketch Points in Hole Wizard Feature Example (VBA)

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
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSketchMgr As SldWorks.SketchManager
Dim swFeatureMgr As SldWorks.FeatureManager
Dim swFeature As SldWorks.Feature
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swWizardHoleFeatureData As SldWorks.WizardHoleFeatureData2
Dim swSketchPoint As SldWorks.SketchPoint
Dim sketchLines As Variant
Dim status As Boolean
Dim count As Long
Dim points As Variant
Dim point As Variant
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    'Create part with Hole Wizard feature
    Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2015\templates\Part.prtdot", 0, 0, 0)
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstToRectEntity, swUserPreferenceOption_e.swDetailingNoOptionSpecified, False)
    status = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, swUserPreferenceOption_e.swDetailingNoOptionSpecified, True)
    Set swSketchMgr = swModel.SketchManager
    sketchLines = swSketchMgr.CreateCornerRectangle(0, 0, 0, 9.68848174375125E-02, -7.08129015764598E-02, 0)
    swModel.ClearSelection2 True
    status = swModelDocExt.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("Line4", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("Line3", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
    Set swFeatureMgr = swModel.FeatureManager
    Set swFeature = swFeatureMgr.FeatureExtrusion2(True, False, False, 0, 0, 0.0254, 0.00254, False, False, False, False, 1.74532925199433E-02, 1.74532925199433E-02, False, False, False, False, True, True, True, 0, 0, False)
    Set swSelectionMgr = swModel.SelectionManager
    swSelectionMgr.EnableContourSelection = False
    status = swModelDocExt.SelectByID2("", "FACE", 4.71052662929878E-02, -3.36338467782298E-02, 2.53999999998769E-02, False, 0, Nothing, 0)
    Set swFeature = swFeatureMgr.HoleWizard5(4, 0, 27, "#0-80", 1, 0.00119126, 0.0254, 0.020066, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1, -1, -1, "2B", False, True, True, True, True, False)
    swModel.ViewZoomtofit2
```

```
    status = swModelDocExt.SelectByID2("#0-80 Tapped Hole1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
    Set swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
    swModel.ClearSelection2 True
    Set swWizardHoleFeatureData = swFeature.GetDefinition
    count = swWizardHoleFeatureData.GetSketchPointCount
    Debug.Print " Number of sketch points in original Hole Wizard Feature = " & count
    points = swWizardHoleFeatureData.GetSketchPoints
    For Each point In points
        Set swSketchPoint = point
        swSketchPoint.Select4 False, Nothing
    Next
    status = swFeature.ModifyDefinition(swWizardHoleFeatureData, swModel, Nothing)
    swModel.ClearSelection2 True
```

```
    'Select sketch point of Hole Wizard feature
    'and add two sketch points to Hole Wizard feature
    status = swModelDocExt.SelectByID2("Sketch3", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
    swSketchMgr.AddToDB = True
    swModel.EditSketch
    Set swSketchPoint = swSketchMgr.CreatePoint(0.01, -0.04, 0)
    Set swSketchPoint = swSketchMgr.CreatePoint(0.01, -0.02, 0)
    swSketchMgr.InsertSketch True
    swSketchMgr.AddToDB = False
    swModel.ForceRebuild3 True
```

```
    'Get number of sketch points in modified Hole Wizard feature
    status = swModelDocExt.SelectByID2("#0-80 Tapped Hole1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
    Set swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
    swModel.ClearSelection2 True
    Set swWizardHoleFeatureData = swFeature.GetDefinition
    count = swWizardHoleFeatureData.GetSketchPointCount
    Debug.Print " Number of sketch points in modified Hole Wizard Feature = " & count
    points = swWizardHoleFeatureData.GetSketchPoints
    For Each point In points
        Set swSketchPoint = point
        swSketchPoint.Select4 False, Nothing
    Next
    status = swFeature.ModifyDefinition(swWizardHoleFeatureData, swModel, Nothing)
    swModel.ClearSelection2 True
```

```
End Sub
```
