---
title: "Get the Remote Load Forces Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Get_Remote_Load_Forces_Example_VBNET.htm"
---

# Get the Remote Load Forces Example (VB.NET)

This example shows how to get the forces applied to selected entities as a result of transferring a remote load.

NOTE: To get persistent reference identifiers (PIDs) for model selections, you can use [pidcollector.exe](GettingStarted-swsimulationapi.html) or IModelDocExtension::GetPersistReference3.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
  ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 '    (in the IDE, click Project > Add Reference > .NET >
 '    SolidWorks.Interop.cosworks > OK).
  ' 3. Modify the path to the specified model.
 ' 4. Open the Immediate window.
 '
 ' Postconditions: Inspect the Immediate window for the remote load forces.
 '
 ' NOTE: Because this assembly document is used by
 ' SOLIDWORKS Simulation tutorial, do not save any
 ' changes when closing the document.
 '----------------------------------------------------------------------------

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
         'of the expected value. If the actual is not within the tolerance
         'range, an error message is reported with {sMessage}
         'as title, and the function returns false. Otherwise, the function
         'returns true to indicate equivalence/success.
         VerifyTolerance =  True
         If (dActual < ((1 - dTol) * dExpected)) Or (dActual > ((1 + dTol) * dExpected)) Then
             ErrorMsg(SwApp, sMessage & ": Expected = " & CStr(dExpected) & " , Actual = " & CStr(dActual) & " , Tolerance = " & CStr(dTol) & " percent")
             VerifyTolerance = False
         End If
     End Function

     Function SelectByPID(ByVal Part As ModelDoc2, ByVal PIDName As String, ByVal PIDCollection As Collection) As Object
         Dim PID() As Byte
         Dim PIDVariant As Object
         Dim PIDString As String
         Dim i As  Integer
         Dim SelObj As Object

         'Get the string from the collection
         PIDString =  ""
         PIDString = PIDCollection.Item(PIDName)

         'Parse the string into an array
         PIDVariant = Split(PIDString, ",")
         ReDim PID(UBound(PIDVariant))

         'Change to a byte array
         For i = 0 To (UBound(PIDVariant) - 1)
             PID(i) = PIDVariant(i)
         Next i

         'Select the entity
         SelObj = Part.Extension.GetObjectByPersistReference((PID))
         SelectByPID = SelObj
         SelObj = Nothing
     End Function

     Function PIDInitializer() As Collection
         Dim PIDCollection As New Collection
         Dim selection1 As String

         'Constants
         selection1 =   "35,29,213,113,218,129,72,162,168,88,152,178,27,137,239,153,161,1,0,0,16,1,0,0,120,1,109,80,77,75,195,64,20,156,42,181,181,234,65,40,232,197,163,224,69,239,182,232,197,84,44,20,34,155,30,60,8,33,110,54,98,219,36,18,183,224,69,200,143,232,111,240,230,69,252,7,30,253,79,141,243,92,226,7,184,135,157,125,51,243,102,121,175,215,5,86,1,84,203,138,55,177,106,96,3,105,126,30,105,163,76,18,234,198,23,13,52,5,197,201,243,244,190,216,127,25,190,142,107,116,109,59,210,86,228,105,48,181,131,204,6,243,34,25,198,202,220,135,218,201,107,34,171,80,203,15,91,124,15,30,173,127,51,49,218,58,106,155,212,89,96,139,187,236,246,34,202,226,153,33,189,172,14,60,244,112,141,75,20,200,49,129,129,134,101,29,32,101,61,101,45,90,68,213,226,129,111,69,70,20,75,28,17,35,196,56,162,123,4,143,62,133,49,214,75,166,118,254,243,173,0,31,39,125,31,184,218,237,28,186,57,221,205,134,150,199,192,132,113,115,204,24,94,159,231,214,49,246,88,188,157,246,125,217,143,140,214,149,209,178,88,246,247,103,5,205,178,253,23"
         selection1 = selection1    "7,173,119,10,108,150,220,236,47,165,78,254,193,79,249,139,99,22,0,0,0,0,0,0,0,0"
         selection1 = selection1   ",Type=1"

         'Store constants in a collection
         PIDCollection.Add(selection1, "selection1")

         PIDInitializer = PIDCollection
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

         Dim FRES As Double, Tol1 As Double, UResMax As Double

         Dim bStudyFound As Boolean

         Dim DispArray1(0) As Object, Force As Object
         Dim iMeshUnit As Long, iSolverType As Long, iNumberOfStudies As Long
         Dim ix As Long, iStudyType As Long

         sModelName =  "K:\api\HELP\Sample Macros\Simulation\2013\RemoteForces\Parts\Remoteload.sldprt" 'Model name

         'SOLIDWORKS configuration that study is active under (Blank "" = use default)
         sStudyConfig =  ""
         sStudyName =  "Study 1"                  'Study name

         iSolverType = swsSolverType_e.swsSolverTypeFFEPlus      'Solver type

         Dim PIDCollection As New Collection
         PIDCollection = PIDInitializer()

         Part = swApp.OpenDoc6(sModelName, swDocumentTypes_e.swDocPART, 1, "", longstatus, longwarnings)
         If Part Is Nothing Then ErrorMsg(SwApp, "Failed to open: " & sModelName) : GoTo Lastline

         CWAddinCallBack = SwApp.GetAddInObject("SldWorks.Simulation")
         If CWAddinCallBack Is Nothing Then ErrorMsg(SwApp, "CWAddinCallBack object not found") :  GoTo Lastline
         COSMOSWORKS = CWAddinCallBack.COSMOSWORKS
         If COSMOSWORKS Is Nothing Then ErrorMsg(SwApp, "COSMOSWORKS object not found") :  GoTo Lastline

         'Get active document
         ActDoc = COSMOSWORKS.ActiveDoc
         If ActDoc Is Nothing Then ErrorMsg(SwApp, "No active document") : GoTo Lastline

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
         If StudyMngr Is Nothing Then ErrorMsg(SwApp, "StudyMngr object not there") :  GoTo Lastline

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
             ErrorMsg(SwApp,  "Failed to find Study named: " & sStudyName) : GoTo Lastline
         End If

         CWMesh = Study.Mesh
         If CWMesh Is Nothing Then ErrorMsg(SwApp, "No mesh object") : GoTo Lastline

         'Check if need to use the default element size or tolerance
         If ((el = 0) Or (tl = 0)) Then

             'Get the default element size and tolerance
             Call CWMesh.GetDefaultElementSizeAndTolerance(iMeshUnit, el_hold, tl_hold)

             'If element size was not entered, use the default
             If el = 0 Then
                 el = el_hold
             End If

             'If tolerance size was not entered, use the default
             If tl = 0 Then
                 tl = tl_hold
             End If

         End If

         'Create Mesh
         'Using the curvature-based mesher?
         If CWMesh.MesherType = swsMesherType_e.swsMesherTypeAlternate  Then
             'Yes, set the minimum element size equal to the maximum element size
             errCode = Study.CreateMesh(0, el, el)
         Else
             'No, using the standard mesher
             errCode = Study.CreateMesh(0, el, tl)
         End If
         If errCode <> 0 Then ErrorMsg(SwApp, "CreateMesh failed: Error code = "   CStr(errCode)) :  GoTo Lastline

         'Check the mesh state
         If VerifyLong(swApp, swsMeshState_e.swsMeshStateExistsAndCurrent, CWMesh.MeshState, "MeshState indicates that mesh is not current and/or doesn't exist") =  False  Then  GoTo Lastline

         'Check the number of components that failed to mesh
         If VerifyLong(SwApp, 0, CWMesh.GetNoOfFailedComponents,  "GetNoOfFailedComponents indicates mesh failure occurred") =  False  Then  GoTo Lastline

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

         'Running analysis
         errCode = Study.RunAnalysis
         If errCode <> 0 Then ErrorMsg(SwApp, "Analysis failed with error code " & errCode) :  GoTo Lastline

         'Getting results
         CWFeatObj = Study.Results
         If CWFeatObj Is Nothing Then ErrorMsg(SwApp, "Failed to get result object") :  GoTo Lastline

         DispArray1(0) = SelectByPID(Part,  "selection1", PIDCollection)  'Face<1>

         Force = CWFeatObj.GetRemoteForces(1, Nothing, (DispArray1), 0, errCode)

         Debug.Print("Remote load forces:")
         Debug.Print("   Remote load force x-component: " & Force(0))
         Debug.Print("   Remote load force y-component: " & Force(1))
         Debug.Print("   Remote load force z-component: " & Force(2))
         Debug.Print("   Resultant remote load force: " & Force(3))

         If errCode <> 0 Then ErrorMsg(SwApp, "Failed to get remote load force result") :  GoTo Lastline

         FRES = Force(3)
         Tol1 = 0.1
         UResMax = 100
         'Check maximum resultant
         If VerifyTolerance(SwApp, UResMax, CDbl(FRES), Tol1, "Resultant remote load force is beyond tolerance") =  False  Then  GoTo Lastline

 Lastline:

     End Sub

     Public swApp As SldWorks

 End  Class
```
