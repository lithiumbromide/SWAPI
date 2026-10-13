---
title: "Change Beam to Solid Body and Back Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Change_Beam_to_Solid_Body_and_Back_Example_VBNET.htm"
---

# Change Beam to Solid Body and Back Example (VB.NET)

This example shows how to change a beam to a solid body and then back to a beam.

```vb
'----------------------------------------------------------------------------
' Preconditions:
' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
'    Tools > Add-ins > SOLIDWORKS Simulation > OK).

' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference

'    (in the IDE, click Project > Add Reference > .NET >
'    SolidWorks.Interop.cosworks > OK).
' 3. Open the Immediate window.

' 4. Verify that the specified part exists.
'
' Postconditions: Examine the Immediate window to verify
' that beams were converted to solid bodies and then back to beams.
' You can also expand and examine the Simulation Study tree to verify the
' macro.
'
' NOTES: Because the part document is used elsewhere, do not save changes.
'-------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports SolidWorks.Interop.cosworks
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim COSMOSWORKS As CosmosWorks
        Dim COSMOSObject As CwAddincallback
        Dim ActDoc As CWModelDoc
        Dim StudyMngr As CWStudyManager
        Dim Study As CWStudy
        Dim BeamMgr As CWBeamManager
        Dim BeamBody As CWBeamBody
        Dim SolidMgr As CWSolidManager
        Dim SolidComponent As CWSolidComponent
        Dim SolidBody As CWSolidBody
        Dim nbrBeamBodies As Integer
        Dim beamBodyType As Integer
        Dim errors As Integer, warnings As Integer
        Dim errCode As Integer
        Dim j As Integer
        Dim nbrSolidComponents As Integer
        Dim nbrSolidBodies As Integer
        Dim k As Integer

        'Get the SOLIDWORKS Simulation object
        COSMOSObject = swApp.GetAddInObject("SldWorks.Simulation")
        If COSMOSObject Is Nothing Then ErrorMsg(swApp, "No CwAddincallbackobject")
        COSMOSWORKS = COSMOSObject.COSMOSWORKS
        If COSMOSWORKS Is Nothing Then ErrorMsg(swApp, "No COSMOSWORKS object")

        'Open and get the active document
        swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\Beams\Beam_Truss.sldprt", swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        ActDoc = COSMOSWORKS.ActiveDoc()
        If ActDoc Is Nothing Then ErrorMsg(swApp, "No active document")

        'Get the study
        StudyMngr = ActDoc.StudyManager()
        If StudyMngr Is Nothing Then ErrorMsg(swApp, "No CWStudyManager object")
        StudyMngr.ActiveStudy = 0
        Study = StudyMngr.GetStudy(0)
        If Study Is Nothing Then ErrorMsg(swApp, "No CWStudy object")

        'Get and set beams to solids and solids to beams
        Debug.Print("Beams...")
        BeamMgr = Study.BeamManager
        nbrBeamBodies = BeamMgr.BeamCount
        Debug.Print("  Number of beams: " & nbrBeamBodies)
        BeamBody = Nothing
        'Convert beams to solid bodies
        For j = 0 To (nbrBeamBodies - 1)
            BeamBody = BeamMgr.GetBeamBodyAt(0, errCode)
            If errCode <> 0 Then ErrorMsg(swApp, "No beam body")
            Debug.Print("    Name of beam body: " & BeamBody.BeamBodyName)
            beamBodyType = BeamBody.BeamType
            If beamBodyType = 0 Then
                BeamBody.ConvertToSolidBody()
                Debug.Print("      Beam converted to solid body")
            End If
            BeamBody = Nothing
        Next j

        Debug.Print(" ")

        'Convert solid bodies to beams
        Debug.Print("Solid components and bodies...")
        'Get solid bodies and components
        SolidMgr = Study.SolidManager
        If SolidMgr Is Nothing Then ErrorMsg(swApp, "No CWSolidManager object")
        nbrSolidComponents = SolidMgr.ComponentCount
        Debug.Print("  Number of solid components: " & nbrSolidComponents)
        For j = 0 To (nbrSolidComponents - 1)
            SolidComponent = SolidMgr.GetComponentAt(j, errCode)
            If SolidComponent Is Nothing Then ErrorMsg(swApp, "No solid component")
            Debug.Print("      Name of solid components: " & SolidComponent.ComponentName)
            ' Get solid bodies
            nbrSolidBodies = SolidComponent.SolidBodyCount
            Debug.Print("        Number of solid bodies: " & nbrSolidBodies)
            For k = 0 To (nbrSolidBodies - 1)
                SolidBody = SolidComponent.GetSolidBodyAt(0, errCode)
                If errCode <> 0 Then ErrorMsg(swApp, "No solid body")
                Debug.Print("           Name of solid body: " & SolidBody.SolidBodyName)
                SolidBody.ConvertToBeamBody()
                Debug.Print("             Solid body converted to beam")
                SolidBody = Nothing
            Next k
        Next j

    End Sub
    Private Sub ErrorMsg(ByVal SwApp As SldWorks, ByVal Message As String)
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
