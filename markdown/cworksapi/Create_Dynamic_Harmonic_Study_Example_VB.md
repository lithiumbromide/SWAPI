---
title: "Create Linear Dynamic Study Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Dynamic_Harmonic_Study_Example_VB.htm"
---

# Create Linear Dynamic Study Example (VBA)

This example shows how to create a linear harmonic dynamic study.

NOTE: To get persistent reference identifiers (PIDs) for model selections, you can use [pidcollector.exe](GettingStarted-swsimulationapi.html) or IModelDocExtension::GetPersistReference3.

```vb
'----------------------------------------------------------------------------
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
 ' 2. Creates a linear harmonic dynamic study.
 ' 3. Runs an analysis.
 ' 4. Prints the study options and results to the Immediate window.
 ' 5. Saves the solution step, displacement, velocity,
 '    and stress result files to c:\temp.
 ' 6. Right-click the Stress1 or Displacement1 plot in the Results folder
 '    and click Show to plot the results in color in the graphics area.
 '
 ' NOTE: Because the model is used elsewhere, do not save any changes.
 '----------------------------------------------------------------------------
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
     Dim CWBaseExcitationU As CosmosWorksLib.CWBaseExcitation
     Dim CWDistribMass As CosmosWorksLib.CWDistributedMass
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
    'Create a dynamic harmonic study
     Set StudyMngr = ActDoc.StudyManager()
     If StudyMngr Is Nothing Then ErrorMsg SwApp, "Failed to get study manager object"
    sStudyName = "Dynamic_Harmonic"
     Set Study = StudyMngr.CreateNewStudy3(sStudyName, swsAnalysisStudyTypeDynamic, swsDynamicAnalysisSubTypeHarmonic, errCode)
    Debug.Print "Linear dynamic study with harmonic analysis"
     Debug.Print ""
     Debug.Print "Study configuration name is " & Study.ConfigurationName
     Debug.Print "Dynamic analysis subtype as defined in swsAnalysisStudyType_e is " & Study.DynamicAnalysisSubType
     Debug.Print "Dynamic study options..."
    Dim DynStudyOptions As CosmosWorksLib.CWDynamicStudyOptions
     Set DynStudyOptions = Study.DynamicStudyOptions
     Dim freqOption As Long
     Dim freqValue As Double
     Dim bChecked As Boolean
     errCode = DynStudyOptions.GetFrequencyOption2(freqOption, freqValue)
     Debug.Print "  Frequency option (0=number of frequencies, 1=upper bound): " & freqOption
     Debug.Print "  No. of frequencies or upper-bound frequency: " & freqValue
     errCode = DynStudyOptions.GetFrequencyShiftOption2(bChecked, freqValue)
     Debug.Print "  Is frequency shift enabled (0=no, 1=yes)? " & bChecked
     Debug.Print "  Frequency shift: " & freqValue
     errCode = DynStudyOptions.SetIncompatibleBondingOption2(0) ' automatic
     errCode = DynStudyOptions.SetUseSoftSpring3(0) ' do not use soft springs to stabilize model
     errCode = DynStudyOptions.SetResultFolderPath2("c:\temp")
     DynStudyOptions.SolverType = 2 ' FFEPlus
     Dim harmbandwidth As Double
     errCode = DynStudyOptions.GetHarmonicBandwidth2(harmbandwidth)
     Debug.Print "  Harmonic bandwidth: " & harmbandwidth
     Dim freqLowerLimit As Double
     errCode = DynStudyOptions.GetHarmonicFrequencyLowerLimit2(freqLowerLimit)
     Debug.Print "  Harmonic frequency lower limit: " & freqLowerLimit
     Dim freqUpperLimit As Double
     errCode = DynStudyOptions.GetHarmonicFrequencyUpperLimit2(freqUpperLimit)
     Debug.Print "  Harmonic frequency upper limit: " & freqUpperLimit
     Dim freqUnits As Long
     errCode = DynStudyOptions.GetHarmonicFrequencyUnits2(freqUnits)
     Debug.Print "  Harmonic frequency units (0=rad/sec, 1=Hz): " & freqUnits
     Dim interpolation As Long
     errCode = DynStudyOptions.GetHarmonicInterpolation2(interpolation)
     Debug.Print "  Harmonic interpolation (0=logarithmic, 1=linear): " & interpolation
     Dim points As Long
     errCode = DynStudyOptions.GetHarmonicNoOfPoints2(points)
     Debug.Print "  Harmonic number of points for each frequency: " & points
     Debug.Print ""

    'Set study result options
     Debug.Print "Study result options..."
     Set ResultOptions = Study.StudyResultOptions
     ResultOptions.SaveResultsForSolutionStepsOption = 1 ' save solution step results
     ResultOptions.SaveDisplacementsAndVelocitiesOption = 1 ' save displacements and velocities
     boolstatus = ResultOptions.SetSaveStressAndReactionsOptions2(-1, 0) ' save stresses and reactions for all stress components
     'Solution step set #1
     errCode = ResultOptions.SetSolutionStepsSetInformation(1, 10, 100, 3)
     Debug.Print "  Set solution steps set #1 (10-100, inc=3)? (0=success): " & errCode
     'Solution step set #3
     errCode = ResultOptions.SetSolutionStepsSetInformation(3, 100, 1000, 5)
     Debug.Print "  Set solution steps set #3 (100-1000, inc=5)? (0=success): " & errCode
     Debug.Print ""

    'Set damping options
     Set DampingOptions = Study.DampingOptions
     DampingOptions.DampingType = 0 'modal damping
     DampingOptions.ComputeFromMaterialDamping2 = 0 ' do not use material damping ratios
     DampingOptions.ClearAllDampingRatios
     DampingRatios = Array(1, 5, 3.45, 6, 15, 15, 16, 25, 34.5)
     errCode = DampingOptions.SetDampingRatios(3, (DampingRatios))

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
    Dim CWFeatObj1 As CosmosWorksLib.CWShell
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
     If LBCMgr Is Nothing Then ErrorMsg SwApp, "Failed to get loads and restraints manager."
    'Create normal pressure
     Dim CWFeatObj2 As CosmosWorksLib.CWPressure
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
     Dim CWFeatObj3 As CosmosWorksLib.CWRestraint
     Set CWFeatObj3 = LBCMgr.AddRestraint(0, (DispArray3), pDisp5, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to create restraint"
     Call CWFeatObj3.RestraintBeginEdit
     Call CWFeatObj3.SetTranslationComponentsValues(0, 0, 1, 0#, 0#, 0#)
     Call CWFeatObj3.SetRotationComponentsValues(0, 0, 0, 0#, 0#, 0#)
     CWFeatObj3.Unit = 2
     errCode = CWFeatObj3.RestraintEndEdit
     If errCode <> 0 Then ErrorMsg SwApp, "Restraint end-edit failed"
    'Add uniform base excitation
     Set CWBaseExcitationU = LBCMgr.AddUniformBaseExcitation2(swsBaseExcitationType_Acceleration, CWBaseExcitationEntity, swsAccelerationUnit_InchesPerSquareSec, -1, 2.3, -1, 3.4, -1, 4.5, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Adding uniform base excitation failed"
    Debug.Print "Uniform base excitation type (0=Disp, 1=Vel, 2=Acc): " & CWBaseExcitationU.BaseExcitationType
     Dim bdir1 As Long, bdir2 As Long, bdir3 As Long, bang As Long
    CWBaseExcitationU.GetExcitationDirections2 bdir1, bdir2, bdir3
     Debug.Print " Excitation in..."
     Debug.Print "   Direction 1 (-1=true)? " & bdir1
     Debug.Print "   Direction 2 (-1=true)? " & bdir2
     Debug.Print "   Direction 3 (-1=true)? " & bdir3
     Dim dval1 As Double, dval2 As Double, dval3 As Double
     CWBaseExcitationU.GetExcitationDirectionValues dval1, dval2, dval3
     CWBaseExcitationU.GetExcitationReverseDirections2 bdir1, bdir2, bdir3, bang
     Debug.Print " Excitation values..."
     Debug.Print " Units as defined in swsAccelerationUnit_e: " & CWBaseExcitationU.Unit
     Debug.Print "   Direction 1: " & dval1
     Debug.Print "     Reversed? (-1=true) " & bdir1
     Debug.Print "   Direction 2: " & dval2
     Debug.Print "     Reversed? (-1=true) " & bdir2
     Debug.Print "   Direction 3: " & dval3
     Debug.Print "     Reversed? (-1=true) " & bdir3
     Debug.Print "   Phase angle (-1 if not set): " & CWBaseExcitationU.PhaseAngle
     Debug.Print "     Reversed? (-1=true) " & bang
     Debug.Print "     Units as defined in swsPhaseAngleUnit_e: " & CWBaseExcitationU.PhaseAngleUnit
    Dim curveData As Variant
     curveData = CWBaseExcitationU.GetTimeOrFrequencyCurve 'variation with frequency data
     Debug.Print " Acceleration excitation variation with frequency data"
     Debug.Print " (number of points, x1, y1, x2, y2...xn, yn):"
     For i = 0 To UBound(curveData)
         Debug.Print ("  * " & curveData(i))
     Next
    Debug.Print ""
    'Add distributed mass
     Set CWDistribMass = LBCMgr.AddDistributedMass((DispArray1), 0, 1, errCode)
     Debug.Print "Total distributed mass: " & CWDistribMass.TotalMass
     Debug.Print "  Units in swsUnitSystem_e units: " & CWDistribMass.Units
     Debug.Print ""
    'Create mesh
     Dim CWFeatObj4 As CosmosWorksLib.CWMesh
     Set CWFeatObj4 = Study.Mesh
     If CWFeatObj4 Is Nothing Then ErrorMsg SwApp, "Failed to create mesh object"
     CWFeatObj4.MesherType = 0
     CWFeatObj4.Quality = 1
    errCode = Study.CreateMesh(0, MeshEleSize, MeshTol)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to create mesh"
     Debug.Print "Worst Jacobian ratio for the mesh: " & CWFeatObj4.GetWorstJacobianRatio
     Debug.Print ""
    'Run analysis
     Debug.Print "Running the analysis"
     Debug.Print ""
     errCode = Study.RunAnalysis
     If errCode <> 0 Then ErrorMsg SwApp, "Analysis failed with error code as defined in swsRunAnalysisError_e: " & errCode
    'Get results
     Dim CWFeatObj5 As CosmosWorksLib.CWResults
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
    Dim forces2 As Variant
     Dim selectedAndModelReactionFM As Variant
     Dim selectedOnlyReactionFM As Variant
     ' Reaction forces and moments for entire model and selected face at solution step 59
     forces2 = CWFeatObj5.GetReactionForcesAndMomentsWithSelections(59, Nothing, swsForceUnitNOrNm, (DispArray1), selectedAndModelReactionFM, selectedOnlyReactionFM, errCode)
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
