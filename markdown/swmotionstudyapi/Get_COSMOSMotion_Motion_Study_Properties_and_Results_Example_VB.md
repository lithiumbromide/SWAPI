---
title: "Get COSMOSMotion Motion Study Properties and Results Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swmotionstudyapi/Get_COSMOSMotion_Motion_Study_Properties_and_Results_Example_VB.htm"
---

# Get COSMOSMotion Motion Study Properties and Results Example (VBA)

This example shows how to get a COSMOSMotion motion study's properties and results.

```vb
'------------------------------------------
' Preconditions: Model is open that has a COSMOSMotion motion study
'                named PhysSim and at least one COSMOSMotion motion study plot.
'
' Postconditions: None
'--------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swMotionMgr As SwMotionStudy.MotionStudyManager
Dim swMotionStudy1 As SwMotionStudy.MotionStudy
Dim swResults As SwMotionStudy.MotionStudyResults
Dim swMotionStudyProps As SwMotionStudy.MotionStudyProperties
Dim swCosmosMotionStudyProps As SwMotionStudy.CosmosMotionStudyProperties
Dim swCosmosMotionStudyResults As SwMotionStudy.CosmosMotionStudyResults

Sub main()
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
    ' Get the MotionManager.
    Set swMotionMgr = swModelDocExt.GetMotionStudyManager()
    If (swMotionMgr Is Nothing) Then
          End
    End If
    ' Get motion study named PhysSim.
    Set swMotionStudy1 = swMotionMgr.GetMotionStudy("PhysSim")
    If (swMotionStudy1 Is Nothing) Then
        MsgBox "PhysSim is not available."
        End
    End If

    swMotionStudy1.StudyType = swMotionStudyType_e.swMotionStudyTypePhysicalSimulation

    'Is the motion study active?  If not, activate it.
    If Not swMotionStudy1.IsActive Then swMotionStudy1.Activate
    Debug.Print "Duration of motion study: " & swMotionStudy1.GetDuration
    Debug.Print "Timebar position on timeline: " & swMotionStudy1.GetTime
    Debug.Print "Number of motion features: " & swMotionStudy1.GetMotionFeaturesCount

    'Get COSMOSMotion study properties.
    Set swMotionStudyProps = swMotionStudy1.GetProperties(4)
    Set swCosmosMotionStudyProps = swMotionStudyProps

    Debug.Print ""
    Debug.Print "COSMOSMotion study properties: "
    Debug.Print "    Animate during simulation: " & swCosmosMotionStudyProps.AnimateDuringSimulation
    Debug.Print "    Make all mates flexible: " & swCosmosMotionStudyProps.MakeAllMatesFlexible
    Debug.Print "    Display results graphics as wireframe: " & swCosmosMotionStudyProps.WireframeGraphics

    ' Get COSMOSMotion study results.
    Set swResults = swMotionStudy1.GetResults(4)
    Set swCosmosMotionStudyResults = swResults
    Debug.Print "    Number of plots: " & swCosmosMotionStudyResults.GetPlotCount

    Debug.Print ""
    Debug.Print "Are the motion study results out of date? " & swResults.IsOutOfDate

End Sub
```
