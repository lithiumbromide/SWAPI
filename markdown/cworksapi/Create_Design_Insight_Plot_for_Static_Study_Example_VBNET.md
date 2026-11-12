---
title: "Create a Design Insight Plot for a Static Study Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Design_Insight_Plot_for_Static_Study_Example_VBNET.htm"
---

# Create a Design Insight Plot for a Static Study Example (VB.NET)

This example shows how to create a Design Insight plot and set its load level.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 '    (in the IDE, click Project > Add Reference > .NET >
 '    SolidWorks.Interop.cosworks > OK).
 ' 3. Open public_documents\samples\Simulation Examples\actuator.sldasm.
 '
 ' Postconditions:
  ' 1. Deletes all default static study plots from the model document.
 ' 2. Activates the Ready static study.
 ' 3. Meshes and runs the study.
 ' 4. Creates a Design Insight plot.
  ' 5. Gets the Design Insight plot and sets its load level to 50.
 ' 6. Inspect the graphics area.
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

         Dim COSMOSWORKS As CosmosWorks
         Dim CWAddinCallBack As CwAddincallback
         Dim ActDoc As CWModelDoc
         Dim StudyMngr As CWStudyManager
         Dim Study As CWStudy
         Dim CWMesh As CWMesh
         Dim CWResult As CWResults
         Dim CWCFf As CWPlot
         Dim plot As CWPlot
         Dim errCode As Integer
         Dim el As Double, tl As Double

         CWAddinCallBack = swApp.GetAddInObject("CosmosWorks.CosmosWorks")
         If CWAddinCallBack Is Nothing Then ErrorMsg(swApp, "No CWAddinCallBack object")
         COSMOSWORKS = CWAddinCallBack.CosmosWorks
         If COSMOSWORKS Is Nothing Then ErrorMsg(swApp, "No CosmosWorks object")

         'Get active document
         ActDoc = COSMOSWORKS.ActiveDoc()
         If ActDoc Is Nothing Then ErrorMsg(swApp, "No active document")

         'Delete all default static study plots from this model
         ActDoc.DeleteAllDefaultStaticStudyPlots()

         'Get Ready study
         StudyMngr = ActDoc.StudyManager()
         If StudyMngr Is Nothing Then ErrorMsg(swApp, "No CWStudyManager object")
         StudyMngr.ActiveStudy = 0
         Study = StudyMngr.GetStudy(0)
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

         'Create Design Insight plot of the results
         CWCFf = CWResult.CreatePlot(swsPlotResultTypes_e.swsResultDesignInsight, 0, swsUnit_e.swsUnitSI, False, errCode)
         If CWCFf Is Nothing Then ErrorMsg(swApp, "Failed to create plot")

         'Get Design Insight plot
         plot = CWResult.GetPlot("Design Insight1", errCode)

         'Set load level of Design Insight plot
         plot.IsoValue = 50

         'Activate plot
         errCode = plot.ActivatePlot()
         If errCode <> 0 Then ErrorMsg(swApp, "Plot is not activated")

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
