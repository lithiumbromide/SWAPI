---
title: "Get Contact or Friction Forces Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Get_Normal_Contact_Friction_Force_Example_VBNET.htm"
---

# Get Contact or Friction Forces Example (VB.NET)

This example shows how to get the contact or friction forces for selected entities.

NOTE: To get persistent reference identifiers (PIDs) for model selections, you can use [pidcollector.exe](GettingStarted-swsimulationapi.html) or IModelDocExtension::GetPersistReference3.

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
 ' Postconditions: Inspect the Immediate window for the x-, y-, z-component
 ' and resultant contact forces for the selected entity.
 '
 ' NOTE: Because this assembly document is used by
 ' SOLIDWORKS Simulation tutorial, do not save any
 ' changes when closing the document.
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

         'Contact plane
         Dim selection1 As String
         'Constants
         selection1 =   "35,29,213,113,218,129,72,162,168,88,152,178,27,137,239,153,84,2,0,0,58,1,0,0,120,1,125,81,193,78,194,64,16,125,168,16,141,26,53,154,112,245,194,17,18,79,38,158,4,132,72,132,104,90,78,132,164,41,237,86,80,218,154,186,68,61,152,244,232,7,248,27,94,252,5,255,139,250,134,210,4,37,233,108,118,103,247,205,190,217,157,55,31,199,192,38,128,100,158,84,26,80,176,225,227,20,47,152,64,99,204,221,24,33,166,196,159,81,197,25,46,49,90,222,177,184,147,136,134,67,31,112,40,238,52,121,114,218,98,198,67,206,194,114,150,229,133,164,128,93,248,97,219,118,148,161,60,203,145,160,88,73,22,249,3,237,253,231,179,242,213,249,238,103,62,165,157,144,214,10,92,97,154,179,200,235,184,134,122,178,156,52,86,146,148,134,229,72,250,125,185,247,170,111,71,15,202,209,41,116,68,168,105,234,104,18,220,95,219,129,59,85,132,231,73,189,137,11,12,209,70,11,117,122,15,209,162,112,41,97,189,152,33,26,57,165,90,44,90,228,209,204,147,47,96,13,38,186,184,194,29,12,244,177,19,243,31,7,249,140,13,224,237,102,208,91,136,"
         selection1 = selection1    "156,234,147,174,100,22,171,108,78,58,87,35,53,30,206,187,131,94,166,173,168,82,22,133,162,208,55,31,117,43,208,127,4,44,198,219,200,40,210,179,189,24,88,197,164,43,255,49,126,106,13,203,158,99,136,246,11,23,144,126,96,0,0,0,0,0,0,0,0"
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
         Dim i As  Long

         Dim el As Double, el_hold As Double
         Dim tl As Double, tl_hold As Double

         Dim bStudyFound As Boolean

         Dim DispArray1(0) As Object, Force As Object

         Dim iMeshUnit As Long, iSolverType As Long, iNumberOfStudies As Long
         Dim ix As Long, iStudyType As Long

         sModelName =  "beam_boltconnection.sldasm"        'Model name

         'SOLIDWORKS configuration that study is active under (Blank "" = use default)
         sStudyConfig =  ""
         sStudyName =  "Study 1"  'Study name

         Dim PIDCollection As New Collection
         PIDCollection = PIDInitializer()

         Part = swApp.OpenDoc6("public_documents\samples\tutorial\api\beam_boltconnection.SLDASM", swDocumentTypes_e.swDocASSEMBLY, 1, "", longstatus, longwarnings)
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
         Study =  Nothing
         iNumberOfStudies = StudyMngr.StudyCount
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
         'Using the curvature-based mesher?
         If CWMesh.MesherType = swsMesherType_e.swsMesherTypeAlternate  Then
             'Yes, set the min element size equal to the max element size
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
         If CWFeatObj Is Nothing Then ErrorMsg(SwApp, "Failed to get results object") :  GoTo Lastline

         DispArray1(0) = SelectByPID(Part,  "selection1", PIDCollection)

         Force = CWFeatObj.GetContactForcesAndFriction(1,  Nothing, (DispArray1), swsNForceType_e.swsNForceTypeNormal, 0, errCode)
         If errCode <> 0 Then ErrorMsg(SwApp, "Failed to get contact force result") :  GoTo Lastline

         Debug.Print("  x, y, z, and resultant contact forces:")
         For i = 0 To UBound(Force)
             Debug.Print("    " & Force(i))
         Next

 Lastline:

     End Sub

     Public swApp As SldWorks

 End  Class
```
