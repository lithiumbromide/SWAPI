---
title: "Get Free Body Forces and Moments Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Get_Free_Body_Forces_and_Moments_Example_VBNET.htm"
---

# Get Free Body Forces and Moments Example (VB.NET)

This example shows how to get the free body forces and moments for selected entities.

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
 ' Postconditions: Inspect the Immediate window for the free body forces and moments.
 '
 ' NOTE: Because this model is used by
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

     Function VerifyTolerance(ByVal SwApp As SldWorks, ByVal dExpected As Double, ByVal dActual As Double, ByVal dTol As  Double,  ByVal sMessage As  String)  As  Boolean
         'This function will compare two double values to ensure that the actual
         'value is within the specified tolerance range
         'of the expected value.  If the actual is not within the tolerance range,
         'an error message is reported with {sMessage}
         'as title, and the function returns false. Otherwise, the function returns
         'true to indicate equivalence/success.
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

         Dim selection2 As String

         'Constants
         selection2 =   "35,29,213,113,218,129,72,162,168,88,152,178,27,137,239,153,155,1,0,0,15,1,0,0,120,1,109,80,203,74,195,64,20,61,245,85,45,186,16,10,186,113,41,184,209,189,6,221,152,20,11,133,200,164,136,11,161,196,201,68,108,155,68,198,41,116,83,200,71,248,13,238,220,72,255,160,75,255,169,241,12,211,136,130,179,184,119,238,121,13,119,188,54,176,14,160,90,86,172,236,85,3,123,200,138,59,165,141,154,10,149,14,100,181,58,86,134,53,91,128,217,226,237,248,163,251,217,175,187,51,182,105,12,242,164,19,75,21,77,116,218,77,132,122,25,72,199,109,145,235,8,155,230,30,8,166,38,124,28,42,105,28,180,79,250,58,50,250,57,127,186,137,243,100,172,8,47,171,19,31,23,120,192,45,52,10,12,161,32,97,56,71,200,56,143,56,91,46,38,107,240,202,187,32,98,25,195,222,99,143,145,224,140,234,30,124,234,4,250,216,41,153,218,250,79,199,197,190,46,189,16,184,63,108,157,186,37,93,165,161,233,51,48,101,220,4,99,134,215,231,189,121,142,35,14,243,43,47,108,172,64,187,222,129,93,85,23,89,52,50,65,110,254,252,196,102,185,253,99,2"
         selection2 = selection2    "17,160,101,183,4,126,99,117,140,77,251,6,67,218,108,28,0,0,0,0,0,0,0,0"
         selection2 = selection2   ",Type=1"

         'Store constants in a collection
         PIDCollection.Add(selection2, "selection2")

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

         Dim UResMax As Double, Tol1 As Double

         Dim bStudyFound As Boolean

         Dim DispArray1(0) As Object, DispArray2(0) As Object, Force As Object
         Dim iMeshUnit As Long, iSolverType As Long, iNumberOfStudies As Long
         Dim ix As Long, iStudyType As Long

         sModelName =  "public_documents\samples\tutorial\api\Remoteload.sldprt"        'Model name

         'SOLIDWORKS configuration that study is active under (Blank "" = use default)
         sStudyConfig =  ""
         sStudyName =  "Study 1"                  'Study name

         iSolverType = swsSolverType_e.swsSolverTypeFFEPlus  'Solver type

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
         Study =  Nothing
         iNumberOfStudies = StudyMngr.StudyCount
         For ix = 0 To iNumberOfStudies
             StudyMngr.ActiveStudy = ix
             Study = StudyMngr.GetStudy(ix)
             If Study Is Nothing Then ErrorMsg(SwApp, "Failed to get study number: " & ix) :  GoTo Lastline
             If UCase(Study.Name) = UCase(sStudyName) Then
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
             'Yes, set the mininum element size equal to the maximum element size
             errCode = Study.CreateMesh(0, el, el)
         Else
             'No, using the standard mesher
             errCode = Study.CreateMesh(0, el, tl)
         End If
         If errCode <> 0 Then ErrorMsg(SwApp, "CreateMesh failed: Error code = "   CStr(errCode)) :  GoTo Lastline

         'Check the mesh stat
         If VerifyLong(swApp, swsMeshState_e.swsMeshStateExistsAndCurrent, CWMesh.MeshState, "MeshState indicates that mesh is not current and/or doesn't exist") = False Then  GoTo Lastline

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

         'Running analysis
         errCode = Study.RunAnalysis
         If errCode <> 0 Then ErrorMsg(SwApp, "Analysis failed with error code " & errCode) :  GoTo Lastline

         'Getting results
         CWFeatObj = Study.Results
         If CWFeatObj Is Nothing Then ErrorMsg(SwApp, "Failed to get result object") :  GoTo Lastline

         DispArray1(0) = SelectByPID(Part,  "selection1", PIDCollection)  'Face<1>
         DispArray2(0) = SelectByPID(Part, "selection2", PIDCollection)  'Vertex moment reference

         Force = CWFeatObj.GetFreeBodyForcesAndMoments(Nothing, (DispArray2), (DispArray1), 0, errCode)

         Debug.Print("Free body forces and moments:")
         Debug.Print("   Free body force x-components of all selections: " & Force(0))
         Debug.Print("   Free body force y-components of all selections: " & Force(1))
         Debug.Print("   Free body force z-components of all selections: " & Force(2))
         Debug.Print("   Resultant free body force of all selections: " & Force(3))
         Debug.Print("   Free body moment x-components of all selections: " & Force(4))
         Debug.Print("   Free body moment y-components of all selections: " & Force(5))
         Debug.Print("   Free body moment z-components of all selections: " & Force(6))
         Debug.Print("   Resultant free body moment of all selections: " & Force(7))
         Debug.Print("   Free body force x-components of entire model: " & Force(8))
         Debug.Print("   Free body force y-components of entire model: " & Force(9))
         Debug.Print("   Free body force z-components of entire model: " & Force(10))
         Debug.Print("   Resultant free body force of entire model: " & Force(11))
         Debug.Print("   Free body moment x-components of entire model: " & Force(12))
         Debug.Print("   Free body moment y-components of entire model: " & Force(13))
         Debug.Print("   Free body moment z-components of entire model: " & Force(14))
         Debug.Print("   Resultant free body moment of entire model: " & Force(15))

         If errCode <> 0 Then ErrorMsg(SwApp, "Failed to get free body force result") :  GoTo Lastline
         UResMax = 100
         Tol1 = 0.1

         'Check resultant free body force
         If VerifyTolerance(SwApp, UResMax, CDbl(Force(3)), Tol1, " Resultant free body force of all selections is beyond tolerance") =  False  Then  GoTo Lastline

 Lastline:

     End Sub

     Public swApp As SldWorks

 End  Class
```
