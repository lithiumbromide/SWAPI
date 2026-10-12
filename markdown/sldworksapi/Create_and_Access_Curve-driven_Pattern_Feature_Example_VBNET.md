---
title: "Create and Access Curve-driven Pattern Feature Example (VB.NET()"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_and_Access_Curve-driven_Pattern_Feature_Example_VBNET.htm"
---

# Create and Access Curve-driven Pattern Feature Example (VB.NET()

## Create and Access Curve-driven Pattern Feature Example (VB.NET)

This example shows how to create a curve-driven pattern feature and access its data.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part to open exists.
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
        Dim swSketchSegment As SketchSegment
        Dim swFeatureMgr As FeatureManager
        Dim swFeature As Feature
        Dim swSelectionMgr As SelectionMgr
        Dim swCurveDrivenPatternFeatureData As CurveDrivenPatternFeatureData
        Dim swEntity As Entity
        Dim patternDirection As Object
        Dim fileName As String
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\tutorial\api\bagel.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

        'Sketch a circle and create a cut extrude
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("", "FACE", 0.0118560192339032, 0, 0.0566664535234693, False, 0, Nothing, 0)
        swSketchMgr = swModel.SketchManager
        swSketchMgr.InsertSketch(True)
        swSketchSegment = swSketchMgr.CreateCircle(-0.059172, -0.048012, 0.0#, -0.044189, -0.040533, 0.0#)
        swSketchMgr.InsertSketch(True)
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("Sketch6", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
        swFeatureMgr = swModel.FeatureManager
        swFeature = swFeatureMgr.FeatureCut3(True, False, False, 1, 0, 0.00254, 0.00254, False, False, False, False, 0.0174532925199433, 0.0174532925199433, False, False, False, False, False, True, True, True, True, False, 0, 0, False)
        swSelectionMgr = swModel.SelectionManager
        swSelectionMgr.EnableContourSelection = False
        swModel.ActivateSelectedFeature()
        status = swModelDocExt.SelectByID2("", "EDGE", 0.0115207253109588, -0.00000889643058599177, 0.0754182969300832, True, 0, Nothing, 0)
        swModel.ClearSelection2(True)

        'Create curve-driven pattern feature
        status = swModelDocExt.SelectByID2("Cut-Extrude2", "BODYFEATURE", 0, 0, 0, False, 4, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "EDGE", 0.0115207253109588, -0.00000889643058599177, 0.0754182969300832, True, 1, Nothing, 0)
```

```vb
        swCurveDrivenPatternFeatureData = swFeatureMgr.CreateDefinition(swFeatureNameID_e.swFmCurvePattern)

        swCurveDrivenPatternFeatureData.D1AlignmentMethod = 0
         swCurveDrivenPatternFeatureData.D1CurveMethod = 0
         swCurveDrivenPatternFeatureData.D1InstanceCount = 3
         swCurveDrivenPatternFeatureData.D1IsEqualSpaced = True
         swCurveDrivenPatternFeatureData.D1ReverseDirection = False
         swCurveDrivenPatternFeatureData.D1Spacing = 0.0254

        swFeature = swFeatureMgr.CreateFeature(swCurveDrivenPatternFeatureData)
```

```
        'Access the curve-driven pattern feature
        status = swModelDocExt.SelectByID2("CrvPattern1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
        swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
        swCurveDrivenPatternFeatureData = swFeature.GetDefinition
        status = swCurveDrivenPatternFeatureData.AccessSelections(swModel, Nothing)
        Debug.Print("Number of pattern instances in Direction 1: " & swCurveDrivenPatternFeatureData.D1InstanceCount)
        Debug.Print("Alignment method of Direction 1: " & swCurveDrivenPatternFeatureData.D1AlignmentMethod)
        Debug.Print("Curve method of Direction 1: " & swCurveDrivenPatternFeatureData.D1CurveMethod)
        patternDirection = swCurveDrivenPatternFeatureData.D1Direction
        swEntity = patternDirection
        Debug.Print("Pattern direction object type of Direction 1: " & swEntity.GetType)
        Debug.Print("Pattern instances spaced equally in Direction 1? " & swCurveDrivenPatternFeatureData.D1IsEqualSpaced)
        Debug.Print("Pattern direction reversed in Direction 1? " & swCurveDrivenPatternFeatureData.D1ReverseDirection)
        Debug.Print("Number of seed bodies in pattern: " & swCurveDrivenPatternFeatureData.GetPatternBodyCount)
        Debug.Print("Number of seed features in pattern: " & swCurveDrivenPatternFeatureData.GetPatternFeatureCount)
        swCurveDrivenPatternFeatureData.ReleaseSelectionAccess()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
