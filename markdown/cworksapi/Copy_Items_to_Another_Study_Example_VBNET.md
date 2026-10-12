---
title: "Copy Items to Another Study Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Copy_Items_to_Another_Study_Example_VBNET.htm"
---

# Copy Items to Another Study Example (VB.NET)

This example shows how to copy contact sets and fixtures from one study to another.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 '    (in the IDE, click Project > Add Reference > .NET >
 '    SolidWorks.Interop.cosworks > OK).
 ' 3. Ensure the specified model exists.
 ' 4. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Opens the assembly document.
 ' 2. Copies fixtures and contact sets from Ready to Partial.
 ' 3. Activates Partial.
 ' 4. Meshes Partial.
 ' 5. Analyzes Partial.
  ' 6. Inspect the Immediate window, the Simulation study tree, and the
 '    graphics area.
 '
  ' NOTE: Because the model is used elsewhere, do not save changes.
  ' ---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.cosworks
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()

         Dim COSMOSWORKS As Object
         Dim COSMOSObject As CwAddincallback
         Dim ActDoc As CWModelDoc
         Dim StudyMngr As CWStudyManager
         Dim Study As CWStudy
         Dim CwMesh As CWMesh
         Dim lrMngr As CWLoadsAndRestraintsManager
         Dim Fixture As CWLoadsAndRestraints
         Dim ContactMgr As CWContactManager
         Dim ContactSet As CWContactSet
         Dim errCode As Integer
         Dim errors As Integer
         Dim warnings As Integer
         Dim contactSets(0) As Object
         Dim fixtures(2) As Object
         Dim i As Integer

         Const fileName As String = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\Contact\slider_locker_mechanism.sldasm"

         COSMOSObject = swApp.GetAddInObject("SldWorks.Simulation")
         If COSMOSObject Is Nothing Then ErrorMsg(swApp, "No Simulation add-in")
         COSMOSWORKS = COSMOSObject.COSMOSWORKS
         If COSMOSWORKS Is Nothing Then ErrorMsg(swApp, "No COSMOSWORKS object")

         swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
         ActDoc = COSMOSWORKS.ActiveDoc()
         If ActDoc Is Nothing Then ErrorMsg(swApp, "No active document")

         StudyMngr = ActDoc.StudyManager()
         If StudyMngr Is Nothing Then ErrorMsg(swApp, "No CWStudyManager object")
         Study = StudyMngr.GetStudy(0)
         StudyMngr.ActiveStudy = 0
         If Study Is Nothing Then ErrorMsg(swApp, "No CWStudy object")
         If (Study.Name <> "Ready") Then ErrorMsg(swApp, "Wrong study")
         Debug.Print("Name of study: " & Study.Name)

         ' Create array of names of contact sets to copy
         ContactMgr = Study.ContactManager
         For i = 0 To (ContactMgr.ContactSetCount - 1)
             ContactSet = ContactMgr.GetContactSetAt(i)
             contactSets(i) = ContactSet.ContactName
         Next

         ' Create array of names of fixtures to copy
         lrMngr = Study.LoadsAndRestraintsManager
         For i = 0 To (lrMngr.Count - 1)
             Fixture = lrMngr.GetLoadsAndRestraints(i, errCode)
             fixtures(i) = Fixture.Name
         Next

         ' Copy fixtures and contact sets from Ready study to Partial study
         errCode = ContactMgr.CopyContactsToStudy("Partial", contactSets)
         errCode = lrMngr.CopyLoadsAndRestraintsToStudy("Partial", fixtures)

         ' Activate Partial study
         Study = StudyMngr.GetStudy(1)
         StudyMngr.ActiveStudy = 1

         CwMesh = Study.Mesh
         If CwMesh Is Nothing Then ErrorMsg(swApp, "No CWMesh object")

         ' Set type of mesh to curvature-based
         CwMesh.MesherType = swsMesherType_e.swsMesherTypeAlternate

         ' Set mesh parameters
         CwMesh.GrowthRatio = 1.6
         CwMesh.MinElementsInCircle = 8

         ' Create mesh
         errCode = Study.CreateMesh(swsLinearUnit_e.swsLinearUnitMillimeters, 20, 1)
         If errCode <> 0 Then ErrorMsg(swApp, "Mesh failed with error code as defined in swsStudyMeshError_e: " & errCode)

         errCode = Study.RunAnalysis
         If errCode <> 0 Then ErrorMsg(swApp, "Analysis failed with error code as defined in swsRunAnalysisError_e: " & errCode)

     End Sub
     Sub ErrorMsg(ByVal swApp As SldWorks, ByVal Message As String)
         swApp.SendMsgToUser2(Message, 0, 0)
         swApp.RecordLine("'*** WARNING - General")
         swApp.RecordLine("'*** " & Message)
         swApp.RecordLine("")
     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
