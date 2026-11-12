---
title: "Insert Swept-boss Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Swept-boss_Feature_Example_VB.htm"
---

# Insert Swept-boss Feature Example (VBA)

This example shows how to create a swept-boss feature and get its guide curves.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the part template exists.
' 2. Open an Immediate window.
'
' Postconditions:
' 1. Creates a new part.
' 2. Creates a swept-boss feature.
' 3. Gets the number of guide curves in the feature.
' 4. Accesses the guide curves in the feature.
' 5. Gets the feature types of the guide curves.
' 6. Releases access to the sweep feature.
' 7. Examine the Immediate window.
'---------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSketchMgr As SldWorks.SketchManager
Dim swSketchSegment As SldWorks.SketchSegment
Dim swFeature As SldWorks.Feature
Dim swPathFeat As SldWorks.Feature
Dim swFeatureMgr As SldWorks.FeatureManager
Dim swSweepFeatureData As SldWorks.SweepFeatureData
Dim swSweep As SldWorks.SweepFeatureData
Dim pointArray As Variant
Dim points() As Double
Dim guideCurves As Variant
Dim guideCurve As Object
Dim nbrGuideCurves As Long
Dim status As Boolean
Dim i As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    'Create new model document
    Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2018\templates\Part.prtdot", 0, 0, 0)
    Set swModelDocExt = swModel.Extension
```

```
    'Sketch an ellipse for sweep profile
    swModel.ClearSelection2 True
    Set swSketchMgr = swModel.SketchManager
    status = swModelDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    swSketchMgr.InsertSketch True
    Set swSketchSegment = swSketchMgr.CreateEllipse(0, 0, 0, -0.064925207354862, 0, 0, 0, -3.60377802938881E-02, 0)
    swModel.ClearSelection2 True
    swSketchMgr.InsertSketch True
```

```
    'Sketch a line for sweep path
    status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    swSketchMgr.InsertSketch True
    Set swSketchSegment = swSketchMgr.CreateLine(0#, 0#, 0#, 0#, 0.059816, 0#)
    swModel.ClearSelection2 True
    swSketchMgr.InsertSketch True
```

```
    'Sketch a spline for sweep guide curve
    status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    swSketchMgr.InsertSketch True
```

```
    ReDim points(0 To 5) As Double
    points(0) = -0.064925207354862
    points(1) = 0
    points(2) = 0
    points(3) = -5.76005360247873E-03
    points(4) = 5.95205538922803E-02
    points(5) = 0
    pointArray = points
    Set swSketchSegment = swSketchMgr.CreateSpline((pointArray))
    swModel.ClearSelection2 True
```

```
    status = swModelDocExt.SelectByID2("Unknown", "MANIPULATOR", -4.81685228359519E-02, 1.68573405240843E-02, 0, False, 0, Nothing, 0)
    swModel.ClearSelection2 True
    swSketchMgr.InsertSketch True
    swModel.ViewZoomtofit2
```

```
    'Select the profile, path, and guide curve
    status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("Sketch3", "SKETCH", 0, 0, 0, True, 0, Nothing, 0)
    swModel.ClearSelection2 True
    status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 1, Nothing, 0)
    status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, True, 4, Nothing, 0)
    status = swModelDocExt.SelectByID2("Sketch3", "SKETCH", 0, 0, 0, True, 2, Nothing, 0)
```

```
    'Create the sweep feature
    Set swFeatureMgr = swModel.FeatureManager

    Set swSweep = swFeatureMgr.CreateDefinition(swFmSweep)

    swSweep.TangentPropagation = False
    swSweep.AlignWithEndFaces = False
    swSweep.TwistControlType = 0
    swSweep.MaintainTangency = False
    swSweep.AdvancedSmoothing = False
    swSweep.StartTangencyType = 0
    swSweep.EndTangencyType = 0
    swSweep.ThinFeature = False
    swSweep.SetWallThickness True, 0#
    swSweep.SetWallThickness False, 0#
    swSweep.ThinWallType = 0
    swSweep.PathAlignmentType = 0
    swSweep.Merge = True
    swSweep.FeatureScope = True
    swSweep.AutoSelect = True
    swSweep.SetTwistAngle 0#
    swSweep.MergeSmoothFaces = True
    swSweep.CircularProfile = False
    swSweep.CircularProfileDiameter = 0#
    swSweep.Direction = 0

    Set swPathFeat = swFeatureMgr.CreateFeature(swSweep)

    Debug.Print "Feature type: " & swPathFeat.GetTypeName2
```

```
    'Change the orientation of the view
    swModel.ShowNamedView2 "*Isometric", 7
```

```
    'Access sweep feature data, get guide curves,
    'get feature types of guide curves, and release
    'access to sweep feature
    Set swSweepFeatureData = swPathFeat.GetDefinition
    nbrGuideCurves = swSweepFeatureData.GetGuideCurvesCount
    Debug.Print ("  Number of guide curves: " & nbrGuideCurves)
    status = swSweepFeatureData.AccessSelections(swModel, Nothing)
    Debug.Print ("    Guide curve: ")
    guideCurves = swSweepFeatureData.guideCurves
    For i = 0 To (nbrGuideCurves - 1)
        Set guideCurve = guideCurves(i)
        Debug.Print ("      Type of feature as defined in swSelectType_e: " & swSweepFeatureData.GetGuideCurvesType(i))
    Next i
    swSweepFeatureData.ReleaseSelectionAccess
```

```
End Sub
```
