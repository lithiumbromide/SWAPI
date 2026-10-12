---
title: "Add Centrifugal Load Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Add_Centrifugal_Load_Example_VB.htm"
---

# Add Centrifugal Load Example (VBA)

This example shows how to add a centrifugal force load to a static study.

NOTE: To get persistent reference identifiers (PIDs) for model selections, you can use [pidcollector.exe](GettingStarted-swsimulationapi.html) or IModelDocExtension::GetPersistReference3.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click Tools > References > SOLIDWORKS Simulation version type library).
 ' 3. Ensure that the specified model document exists.
 ' 4. Ensure that the specified materials library exists.
 ' 5. Open an Immediate window.
 '
 ' Postconditions:
 '  1. Opens the specified model document.
 '  2. Creates new study, Static1.
 '  3. Prints the study options of Static1 to the Immediate window.
 '  4. Adds AISI 1020 steel to the solid bodies in the model.
 '  5. Adds Fixed-1 restraint to Static1.
 '  6. Adds Centrifugal-1 load to Static1.
 '  7. Sets the properties of Centrifugal-1.
 '  8. Prints the properties of Centrifugal-1 to the Immediate window.
 '  9. Meshes the model.
 ' 10. Analyzes Static1.
 ' 11. Creates and activates a von Mises stress plot of the results.
 ' 12. Inspect the Immediate window, the Simulation study tree, and the
 '     graphics area.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 ' ---------------------------------------------------------------------------
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
 Dim LBCMgr          As CosmosWorksLib.CWLoadsAndRestraintsManager
 Dim CWCentrifugalLoad  As CosmosWorksLib.CWCentriFugalForce
 Dim errCode         As Long
 Dim boolstatus      As Boolean
 Dim longstatus      As Long, longwarnings As Long
 Dim DispArray2      As Object
 Dim DispArray3      As Variant
 Const MeshEleSize   As Double = 4.48279654351123
 Const MeshTol       As Double = 0.224139827175561
 Const Tol1          As Double = 0.05
 Option Explicit
 Sub main()
    Set SwApp = Application.SldWorks

    Set Part = SwApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\Educational Examples\spider.sldasm", 2, 0, "", longstatus, longwarnings)
     Set Part = SwApp.ActiveDoc

    Dim PIDCollection   As New Collection
     Set PIDCollection = PIDInitializer()

    Dim strMaterialLib  As String
     strMaterialLib = SwApp.GetExecutablePath & "\lang\english\sldmaterials\solidworks materials.sldmat"

    Set DispArray2 = SelectByPID(Part, "selection2", PIDCollection) ' shaft
     DispArray3 = Array(SelectByPID(Part, "selection3", PIDCollection)) ' arm

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

    'Static study options
     Dim bsOptions As CosmosWorksLib.CWStaticStudyOptions
     Set bsOptions = Study.StaticStudyOptions
     Debug.Print "Static study options"
     Dim zeroStrainTemp As Double
     Dim tempUnit As Long
     bsOptions.GetZeroStrainTemperature zeroStrainTemp, tempUnit
     Debug.Print "  Zero strain temperature: " & zeroStrainTemp
     Debug.Print "  Result folder: " & bsOptions.ResultFolder
     Debug.Print "  Solver type as defined in swsSolverType_e: " & bsOptions.SolverType
     Debug.Print "  Use soft spring to stabilize the model? (1 = yes, 0 = no): " & bsOptions.UseSoftSpring

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

    Set LBCMgr = Study.LoadsAndRestraintsManager
     If LBCMgr Is Nothing Then ErrorMsg SwApp, "Failed to get the loads and restraints manager"
    'Add a restraint
     Dim restraint As CosmosWorksLib.CWRestraint
     Set restraint = LBCMgr.AddRestraint(swsRestraintTypeFixed, (DispArray3), Nothing, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to add a restraint"

    'Add a centrifugal force to the shaft
     Set CWCentrifugalLoad = LBCMgr.AddCentrifugalForce(DispArray2, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to create a centrifugal force load"

    CWCentrifugalLoad.CFForceBeginEdit
     CWCentrifugalLoad.AngularAcceleration = 5
     CWCentrifugalLoad.AngularVelocity = 5
     CWCentrifugalLoad.Unit = swsUnitSystemSI
     CWCentrifugalLoad.CFForceEndEdit

    Debug.Print ""
     Debug.Print "Centrifugal force:"
     Debug.Print "  Units as defined in swsUnitSystem_e: " & CWCentrifugalLoad.Unit
     Debug.Print "  Angular acceleration: " & CWCentrifugalLoad.AngularAcceleration
     Debug.Print "     Reverse? (False=no, True=yes) " & CWCentrifugalLoad.ReverseAngAccelerationDirection2
     Debug.Print "  Angular velocity: " & CWCentrifugalLoad.AngularVelocity
     Debug.Print "     Reverse? (False=no, True=yes) " & CWCentrifugalLoad.ReverseAngVelocityDirection2
     Debug.Print "  Use time curve? (False=no, True=yes) " & CWCentrifugalLoad.UseTimeCurve2
    'Create mesh
     Dim CWMeshObj As CosmosWorksLib.CWMesh
     Set CWMeshObj = Study.Mesh
     If CWMeshObj Is Nothing Then ErrorMsg SwApp, "Failed to get the mesh object"
     CWMeshObj.MesherType = 0
     CWMeshObj.Quality = 0
     errCode = Study.CreateMesh(0, MeshEleSize, MeshTol)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to create the mesh"
     Set CWMeshObj = Nothing

    'Run analysis
     errCode = Study.RunAnalysis
     If errCode <> 0 Then ErrorMsg SwApp, "Analysis failed with error as defined in swsRunAnalysisError_e: " & errCode

    Dim CWResult As CosmosWorksLib.CWResults
     Set CWResult = Study.Results

    'Plot von Mises stresses
     Dim CWPlot As CosmosWorksLib.CWPlot
     Set CWPlot = CWResult.CreatePlot(swsResultStress, swsStaticNodalStress_VON, swsUnitSI, False, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to create plot"

    CWPlot.ActivatePlot

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
     Dim selection2 As String
     Dim selection3 As String

    'Shaft face
     selection2 = "64,31,0,0,3,0,0,0,255,254,255,14,115,0,104,0,97,0,102,0,116,0,45,0,49,0,64,0,115,0,112,0,105,0,100,0,101,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,10,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,97,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,32,0,67,0,111,0,114,0,112,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,92,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,69,0,100,0,117,0,99,0,97,0,11"
     selection2 = selection2 & "6,0,105,0,111,0,110,0,97,0,108,0,32,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,115,0,104,0,97,0,102,0,116,0,46,0,115,0,108,0,100,0,112,0,114,0,116,0,9,128,255,254,255,5,115,0,104,0,97,0,102,0,116,0,2,0,0,155,126,163,53,0,165,25,208,59,1,0,0,0,0,0,0,0,5,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,63,0,0,0,0,0,0,0,7,50,149,70,12,0,0,0,171,126,163,53,1,0,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,12,0,0,0,171,126,163,53,1,0,0,0,255,255,255,255,0,0,12,128,0,0,5,128,8,0,12,0,0,0,171,126,163,53,0,0,0,0,255,255,255,255,0,0,0,0,0,0,0,0,0,0"
     selection2 = selection2 & ",Type=1"
    'Arm
     selection3 = "64,31,0,0,3,0,0,0,255,254,255,15,115,0,112,0,105,0,100,0,101,0,114,0,45,0,49,0,64,0,115,0,112,0,105,0,100,0,101,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,9,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,8,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,98,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,32,0,67,0,111,0,114,0,112,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,92,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,69,0,100,0,117,0,99,0,9"
     selection3 = selection3 & "7,0,116,0,105,0,111,0,110,0,97,0,108,0,32,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,115,0,112,0,105,0,100,0,101,0,114,0,46,0,115,0,108,0,100,0,112,0,114,0,116,0,9,128,255,254,255,6,115,0,112,0,105,0,100,0,101,0,114,0,2,0,0,149,119,163,53,0,73,0,71,0,1,0,0,0,0,0,0,0,3,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,142,0,0,0,0,0,0,0,13,50,149,70,28,0,0,0,119,124,163,53,10,0,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,107,0,0,0,227,104,166,53,1,0,0,0,255,255,255,255,255,255,1,0,19,0,109,111,70,105,108,108,101,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,139,0,0,0,68,107,166,53,4,0,0,0,15,128,0,0,5,128,8,0,141,0,0,0,83,107,166,53,4,0,0,0,15,128,0,0,5,128,8,0,139,0,0,0,68,107,166,53,3,0,0,0,0,0,12,128,0,0,5,128,8,0,48,0,0,0,82,125,163,53,1,0,0,0,255,255,255,255,0,0,0,0,0,0,0,0,0,0"
     selection3 = selection3 & ",Type=1"
    'Store constants in a collection
     PIDCollection.Add selection2, "selection2"
     PIDCollection.Add selection3, "selection3"

    Set PIDInitializer = PIDCollection
 End Function
```
