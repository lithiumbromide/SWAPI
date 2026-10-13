---
title: "Convert Study Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Convert_Study_Example_VBNET.htm"
---

# Convert Study Example (VB.NET)

This example shows how to convert a static study to a linear dynamic harmonic study.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 '    (in the IDE, click Project > Add Reference > .NET >
 '    SolidWorks.Interop.cosworks > OK).
 ' 3. Open  public_documents\samples\Simulation Examples\tutor1.sldprt.
 '
 ' Postconditions:
 ' 1. Converts the Ready study to the LinDynHarmonic study.
 ' 2. Sets damping options for, meshes, and analyzes LinDynHarmonic.
 ' 3. Inspect the Simulation study tree.
 '
  ' NOTE: Because the model is used elsewhere, do not save changes.
  ' ---------------------------------------------------------------------------

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
         Dim DampingOptions As CWDampingOptions
         Dim DampingRatios(8) As Object

         Dim errCode As Integer
         Dim el As Double, tl As Double

         CWAddinCallBack = swApp.GetAddInObject("CosmosWorks.CosmosWorks")
         If CWAddinCallBack Is Nothing Then ErrorMsg(swApp, "No CWAddinCallBack object")
         COSMOSWORKS = CWAddinCallBack.COSMOSWORKS
         If COSMOSWORKS Is Nothing Then ErrorMsg(swApp, "No COSMOSWORKS object")

         'Get active document
         ActDoc = COSMOSWORKS.ActiveDoc()
         If ActDoc Is Nothing Then ErrorMsg(swApp, "No active document")

         'Get Ready study
         StudyMngr = ActDoc.StudyManager()
         If StudyMngr Is Nothing Then ErrorMsg(swApp, "No CWStudyManager object")
         StudyMngr.ActiveStudy = 0
         Study = StudyMngr.GetStudy(0)
         If Study Is Nothing Then ErrorMsg(swApp, "No CWStudy object")

         'Convert study
         Study = StudyMngr.ConvertStudy2("Ready", swsAnalysisStudyType_e.swsAnalysisStudyTypeStatic, "LinDynHarmonic", swsAnalysisStudyType_e.swsAnalysisStudyTypeDynamic, "Default", swsDynamicAnalysisSubType_e.swsDynamicAnalysisSubTypeHarmonic, False, False, errCode)
         If Study Is Nothing Then ErrorMsg(swApp, "Study not converted")

         'Set damping options
         DampingOptions = Study.DampingOptions
         DampingOptions.DampingType = 0 'modal damping
         DampingOptions.ComputeFromMaterialDamping = 0 'do not use material damping ratios
         DampingOptions.ClearAllDampingRatios()
         DampingRatios(0) = 1
         DampingRatios(1) = 5
         DampingRatios(2) = 3.45
         DampingRatios(3) = 6
         DampingRatios(4) = 15
         DampingRatios(5) = 15
         DampingRatios(6) = 16
         DampingRatios(7) = 25
         DampingRatios(8) = 34.5
         errCode = DampingOptions.SetDampingRatios(3, (DampingRatios))

         'Mesh the converted study
         CWMesh = Study.Mesh
         If CWMesh Is Nothing Then ErrorMsg(swApp, "No CWMesh object")
         CWMesh.Quality = 0
         Call CWMesh.GetDefaultElementSizeAndTolerance(0, el, tl)
         errCode = Study.CreateMesh(0, el, tl)
         If errCode <> 0 Then ErrorMsg(swApp, "Mesh failed")

         'Analyze the converted study
         errCode = Study.RunAnalysis
         If errCode <> 0 Then ErrorMsg(swApp, "Analysis failed")

         CWResult = Study.Results
         If CWResult Is Nothing Then ErrorMsg(swApp, "No CWResults object")

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
