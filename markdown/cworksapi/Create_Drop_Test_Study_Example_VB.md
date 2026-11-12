---
title: "Create Drop Test Study Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Drop_Test_Study_Example_VB.htm"
---

# Create Drop Test Study Example (VBA)

This example shows how to create a drop test study.

NOTE: To get persistent reference identifiers (PIDs) for model selections, you can use [pidcollector.exe](GettingStarted-swsimulationapi.html) or IModelDocExtension::GetPersistReference3.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click Tools > References > SOLIDWORKS Simulation version type library).
 ' 3. Open public_documents\samples\tutorial\api\KeyPad_1.sldasm.
 '
 ' Postconditions:
 '  1. Creates a default drop test study results plot.
 '  2. Creates drop test study, Study 2.
 '  3. Applies Nylon 101 SOLIDWORKS material to all components.
 '  4. Meshes the model.
 '  5. Sets drop height to 1000 mm.
 '  6. Runs the analysis.
 '  7. Validates the von Mises stress results.
 '  8. When the macro stops:
 '     a. Inspect the Immediate window for the 1000 mm drop test study's setup
 '        and result options.
 '     b. Inspect the default drop test study results plot.
 '     c. Press F5 to continue.
 '  9. Changes drop height to 2000 mm.
 ' 10. Re-runs the analysis.
 ' 11. Inspect the results folder.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 ' ---------------------------------------------------------------------------

Dim SwApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim COSMOSWORKS As CosmosWorksLib.COSMOSWORKS
 Dim CWAddinCallBack As CosmosWorksLib.CWAddinCallBack
 Dim ActDoc As CosmosWorksLib.CWModelDoc
 Dim StudyMngr As CosmosWorksLib.CWStudyManager
 Dim Study As CosmosWorksLib.CWStudy
 Dim CWMesh As CosmosWorksLib.CWMesh

Dim CWFeatObj As CosmosWorksLib.CWResults
 Dim SolidMgr As CosmosWorksLib.CWSolidManager
 Dim SolidComponent As CosmosWorksLib.CWSolidComponent
 Dim Solidbody As CosmosWorksLib.CWSolidBody
 Dim Setup As CosmosWorksLib.CWDropTestSetup
 Dim ResultOptions As CosmosWorksLib.CWDropTestResultOptions
 Dim StudyOptions As CosmosWorksLib.CWDropTestStudyOptions
 Dim Selection As Object

Dim CosmosFolder As String
 Dim sLibWithPathname As String, sMaterialName As String, sName As String

Dim errCode As Long
 Dim VMS1000 As Double, VMS2000 As Double, Stress As Variant
 Dim nStep As Long, CompCount As Long, j As Long, Height As Double

