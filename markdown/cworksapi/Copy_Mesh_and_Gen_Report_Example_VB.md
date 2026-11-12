---
title: "Copy Mesh and Generate Report Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Copy_Mesh_and_Gen_Report_Example_VB.htm"
---

# Copy Mesh and Generate Report Example (VBA)

This example shows how to copy the mesh from one study to another and generate a report.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click Tools > References > SOLIDWORKS Simulation version type library).
 ' 3. Open public_documents\samples\Simulation Examples\Verification\buckling2.sldprt.
 '
 ' Postconditions:
 ' 1. Meshes the Quality and Draft studies.
 ' 2. Copies the mesh from the Quality study to the Draft study.
 ' 3. Click OK to close any dialog boxes.
 ' 4. Generates a report for the Draft study in c:\temp.
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

    Dim errCode As Long, n As Long
     Dim el As Double, tl As Double

    Const NoOfElements1 As Double = 712
     Const NoOfElements2 As Double = 2686

    If SwApp Is Nothing Then Set SwApp = Application.SldWorks

    Set CWAddinCallBack = SwApp.GetAddInObject("CosmosWorks.CosmosWorks")
     If CWAddinCallBack Is Nothing Then ErrorMsg SwApp, "No CwAddincallback object"
     Set COSMOSWORKS = CWAddinCallBack.COSMOSWORKS
     If COSMOSWORKS Is Nothing Then ErrorMsg SwApp, "No CosmosWorks object"

    'Get active document
     Set ActDoc = COSMOSWORKS.ActiveDoc()
     If ActDoc Is Nothing Then ErrorMsg SwApp, "No active document"

    'Get the first study
     Set StudyMngr = ActDoc.StudyManager()
     If StudyMngr Is Nothing Then ErrorMsg SwApp, "No CWStudyManager object"
     StudyMngr.ActiveStudy = 0
     Set Study = StudyMngr.GetStudy(0)
     If Study Is Nothing Then ErrorMsg SwApp, "No CWStudy object"

    'Mesh the first study
     Set CWMesh = Study.Mesh
     If CWMesh Is Nothing Then ErrorMsg SwApp, "No CWMesh object"
     CWMesh.Quality = 1
     Call CWMesh.GetDefaultElementSizeAndTolerance(0, el, tl)
     errCode = Study.CreateMesh(0, el, tl)
     If errCode <> 0 Then ErrorMsg SwApp, "Mesh failed"

    n = CWMesh.NodeCount

    If (n < 0.95 * NoOfElements2) Or (n > 1.05 * NoOfElements2) Then
     ErrorMsg SwApp, " % error = " & (((n - NoOfElements2) / NoOfElements2) * 100)
     End If

    'Get the second study
     StudyMngr.ActiveStudy = 1
     Set Study = StudyMngr.GetStudy(1)
     If Study Is Nothing Then ErrorMsg SwApp, "No CWStudy object"

    'Mesh the second study
     Set CWMesh = Study.Mesh
     If CWMesh Is Nothing Then ErrorMsg SwApp, "No CWMesh object"
     CWMesh.Quality = 0
     Call CWMesh.GetDefaultElementSizeAndTolerance(0, el, tl)
     errCode = Study.CreateMesh(0, el, tl)
     If errCode <> 0 Then ErrorMsg SwApp, "Mesh failed"

    n = CWMesh.NodeCount
     If (n < 0.95 * NoOfElements1) Or (n > 1.05 * NoOfElements1) Then
     ErrorMsg SwApp, " % error = " & (((n - NoOfElements1) / NoOfElements1) * 100)
     End If

    'Copy mesh from the first study to the second study
     errCode = Study.CopyMeshFromStudy("Quality")
     If errCode <> 0 Then ErrorMsg SwApp, "Mesh failed to copy"

    n = CWMesh.NodeCount
     If (n < 0.95 * NoOfElements2) Or (n > 1.05 * NoOfElements2) Then
     ErrorMsg SwApp, " % error = " & (((n - NoOfElements2) / NoOfElements2) * 100)
     End If

    'Generate Report
     errCode = Study.GenerateReport("C:\temp", "report", False)
     If errCode <> 1 Then ErrorMsg SwApp, "Failed to generate report"

End Sub

Sub ErrorMsg(SwApp As SldWorks.SldWorks, Message As String)
     SwApp.SendMsgToUser2 Message, 0, 0
     SwApp.RecordLine "'*** WARNING - General"
     SwApp.RecordLine "'*** " & Message
     SwApp.RecordLine ""
 End Sub
```
