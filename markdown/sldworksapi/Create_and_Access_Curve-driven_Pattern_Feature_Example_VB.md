---
title: "Create and Access Curve-driven Pattern Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_and_Access_Curve-driven_Pattern_Feature_Example_VB.htm"
---

# Create and Access Curve-driven Pattern Feature Example (VBA)

This example shows how to create a curve-driven pattern feature and access its data.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part document to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified part document.
' 2. Creates a cut extrude feature.
' 3. Creates a curve-driven pattern feature using the
'    the cut extrude feature.
' 4. Gets curve-driven pattern feature data.
' 5. Examine the FeatureManager design tree, graphics area,
'    and Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'--------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSketchMgr As SldWorks.SketchManager
Dim swSketchSegment As SldWorks.SketchSegment
Dim swFeatureMgr As SldWorks.FeatureManager
Dim swFeature As SldWorks.Feature
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swCurveDrivenPatternFeatureData As SldWorks.CurveDrivenPatternFeatureData
Dim swEntity As SldWorks.Entity
Dim patternDirection As Object
Dim fileName As String
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\tutorial\api\bagel.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
```

```
    'Sketch a circle and create a cut extrude
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("", "FACE", 1.18560192339032E-02, 0, 5.66664535234693E-02, False, 0, Nothing, 0)
    Set swSketchMgr = swModel.SketchManager
    swSketchMgr.InsertSketch True
    Set swSketchSegment = swSketchMgr.CreateCircle(-0.059172, -0.048012, 0#, -0.044189, -0.040533, 0#)
    swSketchMgr.InsertSketch True
    swModel.ClearSelection2 True
    status = swModelDocExt.SelectByID2("Sketch6", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
    Set swFeatureMgr = swModel.FeatureManager
    Set swFeature = swFeatureMgr.FeatureCut3(True, False, False, 1, 0, 0.00254, 0.00254, False, False, False, False, 1.74532925199433E-02, 1.74532925199433E-02, False, False, False, False, False, True, True, True, True, False, 0, 0, False)
    Set swSelectionMgr = swModel.SelectionManager
    swSelectionMgr.EnableContourSelection = False
    swModel.ActivateSelectedFeature
    status = swModelDocExt.SelectByID2("", "EDGE", 1.15207253109588E-02, -8.89643058599177E-06, 7.54182969300832E-02, True, 0, Nothing, 0)
    swModel.ClearSelection2 True
```

```
    'Create curve-driven pattern feature
    status = swModelDocExt.SelectByID2("Cut-Extrude2", "BODYFEATURE", 0, 0, 0, False, 4, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "EDGE", 1.15207253109588E-02, -8.89643058599177E-06, 7.54182969300832E-02, True, 1, Nothing, 0)
```

```vb
    Set swCurveDrivenPatternFeatureData = swFeatureMgr.CreateDefinition(swFmCurvePattern)

    swCurveDrivenPatternFeatureData.D1AlignmentMethod = 0
     swCurveDrivenPatternFeatureData.D1CurveMethod = 0
     swCurveDrivenPatternFeatureData.D1InstanceCount = 3
     swCurveDrivenPatternFeatureData.D1IsEqualSpaced = True
     swCurveDrivenPatternFeatureData.D1ReverseDirection = False
     swCurveDrivenPatternFeatureData.D1Spacing = 0.0254

    Set swFeature = swFeatureMgr.CreateFeature(swCurveDrivenPatternFeatureData)
```

```
    'Access the curve-driven pattern feature
    status = swModelDocExt.SelectByID2("CrvPattern1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
    Set swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
    Set swCurveDrivenPatternFeatureData = swFeature.GetDefinition
    status = swCurveDrivenPatternFeatureData.AccessSelections(swModel, Nothing)
        Debug.Print "Number of pattern instances in Direction 1: " & swCurveDrivenPatternFeatureData.D1InstanceCount
        Debug.Print "Alignment method of Direction 1: " & swCurveDrivenPatternFeatureData.D1AlignmentMethod
        Debug.Print "Curve method of Direction 1: " & swCurveDrivenPatternFeatureData.D1CurveMethod
        Set patternDirection = swCurveDrivenPatternFeatureData.D1Direction
        Set swEntity = patternDirection
        Debug.Print "Pattern direction object type of Direction 1: " & swEntity.GetType
        Debug.Print "Pattern instances spaced equally in Direction 1? " & swCurveDrivenPatternFeatureData.D1IsEqualSpaced
        Debug.Print "Pattern direction reversed in Direction 1? " & swCurveDrivenPatternFeatureData.D1ReverseDirection
        Debug.Print "Number of seed bodies in pattern: " & swCurveDrivenPatternFeatureData.GetPatternBodyCount
        Debug.Print "Number of seed features in pattern: " & swCurveDrivenPatternFeatureData.GetPatternFeatureCount
    swCurveDrivenPatternFeatureData.ReleaseSelectionAccess
```

```
End Sub
```
