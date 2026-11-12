---
title: "Get Forces for Selected Beams (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Get_Forces_for_Selected_Beams_Example_VBNET.htm"
---

# Get Forces for Selected Beams (VB.NET)

## Get Forces for Selected Beams Example (VB.NET)

This example shows how to get the force load values for structural members.

```vb
'---------------------------------------------------------------------------
' Preconditions:
' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
'    Tools > Add-ins > SOLIDWORKS Simulation > OK).

' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference

'    (in the IDE, click Project > Add Reference > .NET >
'    SolidWorks.Interop.cosworks > OK).
' 3. Open the Immediate window.
' 4. Open a SOLIDWORKS model that has structural members and a
'    Simulation static study with force loads
'    applied to the structural members.
' 5. Select the Simulation study tab.
' 6. Click the Run button on the Simulation CommandManager to
'    refresh the study results.
' 7. In the Simulation Study tree, select the beams for which
'    you want to know their force loads.
' 8. Run the macro.
'
' Postconditions: The selected beams' forces are printed to the
'    the Immediate window.
'-------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports SolidWorks.Interop.cosworks
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro
    Sub main()

        Dim swModel As ModelDoc2
        Dim swSelMgr As SelectionMgr
        Dim COSMOSWORKS As COSMOSWORKS
        Dim COSMOSObject As CwAddincallback
        Dim ActDoc As CWModelDoc
        Dim StudyMngr As CWStudyManager
        Dim Study As CWStudy
        Dim BeamMgr As CWBeamManager
        Dim Results As CWResults
        Dim actStudy As Long
        Dim beamForce As Long
        Dim nbrSteps As Long
        Dim unit As Long
        Dim errCode As Long
        Dim selBeams() As Object
        Dim nbrSelectedBeams As Long
        Dim varArray As Object
        Dim arrBeamForces As Object
        Dim i As Long
        Dim k As Long

        ' Connect to SOLIDWORKS
        swModel = swApp.ActiveDoc
        swSelMgr = swModel.SelectionManager

        ' Get the SOLIDWORKS Simulation object
        COSMOSObject = swApp.GetAddInObject("SldWorks.Simulation")
        If COSMOSObject Is Nothing Then ErrorMsg(swApp, "COSMOSObject object not found")
        COSMOSWORKS = COSMOSObject.COSMOSWORKS
        If COSMOSWORKS Is Nothing Then ErrorMsg(swApp, "COSMOSWORKS object not found")

        ' Get the active document
        ActDoc = COSMOSWORKS.ActiveDoc()
        If ActDoc Is Nothing Then ErrorMsg(swApp, "No active document")

        ' Get the active study
        StudyMngr = ActDoc.StudyManager()
        If StudyMngr Is Nothing Then ErrorMsg(swApp, "No CWStudyManager object")
        actStudy = StudyMngr.ActiveStudy
        Study = StudyMngr.GetStudy(actStudy)
        If Study Is Nothing Then ErrorMsg(swApp, "Study not created")

        ' Get the results
        Results = Study.Results

        ' Get the selected beams' forces
        BeamMgr = Study.BeamManager
        beamForce = swsBeamForceType_e.swsBeamForceMomentDirection1
        nbrSteps = 1
        unit = swsUnit_e.swsUnitSI
        nbrSelectedBeams = swSelMgr.GetSelectedObjectCount2(-1)
        ReDim selBeams(nbrSelectedBeams)

        For k = 0 To (nbrSelectedBeams - 1)
            selBeams(k) = swSelMgr.GetSelectedObject6(k + 1, -1)
        Next k

        ReDim Preserve selBeams(nbrSelectedBeams - 1)
        varArray = selBeams

        arrBeamForces = Results.GetBeamForcesForEntities(beamForce, nbrSteps, (varArray), unit, errCode)
        For i = 0 To UBound(arrBeamForces)
            Debug.Print(arrBeamForces(i))
        Next

    End Sub

    'Error routine
    Private Sub ErrorMsg(ByVal SwApp As Object, ByVal Message As String)
        SwApp.SendMsgToUser2(Message, 0, 0)
        SwApp.RecordLine("'*** WARNING - General")
        SwApp.RecordLine("'*** " & Message)
        SwApp.RecordLine("")
    End Sub

   Public swApp As SldWorks

End Class
```
