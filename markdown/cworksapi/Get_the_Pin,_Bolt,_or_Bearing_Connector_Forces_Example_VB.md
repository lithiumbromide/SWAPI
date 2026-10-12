---
title: "Get Connector Forces, Moments, and Torques Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Get_the_Pin,_Bolt,_or_Bearing_Connector_Forces_Example_VB.htm"
---

# Get Connector Forces, Moments, and Torques Example (VBA)

This example shows how to get the shear forces, axial forces, bending moments, and torques for a selected connector.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click Tools > References > SOLIDWORKS Simulation version type library).
 ' 3. Add the SOLIDWORKS Constant type library as a reference
 '    (in the IDE, click Tools > References >
 '    SOLIDWORKS version Constant type library).
 ' 4. Modify the path to the specified model.
 ' 5. Open the Immediate window.
 '
 ' Postconditions: Inspect the Immediate window for the connector forces,
 ' moments, and torques.
 '
 ' NOTE: Because this assembly document is used by
 ' SOLIDWORKS Simulation tutorial, do not save any
 ' changes when closing the document.
 '-------------------------------------------------------------------------
Option Explicit
Function VerifyLong(SwApp As SldWorks.SldWorks, lExpected As Long, lActual As Long, sMessage As String) As Boolean
     'This function will compare two long values for equivalence.
     'If they are different, an error message is reported with {sMessage}
     'as title, and the function returns false.
     'If equivalent, the function returns true.
     VerifyLong = True
     If lActual <> lExpected Then
         ErrorMsg SwApp, sMessage & ": Expected = " & CStr(lExpected) & " , Actual = " & CStr(lActual)
         VerifyLong = False
     End If
 End Function
Function VerifyTolerance(SwApp As SldWorks.SldWorks, dExpected As Double, dActual As Double, dTol As Double, sMessage As String) As Boolean
     'This function will compare two double values to ensure that the actual
     'value is within the specified tolerance range
     'of the expected value. If the actual is not within the tolerance range,
     'an error message is reported with {sMessage}
     'as title, and the function returns false.
     'Otherwise, the function returns true to indicate equivalence/success.
    VerifyTolerance = True
     If (dActual < ((1 - dTol) * dExpected)) Or (dActual > ((1 + dTol) * dExpected)) Then
         ErrorMsg SwApp, sMessage & ": Expected = " & CStr(dExpected) & " , Actual = " & CStr(dActual) & " , Tolerance = " & CStr(dTol) & " percent"
         VerifyTolerance = False
     End If
 End Function
Function ErrorMsg(SwApp As SldWorks.SldWorks, Message As String)
     SwApp.SendMsgToUser2 Message, 0, 0
     SwApp.RecordLine "'*** WARNING - General"
     SwApp.RecordLine "'*** " & Message
     SwApp.RecordLine ""
 End Function
