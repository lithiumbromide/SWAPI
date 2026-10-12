---
title: "Create Body From Selected Faces Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Body_From_Selected_Faces_Example_VB.htm"
---

# Create Body From Selected Faces Example (VBA)

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
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim swSketchManager As SldWorks.SketchManager
    Dim swSketchSegment As SldWorks.SketchSegment
    Dim swFeatureManager As SldWorks.FeatureManager
    Dim swFeature As SldWorks.Feature
    Dim swPart As SldWorks.PartDoc
    Dim swNewPart As SldWorks.PartDoc
    Dim swModeler As SldWorks.Modeler
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swSelFace() As SldWorks.Face2
    Dim vFaceList As Variant
    Dim swBody As SldWorks.Body2
    Dim swNewBody As SldWorks.Body2
    Dim swFeat As SldWorks.Feature
    Dim nSelCount As Long
    Dim i As Long
    Dim bRet As Boolean
```

```
    Set swApp = CreateObject("SldWorks.Application")
```

```
    'Create part and select connecting faces
    Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2015\templates\Part.prtdot", 0, 0, 0)
    Set swSketchManager = swModel.SketchManager
    swSketchManager.InsertSketch True
    Set swSketchSegment = swSketchManager.CreateLine(0#, 0#, 0#, -0.062359, 0#, 0#)
    Set swSketchSegment = swSketchManager.CreateLine(-0.062359, 0#, 0#, -0.020485, 0.066264, 0#)
    Set swSketchSegment = swSketchManager.CreateLine(-0.020485, 0.066264, 0#, 0#, 0#, 0#)
    swModel.ClearSelection2 True
    Set swFeatureManager = swModel.FeatureManager
    Set swFeature = swFeatureManager.FeatureExtrusionThin2(True, False, False, 0, 0, 0.03048, 0.00254, False, False, False, False, 1.74532925199433E-02, 1.74532925199433E-02, False, False, False, False, True, 0.00254, 0.00254, 0.00254, 0, 0, False, 0.005, True, True, 0, 0, False)
    Set swSelMgr = swModel.SelectionManager
    swSelMgr.EnableContourSelection = False
    swModel.ClearSelection2 True
    Set swModelDocExt = swModel.Extension
    bRet = swModelDocExt.SelectByID2("", "FACE", -4.84137409629284E-02, 0, 0.018103012393226, True, 0, Nothing, 0)
    bRet = swModelDocExt.SelectByID2("", "FACE", -3.96839112014504E-02, 0.035882458904041, 2.07108765403632E-02, True, 0, Nothing, 0)
    bRet = swModelDocExt.SelectByID2("", "FACE", -1.75462018075336E-02, 5.67577015655729E-02, 0.021527257415471, True, 0, Nothing, 0)
```

```
    'Get the selected faces
    Set swModeler = swApp.GetModeler
    nSelCount = swSelMgr.GetSelectedObjectCount
    ReDim swSelFace(nSelCount - 1)
    For i = 1 To nSelCount
        Set swSelFace(i - 1) = swSelMgr.GetSelectedObject6(i, -1)
    Next
    vFaceList = swSelFace
```

```
    'Create solid body feature using selected faces
    Set swPart = swModel
    Set swBody = swPart.CreateNewBody
    Set swNewBody = swBody.CreateBodyFromFaces(nSelCount, (vFaceList))
    If swNewBody Is Nothing Then
        Debug.Print "Failed to create solid body from selected faces."
        Exit Sub
    Else
        Debug.Print "Solid body and new part can be created from selected faces."
    End If
```

```
    'Open new part and force creation of solid body feature
    Set swNewPart = swApp.NewPart
    Set swFeat = swNewPart.CreateFeatureFromBody3(swNewBody, False, swCreateFeatureBodyOpts_e.swCreateFeatureBodyCheck + swCreateFeatureBodyOpts_e.swCreateFeatureBodySimplify)
    If Not swFeat Is Nothing Then
        Debug.Print "New part with imported solid body created."
    Else
        Debug.Print "New part with imported solid body not created."
    End If
```

```
End Sub
```
