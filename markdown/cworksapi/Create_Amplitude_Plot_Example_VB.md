---
title: "Create Amplitude Plot and Set Mode Shape Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Amplitude_Plot_Example_VB.htm"
---

# Create Amplitude Plot and Set Mode Shape Example (VBA)

This example shows how to create an amplitude plot and set its mode shape number.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click Tools > References > SOLIDWORKS Simulation version type library).
 ' 3. Open public_documents\samples\Simulation Examples\tutor1.sldprt.
 ' 4. Create a frequency study and apply material to the model.
 '
 ' Postconditions:
 ' 1. Activates the Frequency1 study.
 ' 2. Meshes and analyzes the study.
 ' 3. Creates one or more default resultant amplitude plots, depending on your
 '    Tools > Simulation > Options > Default Options > Frequency/Buckling Study
 '    Results settings.
 ' 4. Creates another resultant amplitude plot and sets its mode shape number
 '    to 4.
 ' 5. Gets the minimum and maximum resultant amplitudes for the last plot.
 ' 6. Click OK to close any error dialog boxes.
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
     Dim CWCFf As CosmosWorksLib.CWPlot

    Dim errCode As Long
     Dim el As Double, tl As Double
     Dim Disp  As Variant

    Const DispMax  As Double = 1.424
     Const DispMin  As Double = 0.1

    If SwApp Is Nothing Then Set SwApp = Application.SldWorks

    Set CWAddinCallBack = SwApp.GetAddInObject("CosmosWorks.CosmosWorks")
     If CWAddinCallBack Is Nothing Then ErrorMsg SwApp, "No CWAddinCallBack object"
     Set COSMOSWORKS = CWAddinCallBack.COSMOSWORKS
     If COSMOSWORKS Is Nothing Then ErrorMsg SwApp, "No CosmosWorks object"

    'Get active document
     Set ActDoc = COSMOSWORKS.ActiveDoc()
     If ActDoc Is Nothing Then ErrorMsg SwApp, "No active document"

    'Get Frequency1 study
     Set StudyMngr = ActDoc.StudyManager()
     If StudyMngr Is Nothing Then ErrorMsg SwApp, "No CWStudyManager object"
     StudyMngr.ActiveStudy = 1
     Set Study = StudyMngr.GetStudy(1)
     If Study Is Nothing Then ErrorMsg SwApp, "No CWStudy object"
    'Mesh
     Set CWMesh = Study.Mesh
     If CWMesh Is Nothing Then ErrorMsg SwApp, "No CWMesh object"
     CWMesh.Quality = 0
     Call CWMesh.GetDefaultElementSizeAndTolerance(0, el, tl)
     errCode = Study.CreateMesh(0, el, tl)
     If errCode <> 0 Then ErrorMsg SwApp, "Mesh failed"
    'Run analysis
     errCode = Study.RunAnalysis
     If errCode <> 0 Then ErrorMsg SwApp, "Analysis failed with error code as defined in swsRunAnalysisError_e: " & errCode

    'Get results
     Set CWResult = Study.results
     If CWResult Is Nothing Then ErrorMsg SwApp, "No CWResults object"
    'Create resultant amplitude plot
     Set CWCFf = CWResult.CreatePlot(swsResultDisplacementOrAmplitude, swsFrequencyBucklingDisplacement_URES, swsUnitSI, False, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failure to create plot"

    'Set mode shape number of plot to 4
      errCode = CWCFf.SetModeShape(4)
     If errCode <> 0 Then ErrorMsg SwApp, "Plot is not set for specified mode shape"

    errCode = CWCFf.ActivatePlot()
     If errCode <> 0 Then ErrorMsg SwApp, "Plot is not activated"

    'Get min/max resultant amplitudes from plot
     Disp = CWCFf.GetMinMaxResultValues(errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "No amplitude values"

    If (Disp(1) < 0.95 * DispMin) Or (Disp(1) > 1.05 * DispMin) Then
     ErrorMsg SwApp, " Minimum amplitude % error = " & (((Disp(1) - DispMin) / DispMin) * 100)
     End If

    If (Disp(3) < 0.95 * DispMax) Or (Disp(3) > 1.05 * DispMax) Then
     ErrorMsg SwApp, "Maximum amplitude % error = " & (((Disp(3) - DispMax) / DispMax) * 100)
     End If

End Sub

Sub ErrorMsg(SwApp As SldWorks.SldWorks, Message As String)
     SwApp.SendMsgToUser2 Message, 0, 0
     SwApp.RecordLine "'*** WARNING - General"
     SwApp.RecordLine "'*** " & Message
     SwApp.RecordLine ""
 End Sub
```