Dim bApp As Long
 Dim PIDCollection As New Collection
 Dim Tol As Double, A As Double, B As Double

 Option Explicit
 Sub main()

    Set PIDCollection = PIDInitializer()

    Tol = 0.25                                '25% tolerance
     VMS1000 = 7314431                         'maximum von Mises stress at step 25 for drop height = 1000 mm
     VMS2000 = 10389063                        'maximum von Mises stress at step 25 for drop height = 2000 mm
    Set SwApp = Application.SldWorks
     If SwApp Is Nothing Then Exit Sub

    CosmosFolder = SwApp.GetExecutablePath

    Set Part = SwApp.ActiveDoc

    Set CWAddinCallBack = SwApp.GetAddInObject("SldWorks.Simulation")
     Set COSMOSWORKS = CWAddinCallBack.COSMOSWORKS

    Set ActDoc = COSMOSWORKS.ActiveDoc()

    ' Add a default drop test study results plot
     bApp = ActDoc.AddDefaultDropTestStudyPlot(swsDropTestResultElementalStress, swsStressComponentVON)

     Set StudyMngr = ActDoc.StudyManager()

    'Create a drop test study
     Set Study = StudyMngr.CreateNewStudy3("Study 2", 6, 0, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to create a drop test study"

    Set StudyOptions = Study.DropTestStudyOptions
     Debug.Print "Study results folder: " & StudyOptions.ResultFolder
     Debug.Print "Study displacement formulation (True = large): " & StudyOptions.LargeDisplacement2
     Set ResultOptions = Study.DropTestResultOptions
     Debug.Print "Number of graph steps: " & ResultOptions.NoOfGraphSteps
     Debug.Print "Number of plots: " & ResultOptions.NoOfPlots
     Debug.Print "Save results from starting time (sec): " & ResultOptions.SaveResultsStartingTime
     Debug.Print "Time to solve after impact (sec): " & ResultOptions.SolutionTimeAfterImpact

    'Create mesh
     Set CWMesh = Study.Mesh
     CWMesh.MesherType = 0                                       'standard mesh = 0, CB mesh = 1
     CWMesh.Quality = 0                                          'draft = 0, high quality = 1
     errCode = Study.CreateMesh(0, 2, 0.05)                      'create mesh, 0-1-2-3-4 : mm-cm-m-in-ft

    'Apply material
     sLibWithPathname = CosmosFolder & "\lang\english\sldmaterials\solidworks materials.sldmat"
     sMaterialName = "Nylon 101"                                'Nylon 101 SOLIDWORKS material
     Set SolidMgr = Study.SolidManager
     CompCount = SolidMgr.ComponentCount
     For j = 0 To (CompCount - 1)                               'Apply material to all solid components
         Set SolidComponent = SolidMgr.GetComponentAt(j, errCode)
         sName = SolidComponent.ComponentName
         Set Solidbody = SolidComponent.GetSolidBodyAt(0, errCode)
         bApp = Solidbody.SetLibraryMaterial(sLibWithPathname, sMaterialName)
         Set Solidbody = Nothing
     Next j

    'Assign drop test setup
     Set Selection = SelectByPID(Part, "selection1", PIDCollection)
     Set Setup = Study.AddDropTestSetup(Selection, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to create DropTestSetup object"
     If Setup Is Nothing Then ErrorMsg SwApp, "Failed to get DropTestSetup object"
     Height = Setup.DropHeight
     If Height <> 1000 Then ErrorMsg SwApp, "Failed to validate drop height = 1000 mm from original Study 1"

    Debug.Print "Critical damping ratio: " & Setup.CriticalDampingRatio
     Debug.Print "Drop height (mm): " & Setup.DropHeight
     Debug.Print "Drop height type (swsDropHeightType_e): " & Setup.DropHeightType
     Debug.Print "Drop height units (swsLinearUnit_e): " & Setup.DropHeightUnit
     Debug.Print "Drop type (swsDropType_e): " & Setup.DropType
     Debug.Print "Reverse gravity direction? (True = yes) " & Setup.FlipGravityDirection2
     Debug.Print "Reverse velocity direction? (True = yes) " & Setup.FlipVelocityDirection2
     Debug.Print "Coefficient of friction: " & Setup.FrictionCoefficient
     Debug.Print "Gravity magnitude: " & Setup.Gravity
     Debug.Print "Gravity units (swsAccelerationUnit_e): " & Setup.GravityUnit
     Debug.Print "Mass density of impact layer: " & Setup.MassDensity
     Debug.Print "Stiffness per unit area normal to impact plane: " & Setup.NormalStiffness
     Debug.Print "Units of stiffness (swsUnitSystem_e): " & Setup.StiffnessUnit
     Debug.Print "Stiffness per unit area parallel to the impact plane: " & Setup.TangentialStiffness
     Debug.Print "Orientation of impact plane (swsDropTargetOrientationType_e): " & Setup.TargetOrientationType
     Debug.Print "Stiffness type (swsDropTargetStiffnessType_e): " & Setup.TargetStiffnessType
     Debug.Print "Thickness of the impact layer: " & Setup.TargetThickness
     Debug.Print "Units of thickness (swsLinearUnit_e): " & Setup.ThicknessUnit
     Debug.Print "Velocity at impact: " & Setup.Velocity
     Debug.Print "Units of velocity (swsVelocityUnit_e): " & Setup.VelocityUnit

    'Run study for drop height = 1000 mm
     errCode = Study.RunAnalysis
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to run study (drop height = 1000 mm)"
     Set CWFeatObj = Study.Results
     If CWFeatObj Is Nothing Then ErrorMsg SwApp, "Failed to get Result Object (drop height = 1000 mm)"
     nStep = CWFeatObj.GetMaximumAvailableSteps         'nStep = last step of study
     If nStep <> 25 Then ErrorMsg SwApp, "Total number of steps in result is incorrect (drop height = 1000 mm)"
     Stress = CWFeatObj.GetMinMaxStress(9, 0, nStep, Nothing, 0, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to get von Mises stress result for drop height = 1000 mm"
         A = Stress(3)
         B = VMS1000
         If ResultsVer(A, B, Tol) = True Then
         ErrorMsg SwApp, "The von Mises stress result for drop height = 1000 mm has % error = " & ResultsError(A, B, Tol)
     End If

    'Change drop height from 1000 mm to 2000 mm
     Setup.DropTestSetupBeginEdit
     Setup.DropType = 0
     Setup.DropHeightType = 0
     Setup.DropHeight = 2000
     Setup.DropHeightUnit = 0
     errCode = Setup.DropTestSetupEndEdit

    If errCode <> 0 Then ErrorMsg SwApp, "Failed to make change to drop height"
     Height = Setup.DropHeight
     If Height <> 2000 Then ErrorMsg SwApp, "Failed to correctly change drop height to 2000 mm"

    Stop ' Inspect results for drop height = 1000 mm

    'Run study for drop height = 2000 mm
     errCode = Study.RunAnalysis
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to run study (drop height = 2000 mm)"
     Set CWFeatObj = Study.Results
     If CWFeatObj Is Nothing Then ErrorMsg SwApp, "Failed to get Result Object (drop height = 2000 mm) "
     nStep = CWFeatObj.GetMaximumAvailableSteps         'nStep = last step of study
     If nStep <> 25 Then ErrorMsg SwApp, "Total number of steps in result is incorrect (drop height = 2000 mm)"
     Stress = CWFeatObj.GetMinMaxStress(9, 0, nStep, Nothing, 0, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to get von Mises stress result for drop height = 2000 mm"
         A = Stress(3)
         B = VMS2000
         If A < VMS1000 Or A = VMS1000 Then ErrorMsg SwApp, "The von Mises stress for drop height = 2000 mm is less than or equal to drop height = 1000 mm."
         If ResultsVer(A, B, Tol) = True Then
         ErrorMsg SwApp, "The von Mises stress result for drop height = 2000 mm has % error = " & ResultsError(A, B, Tol)
     End If

End Sub
Function ResultsVer(ActualResult As Variant, ReferenceResult As Variant, Tolerance As Double) As Boolean
     ResultsVer = (ActualResult < (1 - Tolerance) * ReferenceResult) Or (ActualResult > (1 + Tolerance) * ReferenceResult)
 End Function
Function ResultsError(ActualResult As Variant, ReferenceResult As Variant, Tolerence As Double) As Double
     ResultsError = (ActualResult - ReferenceResult) / ReferenceResult * 100
 End Function
Sub ErrorMsg(SwApp As SldWorks.SldWorks, Message As String)
     SwApp.SendMsgToUser2 Message, 0, 0
     SwApp.RecordLine "'*** WARNING - General"
     SwApp.RecordLine "'*** " & Message
     SwApp.RecordLine ""
 End Sub
Function SelectByPID(nPart As SldWorks.ModelDoc2, PIDName As String, PIDCollection As Collection) As Object
     Dim PID() As Byte
     Dim PIDVariant As Variant
     Dim PIDString As String
     Dim EntityType As Long
     Dim i As Long
     Dim SelObj As Object

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
     Set SelObj = nPart.Extension.GetObjectByPersistReference3((PID), errCode)
     Set SelectByPID = SelObj
     Set SelObj = Nothing
 End Function
Function PIDInitializer() As Collection
 Dim PIDCollection As New Collection
    Dim selection1 As String
    selection1 = "230,35,0,0,3,0,0,0,255,254,255,17,112,0,97,0,100,0,95,0,49,0,45,0,49,0,64,0,107,0,101,0,121,0,32,0,112,0,97,0,100,0,95,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,51,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,6,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,55,92,0,92,0,112,0,117,0,110,0,45,0,113,0,97,0,115,0,118,0,114,0,45,0,112,0,108,0,112,0,92,0,81,0,97,0,95,0,100,0,111,0,99,0,117,0,109,0,101,0,110,0,116,0,115,0,92,0,77,0,111,0,98,0,105,0,108,0,101,0,72,0,97,0,110,0,100,0,115,0,101,0,116,0,92,0,80,0,97,0,100,0,95,0,49,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,5,80,0,97,0,100,0,95,0,49,0,2,0,0,0,86,29,67,255,254,2"
     selection1 = selection1 & "55,0,255,254,255,0,0,56,86,29,67,0,0,0,0,0,0,0,0,3,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,56,86,29,67,26,0,0,0,56,86,29,67,0,0,0,0,0,0,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,26,0,0,0,56,86,29,67,1,0,0,0,12,128,0,0,5,128,8,0,26,0,0,0,56,86,29,67,2,0,0,0,12,128,0,0,5,128,8,0,26,0,0,0,56,86,29,67,3,0,0,0,12,128,0,0,5,128,8,0,26,0,0,0,56,86,29,67,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"
     selection1 = selection1 & ",Type=1"
    'Store constants in a collection
     PIDCollection.Add selection1, "selection1"
    Set PIDInitializer = PIDCollection
 End Function
```
