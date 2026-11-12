---
title: "Add Bearing Load Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Add_Bearing_Load_Example_VB.htm"
---

# Add Bearing Load Example (VBA)

This example shows how to add a bearing load to a static study and get its properties.

NOTE: To get persistent reference identifiers (PIDs) for model selections, you can use [pidcollector.exe](GettingStarted-swsimulationapi.html) or IModelDocExtension::GetPersistReference3.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click Tools > References > SOLIDWORKS Simulation version type library).
 ' 3. Ensure that the specified model document exists.
 ' 4. Ensure that the specified material library exists.
 ' 5. Open an Immediate window.
 '
 ' Postconditions:
 '  1. Opens the specified model document.
 '  2. Inserts Axis2 in the FeatureManager design tree.
 '  3. Inserts Coordinate System1 in the FeatureManager design tree.
 '  4. Creates new study, Static1.
 '  5. Applies AISI 1020 steel to the solid bodies in the model.
 '  6. Adds BearingLoads-1 to Static1.
 '  7. Adds Link Connector-1 to Static1.
 '  8. Prints the properties of BearingLoads-1 to the Immediate window.
 '  9. Meshes the bodies in the model.
 ' 10. Sets the study options for Static1.
 ' 11. Analyzes Static1.
 ' 12. Inspect the Immediate window, FeatureManager design tree, and
 '     Simulation study tree.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 ' ---------------------------------------------------------------------------
 Option Explicit

Dim SwApp           As SldWorks.SldWorks
 Dim Part            As SldWorks.ModelDoc2
 Dim coordSys        As SldWorks.Feature
 Dim COSMOSWORKS     As CosmosWorksLib.COSMOSWORKS
 Dim CWAddinCallBack As CosmosWorksLib.CWAddinCallBack
 Dim ActDoc          As CosmosWorksLib.CWModelDoc
 Dim StudyMngr       As CosmosWorksLib.CWStudyManager
 Dim Study           As CosmosWorksLib.CWStudy
 Dim SolidMgr        As CosmosWorksLib.CWSolidManager
 Dim SolidComp       As CosmosWorksLib.CWSolidComponent
 Dim SolidBody       As CosmosWorksLib.CWSolidBody
 Dim LBCMgr          As CosmosWorksLib.CWLoadsAndRestraintsManager
 Dim CWBearingLoad   As CosmosWorksLib.CWBearingLoad
 Dim CWLinkConnector As CosmosWorksLib.CWLinkConnector
 Dim errCode         As Long
 Dim boolstatus      As Boolean
 Dim longstatus      As Long, longwarnings As Long
 Dim StaticOptions   As CosmosWorksLib.CWStaticStudyOptions
 Dim DispArray1      As Object, Vert1 As Object, Vert2 As Object
 Dim DispArray2      As Variant
Const MeshEleSize   As Double = 4.48279654351123
 Const MeshTol       As Double = 0.224139827175561
 Const Tol1          As Double = 0.05
