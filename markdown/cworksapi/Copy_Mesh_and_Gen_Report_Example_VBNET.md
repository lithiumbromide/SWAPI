---
title: "Copy Mesh and Generate Report Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Copy_Mesh_and_Gen_Report_Example_VBNET.htm"
---

# Copy Mesh and Generate Report Example (VB.NET)

This example shows how to copy the mesh from one study to another and generate a report.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 '    (in the IDE, click Project > Add Reference > .NET >
 '    SolidWorks.Interop.cosworks > OK).
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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.cosworks
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Sub main()

         Dim COSMOSWORKS As COSMOSWORKS
         Dim CWAddinCallBack As CWAddinCallBack
         Dim ActDoc As CWModelDoc
         Dim StudyMngr As CWStudyManager
         Dim Study As CWStudy
         Dim CWMesh As CWMesh

         Dim errCode As Integer, n As Integer
         Dim el As Double, tl As Double

         Const NoOfElements1 As Double = 712
         Const NoOfElements2 As Double = 2686

         CWAddinCallBack = swApp.GetAddInObject("CosmosWorks.CosmosWorks")
         If CWAddinCallBack Is Nothing Then ErrorMsg(swApp, "No CWAddincallback object")
         COSMOSWORKS = CWAddinCallBack.COSMOSWORKS
         If COSMOSWORKS Is Nothing Then ErrorMsg(swApp, "No CosmosWorks object")

         'Get active document
         ActDoc = COSMOSWORKS.ActiveDoc()
         If ActDoc Is Nothing Then ErrorMsg(swApp, "No active document")

         'Get the first study
         StudyMngr = ActDoc.StudyManager()
         If StudyMngr Is Nothing Then ErrorMsg(swApp, "No CWStudyManager object")
         StudyMngr.ActiveStudy = 0
         Study = StudyMngr.GetStudy(0)
         If Study Is Nothing Then ErrorMsg(swApp, "No CWStudy object")

         'Mesh the first study
         CWMesh = Study.Mesh
         If CWMesh Is Nothing Then ErrorMsg(swApp, "No CWMesh object")
         CWMesh.Quality = 1
         Call CWMesh.GetDefaultElementSizeAndTolerance(0, el, tl)
         errCode = Study.CreateMesh(0, el, tl)
         If errCode <> 0 Then ErrorMsg(swApp, "Mesh failed")

         n = CWMesh.NodeCount

         If (n < 0.95 * NoOfElements2) Or (n > 1.05 * NoOfElements2) Then
             ErrorMsg(swApp, " % error = " & (((n - NoOfElements2) / NoOfElements2) * 100))
         End If

         'Get the second study
         StudyMngr.ActiveStudy = 1
         Study = StudyMngr.GetStudy(1)
         If Study Is Nothing Then ErrorMsg(swApp, "No CWStudy object")

         'Mesh the second study
         CWMesh = Study.Mesh
         If CWMesh Is Nothing Then ErrorMsg(swApp, "No CWMesh object")
         CWMesh.Quality = 0
         Call CWMesh.GetDefaultElementSizeAndTolerance(0, el, tl)
         errCode = Study.CreateMesh(0, el, tl)
         If errCode <> 0 Then ErrorMsg(swApp, "Mesh failed")

         n = CWMesh.NodeCount
         If (n < 0.95 * NoOfElements1) Or (n > 1.05 * NoOfElements1) Then
             ErrorMsg(swApp, " % error = " & (((n - NoOfElements1) / NoOfElements1) * 100))
         End If

         'Copy mesh from the first study to the second study
         errCode = Study.CopyMeshFromStudy("Quality")
         If errCode <> 0 Then ErrorMsg(swApp, "Mesh failed to copy")

         n = CWMesh.NodeCount
         If (n < 0.95 * NoOfElements2) Or (n > 1.05 * NoOfElements2) Then
             ErrorMsg(swApp, " % error = " & (((n - NoOfElements2) / NoOfElements2) * 100))
         End If

         'Generate Report
         errCode = Study.GenerateReport("C:\temp", "report", 0)
         If errCode <> 1 Then ErrorMsg(swApp, "Failed to generate report")

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
