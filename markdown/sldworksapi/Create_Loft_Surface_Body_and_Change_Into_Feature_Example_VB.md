---
title: "Create Loft Surface Body and Change Into Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Loft_Surface_Body_and_Change_Into_Feature_Example_VB.htm"
---

# Create Loft Surface Body and Change Into Feature Example (VBA)

This example shows how to create a loft surface body and change that body into a feature.

```
'---------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part document template
'    exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens a new part document.
' 2. Creates and selects sketches of two profiles and
'    a guide curve.
' 3. Creates a loft surface body.
' 4. Turns the loft surface body into a feature.
' 5. Examine the FeatureManager design tree and graphics area.
'--------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSketchMgr As SldWorks.SketchManager
Dim sketchSegment As SldWorks.sketchSegment
Dim swSelMgr As SldWorks.SelectionMgr
Dim sketchPoint As SldWorks.sketchPoint
Dim swFeatureMgr As SldWorks.FeatureManager
Dim refPlane As SldWorks.refPlane
Dim swFeat As SldWorks.Feature
Dim status As Boolean
Dim profiles As Variant
Dim guides As Variant
Dim profile(1) As SldWorks.Feature
Dim guideCurve(0) As SldWorks.Feature
Dim swModeler As SldWorks.Modeler
Dim swBody As SldWorks.Body2
Dim swPart As PartDoc
Dim vFeatures As Variant
```

```
Sub main()
    Set swApp = Application.SldWorks
```

```
    'Open new part document
    Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2016\templates\Part.prtdot", 0, 0, 0)
    Set swModelDocExt = swModel.Extension
```

```
    'Create closed profile
    status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    Set swSketchMgr = swModel.SketchManager
    Set sketchSegment = swSketchMgr.CreateCircle(0#, 0#, 0#, 0.021796, -0.030937, 0#)
    Set sketchPoint = swSketchMgr.CreatePoint(0.023454, 0.029699, 0#)
    swModel.ClearSelection2 True
    swSketchMgr.InsertSketch True
```

```
    'Create another closed profile
    status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, True, 0, Nothing, 0)
    Set swFeatureMgr = swModel.FeatureManager
    Set refPlane = swFeatureMgr.InsertRefPlane(8, 0.254, 0, 0, 0, 0)
    status = swModelDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    Set sketchSegment = swSketchMgr.CreateCircle(-0.035118, -0.014102, 0#, -0.025452, -0.02953, 0#)
    Set sketchPoint = swSketchMgr.CreatePoint(-0.018033, -0.020392, 0#)
    swModel.ClearSelection2 True
    swSketchMgr.InsertSketch True
```

```
    'Create guide curve
    status = swModelDocExt.SelectByID2("Point4@Sketch1", "EXTSKETCHPOINT", 2.34541440502721E-02, 2.96993303358475E-02, 0, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("Point5@Sketch2", "EXTSKETCHPOINT", -1.80330744027628E-02, -2.03923494843098E-02, 0, True, 0, Nothing, 0)
    swModel.ClearSelection2 True
    status = swModelDocExt.SelectByID2("Point4@Sketch1", "EXTSKETCHPOINT", 2.34541440502721E-02, 2.96993303358475E-02, 0, False, 1, Nothing, 0)
    status = swModelDocExt.SelectByID2("Point5@Sketch2", "EXTSKETCHPOINT", -1.80330744027628E-02, -2.03923494843098E-02, 0, True, 1, Nothing, 0)
    swModel.Insert3DSplineCurve False
    swModel.ClearSelection2 True
```

```
    'Select guide curve and profiles for loft feature
    status = swModelDocExt.SelectByID2("Curve1", "REFERENCECURVES", 0, 0, 0, False, 2, Nothing, 0)
    Set swSelMgr = swModel.SelectionManager
    Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
    Set guideCurve(0) = swFeat
    guides = guideCurve
    swModel.ClearSelection2 True
    status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 9.84860021145358E-03, 3.65397341178567E-02, 0, True, 1, Nothing, 0)
    Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
    Set profile(0) = swFeat
    swModel.ClearSelection2 True
    status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", -4.01969362026636E-02, 3.38231877308527E-03, 0, True, 1, Nothing, 0)
    Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
    Set profile(1) = swFeat
    profiles = profile
    swModel.ClearSelection2 True
```

```
    'Create loft surface body
    Set swModeler = swApp.GetModeler
    Set swBody = swModeler.CreateLoftBody2(swModel, profiles, guides, Nothing, False, 0, 0, 0, True, False, True, False, False, 1, 1, 1, True, True, 1, 1, False)
```

```
    'Turn loft surface body into a feature
    Set swPart = swModel
    vFeatures = swPart.CreateSurfaceFeatureFromBody(swBody, swCreateFeatureBodyOpts_e.swCreateFeatureBodyCheck)
```

```
    'Update the FeatureManager design tree
    swModel.EditRebuild3
```

```
    'Update graphics
    swModel.ViewZoomtofit2
```

```
End Sub
```
