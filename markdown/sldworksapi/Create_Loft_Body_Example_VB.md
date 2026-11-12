---
title: "Create Loft Body Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Loft_Body_Example_VB.htm"
---

# Create Loft Body Example (VBA)

This example shows how to create a temporary loft body using [IModeler::CreateLoftBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateLoftBody2.html).

```
'-----------------------------------------------------
' Preconditions:
' 1. Verify that the specified part document template
'    exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens a new part document.
' 2. Creates and selects sketches of two profiles and
'    a guide curve.
' 3. Creates a temporary loft body.
' 4. Examine the Immediate window and graphics area.
'-----------------------------------------------------
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
Dim count As Long
Dim featArr As Variant
Dim i As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks

    'Open new part document
    Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2015\templates\Part.prtdot", 0, 0, 0)
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
    Debug.Print "Guide curve name: " & swFeat.Name
    Set guideCurve(0) = swFeat
    guides = guideCurve
    swModel.ClearSelection2 True
    status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 9.84860021145358E-03, 3.65397341178567E-02, 0, True, 1, Nothing, 0)
    Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
    Debug.Print "Profile name: " & swFeat.Name
    Set profile(0) = swFeat
    swModel.ClearSelection2 True
    status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", -4.01969362026636E-02, 3.38231877308527E-03, 0, True, 1, Nothing, 0)
    Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
    Debug.Print "Profile name: " & swFeat.Name
    Set profile(1) = swFeat
    profiles = profile
    swModel.ClearSelection2 True
```

```
    'Create temporary loft body
    Set swModeler = swApp.GetModeler
    Set swBody = swModeler.CreateLoftBody2(swModel, profiles, guides, Nothing, False, 0, 0, 0, True, False, True, False, True, 1, 1, 1, True, True, 1, 1, False)
```

```
    ' Test whether the loft body is a temporary body
    status = swBody.IsTemporaryBody
    Debug.Print "Is the loft body a temporary body?  " & status
    If status Then
        ' Display the temporary loft body
        swBody.Display3 swModel, 256, swTempBodySelectOptions_e.swTempBodySelectOptionNone
        Debug.Print "Temporary loft body displayed; examine the graphics area."
    Else
        Debug.Print "Temporary loft body was not created."
    End If
```

```
    Debug.Print ""
```

```
    'Verify that the temporary loft body is not a loft feature
    'by examining the list of features printed to the
    'Immediate window
    count = swFeatureMgr.GetFeatureCount(False)
    featArr = swFeatureMgr.GetFeatures(False)
    For i = 0 To count - 1
        Set swFeat = featArr(i)
        Debug.Print swFeat.Name
    Next i
```

```
    swModel.ViewZoomtofit2
```

```
End Sub
```
