---
title: "Create Body From Selected Faces Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Body_From_Selected_Faces_Example_VBNET.htm"
---

# Create Body From Selected Faces Example (VB.NET)

This example shows how to:

- use SOLIDWORKS geometry and topology methods to construct a temporary body from selected faces.
- create a solid body feature from the temporary body and a new part containing the solid body feature.

```
'------------------------------------------
' Preconditions:
' 1. Verify that the specified part document
'    template exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens a new part document and creates an
'    extruded thin feature.
' 2. Selects connecting faces on the extruded thin feature.
' 3. Knits the faces into a solid, creates a
'    a new part, and inserts the solid as an imported
'    solid body feature.
' 4. Examine the Immediate window, graphics area,
'    FeatureManager design tree, and document name
'    in the SOLIDWORKS menu bar.
'-------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSketchManager As SketchManager
        Dim swSketchSegment As SketchSegment
        Dim swFeatureManager As FeatureManager
        Dim swFeature As Feature
        Dim swPart As PartDoc
        Dim swNewPart As PartDoc
        Dim swModeler As Modeler
        Dim swSelMgr As SelectionMgr
        Dim swSelFace() As Face2
        Dim vFaceList As Object
        Dim swBody As Body2
        Dim swNewBody As Body2
        Dim swFeat As Feature
        Dim nSelCount As Integer
        Dim i As Integer
        Dim bRet As Boolean

        'Create part and select connecting faces
        swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2015\templates\Part.prtdot", 0, 0, 0)
        swSketchManager = swModel.SketchManager
        swSketchManager.InsertSketch(True)
        swSketchSegment = swSketchManager.CreateLine(0.0#, 0.0#, 0.0#, -0.062359, 0.0#, 0.0#)
        swSketchSegment = swSketchManager.CreateLine(-0.062359, 0.0#, 0.0#, -0.020485, 0.066264, 0.0#)
        swSketchSegment = swSketchManager.CreateLine(-0.020485, 0.066264, 0.0#, 0.0#, 0.0#, 0.0#)
        swModel.ClearSelection2(True)
        swFeatureManager = swModel.FeatureManager
        swFeature = swFeatureManager.FeatureExtrusionThin2(True, False, False, 0, 0, 0.03048, 0.00254, False, False, False, False, 0.0174532925199433, 0.0174532925199433, False, False, False, False, True, 0.00254, 0.00254, 0.00254, 0, 0, False, 0.005, True, True, 0, 0, False)
        swSelMgr = swModel.SelectionManager
        swSelMgr.EnableContourSelection = False
        swModel.ClearSelection2(True)
        swModelDocExt = swModel.Extension
        bRet = swModelDocExt.SelectByID2("", "FACE", -0.0484137409629284, 0, 0.018103012393226, True, 0, Nothing, 0)
        bRet = swModelDocExt.SelectByID2("", "FACE", -0.0396839112014504, 0.035882458904041, 0.0207108765403632, True, 0, Nothing, 0)
        bRet = swModelDocExt.SelectByID2("", "FACE", -0.0175462018075336, 0.0567577015655729, 0.021527257415471, True, 0, Nothing, 0)

        'Get the selected faces
        swModeler = swApp.GetModeler
        nSelCount = swSelMgr.GetSelectedObjectCount
        ReDim swSelFace(nSelCount - 1)
        For i = 1 To nSelCount
            swSelFace(i - 1) = swSelMgr.GetSelectedObject6(i, -1)
        Next
        vFaceList = swSelFace

        'Create solid body feature using selected faces
        swPart = swModel
        swBody = swPart.CreateNewBody
        swNewBody = swBody.CreateBodyFromFaces(nSelCount, (vFaceList))
        If swNewBody Is Nothing Then
            Debug.Print("Failed to create solid body from selected faces.")
            Exit Sub
        Else
            Debug.Print("Solid body and new part can be created from selected faces.")
        End If

        'Open new part and force creation of solid body feature
        swNewPart = swApp.NewPart
        swFeat = swNewPart.CreateFeatureFromBody3(swNewBody, False, swCreateFeatureBodyOpts_e.swCreateFeatureBodyCheck + swCreateFeatureBodyOpts_e.swCreateFeatureBodySimplify)
        If Not swFeat Is Nothing Then
            Debug.Print("New part with imported solid body created.")
        Else
            Debug.Print("New part with imported solid body not created.")
        End If

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
