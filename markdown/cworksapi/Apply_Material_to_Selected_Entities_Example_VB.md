---
title: "Apply Material to Selected Entities Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Apply_Material_to_Selected_Entities_Example_VB.htm"
---

# Apply Material to Selected Entities Example (VBA)

This example shows how to apply SOLIDWORKS-defined material to selected entities.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click Tools > References > SOLIDWORKS Simulation version type library).
 ' 3. Verify that Solidworks materials.sldmat exists.
 ' 4. Open public_documents\samples\Simulation Examples\actuator.sldasm.
 ' 5. Click the Ready study tab.
 ' 6. In the Simulation Study tree, expand the Parts folder and multi-select
 '    actuator_casing-1 and actuator_piston-1.
 '
 ' Postconditions:
 ' 1. Applies 2024 Alloy (SN) material to the selected components.
 ' 2. Inspect the Simulation Study tree to verify step 1.
 '
 ' NOTE: Because the assembly is used elsewhere, do not save changes.
 '----------------------------------------------------------------------------
Option Explicit

Sub main()
   Dim SwApp As SldWorks.SldWorks
    Dim COSMOSWORKS As CosmosWorksLib.COSMOSWORKS
    Dim COSMOSObject As CosmosWorksLib.CwAddincallback
    Dim ActDoc As CosmosWorksLib.CWModelDoc
    Dim StudyMngr As CosmosWorksLib.CWStudyManager
    Dim Study As CosmosWorksLib.CWStudy
    Dim SolidMgr As CosmosWorksLib.CWSolidManager
    Dim returnValue As Long
   ' Connect to SOLIDWORKS
    If SwApp Is Nothing Then Set SwApp = Application.SldWorks
   ' Get SOLIDWORKS Simulation object
    Set COSMOSObject = SwApp.GetAddInObject("SldWorks.Simulation")
    If COSMOSObject Is Nothing Then ErrorMsg SwApp, "COSMOSObject object not found"
   Set COSMOSWORKS = COSMOSObject.COSMOSWORKS
    If COSMOSWORKS Is Nothing Then ErrorMsg SwApp, "COSMOSWORKS object not found"
   Set ActDoc = COSMOSWORKS.ActiveDoc()
    If ActDoc Is Nothing Then ErrorMsg SwApp, "No active document"
   ' Get the Ready study
    Set StudyMngr = ActDoc.StudyManager()
    If StudyMngr Is Nothing Then ErrorMsg SwApp, "CWStudyManager object not found"
    Set Study = StudyMngr.GetStudy(0)
    If Study Is Nothing Then ErrorMsg SwApp, "Study not found"
   Set SolidMgr = Study.SolidManager
    If SolidMgr Is Nothing Then ErrorMsg SwApp, "CWSolidManager object not created"
   ' Apply a SOLIDWORKS material to selected components
    returnValue = SolidMgr.SetLibraryMaterialToSelectedEntities("solidworks materials.sldmat", "2024 Alloy (SN)")
    If returnValue = 1 Then ErrorMsg SwApp, "No material applied"
End Sub
Sub ErrorMsg(SwApp As SldWorks.SldWorks, Message As String)
    SwApp.SendMsgToUser2 Message, 0, 0
    SwApp.RecordLine "'*** WARNING - General"
    SwApp.RecordLine "'*** " & Message
    SwApp.RecordLine ""
 End Sub
```
