---
title: "Create Amplitude Plot and Set Mode Shape Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Amplitude_Plot_Example_VBNET.htm"
---

# Create Amplitude Plot and Set Mode Shape Example (VB.NET)

This example shows how to create an amplitude plot and set its mode shape number.

```vb
'----------------------------------------------------------------------------
 ' Preconditions:
  ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 '    (in the IDE, click Project > Add Reference > .NET >
 '    SolidWorks.Interop.cosworks > OK).
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
 '----------------------------------------------------------------------------

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.cosworks
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Sub main()

         Dim COSMOSWORKS As COSMOSWORKS
         Dim CWAddinCallBack As CwAddincallback
         Dim ActDoc As CWModelDoc
         Dim StudyMngr As CWStudyManager
         Dim Study As CWStudy
         Dim CWMesh As CWMesh
         Dim CWResult As CWResults
         Dim CWCFf As CWPlot

         Dim errCode As Integer
         Dim el As Double, tl As Double
         Dim Disp As Object

         Const DispMax As Double = 1.424
         Const DispMin As Double = 0.1

         CWAddinCallBack = swApp.GetAddInObject("CosmosWorks.CosmosWorks")
         If CWAddinCallBack Is Nothing Then ErrorMsg(swApp, "No CWAddinCallBack object")
         COSMOSWORKS = CWAddinCallBack.COSMOSWORKS
         If COSMOSWORKS Is Nothing Then ErrorMsg(swApp, "No CosmosWorks object")

         'Get active document
         ActDoc = COSMOSWORKS.ActiveDoc()
         If ActDoc Is Nothing Then ErrorMsg(swApp, "No active document")

         'Get Frequency1 study
         StudyMngr = ActDoc.StudyManager()
         If StudyMngr Is Nothing Then ErrorMsg(swApp, "No CWStudyManager object")
         StudyMngr.ActiveStudy = 1
         Study = StudyMngr.GetStudy(1)
         If Study Is Nothing Then ErrorMsg(swApp, "No CWStudy object")

         'Mesh
         CWMesh = Study.Mesh
         If CWMesh Is Nothing Then ErrorMsg(swApp, "No CWMesh object")
         CWMesh.Quality = 0
         Call CWMesh.GetDefaultElementSizeAndTolerance(0, el, tl)
         errCode = Study.CreateMesh(0, el, tl)
         If errCode <> 0 Then ErrorMsg(swApp, "Mesh failed")

         'Run analysis
         errCode = Study.RunAnalysis
         If errCode <> 0 Then ErrorMsg(swApp, "Analysis failed with error code as defined in swsRunAnalysisError_e: " & errCode)

         'Get results
         CWResult = Study.Results
         If CWResult Is Nothing Then ErrorMsg(swApp, "No CWResults object")

         'Create resultant amplitude plot
         CWCFf = CWResult.CreatePlot(swsPlotResultTypes_e.swsResultDisplacementOrAmplitude, swsFrequencyBucklingResultDisplacementComponentTypes_e.swsFrequencyBucklingDisplacement_URES, swsUnit_e.swsUnitSI, False, errCode)
         If errCode <> 0 Then ErrorMsg(swApp, "Failure to create plot")

         'Set mode shape number of plot to 4
         errCode = CWCFf.SetModeShape(4)
         If errCode <> 0 Then ErrorMsg(swApp, "Plot is not set for specified mode shape")

         errCode = CWCFf.ActivatePlot()
         If errCode <> 0 Then ErrorMsg(swApp, "Plot is not activated")

         'Get min/max resultant amplitudes from plot
         Disp = CWCFf.GetMinMaxResultValues(errCode)
         If errCode <> 0 Then ErrorMsg(swApp, "No amplitude values")

         If (Disp(1) < 0.95 * DispMin) Or (Disp(1) > 1.05 * DispMin) Then
             ErrorMsg(swApp, " Minimum amplitude % error = " & (((Disp(1) - DispMin) / DispMin) * 100))
         End If

         If (Disp(3) < 0.95 * DispMax) Or (Disp(3) > 1.05 * DispMax) Then
             ErrorMsg(swApp, "Maximum amplitude % error = " & (((Disp(3) - DispMax) / DispMax) * 100))
         End If

     End Sub

     Sub ErrorMsg(ByVal SwApp As SldWorks, ByVal Message As String)
         SwApp.SendMsgToUser2(Message, 0, 0)
         SwApp.RecordLine("'*** WARNING - General")
         SwApp.RecordLine("'*** " & Message)
         SwApp.RecordLine("")
     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
