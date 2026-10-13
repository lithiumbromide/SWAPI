---
title: "Create Loft Body Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Loft_Body_Example_VBNET.htm"
---

# Create Loft Body Example (VB.NET)

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
        Dim sketchSegment As SketchSegment
        Dim swSelMgr As SelectionMgr
        Dim sketchPoint As SketchPoint
        Dim swFeatureMgr As FeatureManager
        Dim refPlane As RefPlane
        Dim swFeat As Feature
        Dim status As Boolean
        Dim profiles As Object
        Dim guides As Object
        Dim profile(1) As Feature
        Dim guideCurve(0) As Feature
        Dim swModeler As Modeler
        Dim swBody As Body2
        Dim count As Integer
        Dim featArr As Object
        Dim i As Integer

        'Open new part document
        swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2015\templates\Part.prtdot", 0, 0, 0)
        swModelDocExt = swModel.Extension

        'Create closed profile
        status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        swSketchMgr = swModel.SketchManager
        sketchSegment = swSketchMgr.CreateCircle(0.0#, 0.0#, 0.0#, 0.021796, -0.030937, 0.0#)
        sketchPoint = swSketchMgr.CreatePoint(0.023454, 0.029699, 0.0#)
        swModel.ClearSelection2(True)
        swSketchMgr.InsertSketch(True)

        'Create another closed profile
        status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, True, 0, Nothing, 0)
        swFeatureMgr = swModel.FeatureManager
        refPlane = swFeatureMgr.InsertRefPlane(8, 0.254, 0, 0, 0, 0)
        status = swModelDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        sketchSegment = swSketchMgr.CreateCircle(-0.035118, -0.014102, 0.0#, -0.025452, -0.02953, 0.0#)
        sketchPoint = swSketchMgr.CreatePoint(-0.018033, -0.020392, 0.0#)
        swModel.ClearSelection2(True)
        swSketchMgr.InsertSketch(True)

        'Create guide curve
        status = swModelDocExt.SelectByID2("Point4@Sketch1", "EXTSKETCHPOINT", 0.0234541440502721, 0.0296993303358475, 0, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Point5@Sketch2", "EXTSKETCHPOINT", -0.0180330744027628, -0.0203923494843098, 0, True, 0, Nothing, 0)
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("Point4@Sketch1", "EXTSKETCHPOINT", 0.0234541440502721, 0.0296993303358475, 0, False, 1, Nothing, 0)
        status = swModelDocExt.SelectByID2("Point5@Sketch2", "EXTSKETCHPOINT", -0.0180330744027628, -0.0203923494843098, 0, True, 1, Nothing, 0)
        swModel.Insert3DSplineCurve(False)
        swModel.ClearSelection2(True)

        'Select guide curve and profiles for loft feature
        status = swModelDocExt.SelectByID2("Curve1", "REFERENCECURVES", 0, 0, 0, False, 2, Nothing, 0)
        swSelMgr = swModel.SelectionManager
        swFeat = swSelMgr.GetSelectedObject6(1, -1)
        Debug.Print("Guide curve name: " & swFeat.Name)
        guideCurve(0) = swFeat
        guides = guideCurve
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0.00984860021145358, 0.0365397341178567, 0, True, 1, Nothing, 0)
        swFeat = swSelMgr.GetSelectedObject6(1, -1)
        Debug.Print("Profile name: " & swFeat.Name)
        profile(0) = swFeat
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", -0.0401969362026636, 0.00338231877308527, 0, True, 1, Nothing, 0)
        swFeat = swSelMgr.GetSelectedObject6(1, -1)
        Debug.Print("Profile name: " & swFeat.Name)
        profile(1) = swFeat
        profiles = profile
        swModel.ClearSelection2(True)

        'Create temporary loft body
        swModeler = swApp.GetModeler
        swBody = swModeler.CreateLoftBody2(swModel, profiles, guides, Nothing, False, 0, 0, 0, True, False, True, False, True, 1, 1, 1, True, True, 1, 1, False)

        ' Test whether the loft body is a temporary body
        status = swBody.IsTemporaryBody
        Debug.Print("Is the loft body a temporary body?  " & status)
        If status Then
            ' Display the temporary loft body
            swBody.Display3(swModel, 256, swTempBodySelectOptions_e.swTempBodySelectOptionNone)
            Debug.Print("Temporary loft body displayed; examine the graphics area.")
        Else
            Debug.Print("Temporary loft body was not created.")
        End If

        Debug.Print("")

        'Verify that the temporary loft body is not a loft feature
        'by examining the list of features printed to the
        'Immediate window
        count = swFeatureMgr.GetFeatureCount(False)
        featArr = swFeatureMgr.GetFeatures(False)
        For i = 0 To count - 1
            swFeat = featArr(i)
            Debug.Print(swFeat.Name)
        Next i

        swModel.ViewZoomtofit2()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
