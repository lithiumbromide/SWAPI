---
title: "Get Guide Curves in Sweep Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Guide_Curves_in_Sweep_Feature_Example_VBNET.htm"
---

# Get Guide Curves in Sweep Feature Example (VB.NET)

This example shows how to get the guide curves in a sweep feature.

'----------------------------------------
' Preconditions:
' 1. Verify that the part template exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Creates a new part document.
' 2. Creates a sweep feature.
' 3. Gets the number of guide curves in the sweep
' feature.
' 4. Accesses the guide curves in the sweep feature.
' 5. Gets the feature types of the guide curves.
' 6. Releases access of the sweep feature.
' 7. Examine the Immediate window.
'----------------------------------------

```
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
        Dim swFeature As Feature
        Dim swFeatureMgr As FeatureManager
        Dim swSweepFeatureData As SweepFeatureData
        Dim pointArray As Object
        Dim points() As Double
        Dim guideCurves As Object
        Dim guideCurve As Object
        Dim nbrGuideCurves As Integer
        Dim status As Boolean
        Dim i As Integer

        'Create new model document
        swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2017\templates\Part.prtdot", 0, 0, 0)
        swModelDocExt = swModel.Extension

        'Sketch an ellipse for sweep profile
        swModel.ClearSelection2(True)
        swSketchMgr = swModel.SketchManager
        status = swModelDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        swSketchMgr.InsertSketch(True)
        swSketchSegment = swSketchMgr.CreateEllipse(0, 0, 0, -0.064925207354862, 0, 0, 0, -0.0360377802938881, 0)
        swModel.ClearSelection2(True)
        swSketchMgr.InsertSketch(True)

        'Sketch a line for sweep path
        status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        swSketchMgr.InsertSketch(True)
        swSketchSegment = swSketchMgr.CreateLine(0.0#, 0.0#, 0.0#, 0.0#, 0.059816, 0.0#)
        swModel.ClearSelection2(True)
        swSketchMgr.InsertSketch(True)

        'Sketch a spline for sweep guide curve
        status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        swSketchMgr.InsertSketch(True)
        ReDim points(5)
        points(0) = -0.064925207354862
        points(1) = 0
        points(2) = 0
        points(3) = -0.00576005360247873
        points(4) = 0.0595205538922803
        points(5) = 0
        pointArray = points
        swSketchSegment = swSketchMgr.CreateSpline((pointArray))
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("Unknown", "MANIPULATOR", -0.0481685228359519, 0.0168573405240843, 0, False, 0, Nothing, 0)
        swModel.ClearSelection2(True)
        swSketchMgr.InsertSketch(True)
        swModel.ViewZoomtofit2()

        'Select the profile, path, and guide curve
        status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Sketch3", "SKETCH", 0, 0, 0, True, 0, Nothing, 0)
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 1, Nothing, 0)
        status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, True, 4, Nothing, 0)
        status = swModelDocExt.SelectByID2("Sketch3", "SKETCH", 0, 0, 0, True, 2, Nothing, 0)

        'Create the sweep feature
        swFeatureMgr = swModel.FeatureManager
        swFeature = swFeatureMgr.InsertProtrusionSwept4(False, False, swTwistControlType_e.swTwistControlFollowPath, False, False, swTangencyType_e.swTangencyNone, swTangencyType_e.swTangencyNone, False, 0, 0, swThinWallType_e.swThinWallOneDirection, 0, True, True, True, 0, True, False, 0, 0)
        Debug.Print("Feature type: " & swFeature.GetTypeName2)

        'Change the orientation of the view
        swModel.ShowNamedView2("*Isometric", 7)

        'Access sweep feature data, get guide curves,
        'get feature type of guide curves, and release
        'access to sweep feature
        swSweepFeatureData = swFeature.GetDefinition
        nbrGuideCurves = swSweepFeatureData.GetGuideCurvesCount
        Debug.Print("  Number of guide curves: " & nbrGuideCurves)
        status = swSweepFeatureData.AccessSelections(swModel, Nothing)
        Debug.Print("    Guide curve: ")
        guideCurves = swSweepFeatureData.GuideCurves
        For i = 0 To (nbrGuideCurves - 1)
            guideCurve = guideCurves(i)
            Debug.Print("      Type of feature as defined in swSelectType_e: " & swSweepFeatureData.GetGuideCurvesType(i))
        Next i
        swSweepFeatureData.ReleaseSelectionAccess()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
