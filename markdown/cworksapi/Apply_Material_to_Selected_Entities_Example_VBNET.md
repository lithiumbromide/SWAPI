---
title: "Apply Material to Selected Entities Example(VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Apply_Material_to_Selected_Entities_Example_VBNET.htm"
---

# Apply Material to Selected Entities Example(VB.NET)

## Apply Material to Selected Entities Example (VB.NET)

This example shows how to apply SOLIDWORKS-defined materials to selected entities.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 '    (in the IDE, click Project > Add Reference > .NET >
 '    SolidWorks.Interop.cosworks > OK).
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

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.cosworks
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Sub main()

         Dim COSMOSWORKS As CosmosWorks
         Dim COSMOSObject As CwAddincallback
         Dim ActDoc As CWModelDoc
         Dim StudyMngr As CWStudyManager
         Dim Study As CWStudy
         Dim SolidMgr As CWSolidManager
         Dim returnValue As Integer

         ' Get SOLIDWORKS Simulation object
         COSMOSObject = swApp.GetAddInObject("SldWorks.Simulation")
         If COSMOSObject Is Nothing Then ErrorMsg(swApp, "COSMOSObject object not found")

         COSMOSWORKS = COSMOSObject.COSMOSWORKS
         If COSMOSWORKS Is Nothing Then ErrorMsg(swApp, "COSMOSWORKS object not found")

         ActDoc = COSMOSWORKS.ActiveDoc()
         If ActDoc Is Nothing Then ErrorMsg(swApp, "No active document")

         ' Get the Ready study
         StudyMngr = ActDoc.StudyManager()
         If StudyMngr Is Nothing Then ErrorMsg(swApp, "CWStudyManager object not found")
         Study = StudyMngr.GetStudy(0)
         If Study Is Nothing Then ErrorMsg(swApp, "Study not found")

         SolidMgr = Study.SolidManager
         If SolidMgr Is Nothing Then ErrorMsg(swApp, "CWSolidManager object not created")

         ' Apply a SOLIDWORKS material to selected components
         returnValue = SolidMgr.SetLibraryMaterialToSelectedEntities("solidworks materials.sldmat", "2024 Alloy (SN)")
         If returnValue = 1 Then ErrorMsg(swApp, "No material applied")

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
