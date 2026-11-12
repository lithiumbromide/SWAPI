---
title: "Copy Items to Another Study Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Copy_Items_to_Another_Study_Example_VB.htm"
---

# Copy Items to Another Study Example (VBA)

This example shows how to copy contact sets and fixtures from one study to another.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click Tools > References > SOLIDWORKS Simulation version type library).
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
 Option Explicit
 Sub main()
     Dim swApp As SldWorks.SldWorks
     Dim COSMOSWORKS As Object
     Dim COSMOSObject As CosmosWorksLib.CwAddincallback
     Dim ActDoc As CosmosWorksLib.CWModelDoc
     Dim StudyMngr As CosmosWorksLib.CWStudyManager
     Dim Study As CosmosWorksLib.CWStudy
     Dim CwMesh As CosmosWorksLib.CwMesh
     Dim lrMngr As CosmosWorksLib.CWLoadsAndRestraintsManager
     Dim Fixture As CosmosWorksLib.CWLoadsAndRestraints
     Dim ContactMgr As CosmosWorksLib.CWContactManager
     Dim ContactSet As CosmosWorksLib.CWContactSet
     Dim errCode As Long
     Dim errors As Long
     Dim warnings As Long
     Dim contactSets(0) As Variant
     Dim fixtures(2) As Variant
     Dim i As Long

    Const fileName As String = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\Contact\slider_locker_mechanism.sldasm"

    Set swApp = Application.SldWorks
    Set COSMOSObject = swApp.GetAddInObject("SldWorks.Simulation")
     If COSMOSObject Is Nothing Then ErrorMsg swApp, "No Simulation add-in"
     Set COSMOSWORKS = COSMOSObject.COSMOSWORKS
     If COSMOSWORKS Is Nothing Then ErrorMsg swApp, "No COSMOSWORKS object"
    swApp.OpenDoc6 fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_Silent, "", errors, warnings
     Set ActDoc = COSMOSWORKS.ActiveDoc()
     If ActDoc Is Nothing Then ErrorMsg swApp, "No active document"
    Set StudyMngr = ActDoc.StudyManager()
     If StudyMngr Is Nothing Then ErrorMsg swApp, "No CWStudyManager object"
     Set Study = StudyMngr.GetStudy(0)
     StudyMngr.ActiveStudy = 0
     If Study Is Nothing Then ErrorMsg swApp, "No CWStudy object"
     If (Study.Name <> "Ready") Then ErrorMsg swApp, "Wrong study"
     Debug.Print ("Name of study: " & Study.Name)

    ' Create array of names of contact sets to copy
     Set ContactMgr = Study.ContactManager
     For i = 0 To (ContactMgr.ContactSetCount - 1)
         Set ContactSet = ContactMgr.GetContactSetAt(i)
         contactSets(i) = ContactSet.ContactName
     Next

    ' Create array of names of fixtures to copy
     Set lrMngr = Study.LoadsAndRestraintsManager
     For i = 0 To (lrMngr.Count - 1)
         Set Fixture = lrMngr.GetLoadsAndRestraints(i, errCode)
         fixtures(i) = Fixture.Name
     Next

    ' Copy fixtures and contact sets from Ready study to Partial study
     errCode = ContactMgr.CopyContactsToStudy("Partial", contactSets)
     errCode = lrMngr.CopyLoadsAndRestraintsToStudy("Partial", fixtures)

    ' Activate Partial study
     Set Study = StudyMngr.GetStudy(1)
     StudyMngr.ActiveStudy = 1

    Set CwMesh = Study.Mesh
     If CwMesh Is Nothing Then ErrorMsg swApp, "No CWMesh object"
    ' Set type of mesh to curvature-based
     CwMesh.MesherType = swsMesherTypeAlternate
    ' Set mesh parameters
     CwMesh.GrowthRatio = 1.6
     CwMesh.MinElementsInCircle = 8

    ' Create mesh
     errCode = Study.CreateMesh(swsLinearUnitMillimeters, 20, 1)
     If errCode <> 0 Then ErrorMsg swApp, "Mesh failed with error code as defined in swsStudyMeshError_e: " & errCode
    errCode = Study.RunAnalysis
     If errCode <> 0 Then ErrorMsg swApp, "Analysis failed with error code as defined in swsRunAnalysisError_e: " & errCode

End Sub
 Sub ErrorMsg(swApp As SldWorks.SldWorks, Message As String)
     swApp.SendMsgToUser2 Message, 0, 0
     swApp.RecordLine "'*** WARNING - General"
     swApp.RecordLine "'*** " & Message
     swApp.RecordLine ""
 End Sub
```
