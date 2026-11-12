---
title: "Add Remote Load Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Add_Remote_Load_Example_VB.htm"
---

# Add Remote Load Example (VBA)

This example shows how to add a remote load to a static study.

NOTE: To get persistent reference identifiers (PIDs) for model selections, you can use [pidcollector.exe](GettingStarted-swsimulationapi.html) or IModelDocExtension::GetPersistReference3.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click Tools > References > SOLIDWORKS Simulation version type library).
 ' 3. Ensure that the specified material libaray exists.
 ' 4. Open public_documents\samples\tutorial\api\Mxd_asm.sldasm.
 '
 ' Postconditions:
 ' 1. Creates study, Static_Mixed6.
 ' 2. Inspect the Immediate window for the remote load settings and
 '    analysis results.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 ' ---------------------------------------------------------------------------
Option Explicit

Sub main()

    Dim SwApp           As SldWorks.SldWorks
     Dim Part            As SldWorks.ModelDoc2
     Dim COSMOSWORKS     As CosmosWorksLib.COSMOSWORKS
     Dim CWAddinCallBack As CosmosWorksLib.CWAddinCallBack
     Dim ActDoc          As CosmosWorksLib.CWModelDoc
     Dim StudyMngr       As CosmosWorksLib.CWStudyManager
     Dim Study           As CosmosWorksLib.CWStudy
     Dim SolidMgr        As CosmosWorksLib.CWSolidManager
     Dim SolidComp       As CosmosWorksLib.CWSolidComponent
     Dim SolidBody       As CosmosWorksLib.CWSolidBody
     Dim ShellMgr        As CosmosWorksLib.CWShellManager
     Dim ShellMat        As CosmosWorksLib.CWMaterial
     Dim LBCMgr          As CosmosWorksLib.CWLoadsAndRestraintsManager
     Dim CWContactMgr    As CosmosWorksLib.CWContactManager
     Dim CWFeatObj       As CosmosWorksLib.CWResults
     Dim StaticOptions   As CosmosWorksLib.CWStaticStudyOptions
     Dim errCode         As Long
     Dim boolstatus      As Boolean
     Dim pDisp3          As Object
     Dim DispArray1      As Variant
     Dim DispArray2      As Variant
     Dim DispArray3      As Variant
     Dim DispArray4      As Variant
     Dim DispArray5      As Variant
     Dim Disp            As Variant
     Dim Stress          As Variant
    Const MeshEleSize   As Double = 4.48279654351123 'mm
     Const MeshTol       As Double = 0.224139827175561 'mm
     Const Tol1          As Double = 0.05 '5%
    Const URESMax       As Double = 0.488 'mm
     Const VONMax        As Double = 93.8  'MPa

    Dim PIDCollection   As New Collection
     Set PIDCollection = PIDInitializer()

    Set SwApp = Application.SldWorks
     If SwApp Is Nothing Then Exit Sub

    Set Part = SwApp.ActiveDoc
    Dim strMaterialLib  As String
     strMaterialLib = SwApp.GetExecutablePath & "\lang\english\sldmaterials\solidworks materials.sldmat"

    DispArray1 = Array(SelectByPID(Part, "selection1", PIDCollection))
     DispArray2 = Array(SelectByPID(Part, "selection2", PIDCollection))
     DispArray3 = Array(SelectByPID(Part, "selection1", PIDCollection))
     DispArray4 = Array(SelectByPID(Part, "selection4", PIDCollection))
     DispArray5 = Array(SelectByPID(Part, "selection5", PIDCollection))
    Set CWAddinCallBack = SwApp.GetAddInObject("SldWorks.Simulation")
     If CWAddinCallBack Is Nothing Then ErrorMsg SwApp, "CWAddinCallBack object not found"
     Set COSMOSWORKS = CWAddinCallBack.COSMOSWORKS
     If COSMOSWORKS Is Nothing Then ErrorMsg SwApp, "COSMOSWORKS object not found"

    'Get active document
     Set ActDoc = COSMOSWORKS.ActiveDoc()
     If ActDoc Is Nothing Then ErrorMsg SwApp, "Failed to get active document"

    'Create new static study
     Set StudyMngr = ActDoc.StudyManager()
     If StudyMngr Is Nothing Then ErrorMsg SwApp, "Failed to get CWStudyManager object"
     Set Study = StudyMngr.CreateNewStudy3("Static_Mixed6", swsAnalysisStudyType_e.swsAnalysisStudyTypeStatic, 0, errCode)
     If Study Is Nothing Then ErrorMsg SwApp, "Failed to create new study"

    'Add materials
     Set SolidMgr = Study.SolidManager
     If SolidMgr Is Nothing Then ErrorMsg SwApp, "Failed to get CWSolidManager object"
     Set SolidComp = SolidMgr.GetComponentAt(1, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to get solid component"
     Set SolidBody = SolidComp.GetSolidBodyAt(0, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to get solid body"
     boolstatus = SolidBody.SetLibraryMaterial(strMaterialLib, "AISI 1020")
     If boolstatus = False Then ErrorMsg SwApp, "Failed to apply material"

    'Define shells
     Set ShellMgr = Study.ShellManager
     If ShellMgr Is Nothing Then ErrorMsg SwApp, "Failed to get CWShellManager object"
     Dim CWShellObj As CosmosWorksLib.CWShell
     Set CWShellObj = ShellMgr.GetShellAt(0, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to get CWShell object"

    Set ShellMat = CWShellObj.GetDefaultMaterial
     If ShellMat Is Nothing Then ErrorMsg SwApp, "Failed to get default material for shell"
     ShellMat.MaterialUnits = 0
     Call ShellMat.SetPropertyByName("EX", 120000000000#, 0)
     Call ShellMat.SetPropertyByName("NUXY", 0.31, 0)
     errCode = CWShellObj.SetShellMaterial(ShellMat)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to apply material"

    Call CWShellObj.ShellBeginEdit
     CWShellObj.Formulation = 0
     CWShellObj.ShellUnit = 0
     CWShellObj.ShellThickness = 3
     errCode = CWShellObj.ShellEndEdit
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to create shell"
     Set CWShellObj = Nothing

    'Add fixed restraint
     Set LBCMgr = Study.LoadsAndRestraintsManager
     If LBCMgr Is Nothing Then ErrorMsg SwApp, "No CWLoadsAndRestraintsManager object"

    Dim CWRemoteLoad As CosmosWorksLib.CWRemoteLoad
     Set CWRemoteLoad = LBCMgr.AddRemoteLoad(0, (DispArray2), 0, 1.2, 1.5, 1.6, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to create fixed remote load"
     CWRemoteLoad.RemoteLoadBeginEdit
     CWRemoteLoad.SetLocationValues 4.5, 5.6, 6.7
     CWRemoteLoad.RemoteLoadEndEdit

    Debug.Print "Load type as defined in swsRemoteLoadType_e: " & CWRemoteLoad.LoadType
     Debug.Print "Force unit as defined in swsForceUnit_e: " & CWRemoteLoad.ForceOrTranslationUnit
     Debug.Print "Location unit as defined in swsLinearUnit_e: " & CWRemoteLoad.LocationUnit
     Debug.Print "Moment unit as defined in swsMomentUnit_e: " & CWRemoteLoad.MomentOrRotationUnit

    Dim binclude As Long
     Dim bxvalue As Long
     Dim dxvalue As Double
     Dim byvalue As Long
     Dim dyvalue As Double
     Dim bzvalue As Long
     Dim dzvalue As Double
     CWRemoteLoad.GetForceOrTranslationValues2 binclude, bxvalue, dxvalue, byvalue, dyvalue, bzvalue, dzvalue
     Debug.Print "Include force in analysis? (-1=yes) " & binclude
     Debug.Print "x-component of remote force? (-1=yes) " & bxvalue
     Debug.Print "x-component value: " & dxvalue
     Debug.Print "y-component of remote force? (-1=yes) " & byvalue
     Debug.Print "y-component value: " & dyvalue
     Debug.Print "z-component of remote force? (-1=yes) " & bzvalue
     Debug.Print "z-component value: " & dzvalue

    CWRemoteLoad.GetLocationValues dxvalue, dyvalue, dzvalue
     Debug.Print "x-component of remote location: " & dxvalue
     Debug.Print "y-component of remote location: " & dyvalue
     Debug.Print "z-component of remote location: " & dzvalue

    CWRemoteLoad.GetMomentOrRotationValues2 binclude, bxvalue, dxvalue, byvalue, dyvalue, bzvalue, dzvalue
     Debug.Print "x-component of remote moment? (-1=yes) " & bxvalue
     Debug.Print "x-component value: " & dxvalue
     Debug.Print "y-component of remote moment? (-1=yes) " & byvalue
     Debug.Print "y-component value: " & dyvalue
     Debug.Print "z-component of remote moment? (-1=yes) " & bzvalue
     Debug.Print "z-component value: " & dzvalue

    Set CWRemoteLoad = Nothing

    'Create normal pressure
     Dim CWPressure As CosmosWorksLib.CWPressure
     Set pDisp3 = SelectByPID(Part, "selection3", PIDCollection)
     Set CWPressure = LBCMgr.AddPressure(1, (DispArray3), pDisp3, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to create CWPressure object"
     Call CWPressure.PressureBeginEdit
     CWPressure.Unit = 1
     CWPressure.Value = -12
     errCode = CWPressure.PressureEndEdit
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to apply pressure value"
     Set CWPressure = Nothing

    Dim CWContactObj As CosmosWorksLib.CWContactSet
     Set CWContactMgr = Study.ContactManager
     Set CWContactObj = CWContactMgr.CreateContactSet(1, (DispArray4), (DispArray5), errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to create CWContactSet object"
     Set CWContactObj = Nothing

    'Mesh
     Dim CWMeshObj As CosmosWorksLib.CWMesh
     Set CWMeshObj = Study.Mesh
     If CWMeshObj Is Nothing Then ErrorMsg SwApp, "Failed to create CWMesh object"
     CWMeshObj.MesherType = 0
     CWMeshObj.Quality = 0
     errCode = Study.CreateMesh(0, MeshEleSize, MeshTol)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to create mesh"
     Set CWMeshObj = Nothing

    'Set solver type to Automatic
     Set StaticOptions = Study.StaticStudyOptions
     If StaticOptions Is Nothing Then ErrorMsg SwApp, "Failed to get CWStaticStudyOptions object"
     StaticOptions.SolverType = 0
     StaticOptions.UseSoftSpring = 1
     StaticOptions.LargeDisplacement = 0

    'Run analysis
     errCode = Study.RunAnalysis
     If errCode <> 0 Then ErrorMsg SwApp, "Analysis failed with error as defined in swsRunAnalysisError_e: " & errCode

    'Get results
     Set CWFeatObj = Study.Results
     If CWFeatObj Is Nothing Then ErrorMsg SwApp, "Failed to get CWResults object"

    'Get min/max URES displacement
     Disp = CWFeatObj.GetMinMaxDisplacement(3, 0, Nothing, 0, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to get displacement result"
     'Compare max resultant disp with URESMax
     If (Disp(3) < (1 - Tol1) * URESMax) Or (Disp(3) > (1 + Tol1) * URESMax) Then
         Debug.Print "URES displacement % error = " & (((Disp(3) - URESMax) / URESMax) * 100)
     End If

    'Get min/max von Mises stress
     Stress = CWFeatObj.GetMinMaxStress(9, 0, 0, Nothing, 3, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to get stress result"
     'Compare max von Mises stress with VONMax
     If (Stress(3) < (1 - Tol1) * VONMax) Or (Stress(3) > (1 + Tol1) * VONMax) Then
         Debug.Print "VON Mises stress % error = " & (((Stress(3) - VONMax) / VONMax) * 100)
     End If

    Set CWFeatObj = Nothing

End Sub

Sub ErrorMsg(SwApp As SldWorks.SldWorks, Message As String)
     SwApp.SendMsgToUser2 Message, 0, 0
     SwApp.RecordLine "'*** WARNING - General"
     SwApp.RecordLine "'*** " & Message
     SwApp.RecordLine ""
 End Sub
Function SelectByPID(Part As SldWorks.ModelDoc2, PIDName As String, PIDCollection As Collection) As Object
     Dim PID()       As Byte
     Dim PIDVariant  As Variant
     Dim PIDString   As String
     Dim i           As Integer
     Dim SelObj      As Object

    'Get the string from the collection
     PIDString = ""
     PIDString = PIDCollection.Item(PIDName)

    'Parse the string into an array
     PIDVariant = Split(PIDString, ",")
     ReDim PID(UBound(PIDVariant))

    'Change to a byte array
     For i = 0 To (UBound(PIDVariant) - 1)
         PID(i) = PIDVariant(i)
     Next i

    'Select the entity
     Set SelObj = Part.Extension.GetObjectByPersistReference((PID))
     Set SelectByPID = SelObj
     Set SelObj = Nothing
 End Function
Function PIDInitializer() As Collection

    Dim PIDCollection As New Collection
     Dim selection1 As String
     Dim selection2 As String
     Dim selection3 As String
     Dim selection4 As String
     Dim selection5 As String
    'Constants
     selection1 = "35,29,213,113,218,129,72,162,168,88,152,178,27,137,239,153,6,2,0,0,50,1,0,0,120,218,109,81,77,74,195,80,16,254,210,180,85,40,70,11,226,13,4,55,10,117,233,74,104,26,44,40,150,164,238,10,33,38,47,49,146,182,146,164,208,141,208,67,244,26,221,120,5,47,227,41,26,191,105,154,86,161,19,134,247,222,247,51,195,76,6,6,160,3,40,214,197,105,134,55,40,36,252,174,209,193,61,158,48,71,0,23,30,50,140,81,167,234,140,169,109,179,45,174,66,67,11,227,169,229,249,202,86,161,235,11,33,209,100,214,245,242,254,249,189,188,92,245,191,134,213,89,218,206,105,235,77,2,113,58,179,52,236,7,182,250,112,253,146,107,74,73,219,245,229,126,34,186,121,254,252,250,174,252,188,132,12,66,124,91,113,162,76,105,42,88,155,88,215,201,211,120,18,61,120,147,32,81,132,215,69,99,63,210,234,229,202,106,45,136,221,90,184,195,8,67,226,25,114,116,55,227,41,14,235,193,71,138,41,95,35,56,100,60,196,68,92,50,49,23,161,54,171,232,144,27,144,73,201,139,110,95,255,134,158,71,152,100,109,214,254,97,55,153,189,134,42,180,114,201"
     selection1 = selection1 & ",71,38,245,33,43,204,232,201,241,55,46,152,149,15,219,229,202,88,142,138,198,189,32,82,187,21,53,22,199,59,177,252,21,99,241,31,211,14,96,181,3,152,190,107,253,11,105,183,117,188,0,0,0,0,0,0,0,0"
     selection1 = selection1 & ",Type=1"
    selection2 = "35,29,213,113,218,129,72,162,168,88,152,178,27,137,239,153,16,2,0,0,49,1,0,0,120,218,109,81,203,74,195,80,16,61,53,182,10,197,250,64,40,184,23,220,40,212,165,43,161,105,176,96,105,73,234,78,8,241,230,86,170,121,72,122,11,217,8,253,8,127,195,141,191,224,127,53,158,49,173,53,208,11,147,59,57,143,153,204,100,212,2,44,0,197,178,56,244,144,34,194,20,33,46,209,193,45,6,200,153,251,8,48,67,140,93,170,142,24,181,85,156,136,171,168,161,137,56,117,2,165,93,61,241,149,16,114,26,242,176,202,252,253,251,227,252,179,255,53,94,223,165,173,45,182,44,141,189,87,211,75,140,55,207,38,253,208,213,111,190,42,233,134,208,174,175,36,63,96,222,203,205,240,233,69,43,83,66,45,66,124,119,166,145,182,165,175,96,199,196,186,158,201,166,201,243,93,144,132,145,38,188,44,234,155,169,218,15,23,78,115,65,236,218,193,13,30,49,134,230,100,6,221,223,9,53,231,13,160,144,81,63,35,235,145,9,232,83,220,192,128,119,78,133,108,163,67,110,68,38,35,95,234,214,245,175,152,223,195,38,235,178,246,144,221,100,252,29,"
     selection2 = selection2 & "252,63,236,190,103,179,210,132,21,230,244,153,10,123,198,16,159,181,218,237,169,76,158,132,178,222,202,134,234,139,253,63,237,218,107,45,170,184,252,138,214,22,108,155,118,243,141,63,69,114,115,194,0,0,0,0,0,0,0,0"
     selection2 = selection2 & ",Type=1"
    selection3 = "35,29,213,113,218,129,72,162,168,88,152,178,27,137,239,153,246,1,0,0,45,1,0,0,120,218,109,80,203,74,195,80,16,61,109,90,21,138,245,129,80,112,47,184,81,168,75,87,66,211,96,193,210,146,212,157,16,226,205,77,137,230,33,233,45,100,35,228,35,252,13,55,254,130,255,213,120,174,73,212,130,3,195,157,123,30,51,204,204,251,128,1,160,220,148,7,14,82,68,8,225,227,2,67,220,96,138,156,181,11,15,43,196,232,80,117,200,108,213,121,172,93,101,11,61,196,233,216,95,74,91,6,174,208,132,14,45,70,187,170,95,63,223,206,222,39,31,139,230,173,108,3,218,172,44,141,157,103,53,78,148,179,206,130,137,111,203,23,87,84,244,142,166,109,87,232,122,95,79,200,213,236,241,73,10,85,65,125,66,252,91,97,36,77,61,87,99,71,196,70,142,202,194,100,121,235,37,126,36,9,111,202,238,239,86,131,251,115,171,87,16,187,178,112,141,7,44,32,185,153,194,232,123,67,201,125,61,8,100,212,175,200,58,100,60,250,4,47,48,229,155,83,161,175,49,36,55,39,147,145,175,116,77,255,75,214,119,48,201,218,236,61,227,180,63,87,168,131,211,1"
     selection3 = selection3 & "19,77,118,10,216,97,77,159,218,98,79,153,218,215,174,111,123,162,55,79,124,203,19,114,235,66,221,98,239,71,219,120,141,98,27,239,252,131,25,181,246,11,153,198,113,128,0,0,0,0,0,0,0,0"
     selection3 = selection3 & ",Type=1"
    selection4 = "35,29,213,113,218,129,72,162,168,88,152,178,27,137,239,153,242,1,0,0,46,1,0,0,120,218,109,81,65,74,195,80,16,125,209,68,133,98,180,32,222,64,112,163,80,151,174,132,198,96,65,177,36,117,87,8,241,231,39,70,146,84,146,20,186,17,114,8,175,209,141,87,240,50,158,162,241,253,38,105,21,156,48,252,255,223,155,55,195,188,140,77,96,23,64,189,170,143,10,188,64,34,225,119,129,1,110,240,128,5,2,120,240,81,32,133,206,170,99,166,214,102,95,169,106,13,61,164,179,219,32,146,142,12,61,161,8,21,6,83,223,105,238,239,95,31,103,203,209,231,164,59,27,217,137,146,101,129,237,11,233,206,243,112,20,56,242,205,19,13,183,71,206,118,60,161,238,135,170,110,81,62,62,191,74,81,54,144,73,136,111,59,78,164,165,134,42,172,79,108,232,150,121,156,69,119,126,22,36,146,240,170,54,182,43,45,159,206,237,94,69,236,202,198,53,166,152,16,47,80,98,184,94,79,114,89,31,2,57,102,124,77,225,146,241,17,19,241,200,196,52,66,174,173,24,144,27,147,201,201,171,186,109,255,75,106,238,97,145,117,216,251,155,211,212,238,173,5,1"
     selection4 = selection4 & "73,101,156,190,111,177,62,100,135,57,53,37,126,199,41,179,211,53,209,45,230,202,40,85,22,111,76,50,170,131,77,185,250,123,102,245,23,211,254,193,244,182,233,15,36,113,114,226,0,0,0,0,0,0,0,0"
     selection4 = selection4 & ",Type=1"
    selection5 = "35,29,213,113,218,129,72,162,168,88,152,178,27,137,239,153,16,2,0,0,51,1,0,0,120,218,117,80,203,74,195,80,16,61,125,42,20,227,3,161,224,94,112,163,80,151,174,132,166,193,130,165,37,169,59,33,196,155,27,137,182,169,164,183,144,141,208,143,240,55,220,248,11,254,87,227,25,211,84,43,120,97,114,39,231,49,115,103,70,22,80,3,144,175,242,125,15,51,76,16,35,196,57,58,184,198,0,25,115,31,1,230,152,162,78,213,1,163,178,142,35,113,229,21,180,48,157,57,129,210,174,142,124,37,132,156,166,124,106,69,254,250,249,118,250,222,255,24,151,119,97,107,139,45,157,77,189,103,211,75,140,183,72,163,126,232,234,23,95,21,116,83,104,215,87,146,239,49,239,101,102,248,240,164,149,41,32,139,16,255,157,120,162,109,233,43,216,33,177,174,103,210,56,121,188,9,146,112,162,9,175,242,198,207,84,237,187,51,167,181,36,118,233,224,10,247,24,67,115,50,131,238,247,132,154,243,6,80,72,169,159,147,245,200,4,244,41,110,96,192,59,163,66,182,209,33,55,34,147,146,47,116,101,253,11,230,183,176,201,186,172,61,100,55,25,"
     selection5 = selection5 & "191,138,223,135,221,119,108,86,138,88,97,65,159,217,98,79,24,226,171,174,119,123,44,147,39,161,172,119,107,67,141,229,238,70,91,122,107,203,109,92,182,111,253,193,42,255,104,235,155,23,124,1,69,120,115,197,0,0,0,0,0,0,0,0"
     selection5 = selection5 & ",Type=1"

    'Store constants in a collection
     PIDCollection.Add selection1, "selection1"
     PIDCollection.Add selection2, "selection2"
     PIDCollection.Add selection3, "selection3"
     PIDCollection.Add selection4, "selection4"
     PIDCollection.Add selection5, "selection5"
    Set PIDInitializer = PIDCollection
  End Function
```
