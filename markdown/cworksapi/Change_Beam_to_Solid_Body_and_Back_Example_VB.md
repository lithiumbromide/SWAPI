---
title: "Change Beam to Solid Body and Back Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Change_Beam_to_Solid_Body_and_Back_Example_VB.htm"
---

# Change Beam to Solid Body and Back Example (VBA)

This example shows how to change a beam to a solid body and then back to a beam.

```vb
'---------------------------------------------------------------------------
' Preconditions:
' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click

'    Tools > Add-ins > SOLIDWORKS Simulation > OK).

' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,

'    click Tools > References > SOLIDWORKS Simulation version type library).
' 3. Open the Immediate window.

' 4. Verify that the specified part exists.
'
' Postconditions: Examine the output in the Immediate window to verify
' that beams were converted to solid bodies and then back to beams.
' You can also expand and examine the Simulation Study tree to verify the
' macro.
'
' NOTES: Because the part document is used elsewhere, do not save changes.
'---------------------------------------------------------------------------
Option Explicit

Sub main()

   Dim SwApp As SldWorks.SldWorks
   Dim COSMOSWORKS As CosmosWorksLib.COSMOSWORKS
   Dim COSMOSObject As CosmosWorksLib.CwAddincallback
   Dim ActDoc As CosmosWorksLib.CWModelDoc
   Dim StudyMngr As CosmosWorksLib.CWStudyManager
   Dim Study As CosmosWorksLib.CWStudy
   Dim BeamMgr As CosmosWorksLib.CWBeamManager
   Dim BeamBody As CosmosWorksLib.CWBeamBody
   Dim SolidMgr As CosmosWorksLib.CWSolidManager
   Dim SolidComponent As CosmosWorksLib.CWSolidComponent
   Dim SolidBody As CosmosWorksLib.CWSolidBody
   Dim nbrBeamBodies As Long
   Dim beamBodyType As Long
   Dim errors As Long, warnings As Long
   Dim errCode As Long
   Dim j As Long
   Dim nbrSolidComponents As Long
   Dim nbrSolidBodies As Long
   Dim k As Long

    'Connect to SOLIDWORKS
    If SwApp Is Nothing Then Set SwApp = Application.SldWorks

    'Get the SOLIDWORKS Simulation object
    Set COSMOSObject = SwApp.GetAddInObject("SldWorks.Simulation")
    If COSMOSObject Is Nothing Then ErrorMsg SwApp, "No CwAddincallback object"
    Set COSMOSWORKS = COSMOSObject.COSMOSWORKS
    If COSMOSWORKS Is Nothing Then ErrorMsg SwApp, "No COSMOSWORKS object"

    'Open and get the active document
    SwApp.OpenDoc6 "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\Beams\Beam_Truss.sldprt", swDocPART, swOpenDocOptions_Silent, "", errors, warnings
    Set ActDoc = COSMOSWORKS.ActiveDoc()
    If ActDoc Is Nothing Then ErrorMsg SwApp, "No active document"

    'Get the study
    Set StudyMngr = ActDoc.StudyManager()
    If StudyMngr Is Nothing Then ErrorMsg SwApp, "No CWStudyManager object"
    StudyMngr.ActiveStudy = 0
    Set Study = StudyMngr.GetStudy(0)
    If Study Is Nothing Then ErrorMsg SwApp, "No CWStudy object"

    'Get and set beams to solids and solids to beams
    Debug.Print "Beams..."
    Set BeamMgr = Study.BeamManager
    nbrBeamBodies = BeamMgr.BeamCount
    Debug.Print "  Number of beams: " & nbrBeamBodies
    Set BeamBody = Nothing
    'Convert beams to solid bodies
    For j = 0 To (nbrBeamBodies - 1)
        Set BeamBody = BeamMgr.GetBeamBodyAt(0, errCode)
        If errCode <> 0 Then ErrorMsg SwApp, "No beam body"
        Debug.Print "    Name of beam body: " & BeamBody.BeamBodyName
        beamBodyType = BeamBody.BeamType
        If beamBodyType = 0 Then
            BeamBody.ConvertToSolidBody
            Debug.Print "      Beam converted to solid body"
        End If
        Set BeamBody = Nothing
    Next j

    Debug.Print " "

    'Convert solid bodies to beams
    Debug.Print "Solid components and bodies..."
    'Get solid bodies and components
    Set SolidMgr = Study.SolidManager
    If SolidMgr Is Nothing Then ErrorMsg SwApp, "No CWSolidManager object"
    nbrSolidComponents = SolidMgr.ComponentCount
    Debug.Print "  Number of solid components: " & nbrSolidComponents
    For j = 0 To (nbrSolidComponents - 1)
        Set SolidComponent = SolidMgr.GetComponentAt(j, errCode)
        If SolidComponent Is Nothing Then ErrorMsg SwApp, "No solid component"
        Debug.Print "      Name of solid components: " & SolidComponent.ComponentName
        ' Get solid bodies
        nbrSolidBodies = SolidComponent.SolidBodyCount
        Debug.Print "        Number of solid bodies: " & nbrSolidBodies
        For k = 0 To (nbrSolidBodies - 1)
            Set SolidBody = SolidComponent.GetSolidBodyAt(0, errCode)
            If errCode <> 0 Then ErrorMsg SwApp, "No solid body"
            Debug.Print "           Name of solid body: " & SolidBody.SolidBodyName
            SolidBody.ConvertToBeamBody
            Debug.Print "             Solid body converted to beam"
            Set SolidBody = Nothing
        Next k
    Next j

End Sub
Function ErrorMsg(SwApp As SldWorks.SldWorks, Message As String)
    SwApp.SendMsgToUser2 Message, 0, 0
    SwApp.RecordLine "'*** WARNING - General"
    SwApp.RecordLine "'*** " & Message
    SwApp.RecordLine ""

End Function
```
