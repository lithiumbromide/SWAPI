---
title: "Create a Design Insight Plot for a Static Study Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Design_Insight_Plot_for_Static_Study_Example_VB.htm"
---

# Create a Design Insight Plot for a Static Study Example (VBA)

This example shows how to create a Design Insight plot and set its load level.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click Tools > References > SOLIDWORKS Simulation version type library).
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
     Dim plot As CosmosWorksLib.CWPlot
     Dim errCode As Long
     Dim el As Double, tl As Double
    If SwApp Is Nothing Then Set SwApp = Application.SldWorks
    Set CWAddinCallBack = SwApp.GetAddInObject("CosmosWorks.CosmosWorks")
     If CWAddinCallBack Is Nothing Then ErrorMsg SwApp, "No CWAddinCallBack object"
     Set COSMOSWORKS = CWAddinCallBack.COSMOSWORKS
     If COSMOSWORKS Is Nothing Then ErrorMsg SwApp, "No CosmosWorks object"
    'Get active document
     Set ActDoc = COSMOSWORKS.ActiveDoc()
     If ActDoc Is Nothing Then ErrorMsg SwApp, "No active document"
    'Delete all default static study plots from this model
     ActDoc.DeleteAllDefaultStaticStudyPlots
    'Get Ready study
     Set StudyMngr = ActDoc.StudyManager()
     If StudyMngr Is Nothing Then ErrorMsg SwApp, "No CWStudyManager object"
     StudyMngr.ActiveStudy = 0
     Set Study = StudyMngr.GetStudy(0)
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
     Set CWResult = Study.Results
     If CWResult Is Nothing Then ErrorMsg SwApp, "No CWResults object"
    'Create Design Insight plot of the results
     Set CWCFf = CWResult.CreatePlot(swsResultDesignInsight, 0, swsUnitSI, False, errCode)
     If CWCFf Is Nothing Then ErrorMsg SwApp, "Failed to create plot"
    'Get Design Insight plot
     Set plot = CWResult.GetPlot("Design Insight1", errCode)
    'Set load level of Design Insight plot
     plot.IsoValue = 50
    'Activate plot
     errCode = plot.ActivatePlot()
     If errCode <> 0 Then ErrorMsg SwApp, "Plot is not activated"
End Sub
Sub ErrorMsg(SwApp As SldWorks.SldWorks, Message As String)
     SwApp.SendMsgToUser2 Message, 0, 0
     SwApp.RecordLine "'*** WARNING - General"
     SwApp.RecordLine "'*** " & Message
     SwApp.RecordLine ""
 End Sub
```
