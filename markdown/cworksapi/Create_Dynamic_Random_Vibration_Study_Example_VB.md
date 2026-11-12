---
title: "Create Linear Dynamic Random Vibration Study Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Dynamic_Random_Vibration_Study_Example_VB.htm"
---

# Create Linear Dynamic Random Vibration Study Example (VBA)

This example shows how to create a linear dynamic study with a random vibration analysis and get some study options.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click Tools > References > SOLIDWORKS Simulation version type library).
 ' 3. Ensure that the specified file to open exists.
 ' 4. Ensure that the c:\temp folder exists.
 '
 ' Postconditions:
 ' 1. Opens the specified file.
 ' 2. Creates a linear dynamic study for random vibration analysis.
 ' 3. Runs the analysis.
 ' 4. Prints some study options and results to the Immediate window.
 ' 5. Saves the solution step, displacement, velocity,
 '    and stress result files to c:\temp.
 '
 ' NOTE: Because the model is used elsewhere, do not save any changes.
 '---------------------------------------------------------------------------
Option Explicit
Sub main()
    Dim SwApp As SldWorks.SldWorks
     Dim Part As SldWorks.ModelDoc2
     Dim COSMOSWORKS As CosmosWorksLib.COSMOSWORKS
     Dim CWAddinCallBack As CosmosWorksLib.CWAddinCallBack
     Dim ActDoc As CosmosWorksLib.CWModelDoc
     Dim StudyMngr As CosmosWorksLib.CWStudyManager
     Dim Study As CosmosWorksLib.CWStudy
     Dim ShellMgr As CosmosWorksLib.CWShellManager
     Dim ShellMat As CosmosWorksLib.CWMaterial
     Dim LBCMgr As CosmosWorksLib.CWLoadsAndRestraintsManager
     Dim CWDistribMass As CosmosWorksLib.CWDistributedMass
     Dim DynStudyOptions As CosmosWorksLib.CWDynamicStudyOptions
     Dim CWBaseExcitationEntity As Object
     Dim CWDirectionEntity As Object
     Dim longstatus As Long
     Dim longwarnings As Long
     Dim errCode As Long
     Dim boolstatus As Boolean
     Dim nStep As Long
     Dim pDisp5 As Object
     Dim DispArray1 As Variant, DispArray3 As Variant
     Dim Disp As Variant, Stress As Variant, Velocity As Variant, Acceleration As Variant
     Dim sStudyName As String
     Dim ResultOptions As CosmosWorksLib.CWStudyResultOptions
     Dim DampingOptions As CosmosWorksLib.CWDampingOptions
     Dim DampingRatios As Variant
     Dim i As Long
     Dim freqOption As Long
     Dim freqValue As Double
     Dim bChecked As Long
     Dim forces2 As Variant
     Dim selectedAndModelReactionFM As Variant
     Dim selectedOnlyReactionFM As Variant
     Dim CWFeatObj1 As CosmosWorksLib.CWShell
     Dim CWFeatObj2 As CosmosWorksLib.CWPressure
     Dim CWFeatObj3 As CosmosWorksLib.CWRestraint
     Dim CWFeatObj4 As CosmosWorksLib.CWMesh
     Dim CWFeatObj5 As CosmosWorksLib.CWResults
     Dim param As Long
     Dim dParam As Double
     Dim inRadius As Double
     Dim outRadius As Double
    'Tolerances and baselines
     Const MeshEleSize   As Double = 26.5868077635828 'mm
     Const MeshTol       As Double = 1.32934038817914 'mm
    'Connect to SOLIDWORKS
     Set SwApp = Application.SldWorks
     If SwApp Is Nothing Then Exit Sub
    'Open document
     Set Part = SwApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\lineardynamic.SLDPRT", swDocPART, swOpenDocOptions_Silent, "", longstatus, longwarnings)
     If Part Is Nothing Then ErrorMsg SwApp, "Failed to open lineardynamic.SLDPRT"
    'Add-in callback
     Set CWAddinCallBack = SwApp.GetAddInObject("CosmosWorks.CosmosWorks")
     If CWAddinCallBack Is Nothing Then ErrorMsg SwApp, "Failed to get CwAddincallback object"
     Set COSMOSWORKS = CWAddinCallBack.COSMOSWORKS
     If COSMOSWORKS Is Nothing Then ErrorMsg SwApp, "Failed to get CosmosWorks object"
    'Get active document
     Set ActDoc = COSMOSWORKS.ActiveDoc()
     If ActDoc Is Nothing Then ErrorMsg SwApp, "Failed to get active document"
    'Create a dynamic random vibration study
     Set StudyMngr = ActDoc.StudyManager()
     If StudyMngr Is Nothing Then ErrorMsg SwApp, "Failed to get study manager object"
    sStudyName = "Dynamic_Random_Vibration"
     Set Study = StudyMngr.CreateNewStudy3(sStudyName, swsAnalysisStudyTypeDynamic, swsDynamicAnalysisSubTypeRandom, errCode)
    Debug.Print "Linear dynamic study with random vibration analysis"
     Debug.Print ""
     Debug.Print "Study configuration name is " & Study.ConfigurationName
     Debug.Print "Dynamic analysis subtype as defined in swsAnalysisStudyType_e is " & Study.DynamicAnalysisSubType
     Debug.Print "Dynamic study options..."
    Set DynStudyOptions = Study.DynamicStudyOptions
    errCode = DynStudyOptions.GetFrequencyOption2(freqOption, freqValue)
     Debug.Print "  Frequency option (0=number of frequencies, 1=upper bound): " & freqOption
     Debug.Print "  No. of frequencies or upper-bound frequency: " & freqValue
     errCode = DynStudyOptions.GetFrequencyShiftOption2(bChecked, freqValue)
     Debug.Print "  Is frequency shift enabled (0=no, 1=yes)? " & bChecked
     Debug.Print "  Frequency shift: " & freqValue
    errCode = DynStudyOptions.SetIncompatibleBondingOption2(0) ' automatic
     errCode = DynStudyOptions.SetUseSoftSpring2(0) ' do not use soft springs to stabilize model
     errCode = DynStudyOptions.SetResultFolderPath2("c:\temp")
    DynStudyOptions.SolverType = 2 ' FFEPlus
    errCode = DynStudyOptions.GetRandomVibrationAnalysisMethod2(param)
     Debug.Print "  Analysis method as defined in swsRandomVibrationAnalysisMethod_e: " & param
     errCode = DynStudyOptions.GetRandomVibrationBiasingParameter2(dParam)
     Debug.Print "  Biasing parameter: " & param
     errCode = DynStudyOptions.GetRandomVibrationCorrelationOption2(param)
     Debug.Print "  Correlation option as defined in swsRandomVibrationCorrelationOption_e: " & param
     errCode = DynStudyOptions.GetRandomVibrationCrossModeCutOffRatio2(dParam)
     Debug.Print "  Cross-mode cut-off ratio: " & param
     errCode = DynStudyOptions.GetRandomVibrationFrequencyLowerLimit2(dParam)
     Debug.Print "  Operating frequency lower limit: " & param
     errCode = DynStudyOptions.GetRandomVibrationFrequencyUnits2(param)
     Debug.Print "  Units of operating frequency as defined in swsFrequencyUnit_e: " & param
     errCode = DynStudyOptions.GetRandomVibrationFrequencyUpperLimit2(dParam)
     Debug.Print "  Operating frequency upper limit: " & param
     errCode = DynStudyOptions.GetRandomVibrationGaussIntegrationOrder2(param)
     Debug.Print "  Gauss integration order as defined in swsGaussIntegrationOrder_e: " & param
     errCode = DynStudyOptions.GetRandomVibrationNoOfFrequencyPoints2(param)
     Debug.Print "  Number of frequency points: " & param
     errCode = DynStudyOptions.GetRandomVibrationPartialCorrelationDetails2(param, inRadius, outRadius)
     Debug.Print "  Partially correlated units as defined in swsLinearUnit_e: " & param
     Debug.Print "  Inside radius: " & inRadius
     Debug.Print "  Outside radius: " & outRadius
    Debug.Print ""
    'Set study result options
     Debug.Print "Study result options..."
     Set ResultOptions = Study.StudyResultOptions
     ResultOptions.SaveResultsForSolutionStepsOption = 1 ' save solution step results
     ResultOptions.SaveDisplacementsAndVelocitiesOption = 1 ' save displacements and velocities
     ResultOptions.SaveStresses = 1 ' save stresses
     'Solution step set #1
     errCode = ResultOptions.SetSolutionStepsSetInformation(1, 10, 100, 3)
     Debug.Print "  Set solution steps set #1 (10-100, inc=3)? (0=success): " & errCode
     'Solution step set #3
     errCode = ResultOptions.SetSolutionStepsSetInformation(3, 100, 1000, 5)
     Debug.Print "  Set solution steps set #3 (100-1000, inc=5)? (0=success): " & errCode
     Debug.Print ""
    'Set damping options
     Set DampingOptions = Study.DampingOptions
     DampingOptions.DampingType = 0 'Modal damping
     DampingRatios = Array(1, 5, 3.45, 6, 15, 15, 16, 25, 34.5)
     errCode = DampingOptions.SetDampingRatios(3, (DampingRatios))
     DampingOptions.ComputeFromMaterialDamping = 0 ' do not use the material damping ratio
    Dim PID       As Variant
     Dim SelObj    As Object
     Dim obj       As Object
    'Get face by persistent ID
     boolstatus = Part.Extension.SelectByID2("", "FACE", 0.367377178180561, 1.53999999998859E-02, -0.443699715030164, False, 0, Nothing, 0)
     Set obj = Part.SelectionManager.GetSelectedObject6(1, -1)
     PID = Part.Extension.GetPersistReference3(obj)
     Set SelObj = Part.Extension.GetObjectByPersistReference3((PID), errCode)
     DispArray1 = Array(SelObj) 'Face
    'Get edge by persistent ID
     boolstatus = Part.Extension.SelectByID2("", "EDGE", 0.473843326221299, 1.60904480509885E-02, -6.90335842989498E-04, False, 0, Nothing, 0)
     Set obj = Part.SelectionManager.GetSelectedObject6(1, -1)
     PID = Part.Extension.GetPersistReference3(obj)
     Set CWBaseExcitationEntity = Part.Extension.GetObjectByPersistReference3((PID), errCode)
     DispArray3 = Array(CWBaseExcitationEntity) 'Edge
    'Get Axis1 reference geometry by persistent ID
     boolstatus = Part.Extension.SelectByID2("Axis1", "AXIS", -3.20045390890095E-02, 6.39408825367532E-02, -3.19259521004658E-02, False, 0, Nothing, 0)
     Set obj = Part.SelectionManager.GetSelectedObject6(1, -1)
     PID = Part.Extension.GetPersistReference3(obj)
     Set CWDirectionEntity = Part.Extension.GetObjectByPersistReference3((PID), errCode)
     Set pDisp5 = CWDirectionEntity
    'Add materials
     Set ShellMgr = Study.ShellManager
     If ShellMgr Is Nothing Then ErrorMsg SwApp, "Failed to get shell manager object"
    Set CWFeatObj1 = ShellMgr.GetShellAt(0, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to get shell component"
     Set ShellMat = CWFeatObj1.GetDefaultMaterial
     ShellMat.MaterialUnits = 0
     Call ShellMat.SetPropertyByName("EX", 2000000000000#, 0)
     Call ShellMat.SetPropertyByName("NUXY", 0.25, 0)
     errCode = CWFeatObj1.SetShellMaterial(ShellMat)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to apply material"
    Call CWFeatObj1.ShellBeginEdit
     CWFeatObj1.Formulation = 1 ' thick shell
     CWFeatObj1.ShellUnit = 1 ' centimeters
     CWFeatObj1.ShellThickness = 5 ' 5 cm
     CWFeatObj1.ShellOffsetOption = 3 ' specify reference surface
     CWFeatObj1.ShellOffsetValue = 0.3
     errCode = CWFeatObj1.ShellEndEdit
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to create shell"
     Set CWFeatObj1 = Nothing
    'Get loads and restraints manager
     Set LBCMgr = Study.LoadsAndRestraintsManager
     If LBCMgr Is Nothing Then ErrorMsg SwApp, "Failed to get loads and restraints manager"
    'Create normal pressure
     Set CWFeatObj2 = LBCMgr.AddPressure(swsPressureTypeNormal, (DispArray1), Nothing, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to create normal pressure"
     Call CWFeatObj2.PressureBeginEdit
     Debug.Print "Normal pressure values..."
     Debug.Print ("  Pressure unit in swsStrengthUnit_e units: " & CWFeatObj2.Unit)
     Debug.Print ("  Pressure value: " & CWFeatObj2.Value)
     Debug.Print ("  Pressure phase angle (-1 if not set): " & CWFeatObj2.PhaseAngle)
     Debug.Print ("  Pressure phase angle unit in swsPhaseAngleUnit_e units: " & CWFeatObj2.PhaseAngleUnit)
     errCode = CWFeatObj2.PressureEndEdit
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to apply normal pressure value"
     Set CWFeatObj2 = Nothing
     Debug.Print " "
    'Add a restraint
     Set CWFeatObj3 = LBCMgr.AddRestraint(0, (DispArray3), pDisp5, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to create restraint"
     Call CWFeatObj3.RestraintBeginEdit
     Call CWFeatObj3.SetTranslationComponentsValues(0, 0, 1, 0#, 0#, 0#)
     Call CWFeatObj3.SetRotationComponentsValues(0, 0, 0, 0#, 0#, 0#)
     CWFeatObj3.Unit = 2
     errCode = CWFeatObj3.RestraintEndEdit
     If errCode <> 0 Then ErrorMsg SwApp, "Restraint end-edit failed"
    'Create mesh
     Set CWFeatObj4 = Study.Mesh
     If CWFeatObj4 Is Nothing Then ErrorMsg SwApp, "Failed to create mesh object"
     CWFeatObj4.MesherType = 0
     CWFeatObj4.Quality = 1
    errCode = Study.CreateMesh(0, MeshEleSize, MeshTol)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to create mesh"
     Debug.Print "Worst Jacobian ratio for the mesh: " & CWFeatObj4.GetWorstJacobianRatio
     Debug.Print ""
    'Add distributed mass
     Set CWDistribMass = LBCMgr.AddDistributedMass((DispArray1), 0, 1, errCode)
     Debug.Print "Total distributed mass: " & CWDistribMass.TotalMass
     Debug.Print "  Units in swsUnitSystem_e units: " & CWDistribMass.Units
     Debug.Print ""
    'Run analysis
     Debug.Print "Running the analysis"
     Debug.Print ""
     errCode = Study.RunAnalysis
     If errCode <> 0 Then ErrorMsg SwApp, "Analysis failed with error code as defined in swsRunAnalysisError_e:" & errCode

     'Get results
     Set CWFeatObj5 = Study.Results
     If CWFeatObj5 Is Nothing Then ErrorMsg SwApp, "Failed to get results object"
    Debug.Print "Study results..."
     nStep = CWFeatObj5.GetMaximumAvailableSteps
     Debug.Print "  Maximum available steps: " & nStep
    'Get algebraic minimum/maximum resultant displacements
     Disp = CWFeatObj5.GetMinMaxDisplacement(3, nStep, Nothing, 0, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to get displacement results"
     Debug.Print "  Min/Max URES Resultant Displacements (Node, Min, Node, Max):"
     For i = 0 To UBound(Disp)
         Debug.Print ("  * " & Disp(i))
     Next
     Debug.Print ""
    'Get algebraic minimum/maximum von Mises stresses
     Stress = CWFeatObj5.GetMinMaxStress(9, 0, nStep, Nothing, 3, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to get stress results"
     Debug.Print "  Algebraic Min/Max von Mises Stresses (Node, Min, Node, Max):"
     For i = 0 To UBound(Stress)
         Debug.Print ("  * " & Stress(i))
     Next
     Debug.Print ""
    'Get algebraic minimum/maximum velocities
     Velocity = CWFeatObj5.GetMinMaxVelocity(0, nStep, CWDirectionEntity, 0, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to get velocity results"
     Debug.Print "  Algebraic Min/Max Velocities (Node, Min, Node, Max):"
     For i = 0 To UBound(Velocity)
         Debug.Print ("  * " & Velocity(i))
     Next
     Debug.Print ""
    'Get algebraic minimum/maximum accelerations
     Acceleration = CWFeatObj5.GetMinMaxAcceleration(0, nStep, CWDirectionEntity, 0, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to get acceleration results"
     Debug.Print "  Algebraic Min/Max Accelerations (Node, Min, Node, Max):"
     For i = 0 To UBound(Acceleration)
         Debug.Print ("  * " & Acceleration(i))
     Next
    'Reaction forces and moments for entire model and selected face at solution step 40
     forces2 = CWFeatObj5.GetReactionForcesAndMomentsWithSelections(40, Nothing, swsForceUnitNOrNm, (DispArray1), selectedAndModelReactionFM, selectedOnlyReactionFM, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to get reaction forces and moments"
     Debug.Print "  Reaction forces (N) and moments (N-m) for selected face "
     Debug.Print "  {xcoord_force, ycoord_force, zcoord_force, resultant_force, "
     Debug.Print "   xcoord_moment, ycoord_moment, zcoord_moment, resultant_moment}:"
     For i = 0 To UBound(selectedOnlyReactionFM)
         Debug.Print ("  * " & selectedOnlyReactionFM(i))
     Next
End Sub
Sub ErrorMsg(SwApp As SldWorks.SldWorks, Message As String)
     SwApp.SendMsgToUser2 Message, 0, 0
     SwApp.RecordLine "'*** WARNING - General"
     SwApp.RecordLine "'*** " & Message
     SwApp.RecordLine ""
 End Sub
```
