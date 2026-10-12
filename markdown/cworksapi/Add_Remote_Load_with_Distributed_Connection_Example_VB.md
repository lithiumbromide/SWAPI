---
title: "Add a Remote Load with Distributed Coupling Example (VBA"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Add_Remote_Load_with_Distributed_Connection_Example_VB.htm"
---

# Add a Remote Load with Distributed Coupling Example (VBA

## Add a Remote Load with Distributed Coupling Example (VBA)

This example shows how to create a linear static study and add a remote load with distributed coupling.

```vb
'----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click Tools > References > SOLIDWORKS Simulation version type library).
 ' 3. Open public_documents\samples\Simulation Examples\link1.sldprt.
 '
 ' Postconditions:
 ' 1. Creates Static 1.
 ' 2. Applies material and a fixture.
 ' 3. Adds a remote load of 10mm translation in the X-direction
 '    and -100N force in the Y-direction
 '    with distributed coupling at the origin.
 ' 4. Meshes, analyses, and reports on Static 1.
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
     Dim StaticOptions   As CosmosWorksLib.CWStaticStudyOptions
     Dim SolidMgr        As CosmosWorksLib.CWSolidManager
     Dim SolidComp       As CosmosWorksLib.CWSolidComponent
     Dim SolidBody       As CosmosWorksLib.CWSolidBody
     Dim LBCMgr          As CosmosWorksLib.CWLoadsAndRestraintsManager
     Dim CWLoad          As CosmosWorksLib.CWLoadsAndRestraints
     Dim CWMesh          As CosmosWorksLib.CWMesh
     Dim CWResult        As CosmosWorksLib.CWResults
     Dim lStatus         As Long
     Dim boolStatus      As Boolean
     Dim longstatus      As Long
     Dim longwarnings    As Long
     Dim errCode         As Long
     Dim pValue          As Long
     Dim el              As Double
     Dim tl              As Double
     Dim bApp            As Boolean
     Dim bXVal           As Boolean
     Dim bYYVal          As Boolean
     Dim bZVal           As Boolean
     Dim bAllowDC        As Boolean
     Dim lXCode          As Long
     Dim lYCode          As Long
     Dim lZCode          As Long
     Dim xVal            As Double
     Dim yVal            As Double
     Dim zVal            As Double
     Dim var1 As Variant
     Dim pDisp1 As Object
     Dim DispArray1 As Variant
     Dim Disp As Variant, Stress As Variant

    Const URESMax       As Double = 3.931252 'mm '0.00452 'mm
     Const VONMax        As Double = 42872.33 'Pa '22.1  'MPa

    Dim PIDCollection As New Collection
     Set PIDCollection = PIDInitializer()

    Set SwApp = Application.SldWorks
     If SwApp Is Nothing Then Exit Sub
    Set Part = SwApp.ActiveDoc

    Set CWAddinCallBack = SwApp.GetAddInObject("CosmosWorks.CosmosWorks")
     If CWAddinCallBack Is Nothing Then ErrorMsg SwApp, "CWAddinCallBack object not found"
     Set COSMOSWORKS = CWAddinCallBack.COSMOSWORKS
     If COSMOSWORKS Is Nothing Then ErrorMsg SwApp, "COSMOSWORKS object not found"

    'Get the active document
     Set ActDoc = COSMOSWORKS.ActiveDoc()
     If ActDoc Is Nothing Then ErrorMsg SwApp, "No active document"

    'Create the static study
     Set StudyMngr = ActDoc.StudyManager()

    StudyMngr.ActiveStudy = 0
     Dim NewStudyName As String
     NewStudyName = "Static 1"

    Set Study = StudyMngr.CreateNewStudy3(NewStudyName, 0, 0, errCode)
     boolStatus = Part.Extension.SelectByID2("Boss-Extrude1", "SOLIDBODY", 0, 0, 0, True, 0, Nothing, 0)

    Dim SolidManagerObj As Object
     Set SolidManagerObj = Study.SolidManager()
     errCode = SolidManagerObj.SetLibraryMaterialToSelectedEntities("solidworks materials", "Plain Carbon Steel")
     Part.ClearSelection2 True

    Part.GraphicsRedraw2
     boolStatus = Part.Extension.SelectByRay(-3.7348334934677E-03, -1.40549072772123E-03, 3.08049871188132E-03, 0.651406664432463, -4.91062309924361E-03, -0.758712885954726, 8.13813747228381E-04, 1, True, 0, 0)

    Part.GraphicsRedraw2
     Set LBCMgr = Study.LoadsAndRestraintsManager()
     Dim DispatchObj1 As Object
     Set DispatchObj1 = Part.SelectionManager.GetSelectedObject6(1, -1)
     Dim DispArray As Variant
     DispArray = Array(DispatchObj1)
     Dim CWRestraintObj As Object
     Set CWRestraintObj = LBCMgr.AddRestraint(0, (DispArray), Nothing, errCode)

    StudyMngr.ActiveStudy = 0

    'Get persist ID for the origin
     SelectByPID "selection1", PIDCollection, var1

    Set pDisp1 = Part.Extension.GetObjectByPersistReference((var1))

    'Create variant array
     DispArray1 = Array(pDisp1)

    'Add a remote load of 10mm in X-direction and -100N in Y-direction with distributed coupling at the origin
     Set CWLoad = LBCMgr.AddRemoteLoad(0, (DispArray1), 0, 0, 0, 0, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Remote load not created"
    CWLoad.RemoteLoadBeginEdit

    bAllowDC = CWLoad.AllowDistributedCoupling2
     xVal = 0 'Force in X-direction
     yVal = -100 'Force in Y-direction
     zVal = 0
     bXVal = False
     bYYVal = True
     bZVal = False
     lXCode = 0
     lYCode = 1
     lZCode = 0
    If bAllowDC = True Then
         CWLoad.ConnectionType = swsRemoteLoadConnectionType_Distributed
         CWLoad.WeightingFactor = swsRemoteLoadWeightingFactor_Default_Constant
         CWLoad.ForceUnit = swsForceUnitNOrNm
         CWLoad.TranslationUnit = swsLinearUnitMillimeters
         xVal = 10 'Translation in X-direction
         lXCode = 2
         CWLoad.SetForceOrTranslationValuesEx2 -1, lXCode, xVal, lYCode, yVal, lZCode, zVal
     End If
     If bAllowDC = False Then
         CWLoad.SetForceOrTranslationValues2 -1, bXVal, xVal, bYYVal, yVal, bZVal, zVal
     End If

    CWLoad.RemoteLoadEndEdit

    'Mesh
     Set CWMesh = Study.Mesh
     If CWMesh Is Nothing Then ErrorMsg SwApp, "No mesh object"
     CWMesh.Quality = 1
     Call CWMesh.GetDefaultElementSizeAndTolerance(0, el, tl)
     errCode = Study.CreateMesh(0, el, tl)
     If errCode <> 0 Then ErrorMsg SwApp, "Mesh failed"
    'Set solver type to FFEPlus solver
     Set StaticOptions = Study.StaticStudyOptions
     If StaticOptions Is Nothing Then ErrorMsg SwApp, "No StaticStudyOptions object"
     StaticOptions.SolverType = 2

    'Run analysis
     errCode = Study.RunAnalysis
     If errCode <> 0 Then ErrorMsg SwApp, "Analysis failed with error: " & errCode

    'Get results
     Set CWResult = Study.Results
     If CWResult Is Nothing Then ErrorMsg SwApp, "No results object"

    'Get displacement
     Disp = CWResult.GetMinMaxDisplacement(3, 1, Nothing, 0, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "No displacement results"

    'Compare displacement
     If (Disp(3) < 0.95 * URESMax) Or (Disp(3) > 1.05 * URESMax) Then
         ErrorMsg SwApp, "URES % error = " & (((Disp(3) - URESMax) / URESMax) * 100)
     End If

    'Get Min/Max von Mises stress
     Stress = CWResult.GetMinMaxStress(9, 0, 0, Nothing, 3, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "No stress results"

    'Compare maximum von Mises stress
     If (Stress(3) < 0.95 * VONMax) Or (Stress(3) > 1.05 * VONMax) Then
         ErrorMsg SwApp, "VON % error = " & (((Stress(3) - VONMax) / VONMax) * 100)
     End If

End Sub
Function ErrorMsg(SwApp As Object, Message As String)
     SwApp.SendMsgToUser2 Message, 0, 0
     SwApp.RecordLine "'*** WARNING - General"
     SwApp.RecordLine "'*** " & Message
     SwApp.RecordLine ""
 End Function

Function SelectByPID(PIDName As String, PIDCollection As Collection, varEntity As Variant)

    Dim SelObj As Object
     Dim PID() As Byte
     Dim PIDVariant As Variant
     Dim PIDString As String
     Dim EntityType As Long
     Dim i As Integer

    'Get the string from the collection.
     PIDString = ""
     PIDString = PIDCollection.Item(PIDName)

    'Parse the string into an array
     PIDVariant = Split(PIDString, ",")
     ReDim PID(UBound(PIDVariant))

    'Change to a byte array
     For i = 0 To (UBound(PIDVariant) - 1)
         PID(i) = PIDVariant(i)
     Next i
         varEntity = PID
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
     selection1 = "35,29,213,113,218,129,72,162,168,88,152,178,27,137,239,153,30,2,0,0,63,1,0,0,120,218,109,146,75,75,195,64,16,199,255,105,105,90,40,22,4,81,15,30,188,120,212,131,151,128,34,84,250,192,130,143,146,244,88,8,49,217,104,108,154,212,184,133,94,132,222,69,188,228,67,120,241,226,87,240,123,53,206,116,83,137,144,129,157,199,111,118,102,97,102,135,45,160,10,32,91,101,96,201,50,13,77,76,227,190,227,10,83,248,182,171,65,73,131,85,85,249,175,63,233,209,215,224,123,180,177,170,108,143,203,146,120,106,77,100,47,146,214,60,241,7,158,41,102,182,171,210,58,167,77,219,101,127,139,252,222,66,222,221,63,9,87,42,212,34,68,113,63,8,69,151,223,101,182,77,172,99,201,36,136,30,174,156,200,11,5,225,85,166,135,8,16,97,2,27,167,184,125,75,141,230,146,232,69,15,103,24,99,4,129,23,72,116,224,144,21,184,33,235,34,65,76,209,33,233,136,244,51,177,227,117,254,145,58,177,30,195,204,235,18,226,220,93,82,52,198,144,162,36,247,139,175,158,192,194,53,186,152,173,179,237,221,131,75,30,75,5,155,97,85,212,68,235,"
     selection1 = selection1 & "93,234,234,83,143,57,85,75,20,101,159,78,251,61,53,116,158,234,18,168,45,27,127,172,86,96,231,228,127,126,164,134,86,194,42,37,172,90,210,175,158,239,117,135,167,30,121,188,218,127,219,41,222,213,214,119,51,245,25,240,11,144,100,129,59,0,0,0,0,0,0,0,0"
     selection1 = selection1 & ",Type=1"

    'Store constants in a collection
     PIDCollection.Add selection1, "selection1"

    'Pass the collection back
     Set PIDInitializer = PIDCollection

End Function
```
