---
title: "Convert Study Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Convert_Study_Example_VB.htm"
---

# Convert Study Example (VBA)

This example shows how to convert a static study to a linear dynamic harmonic study.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click Tools > References > SOLIDWORKS Simulation version type library).
 ' 3. Open public_documents\samples\Simulation Examples\tutor1.sldprt.
 '
 ' Postconditions:
 ' 1. Converts the Ready study to the LinDynHarmonic study.
 ' 2. Sets damping options for, meshes, and analyzes LinDynHarmonic.
 ' 3. Inspect the Simulation study tree.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 ' ---------------------------------------------------------------------------
Option Explicit
Sub main()
    Dim SwApp As SldWorks.SldWorks

    Dim COSMOSWORKS As CosmosWorksLib.COSMOSWORKS
     Dim CWAddinCallBack As CosmosWorksLib.CWAddinCallBack
     Dim ActDoc As CosmosWorksLib.CWModelDoc
     Dim StudyMngr As CosmosWorksLib.CWStudyManager
     Dim Study As CosmosWorksLib.CWStudy
     Dim CWMesh As CosmosWorksLib.CWMesh
     Dim CWResult As CosmosWorksLib.CWResults
     Dim DampingOptions As CosmosWorksLib.CWDampingOptions
     Dim DampingRatios As Variant

    Dim errCode As Long
     Dim el As Double, tl As Double
    If SwApp Is Nothing Then Set SwApp = Application.SldWorks

    Set CWAddinCallBack = SwApp.GetAddInObject("CosmosWorks.CosmosWorks")
     If CWAddinCallBack Is Nothing Then ErrorMsg SwApp, "No CWAddinCallBack object"
     Set COSMOSWORKS = CWAddinCallBack.COSMOSWORKS
     If COSMOSWORKS Is Nothing Then ErrorMsg SwApp, "No COSMOSWORKS object"

    'Get active document
     Set ActDoc = COSMOSWORKS.ActiveDoc()
     If ActDoc Is Nothing Then ErrorMsg SwApp, "No active document"

    'Get Ready study
     Set StudyMngr = ActDoc.StudyManager()
     If StudyMngr Is Nothing Then ErrorMsg SwApp, "No CWStudyManager object"
     StudyMngr.ActiveStudy = 0
     Set Study = StudyMngr.GetStudy(0)
     If Study Is Nothing Then ErrorMsg SwApp, "No CWStudy object"

    'Convert study
     Set Study = StudyMngr.ConvertStudy2("Ready", swsAnalysisStudyTypeStatic, "LinDynHarmonic", swsAnalysisStudyTypeDynamic, "Default", swsDynamicAnalysisSubTypeHarmonic, False, False, errCode)
     If Study Is Nothing Then ErrorMsg SwApp, "Study not converted"

    'Set damping options
     Set DampingOptions = Study.DampingOptions
     DampingOptions.DampingType = 0 'modal damping
     DampingOptions.ComputeFromMaterialDamping = 0 'do not use material damping ratios
     DampingOptions.ClearAllDampingRatios
     DampingRatios = Array(1, 5, 3.45, 6, 15, 15, 16, 25, 34.5)
     errCode = DampingOptions.SetDampingRatios(3, (DampingRatios))

    'Mesh the converted study
     Set CWMesh = Study.Mesh
     If CWMesh Is Nothing Then ErrorMsg SwApp, "No CWMesh object"
     CWMesh.Quality = 0
     Call CWMesh.GetDefaultElementSizeAndTolerance(0, el, tl)
     errCode = Study.CreateMesh(0, el, tl)
     If errCode <> 0 Then ErrorMsg SwApp, "Mesh failed"

    'Analyze the converted study
     errCode = Study.RunAnalysis
     If errCode <> 0 Then ErrorMsg SwApp, "Analysis failed"
    Set CWResult = Study.results
     If CWResult Is Nothing Then ErrorMsg SwApp, "No CWResults object"

End Sub

Sub ErrorMsg(SwApp As SldWorks.SldWorks, Message As String)
     SwApp.SendMsgToUser2 Message, 0, 0
     SwApp.RecordLine "'*** WARNING - General"
     SwApp.RecordLine "'*** " & Message
     SwApp.RecordLine ""
 End Sub
```
