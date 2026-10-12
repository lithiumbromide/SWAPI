---
title: "Change Linear Pattern Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Linear_Pattern_Example_VB.htm"
---

# Change Linear Pattern Example (VBA)

This example shows how to change a linear pattern from a bodies to a features and faces pattern.

```
'-----------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part template exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens a new part.
' 2. Creates three boss extrude features.
' 3. Creates a linear pattern using Boss-Extrude2 as a bodies
'    pattern.
' 4. Examine the graphics area and press F5.
' 5. Changes the linear pattern to use Boss-Extrude3 as a
'    features and faces pattern.
' 6. Examine the Immediate window and graphics area.
'------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSketchMgr As SldWorks.SketchManager
Dim swFeatureMgr As SldWorks.FeatureManager
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swSketchSegment as SldWorks.SketchSegment
Dim swFeature As SldWorks.Feature
Dim swLinearPatternFeatureData As SldWorks.LinearPatternFeatureData
Dim sketchSegments As Variant
Dim status As Boolean
Dim obj As Object
Dim patternFeatures(0) As Object
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2015\templates\Part.prtdot", 0, 0, 0)
    Set swModelDocExt = swModel.Extension
    Set swSketchMgr = swModel.SketchManager
    Set swFeatureMgr = swModel.FeatureManager
    Set swSelectionMgr = swModel.SelectionManager
```

```
    'Create boss extrudes
    status = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstToRectEntity, swUserPreferenceOption_e.swDetailingNoOptionSpecified, False)
    status = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, swUserPreferenceOption_e.swDetailingNoOptionSpecified, True)
    sketchSegments = swSketchMgr.CreateCornerRectangle(0, 0, 0, -0.113876153512535, -0.101331667625686, 0)
    swModel.ClearSelection2 True
    status = swModelDocExt.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("Line4", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("Line3", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
    Set swFeature = swFeatureMgr.FeatureExtrusion3(True, False, False, 0, 0, 0.00254, 0.00254, False, False, False, False, 1.74532925199433E-02, 1.74532925199433E-02, False, False, False, False, True, True, True, 0, 0, False)
    swSelectionMgr.EnableContourSelection = False
    status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    swModel.ClearSelection2 True
    Set swSketchSegment = swSketchMgr.CreateCircle(-0.105874, -0.015731, 0#, -0.099776, -0.0152, 0#)
    swModel.ClearSelection2 True
    status = swModelDocExt.SelectByID2("Arc1", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
    Set swFeature = swFeatureMgr.FeatureExtrusion3(True, False, False, 0, 0, 0.01778, 0.00254, False, False, False, False, 1.74532925199433E-02, 1.74532925199433E-02, False, False, False, False, False, True, True, 0, 0, False)
    swSelectionMgr.EnableContourSelection = False
    status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    swModel.ClearSelection2 True
    status = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstToRectEntity, swUserPreferenceOption_e.swDetailingNoOptionSpecified, False)
    status = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, swUserPreferenceOption_e.swDetailingNoOptionSpecified, True)
    sketchSegments = swSketchMgr.CreateCornerRectangle(-0.10892213539114, -7.83168275860362E-02, 0, -8.79628279544704E-02, -9.28855015339991E-02, 0)
    swModel.ClearSelection2 True
    status = swModelDocExt.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("Line4", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("Line3", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
    Set swFeature = swFeatureMgr.FeatureExtrusion3(True, False, False, 0, 0, 0.01778, 0.01778, False, False, False, False, 1.74532925199433E-02, 1.74532925199433E-02, False, False, False, False, False, True, True, 0, 0, False)
    swSelectionMgr.EnableContourSelection = False
```

```
    'Create linear pattern using Boss-Extrude2 as bodies pattern
    status = swModelDocExt.SelectByID2("", "EDGE", -0.091185205959107, -2.85588595829722E-05, 2.55940246768205E-03, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("Boss-Extrude2", "SOLIDBODY", 0, 0, 0, True, 0, Nothing, 0)
    swModel.ClearSelection2 True
    status = swModelDocExt.SelectByID2("", "EDGE", -0.091185205959107, -2.85588595829722E-05, 2.55940246768205E-03, True, 1, Nothing, 0)
    status = swModelDocExt.SelectByID2("Boss-Extrude2", "SOLIDBODY", 0, 0, 0, True, 256, Nothing, 0)
    Set swFeature = swFeatureMgr.FeatureLinearPattern4(3, 0.0254, 1, 0.00254, True, False, "NULL", "NULL", False, False, False, False, False, False, True, True, False, False, 0, 0)
```

```
    Stop
    'Examine the graphics area
    'Press F5
```

```
    'Select LPattern1
    'Get whether LPattern1 is a features and faces pattern or a bodies pattern
    status = swModelDocExt.SelectByID2("LPattern1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
    Set swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
    Set swLinearPatternFeatureData = swFeature.GetDefinition
    swLinearPatternFeatureData.AccessSelections swModel, Nothing
    Debug.Print "Original LPattern1 is a features and faces pattern or a bodies pattern (true if a bodies pattern)? " & swLinearPatternFeatureData.BodyPattern
```

```
    'Change LPattern1 to features and faces pattern
    status = swModelDocExt.SelectByID2("Boss-Extrude3", "BODYFEATURE", 0, 0, 0, True, 0, Nothing, 0)
    Set obj = swSelectionMgr.GetSelectedObject6(1, 0)
    Set patternFeatures(0) = obj
    swLinearPatternFeatureData.BodyPattern = False
    swLinearPatternFeatureData.PatternFeatureArray = patternFeatures
```

```
    swFeature.ModifyDefinition swLinearPatternFeatureData, swModel, Nothing
```

```
    'Get whether LPattern1 is a features and faces pattern or a bodies pattern
    Debug.Print "Modified LPattern1 is a features and faces pattern or a bodies pattern (false if a features and faces pattern)? " & swLinearPatternFeatureData.BodyPattern
```

```
End Sub
```
