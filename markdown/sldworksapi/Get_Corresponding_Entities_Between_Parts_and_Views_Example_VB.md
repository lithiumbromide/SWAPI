---
title: "Get Corresponding Entities Between Parts and Drawing Views Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Corresponding_Entities_Between_Parts_and_Views_Example_VB.htm"
---

# Get Corresponding Entities Between Parts and Drawing Views Example (VBA)

This example shows how to get corresponding entities or objects between a part and its drawing.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Ensure that the specified part and drawing exist.
 ' 2. Open the Immediate window.
 ' 3. Run either subroutine.
 ' 4. At the pause, select a face, edge, vertex, feature, annotation,
 '    or sketch segment.
 ' 5. Press F5.
 '
 ' Postconditions:
 ' 1. Inspect the Immediate window.
 ' 2. If a corresponding face, edge, or vertex is found, it is selected in the
 '    underlying part or drawing.
 '
 ' NOTE: Because the models are used elsewhere, do not save changes.
 '----------------------------------------------------------------------------
 Option Explicit
 Dim swApp As SldWorks.SldWorks
 Dim docSpec As SldWorks.DocumentSpecification
 Dim swModelPart As SldWorks.ModelDoc2
 Dim swModelDrawing As SldWorks.ModelDoc2
 Dim swDrawing As SldWorks.DrawingDoc
 Dim swView As SldWorks.View
 Dim lErr As Long
 Dim selMgr As SldWorks.SelectionMgr
 Dim inputEntity As SldWorks.Entity
 Dim outputEntity As SldWorks.Entity
 Dim bSelected As Boolean
 Dim inputObject As Object
 Dim outputObject As Object
 Dim drComp As SldWorks.DrawingComponent
Sub PartToView()

    Set swApp = Application.SldWorks

    Set docSpec = swApp.GetOpenDocSpec("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\clamp1.SLDPRT")
     Set swModelPart = swApp.OpenDoc7(docSpec)

    Set docSpec = swApp.GetOpenDocSpec("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\clamp1.SLDDRW")
     Set swModelDrawing = swApp.OpenDoc7(docSpec)

    Set swDrawing = swModelDrawing
     Set swView = swDrawing.FeatureByName("Drawing View1").GetSpecificFeature()

    swApp.ActivateDoc3 swModelPart.GetTitle, True, swRebuildOnActivation_e.swUserDecision, lErr

    Set selMgr = swModelPart.SelectionManager
     swModelPart.ClearSelection2 True

    Debug.Assert False ' Select something in the model and press F5

     Select Case selMgr.GetSelectedObjectType3(1, -1)
     Case swSelFACES, swSelEDGES, swSelVERTICES

        Set inputEntity = selMgr.GetSelectedObject6(1, -1)

        Debug.Print "Using IView::GetCorrespondingEntity()"

        Set outputEntity = swView.GetCorrespondingEntity(inputEntity)

        If outputEntity Is Nothing Then
             Debug.Print "No corresponding entity found in the drawing view"
         Else
             Debug.Print "Corresponding entity found....selecting in drawing"
             swApp.ActivateDoc3 swModelDrawing.GetTitle, False, swRebuildOnActivation_e.swDontRebuildActiveDoc, lErr
             bSelected = outputEntity.Select4(False, Nothing)
         End If

    Case swSelNOTHING

    Case Else

        Set inputObject = selMgr.GetSelectedObject6(1, -1)

        Debug.Print "Using IView::GetCorresponding()"

        Set outputObject = swView.GetCorresponding(inputObject)

        If outputObject Is Nothing Then
             Debug.Print "No corresponding object found in the drawing view"
         Else
             Debug.Print "Corresponding object found in the drawing view"
         End If
     End Select
End Sub
Sub ViewToPart()
    Set swApp = Application.SldWorks

    Set docSpec = swApp.GetOpenDocSpec("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\clamp1.SLDPRT")
     Set swModelPart = swApp.OpenDoc7(docSpec)

    Set docSpec = swApp.GetOpenDocSpec("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\clamp1.SLDDRW")
     Set swModelDrawing = swApp.OpenDoc7(docSpec)

    Set swDrawing = swModelDrawing

    swApp.ActivateDoc3 swModelDrawing.GetTitle, False, swRebuildOnActivation_e.swDontRebuildActiveDoc, lErr

    Set selMgr = swModelDrawing.SelectionManager
     swModelDrawing.ClearSelection2 True

    Debug.Assert False ' Select something in the drawing and press F5

    Set swView = swDrawing.FeatureByName("Drawing View1").GetSpecificFeature()
    Select Case selMgr.GetSelectedObjectType3(2, -1)
     Case swSelFACES, swSelEDGES, swSelVERTICES

        Set inputEntity = selMgr.GetSelectedObject6(2, -1)
         Set drComp = selMgr.GetSelectedObjectsComponent4(2, -1)

        Debug.Print "Using IModelDocExtension::GetCorrespondingEntity2()"
        Set outputEntity = swModelPart.Extension.GetCorrespondingEntity2(inputEntity)

        If outputEntity Is Nothing Then
             Debug.Print "No corresponding entity found in the part"
         Else
             Debug.Print "Corresponding entity found...selecting in part"
             swApp.ActivateDoc3 swModelPart.GetTitle, False, swRebuildOnActivation_e.swDontRebuildActiveDoc, lErr
             bSelected = outputEntity.Select4(False, Nothing)
         End If

    Case swSelNOTHING

    Case Else
        Set inputObject = selMgr.GetSelectedObject6(2, -1)
         Set drComp = selMgr.GetSelectedObjectsComponent4(2, -1)

        Debug.Print "Using IModelDocExtension::GetCorresponding2()"
        Set outputObject = swModelPart.Extension.GetCorresponding2(inputObject)

        If outputObject Is Nothing Then
             Debug.Print "No corresponding object found in the part"
         Else
             Debug.Print "Corresponding object found in the part"
         End If
     End Select
End Sub
```
