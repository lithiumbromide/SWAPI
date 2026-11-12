---
title: "Change Linear Pattern Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Linear_Pattern_Example_VBNET.htm"
---

# Change Linear Pattern Example (VB.NET)

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
        Dim swSelectionMgr As SelectionMgr
        Dim swSketchSegment As SketchSegment
        Dim swFeature As Feature
        Dim swLinearPatternFeatureData As LinearPatternFeatureData
        Dim sketchSegments As Object
        Dim status As Boolean
        Dim obj As Object
        Dim patternFeatures(0) As Object

        swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2015\templates\Part.prtdot", 0, 0, 0)
        swModelDocExt = swModel.Extension
        swSketchMgr = swModel.SketchManager
        swFeatureMgr = swModel.FeatureManager
        swSelectionMgr = swModel.SelectionManager

        'Create boss extrudes
        status = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstToRectEntity, swUserPreferenceOption_e.swDetailingNoOptionSpecified, False)
        status = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, swUserPreferenceOption_e.swDetailingNoOptionSpecified, True)
        sketchSegments = swSketchMgr.CreateCornerRectangle(0, 0, 0, -0.113876153512535, -0.101331667625686, 0)
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Line4", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Line3", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
        swFeature = swFeatureMgr.FeatureExtrusion3(True, False, False, 0, 0, 0.00254, 0.00254, False, False, False, False, 0.0174532925199433, 0.0174532925199433, False, False, False, False, True, True, True, 0, 0, False)
        swSelectionMgr.EnableContourSelection = False
        status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        swModel.ClearSelection2(True)
        swSketchSegment = swSketchMgr.CreateCircle(-0.105874, -0.015731, 0.0#, -0.099776, -0.0152, 0.0#)
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("Arc1", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
        swFeature = swFeatureMgr.FeatureExtrusion3(True, False, False, 0, 0, 0.01778, 0.00254, False, False, False, False, 0.0174532925199433, 0.0174532925199433, False, False, False, False, False, True, True, 0, 0, False)
        swSelectionMgr.EnableContourSelection = False
        status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        swModel.ClearSelection2(True)
        status = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstToRectEntity, swUserPreferenceOption_e.swDetailingNoOptionSpecified, False)
        status = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, swUserPreferenceOption_e.swDetailingNoOptionSpecified, True)
        sketchSegments = swSketchMgr.CreateCornerRectangle(-0.10892213539114, -0.0783168275860362, 0, -0.0879628279544704, -0.0928855015339991, 0)
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Line4", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Line3", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
        swFeature = swFeatureMgr.FeatureExtrusion3(True, False, False, 0, 0, 0.01778, 0.01778, False, False, False, False, 0.0174532925199433, 0.0174532925199433, False, False, False, False, False, True, True, 0, 0, False)
        swSelectionMgr.EnableContourSelection = False

        'Create linear pattern using Boss-Extrude2 as bodies pattern
        status = swModelDocExt.SelectByID2("", "EDGE", -0.091185205959107, -0.0000285588595829722, 0.00255940246768205, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Boss-Extrude2", "SOLIDBODY", 0, 0, 0, True, 0, Nothing, 0)
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("", "EDGE", -0.091185205959107, -0.0000285588595829722, 0.00255940246768205, True, 1, Nothing, 0)
        status = swModelDocExt.SelectByID2("Boss-Extrude2", "SOLIDBODY", 0, 0, 0, True, 256, Nothing, 0)
        swFeature = swFeatureMgr.FeatureLinearPattern4(3, 0.0254, 1, 0.00254, True, False, "NULL", "NULL", False, False, False, False, False, False, True, True, False, False, 0, 0)

        Stop
        'Examine the graphics area
        'Press F5

        'Select LPattern1
        'Get whether LPattern1 is a features and faces pattern or a bodies pattern
        status = swModelDocExt.SelectByID2("LPattern1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
        swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
        swLinearPatternFeatureData = swFeature.GetDefinition
        swLinearPatternFeatureData.AccessSelections(swModel, Nothing)
        Debug.Print("Original LPattern1 is a features and faces pattern or a bodies pattern (true if a bodies pattern)? " & swLinearPatternFeatureData.BodyPattern)

        'Change LPattern1 to features and faces pattern
        status = swModelDocExt.SelectByID2("Boss-Extrude3", "BODYFEATURE", 0, 0, 0, True, 0, Nothing, 0)
        obj = swSelectionMgr.GetSelectedObject6(1, 0)
        patternFeatures(0) = obj
        Dim patternFeaturesArray() As DispatchWrapper
        patternFeaturesArray = ObjectArrayToDispatchWrapperArray(patternFeatures)
        swLinearPatternFeatureData.BodyPattern = False
        swLinearPatternFeatureData.PatternFeatureArray = patternFeaturesArray
        swFeature.ModifyDefinition(swLinearPatternFeatureData, swModel, Nothing)

        'Get whether LPattern1 is a features and faces pattern or a bodies pattern
        Debug.Print("Modified LPattern1 is a features and faces pattern or a bodies pattern (false if a features and faces pattern)? " & swLinearPatternFeatureData.BodyPattern)

    End Sub

    Function ObjectArrayToDispatchWrapperArray(ByVal Objects As Object()) As DispatchWrapper()
        Dim ArraySize As Integer
        ArraySize = Objects.GetUpperBound(0)
        Dim d(ArraySize) As DispatchWrapper
        Dim ArrayIndex As Integer
        For ArrayIndex = 0 To ArraySize
            d(ArrayIndex) = New DispatchWrapper(Objects(ArrayIndex))
        Next
        Return d

    End Function

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