Sub main()
    Set SwApp = Application.SldWorks
    Set Part = SwApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\Educational Examples\spider.sldasm", swDocASSEMBLY, swOpenDocOptions_Silent, "", longstatus, longwarnings)
     Set Part = SwApp.ActiveDoc

    'Create Axis2
     boolstatus = Part.Extension.SelectByID2("", "FACE", 7.3775062512027E-03, 6.02478435399689E-03, 5.37262605714091E-02, True, 0, Nothing, 0)
     boolstatus = Part.InsertAxis2(True)

    'Create Coordinate System1
     boolstatus = Part.Extension.SelectByID2("", "EDGE", 2.52708736488216E-03, 0.03884014356629, -1.55712463055693E-02, False, 2, Nothing, 0)
     boolstatus = Part.Extension.SelectByID2("Axis2", "AXIS", 0, 0, 0, True, 8, Nothing, 0)
    Set coordSys = Part.FeatureManager.InsertCoordinateSystem(False, False, False)
    Dim PIDCollection   As New Collection
     Set PIDCollection = PIDInitializer()

    Dim strMaterialLib  As String
     strMaterialLib = SwApp.GetExecutablePath & "\lang\english\sldmaterials\solidworks materials.sldmat"

    Set DispArray1 = SelectByPID(Part, "selection1", PIDCollection) ' coordinate system
     DispArray2 = Array(SelectByPID(Part, "selection2", PIDCollection)) ' cylindrical face
    Set Vert1 = SelectByPID(Part, "selection3", PIDCollection) ' link connector first location
     Set Vert2 = SelectByPID(Part, "selection4", PIDCollection) ' link connector second location

    Set CWAddinCallBack = SwApp.GetAddInObject("SldWorks.Simulation")
     If CWAddinCallBack Is Nothing Then ErrorMsg SwApp, "Failed to get Simulation add-in"
     Set COSMOSWORKS = CWAddinCallBack.COSMOSWORKS
     If COSMOSWORKS Is Nothing Then ErrorMsg SwApp, "Failed to get COSMOSWORKS"
    Set ActDoc = COSMOSWORKS.ActiveDoc()
     If ActDoc Is Nothing Then ErrorMsg SwApp, "Failed to get active document"

    'Create new static study
     Set StudyMngr = ActDoc.StudyManager()
     If StudyMngr Is Nothing Then ErrorMsg SwApp, "Failed to get the study manager"
     Set Study = StudyMngr.CreateNewStudy3("Static1", swsAnalysisStudyType_e.swsAnalysisStudyTypeStatic, 0, errCode)
     If Study Is Nothing Then ErrorMsg SwApp, "Failed to create new study"
    'Add materials
     Set SolidMgr = Study.SolidManager
     If SolidMgr Is Nothing Then ErrorMsg SwApp, "Failed to get solid manager"
     Set SolidComp = SolidMgr.GetComponentAt(0, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to get component"
     Set SolidBody = SolidComp.GetSolidBodyAt(0, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to get solid body"
     boolstatus = SolidBody.SetLibraryMaterial(strMaterialLib, "AISI 1020")
     If boolstatus = False Then ErrorMsg SwApp, "Failed to apply material"

    Set SolidComp = SolidMgr.GetComponentAt(1, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to get component"
     Set SolidBody = SolidComp.GetSolidBodyAt(0, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to get solid body"
     boolstatus = SolidBody.SetLibraryMaterial(strMaterialLib, "AISI 1020")
     If boolstatus = False Then ErrorMsg SwApp, "Failed to apply material"
    Set SolidComp = SolidMgr.GetComponentAt(2, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to get component"
     Set SolidBody = SolidComp.GetSolidBodyAt(0, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to get solid body"
     boolstatus = SolidBody.SetLibraryMaterial(strMaterialLib, "AISI 1020")
     If boolstatus = False Then ErrorMsg SwApp, "Failed to apply material"

    'Add a bearing load
     Set LBCMgr = Study.LoadsAndRestraintsManager
     If LBCMgr Is Nothing Then ErrorMsg SwApp, "Failed to get the loads and restraints manager"
    Set CWBearingLoad = LBCMgr.AddBearingLoad(DispArray1, (DispArray2), errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to create a bearing load"

    CWBearingLoad.BearingLoadBeginEdit
     CWBearingLoad.Direction = 1
     CWBearingLoad.YDirectionValue = 1
     CWBearingLoad.BearingLoadEndEdit
    Debug.Print "Bearing load properties:"
     Debug.Print "  Unit system as defined in swsUnit_e: " & CWBearingLoad.BearingLoadUnit
     Debug.Print "  Distribution type as defined in swsBearingLoadDistributionType_e: " & CWBearingLoad.DistributionType
     Debug.Print "  Use time curve? (False = no, True = yes): " & CWBearingLoad.UseTimeCurve2
     Debug.Print "  Bearing load values:"
     Debug.Print "    X direction: " & CWBearingLoad.XDirectionValue
     Debug.Print "       Reverse? (False = no, True = yes): " & CWBearingLoad.XDirectionReverse2
     Debug.Print "    Y direction: " & CWBearingLoad.YDirectionValue
     Debug.Print "       Reverse? (False = no, True = yes): " & CWBearingLoad.YDirectionReverse2

    'Add a link connector
     Set CWLinkConnector = LBCMgr.AddLinkConnector(Vert1, Vert2, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to add a link connector"

    'Create mesh
     Dim CWMeshObj As CosmosWorksLib.CWMesh
     Set CWMeshObj = Study.Mesh
     If CWMeshObj Is Nothing Then ErrorMsg SwApp, "Failed to create mesh object"
     CWMeshObj.MesherType = 0
     CWMeshObj.Quality = 0
     errCode = Study.CreateMesh(0, MeshEleSize, MeshTol)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to create mesh"
     Set CWMeshObj = Nothing

    'Static study options
     Set StaticOptions = Study.StaticStudyOptions
     If StaticOptions Is Nothing Then ErrorMsg SwApp, "Failed to get static study options"
     StaticOptions.SolverType = 1
     StaticOptions.UseSoftSpring = 1
     StaticOptions.LargeDisplacement = 0

    Debug.Print "    Flow/Thermal Effects:"
     Debug.Print "       Thermal options:"
     Debug.Print "          Temperature source as defined in swsThermalOption_e: " & StaticOptions.ThermalResults
     Debug.Print "          Temperature source:"
     If StaticOptions.ThermalResults = 1 Then
         Debug.Print "          Thermal study: " & StaticOptions.ThermalStudyName
         Debug.Print "              Time step (for transient thermal study only): " & StaticOptions.TimeStep
     ElseIf StaticOptions.ThermalResults = 2 Then
         Debug.Print "               SOLIDWORKS Flow Simulation results file " & StaticOptions.FlowTemperatureFile
     Else
         Debug.Print "               The current model"
     End If
    Debug.Print "       Fluid pressure option:"
     Debug.Print "          Import fluid pressure loads from SOLIDWORKS Flow Simulation? (1=yes, 0=no): " & StaticOptions.CheckFlowPressure
     If StaticOptions.CheckFlowPressure = 1 Then
         Debug.Print "           SOLIDWORKS Flow Simulation results file: " & StaticOptions.FlowPressureFile
         Debug.Print "           Use reference pressure offset from Flow Simulation? (1=yes, 0=no): " & StaticOptions.ReferencePressureOption
         If StaticOptions.ReferencePressureOption = 0 Then
             Debug.Print "             Reference pressure offset: " & StaticOptions.DefinedReferencePressure
         End If
         Debug.Print "          Run as legacy study and import only the normal component of the pressure load? (1=yes, 0=no): " & StaticOptions.CheckRunAsLegacy
     End If

    'Run analysis
     errCode = Study.RunAnalysis
     If errCode <> 0 Then ErrorMsg SwApp, "Analysis failed with error as defined in swsRunAnalysisError_e: " & errCode
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
     Dim i           As Long
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
     Set SelObj = Part.Extension.GetObjectByPersistReference3((PID), errCode)
     Set SelectByPID = SelObj
     Set SelObj = Nothing

End Function
Function PIDInitializer() As Collection
    Dim PIDCollection As New Collection
     Dim selection1 As String
     Dim selection2 As String
     Dim selection3 As String
     Dim selection4 As String
    'Coordinate system
     selection1 = "181,35,0,0,1,0,0,0,255,254,255,0,0,0,0,0,35,2,0,0"
     selection1 = selection1 & ",Type=1"
    'Cylindrical face
     selection2 = "64,31,0,0,3,0,0,0,255,254,255,14,115,0,104,0,97,0,102,0,116,0,45,0,49,0,64,0,115,0,112,0,105,0,100,0,101,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,10,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,97,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,32,0,67,0,111,0,114,0,112,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,92,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,69,0,100,0,117,0,99,0,97,0,11"
     selection2 = selection2 & "6,0,105,0,111,0,110,0,97,0,108,0,32,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,115,0,104,0,97,0,102,0,116,0,46,0,115,0,108,0,100,0,112,0,114,0,116,0,9,128,255,254,255,5,115,0,104,0,97,0,102,0,116,0,2,0,0,155,126,163,53,0,165,25,208,59,1,0,0,0,0,0,0,0,5,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,63,0,0,0,0,0,0,0,7,50,149,70,12,0,0,0,171,126,163,53,1,0,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,12,0,0,0,171,126,163,53,1,0,0,0,255,255,255,255,0,0,12,128,0,0,5,128,8,0,12,0,0,0,171,126,163,53,0,0,0,0,255,255,255,255,0,0,0,0,0,0,0,0,0,0"
     selection2 = selection2 & ",Type=1"
    'Vertex 1
     selection3 = "189,35,0,0,3,0,0,0,255,254,255,15,115,0,112,0,105,0,100,0,101,0,114,0,45,0,49,0,64,0,115,0,112,0,105,0,100,0,101,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,9,0,0,0,255,255,1,0,13,0,109,111,86,101,114,116,101,120,82,101,102,95,99,255,255,255,255,255,255,255,255,3,0,0,0,0,2,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,19,0,109,111,70,105,108,108,101,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,98,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,32,0,67,0,111,0,114,0,112,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,92,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,69,0,100,0"
     selection3 = selection3 & ",117,0,99,0,97,0,116,0,105,0,111,0,110,0,97,0,108,0,32,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,115,0,112,0,105,0,100,0,101,0,114,0,46,0,115,0,108,0,100,0,112,0,114,0,116,0,9,128,255,254,255,6,115,0,112,0,105,0,100,0,101,0,114,0,2,0,0,149,119,163,53,255,254,255,0,0,184,241,44,76,1,0,0,0,0,0,0,0,5,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,142,0,0,0,0,0,0,0,13,50,149,70,141,0,0,0,83,107,166,53,4,0,0,0,3,128,0,0,5,128,8,0,139,0,0,0,68,107,166,53,4,0,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,28,0,0,0,119,124,163,53,0,0,0,0,255,255,255,255,0,0,0,0,0,0,0,0,0,0,0,0"
     selection3 = selection3 & ",Type=1"
    'Vertex 2
     selection4 = "189,35,0,0,3,0,0,0,255,254,255,15,115,0,112,0,105,0,100,0,101,0,114,0,45,0,49,0,64,0,115,0,112,0,105,0,100,0,101,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,9,0,0,0,255,255,1,0,13,0,109,111,86,101,114,116,101,120,82,101,102,95,99,255,255,255,255,255,255,255,255,3,0,0,0,0,2,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,98,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,32,0,67,0,111,0,114,0,112,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,92,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0"
     selection4 = selection4 & ",92,0,69,0,100,0,117,0,99,0,97,0,116,0,105,0,111,0,110,0,97,0,108,0,32,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,115,0,112,0,105,0,100,0,101,0,114,0,46,0,115,0,108,0,100,0,112,0,114,0,116,0,9,128,255,254,255,6,115,0,112,0,105,0,100,0,101,0,114,0,2,0,0,149,119,163,53,255,254,255,0,0,184,241,44,76,1,0,0,0,0,0,0,0,5,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,142,0,0,0,0,0,0,0,13,50,149,70,28,0,0,0,119,124,163,53,6,0,0,0,255,255,1,0,19,0,109,111,70,105,108,108,101,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,141,0,0,0,83,107,166,53,5,0,0,0,12,128,0,0,5,128,8,0,139,0,0,0,68,107,166,53,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"
     selection4 = selection4 & ",Type=1"
    'Store constants in a collection
     PIDCollection.Add selection1, "selection1"
     PIDCollection.Add selection2, "selection2"
     PIDCollection.Add selection3, "selection3"
     PIDCollection.Add selection4, "selection4"

    Set PIDInitializer = PIDCollection

End Function
```
