---
title: "Get Connector Forces, Moments, and Torques at a Time Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Get_Connector_Forces_at_a_Time_Example_VBNET.htm"
---

# Get Connector Forces, Moments, and Torques at a Time Example (VB.NET)

This example shows how to get the forces, bending moments, and torques for a selected connector at a specified time.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
  ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 '    (in the IDE, click Project > Add Reference > .NET >
 '    SolidWorks.Interop.cosworks > OK).
 ' 3. Ensure the specified model exists.
 ' 4. Open the Immediate window.
 '
 ' Postconditions: Inspect the Immediate window for the connector forces,
 ' moments, and torques.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 '-------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.cosworks
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Function VerifyLong(ByVal SwApp As SldWorks, ByVal lExpected As Long, ByVal lActual As Long, ByVal sMessage As String) As  Boolean
         'This function will compare two long values for equivalence.
         'If they are different, an error message is reported with {sMessage}
         'as title, and the function returns false.
         'If equivalent, the function returns true.
         VerifyLong =  True
         If lActual <> lExpected Then
             ErrorMsg(SwApp, sMessage & ": Expected = " & CStr(lExpected) & " , Actual = " & CStr(lActual))
             VerifyLong = False
         End If
     End Function

     Function VerifyTolerance(ByVal SwApp As SldWorks, ByVal dExpected As Double, ByVal dActual As Double, ByVal dTol As  Double,  ByVal sMessage As  String)  As  Boolean
         'This function will compare two double values to ensure that the actual
         'value is within the specified tolerance range
         'of the expected value. If the actual is not within the tolerance range,
         'an error message is reported with {sMessage}
         'as title, and the function returns false.
         'Otherwise, the function returns true to indicate equivalence/success.

         VerifyTolerance =  True
         If (dActual < ((1 - dTol) * dExpected)) Or (dActual > ((1 + dTol) * dExpected)) Then
             ErrorMsg(SwApp, sMessage & ": Expected = " & CStr(dExpected) & " , Actual = " & CStr(dActual) & " , Tolerance = " & CStr(dTol) & " percent")
             VerifyTolerance = False
         End If
     End Function

     Sub ErrorMsg(ByVal SwApp As SldWorks, ByVal Message As String)
         SwApp.SendMsgToUser2(Message, 0, 0)
         SwApp.RecordLine("'*** WARNING - General")
         SwApp.RecordLine("'*** " & Message)
         SwApp.RecordLine("")
     End Sub

     Sub main()

         Dim Part As ModelDoc2

         Dim COSMOSWORKS As CosmosWorks, CWAddinCallBack As CwAddincallback, ActDoc As CWModelDoc
         Dim StudyMngr As CWStudyManager, Study As CWStudy, CWMesh As CWMesh
         Dim StudyOptions As Object, CWFeatObj As CWResults, ActDocExt As ModelDocExtension

         Dim sModelName As String, sStudyName As String
         Dim sStudyConfig As String

         Dim longstatus As Long, longwarnings As Long, errCode As Integer
         Dim accurateTime as Double

         Dim el As Double, el_hold As Double
         Dim tl As Double, tl_hold As Double

         Dim UResMax As Double, Tol1 As Double

         Dim bStudyFound As Boolean

         Dim Force(15) As Object

         Dim iMeshUnit As Integer, iSolverType As Integer, iNumberOfStudies As Integer
         Dim ix As Integer, iStudyType As Integer

         'Model names
         sModelName =  "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\beam_boltconnection.sldasm"

         'SOLIDWORKS configuration for which study is active (Blank "" = use default)
         sStudyConfig =  ""
         'Study name
         sStudyName =  "Study 1"

         iSolverType = swsSolverType_e.swsSolverTypeDirectSparse  'Solver type

         Part = swApp.OpenDoc6(sModelName, swDocumentTypes_e.swDocASSEMBLY, 1, "", longstatus, longwarnings)
         If Part Is Nothing Then ErrorMsg(SwApp, "Failed to open: " & sModelName)

         CWAddinCallBack = SwApp.GetAddInObject("SldWorks.Simulation")
         If CWAddinCallBack Is Nothing Then ErrorMsg(SwApp, "No CWAddinCallBack object")
         COSMOSWORKS = CWAddinCallBack.COSMOSWORKS
         If COSMOSWORKS Is Nothing Then ErrorMsg(SwApp, "No CosmosWorks object")

         'Get active document
         ActDoc = COSMOSWORKS.ActiveDoc
         If ActDoc Is Nothing Then ErrorMsg(SwApp, "Failed to get active document")

         'If needed, rebuild the model
         ActDocExt = Part.Extension
         If (ActDocExt.NeedsRebuild = True) Then
             Part.ForceRebuild3(False)
         End If

         'If needed, change the SOLIDWORKS configuration to activate the study
         If sStudyConfig <> "" Then
             Part.ShowConfiguration2(sStudyConfig)
         End If

         StudyMngr = ActDoc.StudyManager
         If StudyMngr Is Nothing Then ErrorMsg(SwApp, "No study manager object")

         'Find the study
         bStudyFound =  False
         iNumberOfStudies = StudyMngr.StudyCount
         Study = Nothing
         For ix = 0 To iNumberOfStudies
             StudyMngr.ActiveStudy = ix
             Study = StudyMngr.GetStudy(ix)
             If Study Is Nothing Then ErrorMsg(SwApp, "Failed to get study: " & ix)
             If UCase(Study.Name) = UCase(sStudyName)  Then
                 bStudyFound =  True
                 Exit For
             End If
         Next
         If bStudyFound = False Then
             ErrorMsg(SwApp,  "Failed to find study named: " & sStudyName)
         End If

         'Create mesh
         CWMesh = Study.Mesh
         If CWMesh Is Nothing Then ErrorMsg(SwApp, "No mesh object")

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

         'Create mesh
         If CWMesh.MesherType = swsMesherType_e.swsMesherTypeAlternate  Then
             'Using the curvature-based mesher; set the min element size equal to the max element size
             errCode = Study.CreateMesh(0, el, el)
         Else
             'Using the standard mesher
             errCode = Study.CreateMesh(0, el, tl)
         End If
         If errCode <> 0 Then ErrorMsg(SwApp, "Failed to create mesh: Error code = "   CStr(errCode))

         'Check the mesh state
         VerifyLong(swApp, swsMeshState_e.swsMeshStateExistsAndCurrent, CWMesh.MeshState, "Mesh is not current or does not exist")

         'Check the number of components that failed to mesh
         VerifyLong(SwApp, 0, CWMesh.GetNoOfFailedComponents,  "Mesh failure")

         'Get analysis type
         iStudyType = Study.AnalysisType
         If iStudyType = swsAnalysisStudyType_e.swsAnalysisStudyTypeStatic  Then
             StudyOptions = Study.StaticStudyOptions
         ElseIf iStudyType = swsAnalysisStudyType_e.swsAnalysisStudyTypeThermal  Then
             StudyOptions = Study.ThermalStudyOptions
         ElseIf iStudyType = swsAnalysisStudyType_e.swsAnalysisStudyTypeFrequency  Then
             StudyOptions = Study.FrequencyStudyOptions
         ElseIf iStudyType = swsAnalysisStudyType_e.swsAnalysisStudyTypeBuckling  Then
             StudyOptions = Study.BucklingStudyOptions
         ElseIf iStudyType = swsAnalysisStudyType_e.swsAnalysisStudyTypeNonlinear  Then
             StudyOptions = Study.NonLinearStudyOptions
         Else
             ErrorMsg(swApp,  "Study options for this type of analysis are not available")
         End If
         If StudyOptions Is Nothing Then ErrorMsg(SwApp, "Failed to get study options object")

         'Set solver type
         StudyOptions.SolverType = iSolverType

         'Run analysis
         errCode = Study.RunAnalysis
         If errCode <> 0 Then ErrorMsg(SwApp, "Analysis failed with error code " & errCode)

         'Get results
         CWFeatObj = Study.Results
         If CWFeatObj Is Nothing Then ErrorMsg(SwApp, "Failed to get results object")

         Force = CWFeatObj.GetConnectorForcesWithTimeValue(0.0,  "Counterbore with Nut-1", swsUnit_e.swsUnitSI, accurateTime, errCode)

         If errCode <> 0 Then ErrorMsg(SwApp, "Failed to get connector results at the specified time")

         Debug.Print("Connector forces, moments, and torques for Counterbore with Nut-1 at time, " & accurateTime & ":")
         Debug.Print("   Shear force x-component: " & Force(0))
         Debug.Print("   Shear force y-component: " & Force(1))
         Debug.Print("   Shear force z-component: " & Force(2))
         Debug.Print("   Resultant shear force: " & Force(3))
         Debug.Print("   Axial force x-component: " & Force(4))
         Debug.Print("   Axial force y-component: " & Force(5))
         Debug.Print("   Axial force z-component: " & Force(6))
         Debug.Print("   Resultant axial force: " & Force(7))
         Debug.Print("   Bending moment x-component: " & Force(8))
         Debug.Print("   Bending moment y-component: " & Force(9))
         Debug.Print("   Bending moment z-component: " & Force(10))
         Debug.Print("   Resultant bending moment: " & Force(11))
          Debug.Print("   Torque x-component: " & Force(12))
         Debug.Print("   Torque y-component: " & Force(13))
         Debug.Print("   Torque z-component: " & Force(14))
         Debug.Print("   Resultant torque: " & Force(15))

         'Check maximum resultant bending moment
         UResMax = 0.467
         Tol1 = 0.1
         VerifyTolerance(SwApp, UResMax, CDbl(Force(11)), Tol1, "Resultant bending moment is beyond tolerance")

     End Sub

     Public swApp As SldWorks

 End  Class
```
