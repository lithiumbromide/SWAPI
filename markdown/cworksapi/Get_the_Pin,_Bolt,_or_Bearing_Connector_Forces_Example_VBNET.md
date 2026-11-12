---
title: "Get Connector Forces, Moments, and Torques Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Get_the_Pin,_Bolt,_or_Bearing_Connector_Forces_Example_VBNET.htm"
---

# Get Connector Forces, Moments, and Torques Example (VB.NET)

This example shows how to get the shear forces, axial forces, bending moments, and torques for a selected connector.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
  ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 '    (in the IDE, click Project > Add Reference > .NET >
 '    SolidWorks.Interop.cosworks > OK).
 ' 3. Modify the path to the specified model.
 ' 4. Open the Immediate window.
 '
 ' Postconditions: Inspect the Immediate window for the connector forces,
 ' moments, and torques.
 '
 ' NOTE: Because this assembly document is used elsewhere,
 '  do not save any changes when closing the document.
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

         Dim longstatus As Long, longwarnings As Long, errCode As Long

         Dim el As Double, el_hold As Double
         Dim tl As Double, tl_hold As Double

         Dim UResMax As Double, Tol1 As Double

         Dim bStudyFound As Boolean

         Dim Force(15) As Object

         Dim iMeshUnit As Long, iSolverType As Long, iNumberOfStudies As Long
         Dim ix As Long, iStudyType As Long

         'Model names
         sModelName =  "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\beam_boltconnection.sldasm"

         'SOLIDWORKS configuration for which study is active (Blank "" = use default)
         sStudyConfig =  ""
         'Study name
         sStudyName =  "Study 1"

         iSolverType = swsSolverType_e.swsSolverTypeDirectSparse  'Solver type

         Part = swApp.OpenDoc6(sModelName, swDocumentTypes_e.swDocASSEMBLY, 1, "", longstatus, longwarnings)
         If Part Is Nothing Then ErrorMsg(SwApp, "Failed to open: " & sModelName) : GoTo Lastline

         CWAddinCallBack = SwApp.GetAddInObject("SldWorks.Simulation")
         If CWAddinCallBack Is Nothing Then ErrorMsg(SwApp, "Failed to get CWAddinCallBack object") :  GoTo Lastline
         COSMOSWORKS = CWAddinCallBack.COSMOSWORKS
         If COSMOSWORKS Is Nothing Then ErrorMsg(SwApp, "Failed to get COSMOSWORKS object") :  GoTo Lastline

         'Get Active document
         ActDoc = COSMOSWORKS.ActiveDoc
         If ActDoc Is Nothing Then ErrorMsg(SwApp, "Failed to get active document") : GoTo Lastline

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
         If StudyMngr Is Nothing Then ErrorMsg(SwApp, "Failed to get StudyManager object") :  GoTo Lastline

         'Find the study
         bStudyFound =  False
         iNumberOfStudies = StudyMngr.StudyCount
         Study = Nothing
         For ix = 0 To iNumberOfStudies
             StudyMngr.ActiveStudy = ix
             Study = StudyMngr.GetStudy(ix)
             If Study Is Nothing Then ErrorMsg(SwApp, "Failed to get study number: " & ix) :  GoTo Lastline
             If UCase(Study.Name) = UCase(sStudyName)  Then
                 bStudyFound =  True
                 Exit For
             End If
         Next
         If bStudyFound = False Then
             ErrorMsg(SwApp,  "Failed to find study named: " & sStudyName) : GoTo Lastline
         End If

         'Create mesh
         CWMesh = Study.Mesh
         If CWMesh Is Nothing Then ErrorMsg(SwApp, "No mesh object") : GoTo Lastline

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
         If CWMesh.MesherType = swsMesherType_e.swsMesherTypeAlternate  Then
             'Using the curvature-based mesher; set the min element size equal to the max element size
             errCode = Study.CreateMesh(0, el, el)
         Else
             'Using the standard mesher
             errCode = Study.CreateMesh(0, el, tl)
         End If
         If errCode <> 0 Then ErrorMsg(SwApp, "CreateMesh failed: Error code = "   CStr(errCode)) :  GoTo Lastline

         'Check the mesh state
         If VerifyLong(swApp, swsMeshState_e.swsMeshStateExistsAndCurrent, CWMesh.MeshState, "MeshState indicates that mesh is not current and/or doesn't exist") =  False  Then  GoTo Lastline

         'Check the number of components that failed to mesh
         If VerifyLong(SwApp, 0, CWMesh.GetNoOfFailedComponents,  "GetNoOfFailedComponents indicates mesh failure") = False Then  GoTo Lastline

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
             ErrorMsg(swApp,  "StudyOptions for this analysis type is not yet supported") :  GoTo Lastline
         End If
         If StudyOptions Is Nothing Then ErrorMsg(SwApp, "Failed to get StudyOptions object") :  GoTo Lastline

         'Set solver type
         StudyOptions.SolverType = iSolverType

         'Running Analysis
         errCode = Study.RunAnalysis
         If errCode <> 0 Then ErrorMsg(SwApp, "Analysis failed with error code " & errCode) :  GoTo Lastline

         'Getting Results
         CWFeatObj = Study.Results
         If CWFeatObj Is Nothing Then ErrorMsg(SwApp, "Failed to get result object") :  GoTo Lastline

         Force = CWFeatObj.GetConnectorForces2(1,  "Counterbore with Nut-1", 0, errCode)

         If errCode <> 0 Then ErrorMsg(SwApp, "Failed to get connector force result") :  GoTo Lastline

         Debug.Print("Connector forces, moments, and torques for Counterbore with Nut-1:")
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

         'Check max resultant bending moment
         UResMax = 0.467
         Tol1 = 0.1
         If VerifyTolerance(SwApp, UResMax, CDbl(Force(11)), Tol1, "Resultant bending moment is beyond tolerance") =  False  Then  GoTo Lastline

 Lastline:

     End Sub

     Public swApp As SldWorks

 End  Class
```
