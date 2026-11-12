---
title: "Create Sheet Body From Faces and Feature from Sheet Body Example (VB)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Sheet_Body_From_Faces_and_Feature_from_Sheet_Body_Example_VB.htm"
---

# Create Sheet Body From Faces and Feature from Sheet Body Example (VB)

This example shows how to create a sheet body from the faces of a solid body and how to create a feature from the sheet body.

```vb
'-------------------------------------------------------
'
' Preconditions: Part document is open that contains
'                a solid body named Extrude1.
'
' Postconditions: Surface-Imported feature is created from
'                the sheet body.
'
'-------------------------------------------------------
Option Explicit

    Dim swApp                   As SldWorks.SldWorks
    Dim swModel                 As SldWorks.ModelDoc2
    Dim swModeler               As SldWorks.Modeler
    Dim swBody                  As SldWorks.Body2
    Dim swFace                  As SldWorks.Face2
    Dim swWorkPieceBody         As SldWorks.Body2
    Dim swWorkPieceFacesBody    As SldWorks.Body2
    Dim swWorkPieceBodyCopy     As SldWorks.Body2
    Dim aFaces()                As SldWorks.Face2
    Dim swThickenedBody         As SldWorks.Body2
    Dim swFeatureManager        As SldWorks.FeatureManager
    Dim aBodies(0)              As SldWorks.Body2
    Dim vBodies                 As Variant
    Dim swPart                  As PartDoc
    Dim swFeature               As SldWorks.Feature
    Dim bValue                  As Boolean
    Dim lErrors                 As Long
    Dim lWarnings               As Long
    Dim vFaces                  As Variant
    Dim lIdx                    As Long
    Dim retval                  As Long

    Sub main()

    ' Connect to SOLIDWORKS Design
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swFeatureManager = swModel.FeatureManager

    ' Get Modeler object
    Set swModeler = swApp.GetModeler

    ' Clear selection
    swModel.ClearSelection2 True

    ' Select the body
    bValue = swModel.Extension.SelectByID2("Extrude1", "SOLIDBODY", 0, 0, 0, True, 0, Nothing, 0)
    Set swWorkPieceBody = swModel.SelectionManager.GetSelectedObject6(1, -1)

    ' Create temporary body by copying the selected body
    ' Boolean operations consume bodies
    Set swWorkPieceBodyCopy = swWorkPieceBody.Copy

    ' Clear the selection
    swModel.ClearSelection2 True

    ' Collect the faces on the selected body
    lIdx = 0
    Set swFace = swWorkPieceBodyCopy.GetFirstFace
    Do While (Not (swFace Is Nothing))
        ReDim Preserve aFaces(lIdx)
        Set aFaces(lIdx) = swFace
        lIdx = lIdx + 1
      Set swFace = swFace.GetNextFace
    Loop

    ' Create a sheet body from the faces
    vFaces = aFaces
    Set swWorkPieceFacesBody = swModeler.CreateSheetFromFaces(vFaces)

    ' Create a feature from the sheet body
    Set aBodies(0) = swWorkPieceFacesBody
    vBodies = aBodies
    Set swPart = swModel
    Set swFeature = swPart.CreateFeatureFromBody3(vBodies(0), False, swCreateFeatureBodyOpts_e.swCreateFeatureBodyCheck)

    ' Rebuild the model; a Surface-Imported feature should
    ' appear in the FeatureManager design tree after the rebuild
    swModel.EditRebuild3

    End Sub
```
