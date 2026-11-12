---
title: "Add Spring to Motion Study (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swmotionstudyapi/Add_Spring_to_Motion_Study_Example_VB.htm"
---

# Add Spring to Motion Study (VBA)

This example shows how to add a spring to a motion study.

```vb
'--------------------------------------------------------
'
' Preconditions:  (1) Open wrench.sldasm in any SOLIDWORKS 2009
'                     <install dir>\samples\whats new\motion study
'                     folder.
'                 (2) The MotionManager tab is visible. If it is not visible,
'                     click View, MotionManager.
'                 (3) SOLIDWORKS MotionStudy type library is
'                     referenced.
'
'
' Postconditions: Spring feature is added between the grips of the wrench.
'
'                 NOTE: Do not save the model after running the macro. The model
'                       is intended for use with the SOLIDWORKS 2009 "What's New" book.
'                       The model is used in this example for demonstration purposes only.
'
'-------------------------------------------------------
Option Explicit

Sub main()

    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim swMotionMgr As MotionStudyManager
    Dim swMotionStudy1 As MotionStudy
    Dim swSpringFeat As SimulationSpringFeatureData
    Dim boolstatus As Boolean
    Dim swFeat As SldWorks.Feature
    Dim swSelMgr As SelectionMgr

    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
    Set swSelMgr = swModel.SelectionManager

    ' Get the MotionManager
    Set swMotionMgr = swModelDocExt.GetMotionStudyManager()
    If (swMotionMgr Is Nothing) Then
          End
    End If

    ' Get and activate "MotionStudy1_Distance=0.5in"
    Set swMotionStudy1 = swMotionMgr.GetMotionStudy("MotionStudy1_Distance=0.5in")
    If (swMotionStudy1 Is Nothing) Then
        MsgBox "MotionStudy1_Distance=0.5in is not available."
        End
    End If

    ' Activate swMotionStudy1
    swMotionStudy1.Activate

    ' Define Spring feature
    Set swSpringFeat = swMotionStudy1.CreateDefinition(swFmAEMLinearMotionSpring)
    If swSpringFeat Is Nothing Then
       Debug.Print "ERROR: Creation of Spring feature data object failed."
        Exit Sub
    End If

    ' Select the faces for the spring's endpoints
    Dim swFace1 As face2, swFace2 As face2
    swModel.ShowNamedView2 "*Left", 3
    swModel.ViewZoomtofit2
    boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.03344586330968, 0.0525345575174, 0, True, 0, Nothing, 0)
    Set swFace1 = swSelMgr.GetSelectedObject6(1, -1)
    boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.02244533711473, 0.0131288302002, 2.238961779386E-04, True, 0, Nothing, 0)
    Set swFace2 = swSelMgr.GetSelectedObject6(2, -1)

   ' Set spring's characteristics
    swSpringFeat.SetEndPoints swFace1, swFace2
    swSpringFeat.CoilDiameter = 0.0102
    swSpringFeat.NumberOfCoils = 3
    swSpringFeat.WireDiameter = 0.00152
    swSpringFeat.FreeLength = 0.02

     ' Create Spring feature
    Set swFeat = swMotionStudy1.CreateFeature(swSpringFeat)

    If swFeat Is Nothing Then
        Debug.Print " ERROR: Creation of the Spring feature failed."
    Else
        Debug.Print "Type of the feature added: " & swFeat.GetTypeName2
    End If
End Sub
```
