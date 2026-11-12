---
title: "Create Fatigue Study for Dynamic Random Vibration Study Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Fatigue_Study_for_Dynamic_Random_Vibration_Study_Example_VB.htm"
---

# Create Fatigue Study for Dynamic Random Vibration Study Example (VBA)

This example shows how to create a fatigue study for a linear dynamic random vibration study.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click Tools > References > SOLIDWORKS Simulation version type library).
 ' 3. Ensure that the specified part and material library exist.
 ' 4. Open an Immediate window.
 '
 ' Postconditions:
 '  1. Opens the specified file.
 '  2. Creates and analyzes study, Dynamic_Random_Vibration.
 '  3. Creates a default fatigue study damage plot.
 '  4. Creates study, RandomVibrationFatigue.
 '  5. Adds a fatigue event of duration 60 seconds to  RandomVibrationFatigue.
 '  6. Modifies the fatigue S-N curve equation for the model's material.
 '  7. Analyzes RandomVibrationFatigue and displays message boxes with damage
 '     percentage errors for each of the following computational methods:
 '     * Narrow Band
 '     * Steinberg
 '     * Wirsching
 '  8. Click OK to close each message box.
 '  9. Inspect the Immediate window for the Narrow Band method
 '     minimum and maximum fatigue.
 ' 10. Inspect the damage plot.
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
     Dim SolidMat As CosmosWorksLib.CWMaterial
     Dim LBCMgr As CosmosWorksLib.CWLoadsAndRestraintsManager
     Dim DynStudyOptions As CosmosWorksLib.CWDynamicStudyOptions
     Dim CWDirectionEntity As Object
     Dim CWBaseExcitationEntity as Object
     Dim longstatus As Long
     Dim longwarnings As Long
     Dim errCode As Long
     Dim boolstatus As Boolean
     Dim pDisp5 As Object
     Dim DispArray1 As Variant, DispArray3 As Variant
     Dim sStudyName As String
     Dim ResultOptions As CosmosWorksLib.CWStudyResultOptions
     Dim DampingOptions As CosmosWorksLib.CWDampingOptions
     Dim DampingRatios As Variant
     Dim freqOption As Long
     Dim freqValue As Double
     Dim bChecked As Boolean
     Dim CWFeatObj As Object
     Dim CWFeatObj2 As CosmosWorksLib.CWPressure
     Dim CWFeatObj3 As CosmosWorksLib.CWRestraint
     Dim CWFeatObj4 As CosmosWorksLib.CWMesh
     Dim CWFeatObj5 As CosmosWorksLib.CWResults
     Dim param As Long
     Dim dParam As Double
     Dim inRadius As Double
     Dim outRadius As Double
     Dim FatigueOptions As CosmosWorksLib.CWFatigueStudyOptions
     Dim FatigueEvent As CosmosWorksLib.CWFatigueEvent
     Dim Damage As Variant

    Const Tol As Double = 0.05 '5% - damage tolerance
     Const DamageMax_NarrowBand As Double = 1305.36  'baseline percentage
     Const DamageMax_Steinberg As Double = 741.951  'baseline percentage
     Const DamageMax_Wirsching As Double = 907.23  'baseline percentage
     Const MeshEleSize As Double = 26.5868077635828 'mm
     Const MeshTol As Double = 1.32934038817914 'mm
    Set SwApp = Application.SldWorks
     If SwApp Is Nothing Then Exit Sub

    Set Part = SwApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\block.SLDPRT", swDocPART, swOpenDocOptions_Silent, "", longstatus, longwarnings)
     If Part Is Nothing Then ErrorMsg SwApp, "Failed to open block.SLDPRT"
    Set CWAddinCallBack = SwApp.GetAddInObject("CosmosWorks.CosmosWorks")
     If CWAddinCallBack Is Nothing Then ErrorMsg SwApp, "Failed to get CwAddincallback object"
     Set COSMOSWORKS = CWAddinCallBack.COSMOSWORKS
     If COSMOSWORKS Is Nothing Then ErrorMsg SwApp, "Failed to get CosmosWorks object"
    Set ActDoc = COSMOSWORKS.ActiveDoc()
     If ActDoc Is Nothing Then ErrorMsg SwApp, "Failed to get active document"
    ' Create a dynamic random vibration study
     Set StudyMngr = ActDoc.StudyManager()
     If StudyMngr Is Nothing Then ErrorMsg SwApp, "Failed to get CWStudyManager object"
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
    errCode = DynStudyOptions.SetIncompatibleBondingOption2(swsIncompatibleBondingOption_Automatic)
     errCode = DynStudyOptions.SetUseSoftSpring2(0) ' Not using soft spring to stabilize model
     errCode = DynStudyOptions.SetResultFolderPath2("c:\temp")
    DynStudyOptions.SolverType = swsSolverTypeFFEPlus
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
    ' Set study result options
     Debug.Print "Study result options..."
     Set ResultOptions = Study.StudyResultOptions
     ResultOptions.SaveResultsForSolutionStepsOption = swsSaveResultsOption_ForAllSolutionSteps
     ResultOptions.SaveDisplacementsAndVelocitiesOption = swsResultsDisplacementAndVelocityOption_Absolute
     ResultOptions.SaveStresses = 1 ' Save stress results

    ' Set damping options
     Set DampingOptions = Study.DampingOptions
     DampingOptions.DampingType = swsDampingType_Modal
     DampingRatios = Array(1, 5, 3.45, 6, 15, 15, 16, 25, 34.5)
     errCode = DampingOptions.SetDampingRatios(3, (DampingRatios))
     DampingOptions.ComputeFromMaterialDamping = 0 ' Not using the material damping ratio to calculate modal damping ratios
    Dim PID       As Variant
     Dim SelObj    As Object
     Dim obj       As Object
     Dim fixtureEntity As Object
    ' Get a face to which to apply a pressure
     boolstatus = Part.Extension.SelectByID2("", "FACE", -7.95509158535879E-03, 0, -1.13043904061669E-02, False, 0, Nothing, 0)
     Set obj = Part.SelectionManager.GetSelectedObject6(1, -1)
     PID = Part.Extension.GetPersistReference3(obj)
     Set SelObj = Part.Extension.GetObjectByPersistReference3((PID), errCode)
     DispArray1 = Array(SelObj)
    ' Get a face to use as a fixture
     boolstatus = Part.Extension.SelectByID2("", "FACE", -2.07435908961884E-02, -1.34200983288792E-02, -9.99045700837087E-03, False, 0, Nothing, 0)
     Set obj = Part.SelectionManager.GetSelectedObject6(1, -1)
     PID = Part.Extension.GetPersistReference3(obj)
     Set fixtureEntity = Part.Extension.GetObjectByPersistReference3((PID), errCode)
     DispArray3 = Array(fixtureEntity)

     ' Get a face to use as a reference entity
     boolstatus = Part.Extension.SelectByID2("", "FACE", 1.80913769526114E-02, -1.29337958455835E-02, -1.01226987114842E-02, False, 0, Nothing, 0)
     Set obj = Part.SelectionManager.GetSelectedObject6(1, -1)
     PID = Part.Extension.GetPersistReference3(obj)
     Set CWDirectionEntity = Part.Extension.GetObjectByPersistReference3((PID), errCode)
     Set pDisp5 = CWDirectionEntity
    ' Add a material
     Dim SolidMgr As CosmosWorksLib.CWSolidManager
     Dim SolidComponent As CosmosWorksLib.CWSolidComponent
     Dim SName As String
     Dim SolidBody As CosmosWorksLib.CWSolidBody

    Set SolidMgr = Study.SolidManager
     Set SolidComponent = SolidMgr.GetComponentAt(0, errCode)
     SName = SolidComponent.ComponentName
    Set SolidBody = SolidComponent.GetSolidBodyAt(0, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "No solid body"
    boolstatus = SolidBody.SetLibraryMaterial("C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\sldmaterials\solidworks materials.sldmat", "Ductile Iron (SN)")
     If boolstatus = False Then ErrorMsg SwApp, "No material applied"
    ' Get loads and restraints manager
     Set LBCMgr = Study.LoadsAndRestraintsManager
     If LBCMgr Is Nothing Then ErrorMsg SwApp, "Failed to get loads and restraints manager"
    ' Apply pressure normal to the selected face
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
    Debug.Print " "
    ' Add a fixture
     Set CWFeatObj3 = LBCMgr.AddRestraint(swsRestraintTypeFixed, (DispArray3), pDisp5, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to create restraint"
     Call CWFeatObj3.RestraintBeginEdit
     Call CWFeatObj3.SetTranslationComponentsValues(0, 0, 1, 0#, 0#, 0#)
     Call CWFeatObj3.SetRotationComponentsValues(0, 0, 0, 0#, 0#, 0#)
     CWFeatObj3.Unit = swsLinearUnitMeters
     errCode = CWFeatObj3.RestraintEndEdit
     If errCode <> 0 Then ErrorMsg SwApp, "Restraint end-edit failed"
    ' Create mesh
     Set CWFeatObj4 = Study.Mesh
     If CWFeatObj4 Is Nothing Then ErrorMsg SwApp, "Failed to create mesh object"
     CWFeatObj4.MesherType = swsMesherTypeStandard
     CWFeatObj4.Quality = swsMeshQualityHigh
    errCode = Study.CreateMesh(swsLinearUnitMillimeters, MeshEleSize, MeshTol)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to create mesh"
     Debug.Print "Worst Jacobian ratio for the mesh: " & CWFeatObj4.GetWorstJacobianRatio
     Debug.Print ""
    ' Run analysis
     Debug.Print "Running the analysis"
     Debug.Print ""
     errCode = Study.RunAnalysis
     If errCode <> 0 Then ErrorMsg SwApp, "Analysis failed with error code as defined in swsRunAnalysisError_e:" & errCode
     Set CWFeatObj5 = Study.Results
     If CWFeatObj5 Is Nothing Then ErrorMsg SwApp, "Failed to get results object"

    ' Add default fatigue study results plot
     errCode = ActDoc.AddDefaultFatigueStudyPlot(swsFatigueStudy_DamagePlot)

    Set StudyMngr = ActDoc.StudyManager()
     If StudyMngr Is Nothing Then ErrorMsg SwApp, "Failed to get CWStudyManager object"

    ' Create random vibration fatigue study
     Debug.Print "Creating RandomVibrationFatigue study..."
     Set Study = StudyMngr.CreateNewStudy3("RandomVibrationFatigue", swsAnalysisStudyTypeFatigue, 3, errCode)
     If Study Is Nothing Then ErrorMsg SwApp, "Failed to create new study"

    errCode = Study.SetFatigueResultOptions(swsFatigueCalculationsOption_SurfaceOnly, Nothing)

    Set FatigueOptions = Study.FatigueStudyOptions
     If FatigueOptions Is Nothing Then ErrorMsg SwApp, "Failed to get CWFatigueStudyOptions object"
    Set FatigueEvent = FatigueOptions.AddFatigueEventForRandomVibration("Dynamic_Random_Vibration", 60, 0, errCode)

    Set SolidMgr = Study.SolidManager
     Set SolidComponent = SolidMgr.GetComponentAt(0, errCode)
     SName = SolidComponent.ComponentName
    Set SolidBody = SolidComponent.GetSolidBodyAt(0, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "No solid body"
    boolstatus = SolidBody.SetLibraryMaterial("C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\sldmaterials\solidworks materials.sldmat", "Ductile Iron (SN)")
     If boolstatus = False Then ErrorMsg SwApp, "No material applied"
    Set SolidMat = SolidBody.GetSolidBodyMaterial
    SolidMat.SNCurveSource = swsMaterialSNCurveSourceEquation
     SolidMat.SNCurveEstimateConstants = 0 ' Specify Basquin Equation constants, B and m
     SolidMat.SNCurveSpecificConstantBUnit = 3 ' N/mm^2
     SolidMat.SNCurveSpecificConstantB = 2E+20 ' B constant
     SolidMat.SNCurveSlopeM = 0.5 ' Slope m

    errCode = SolidBody.SetSolidBodyMaterial(SolidMat)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to apply material"

     FatigueOptions.RandomVibrationComputationalMethod = 0 ' Narrow Band computational method
    errCode = Study.RunAnalysis
     If errCode <> 0 Then ErrorMsg SwApp, "Narrow Band analysis failed with error code as defined in swsRunAnalysisError_e: " & errCode

    Set CWFeatObj = Study.Results
     If CWFeatObj Is Nothing Then ErrorMsg SwApp, "Failed to get CWResults object"

    ' Get minimum and maximum damage
     Damage = CWFeatObj.GetMinMaxFatigue(swsFatigueComponent_Damage, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to get Narrow Band minimum and maximum damage. Error code as defined in swsResultsError_e: " & errCode

    ' Compare maximum damage percentage with baseline and report errors
     If (Damage(3) < (1 - Tol) * DamageMax_NarrowBand) Or (Damage(3) > (1 + Tol) * DamageMax_NarrowBand) Then
         ErrorMsg SwApp, "Narrow Band damage % error = " & (((Damage(3) - DamageMax_NarrowBand) / DamageMax_NarrowBand) * 100)
     End If

     Debug.Print "Narrow Band computational method..."
     Debug.Print "  Minimum fatigue is " & Damage(1) & " at node " & Damage(0)
     Debug.Print "  Maximum fatigue is " & Damage(3) & " at node " & Damage(2)

     FatigueOptions.RandomVibrationComputationalMethod = 1 ' Steinberg computational method
     errCode = Study.RunAnalysis
     If errCode <> 0 Then ErrorMsg SwApp, "Steinberg analysis failed with error code as defined in swsRunAnalysisError_e: " & errCode

    Set CWFeatObj = Study.Results
     If CWFeatObj Is Nothing Then ErrorMsg SwApp, "Failed to get CWResults object"

    ' Get minimum and maximum damage
     Damage = CWFeatObj.GetMinMaxFatigue(swsFatigueComponent_Damage, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to get Steinberg minimum and maximum damage. Error code as defined in swsResultsError_e: " & errCode

    ' Compare maximum damage percentage with baseline and report errors
     If (Damage(3) < (1 - Tol) * DamageMax_Steinberg) Or (Damage(3) > (1 + Tol) * DamageMax_Steinberg) Then
         ErrorMsg SwApp, "Steinberg damage % error = " & (((Damage(3) - DamageMax_Steinberg) / DamageMax_Steinberg) * 100)
     End If

     FatigueOptions.RandomVibrationComputationalMethod = 2 ' Wirsching computational method
     errCode = Study.RunAnalysis
     If errCode <> 0 Then ErrorMsg SwApp, "Wirsching analysis failed with error code as defined in swsRunAnalysisError_e: " & errCode

    Set CWFeatObj = Study.Results
     If CWFeatObj Is Nothing Then ErrorMsg SwApp, "Failed to get CWResults object"

    ' Get minimum and maximum damage
     Damage = CWFeatObj.GetMinMaxFatigue(swsFatigueComponent_Damage, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to get Wirsching minimum and maximum damage. Error code as defined in swsResultsError_e: " & errCode

    ' Compare maximum damage percentage with baseline and report errors
     If (Damage(3) < (1 - Tol) * DamageMax_Wirsching) Or (Damage(3) > (1 + Tol) * DamageMax_Wirsching) Then
         ErrorMsg SwApp, "Wirsching damage % error = " & (((Damage(3) - DamageMax_Wirsching) / DamageMax_Wirsching) * 100)
     End If

End Sub
Sub ErrorMsg(SwApp As SldWorks.SldWorks, Message As String)
     SwApp.SendMsgToUser2 Message, 0, 0
     SwApp.RecordLine "'*** WARNING - General"
     SwApp.RecordLine "'*** " & Message
     SwApp.RecordLine ""
 End Sub
```