Sub main()

    Dim SwApp As SldWorks.SldWorks
     Dim Part As ModelDoc2
    Dim COSMOSWORKS As CosmosWorksLib.COSMOSWORKS, CWAddinCallBack As CosmosWorksLib.CWAddinCallBack, ActDoc As CosmosWorksLib.CWModelDoc
     Dim StudyMngr As CosmosWorksLib.CWStudyManager, Study As CosmosWorksLib.CWStudy, CWMesh As CosmosWorksLib.CWMesh
     Dim StudyOptions As Object, CWFeatObj As CosmosWorksLib.CWResults, ActDocExt As SldWorks.ModelDocExtension

    Dim sModelName As String, sStudyName As String
     Dim sStudyConfig As String

    Dim longstatus As Long, longwarnings As Long, errCode As Long

    Dim el As Double, el_hold As Double
     Dim tl As Double, tl_hold As Double

    Dim UResMax As Double, Tol1 As Double

    Dim bStudyFound As Boolean

    Dim Force As Variant

     Dim iMeshUnit As Long, iSolverType As Long, iNumberOfStudies As Long
     Dim ix As Long, iStudyType As Long

    'Model names
     sModelName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\beam_boltconnection.sldasm"

    'SOLIDWORKS configuration for which study is active (Blank "" = use default)
     sStudyConfig = ""
     'Study name
     sStudyName = "Study 1"

    iSolverType = swsSolverTypeDirectSparse 'Solver type
    Set SwApp = Application.SldWorks
     If SwApp Is Nothing Then Exit Sub
    Set Part = SwApp.OpenDoc6(sModelName, swDocASSEMBLY, 1, "", longstatus, longwarnings)
     If Part Is Nothing Then ErrorMsg SwApp, "Failed to open: " & sModelName: GoTo Lastline

    Set CWAddinCallBack = SwApp.GetAddInObject("SldWorks.Simulation")
     If CWAddinCallBack Is Nothing Then ErrorMsg SwApp, "CWAddinCallBack object not found": GoTo Lastline
     Set COSMOSWORKS = CWAddinCallBack.COSMOSWORKS
     If COSMOSWORKS Is Nothing Then ErrorMsg SwApp, "COSMOSWORKS object not found": GoTo Lastline

    'Get Active document
     Set ActDoc = COSMOSWORKS.ActiveDoc
     If ActDoc Is Nothing Then ErrorMsg SwApp, "No active document": GoTo Lastline

    'If needed, rebuild the model
     Set ActDocExt = Part.Extension
     If (ActDocExt.NeedsRebuild = True) Then
         Part.ForceRebuild3 (False)
     End If

    'If needed, change the SOLIDWORKS configuration to activate the study
     If sStudyConfig <> "" Then
         Part.ShowConfiguration2 (sStudyConfig)
     End If

    Set StudyMngr = ActDoc.StudyManager
     If StudyMngr Is Nothing Then ErrorMsg SwApp, "StudyMngr object not there": GoTo Lastline

    'Find the study
     bStudyFound = False
     iNumberOfStudies = StudyMngr.StudyCount
     For ix = 0 To iNumberOfStudies
         StudyMngr.ActiveStudy = ix
         Set Study = StudyMngr.GetStudy(ix)
         If Study Is Nothing Then ErrorMsg SwApp, "Failed to get study number: " & ix: GoTo Lastline
         If UCase(Study.Name) = UCase(sStudyName) Then
             bStudyFound = True
             Exit For
         End If
     Next
     If bStudyFound = False Then
         ErrorMsg SwApp, "Failed to find study named: " & sStudyName: GoTo Lastline
     End If

    'Create mesh
     Set CWMesh = Study.Mesh
     If CWMesh Is Nothing Then ErrorMsg SwApp, "No mesh object": GoTo Lastline

    'Check to use the default element size or tolerance
     If ((el = 0) Or (tl = 0)) Then

        'Get the default element size and tolerance
         Call CWMesh.GetDefaultElementSizeAndTolerance(iMeshUnit, el_hold, tl_hold)

       'If element size was not entered, use the default
         If el = 0 Then
            el = el_hold
         End If

        'If tolerance size was not entered, use the default
         tl = 0.025
         If tl = 0 Then
             tl = tl_hold
         End If

    End If

    'Create Mesh
     If CWMesh.MesherType = swsMesherTypeAlternate Then
         'Using the curvature-based mesher; set the min element size equal to the max element size
         errCode = Study.CreateMesh(0, el, el)
     Else
         'Using the standard mesher
         errCode = Study.CreateMesh(0, el, tl)
     End If
     If errCode <> 0 Then ErrorMsg SwApp, "CreateMesh failed: Error code = " & CStr(errCode): GoTo Lastline

    'Check the mesh state
     If VerifyLong(SwApp, swsMeshStateExistsAndCurrent, CWMesh.MeshState, "MeshState indicates that mesh is not current and/or doesn't exist") = False Then GoTo Lastline
    'Check the number of components that failed to mesh
     If VerifyLong(SwApp, 0, CWMesh.GetNoOfFailedComponents, "GetNoOfFailedComponents indicates mesh failure") = False Then GoTo Lastline
    'Get analysis type
     iStudyType = Study.AnalysisType
     If iStudyType = swsAnalysisStudyTypeStatic Then
         Set StudyOptions = Study.StaticStudyOptions
     ElseIf iStudyType = swsAnalysisStudyTypeThermal Then
         Set StudyOptions = Study.ThermalStudyOptions
     ElseIf iStudyType = swsAnalysisStudyTypeFrequency Then
         Set StudyOptions = Study.FrequencyStudyOptions
     ElseIf iStudyType = swsAnalysisStudyTypeBuckling Then
         Set StudyOptions = Study.BucklingStudyOptions
     ElseIf iStudyType = swsAnalysisStudyTypeNonlinear Then
         Set StudyOptions = Study.NonlinearStudyOptions
     Else
         ErrorMsg SwApp, "StudyOptions for this analysis type is not yet supported": GoTo Lastline
     End If
     If StudyOptions Is Nothing Then ErrorMsg SwApp, "Failed to get StudyOptions object": GoTo Lastline

    'Set solver type
     StudyOptions.SolverType = iSolverType

    'Running Analysis
     errCode = Study.RunAnalysis
     If errCode <> 0 Then ErrorMsg SwApp, "Analysis failed with error code " & errCode: GoTo Lastline

    'Getting Results
     Set CWFeatObj = Study.Results
     If CWFeatObj Is Nothing Then ErrorMsg SwApp, "Failed to get result object": GoTo Lastline

    Force = CWFeatObj.GetConnectorForces2(1, "Counterbore with Nut-1", 0, errCode)

    If errCode <> 0 Then ErrorMsg SwApp, "Failed to get connector force result": GoTo Lastline

    Debug.Print "Connector forces, moments, and torques for Counterbore with Nut-1:"
     Debug.Print "   Shear force x-component: " & Force(0)
     Debug.Print "   Shear force y-component: " & Force(1)
     Debug.Print "   Shear force z-component: " & Force(2)
     Debug.Print "   Resultant shear force: " & Force(3)
     Debug.Print "   Axial force x-component: " & Force(4)
     Debug.Print "   Axial force y-component: " & Force(5)
     Debug.Print "   Axial force z-component: " & Force(6)
     Debug.Print "   Resultant axial force: " & Force(7)
     Debug.Print "   Bending moment x-component: " & Force(8)
     Debug.Print "   Bending moment y-component: " & Force(9)
     Debug.Print "   Bending moment z-component: " & Force(10)
     Debug.Print "   Resultant bending moment: " & Force(11)
     Debug.Print "   Torque x-component: " & Force(12)
     Debug.Print "   Torque y-component: " & Force(13)
     Debug.Print "   Torque z-component: " & Force(14)
     Debug.Print "   Resultant torque: " & Force(15)

    'Check max resultant bending moment
     UResMax = 0.467
     Tol1 = 0.1
     If VerifyTolerance(SwApp, UResMax, CDbl(Force(11)), Tol1, "Resultant bending moment is beyond tolerance") = False Then GoTo Lastline
Lastline:

End Sub
```
