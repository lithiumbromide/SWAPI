---
title: "Create Linear Dynamic Random Vibration Study Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Dynamic_Random_Vibration_Study_Example_VBNET.htm"
---

# Create Linear Dynamic Random Vibration Study Example (VB.NET)

This example shows how to create a linear dynamic study with a random vibration analysis and get some study options.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 '    (in the IDE, click Project > Add Reference > .NET >
 '    SolidWorks.Interop.cosworks > OK).
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
  '----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.cosworks
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()

         Dim Part As ModelDoc2
         Dim COSMOSWORKS As COSMOSWORKS
         Dim CWAddinCallBack As CwAddincallback
         Dim ActDoc As CWModelDoc
         Dim StudyMngr As CWStudyManager
         Dim Study As CWStudy
         Dim ShellMgr As CWShellManager
         Dim ShellMat As CWMaterial
         Dim LBCMgr As CWLoadsAndRestraintsManager
         Dim CWDistribMass As CWDistributedMass
         Dim DynStudyOptions As CWDynamicStudyOptions
         Dim CWBaseExcitationEntity As Object
         Dim CWDirectionEntity As Object
         Dim longstatus As Integer
         Dim longwarnings As Integer
         Dim errCode As Integer
         Dim boolstatus As Boolean
         Dim nStep As Integer
         Dim pDisp5 As Object
         Dim DispArray1(0) As Object
         Dim DispArray3(0) As Object
         Dim Disp As Object, Stress As Object, Velocity As Object, Acceleration As Object
         Dim sStudyName As String
         Dim ResultOptions As CWStudyResultOptions
         Dim DampingOptions As CWDampingOptions
         Dim DampingRatios(8) As Object
         Dim i As Integer
         Dim freqOption As Integer
         Dim freqValue As Double
         Dim bChecked As Integer
         Dim forces2 As Object
         Dim selectedAndModelReactionFM As Object = Nothing
         Dim selectedOnlyReactionFM As Object = Nothing
         Dim CWFeatObj1 As CWShell
         Dim CWFeatObj2 As CWPressure
         Dim CWFeatObj3 As CWRestraint
         Dim CWFeatObj4 As CWMesh
         Dim CWFeatObj5 As CWResults
         Dim param As Integer
         Dim dParam As Double
         Dim inRadius As Double
         Dim outRadius As Double

         'Tolerances and baselines
         Const MeshEleSize As Double = 26.5868077635828 'mm
         Const MeshTol As Double = 1.32934038817914 'mm

         'Open document
         Part = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\lineardynamic.SLDPRT", swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", longstatus, longwarnings)
         If Part Is Nothing Then ErrorMsg(SwApp, "Failed to open lineardynamic.SLDPRT")

         'Add-in callback
         CWAddinCallBack = SwApp.GetAddInObject("CosmosWorks.CosmosWorks")
         If CWAddinCallBack Is Nothing Then ErrorMsg(SwApp, "Failed to get CwAddincallback object")
         COSMOSWORKS = CWAddinCallBack.COSMOSWORKS
         If COSMOSWORKS Is Nothing Then ErrorMsg(SwApp, "Failed to get CosmosWorks object")

         'Get active document
         ActDoc = COSMOSWORKS.ActiveDoc()
         If ActDoc Is Nothing Then ErrorMsg(SwApp, "Failed to get active document")

         'Create a dynamic random vibration study
         StudyMngr = ActDoc.StudyManager()
         If StudyMngr Is Nothing Then ErrorMsg(SwApp, "Failed to get study manager object")

         sStudyName = "Dynamic_Random_Vibration"
         Study = StudyMngr.CreateNewStudy3(sStudyName, swsAnalysisStudyType_e.swsAnalysisStudyTypeDynamic, swsDynamicAnalysisSubType_e.swsDynamicAnalysisSubTypeRandom, errCode)

         Debug.Print("Linear dynamic study with random vibration analysis")
         Debug.Print("")
         Debug.Print("Study configuration name is " & Study.ConfigurationName)
         Debug.Print("Dynamic analysis subtype as defined in swsAnalysisStudyType_e is " & Study.DynamicAnalysisSubType)
         Debug.Print("Dynamic study options...")

         DynStudyOptions = Study.DynamicStudyOptions

         errCode = DynStudyOptions.GetFrequencyOption2(freqOption, freqValue)
         Debug.Print("  Frequency option (0=number of frequencies, 1=upper bound): " & freqOption)
         Debug.Print("  No. of frequencies or upper-bound frequency: " & freqValue)
         errCode = DynStudyOptions.GetFrequencyShiftOption2(bChecked, freqValue)
         Debug.Print("  Is frequency shift enabled (0=no, 1=yes)? " & bChecked)
         Debug.Print("  Frequency shift: " & freqValue)

         errCode = DynStudyOptions.SetIncompatibleBondingOption2(0) ' automatic
         errCode = DynStudyOptions.SetUseSoftSpring2(0) ' do not use soft springs to stabilize model
         errCode = DynStudyOptions.SetResultFolderPath2("c:\temp")

         DynStudyOptions.SolverType = 2 ' FFEPlus

         errCode = DynStudyOptions.GetRandomVibrationAnalysisMethod2(param)
         Debug.Print("  Analysis method as defined in swsRandomVibrationAnalysisMethod_e: " & param)
         errCode = DynStudyOptions.GetRandomVibrationBiasingParameter2(dParam)
         Debug.Print("  Biasing parameter: " & param)
         errCode = DynStudyOptions.GetRandomVibrationCorrelationOption2(param)
         Debug.Print("  Correlation option as defined in swsRandomVibrationCorrelationOption_e: " & param)
         errCode = DynStudyOptions.GetRandomVibrationCrossModeCutOffRatio2(dParam)
         Debug.Print("  Cross-mode cut-off ratio: " & param)
         errCode = DynStudyOptions.GetRandomVibrationFrequencyLowerLimit2(dParam)
         Debug.Print("  Operating frequency lower limit: " & param)
         errCode = DynStudyOptions.GetRandomVibrationFrequencyUnits2(param)
         Debug.Print("  Units of operating frequency as defined in swsFrequencyUnit_e: " & param)
         errCode = DynStudyOptions.GetRandomVibrationFrequencyUpperLimit2(dParam)
         Debug.Print("  Operating frequency upper limit: " & param)
         errCode = DynStudyOptions.GetRandomVibrationGaussIntegrationOrder2(param)
         Debug.Print("  Gauss integration order as defined in swsGaussIntegrationOrder_e: " & param)
         errCode = DynStudyOptions.GetRandomVibrationNoOfFrequencyPoints2(param)
         Debug.Print("  Number of frequency points: " & param)
         errCode = DynStudyOptions.GetRandomVibrationPartialCorrelationDetails2(param, inRadius, outRadius)
         Debug.Print("  Partially correlated units as defined in swsLinearUnit_e: " & param)
         Debug.Print("  Inside radius: " & inRadius)
         Debug.Print("  Outside radius: " & outRadius)

         Debug.Print("")

         'Set study result options
         Debug.Print("Study result options...")
         ResultOptions = Study.StudyResultOptions
         ResultOptions.SaveResultsForSolutionStepsOption = 1 ' save solution step results
         ResultOptions.SaveDisplacementsAndVelocitiesOption = 1 ' save displacements and velocities
         ResultOptions.SaveStresses = 1 ' save stresses
         'Solution step set #1
         errCode = ResultOptions.SetSolutionStepsSetInformation(1, 10, 100, 3)
         Debug.Print("  Set solution steps set #1 (10-100, inc=3)? (0=success): " & errCode)
         'Solution step set #3
         errCode = ResultOptions.SetSolutionStepsSetInformation(3, 100, 1000, 5)
         Debug.Print("  Set solution steps set #3 (100-1000, inc=5)? (0=success): " & errCode)
         Debug.Print("")

         'Set damping options
         DampingOptions = Study.DampingOptions
         DampingOptions.DampingType = 0 'Modal damping
         DampingRatios(0) = 1
         DampingRatios(1) = 5
         DampingRatios(2) = 3.45
         DampingRatios(3) = 6
         DampingRatios(4) = 15
         DampingRatios(5) = 15
         DampingRatios(6) = 16
         DampingRatios(7) = 25
         DampingRatios(8) = 34.5
         errCode = DampingOptions.SetDampingRatios(3, (DampingRatios))
         DampingOptions.ComputeFromMaterialDamping = 0 ' do not use the material damping ratio

         Dim PID As Object
         Dim SelObj As Object
         Dim obj As Object

         'Get face by persistent ID
         boolstatus = Part.Extension.SelectByID2("", "FACE", 0.367377178180561, 0.0153999999998859, -0.443699715030164, False, 0, Nothing, 0)
         obj = Part.SelectionManager.GetSelectedObject6(1, -1)
         PID = Part.Extension.GetPersistReference3(obj)
         SelObj = Part.Extension.GetObjectByPersistReference3((PID), errCode)
         DispArray1(0) = SelObj 'Face

         'Get edge by persistent ID
         boolstatus = Part.Extension.SelectByID2("", "EDGE", 0.473843326221299, 0.0160904480509885, -0.000690335842989498, False, 0, Nothing, 0)
         obj = Part.SelectionManager.GetSelectedObject6(1, -1)
         PID = Part.Extension.GetPersistReference3(obj)
         CWBaseExcitationEntity = Part.Extension.GetObjectByPersistReference3((PID), errCode)
         DispArray3(0) = CWBaseExcitationEntity 'Edge

         'Get Axis1 reference geometry by persistent ID
         boolstatus = Part.Extension.SelectByID2("Axis1", "AXIS", -0.0320045390890095, 0.0639408825367532, -0.0319259521004658, False, 0, Nothing, 0)
         obj = Part.SelectionManager.GetSelectedObject6(1, -1)
         PID = Part.Extension.GetPersistReference3(obj)
         CWDirectionEntity = Part.Extension.GetObjectByPersistReference3((PID), errCode)
         pDisp5 = CWDirectionEntity

         'Add materials
         ShellMgr = Study.ShellManager
         If ShellMgr Is Nothing Then ErrorMsg(SwApp, "Failed to get shell manager object")

         CWFeatObj1 = ShellMgr.GetShellAt(0, errCode)
         If errCode <> 0 Then ErrorMsg(SwApp, "Failed to get shell component")
         ShellMat = CWFeatObj1.GetDefaultMaterial
         ShellMat.MaterialUnits = 0
         Call ShellMat.SetPropertyByName("EX", 2000000000000.0#, 0)
         Call ShellMat.SetPropertyByName("NUXY", 0.25, 0)
         errCode = CWFeatObj1.SetShellMaterial(ShellMat)
         If errCode <> 0 Then ErrorMsg(SwApp, "Failed to apply material")

         Call CWFeatObj1.ShellBeginEdit()
         CWFeatObj1.Formulation = 1 ' thick shell
         CWFeatObj1.ShellUnit = 1 ' centimeters
         CWFeatObj1.ShellThickness = 5 ' 5 cm
         CWFeatObj1.ShellOffsetOption = 3 ' specify reference surface
         CWFeatObj1.ShellOffsetValue = 0.3
         errCode = CWFeatObj1.ShellEndEdit
         If errCode <> 0 Then ErrorMsg(SwApp, "Failed to create shell")
         CWFeatObj1 = Nothing

         'Get loads and restraints manager
         LBCMgr = Study.LoadsAndRestraintsManager
         If LBCMgr Is Nothing Then ErrorMsg(SwApp, "Failed to get loads and restraints manager")

         'Create normal pressure
         CWFeatObj2 = LBCMgr.AddPressure(swsPressureType_e.swsPressureTypeNormal, (DispArray1), Nothing, errCode)
         If errCode <> 0 Then ErrorMsg(SwApp, "Failed to create normal pressure")
         Call CWFeatObj2.PressureBeginEdit()
         Debug.Print("Normal pressure values...")
         Debug.Print("  Pressure unit in swsStrengthUnit_e units: " & CWFeatObj2.Unit)
         Debug.Print("  Pressure value: " & CWFeatObj2.Value)
         Debug.Print("  Pressure phase angle (-1 if not set): " & CWFeatObj2.PhaseAngle)
         Debug.Print("  Pressure phase angle unit in swsPhaseAngleUnit_e units: " & CWFeatObj2.PhaseAngleUnit)
         errCode = CWFeatObj2.PressureEndEdit
         If errCode <> 0 Then ErrorMsg(SwApp, "Failed to apply normal pressure value")
         CWFeatObj2 = Nothing
         Debug.Print(" ")

         'Add a restraint
         CWFeatObj3 = LBCMgr.AddRestraint(0, (DispArray3), pDisp5, errCode)
         If errCode <> 0 Then ErrorMsg(SwApp, "Failed to create restraint")
         Call CWFeatObj3.RestraintBeginEdit()
         Call CWFeatObj3.SetTranslationComponentsValues(0, 0, 1, 0.0#, 0.0#, 0.0#)
         Call CWFeatObj3.SetRotationComponentsValues(0, 0, 0, 0.0#, 0.0#, 0.0#)
         CWFeatObj3.Unit = 2
         errCode = CWFeatObj3.RestraintEndEdit
         If errCode <> 0 Then ErrorMsg(SwApp, "Restraint end-edit failed")

         'Create mesh
         CWFeatObj4 = Study.Mesh
         If CWFeatObj4 Is Nothing Then ErrorMsg(SwApp, "Failed to create mesh object")
         CWFeatObj4.MesherType = 0
         CWFeatObj4.Quality = 1

         errCode = Study.CreateMesh(0, MeshEleSize, MeshTol)
         If errCode <> 0 Then ErrorMsg(SwApp, "Failed to create mesh")
         Debug.Print("Worst Jacobian ratio for the mesh: " & CWFeatObj4.GetWorstJacobianRatio)
         Debug.Print("")

         'Add distributed mass
         CWDistribMass = LBCMgr.AddDistributedMass((DispArray1), 0, 1, errCode)
         Debug.Print("Total distributed mass: " & CWDistribMass.TotalMass)
         Debug.Print("  Units in swsUnitSystem_e units: " & CWDistribMass.Units)
         Debug.Print("")

         'Run analysis
         Debug.Print("Running the analysis")
         Debug.Print("")
         errCode = Study.RunAnalysis
         If errCode <> 0 Then ErrorMsg(SwApp, "Analysis failed with error code as defined in swsRunAnalysisError_e: " & errCode)

         'Get results
         CWFeatObj5 = Study.Results
         If CWFeatObj5 Is Nothing Then ErrorMsg(SwApp, "Failed to get results object")

         Debug.Print("Study results...")
         nStep = CWFeatObj5.GetMaximumAvailableSteps
         Debug.Print("  Maximum available steps: " & nStep)

         'Get algebraic minimum/maximum resultant displacements
         Disp = CWFeatObj5.GetMinMaxDisplacement(3, nStep, Nothing, 0, errCode)
         If errCode <> 0 Then ErrorMsg(SwApp, "Failed to get displacement results")
         Debug.Print("  Min/Max URES Resultant Displacements (Node, Min, Node, Max):")
         For i = 0 To UBound(Disp)
             Debug.Print("  * " & Disp(i))
         Next
         Debug.Print("")

         'Get algebraic minimum/maximum von Mises stresses
         Stress = CWFeatObj5.GetMinMaxStress(9, 0, nStep, Nothing, 3, errCode)
         If errCode <> 0 Then ErrorMsg(SwApp, "Failed to get stress results")
         Debug.Print("  Algebraic Min/Max von Mises Stresses (Node, Min, Node, Max):")
         For i = 0 To UBound(Stress)
             Debug.Print("  * " & Stress(i))
         Next
         Debug.Print("")

         'Get algebraic minimum/maximum velocities
         Velocity = CWFeatObj5.GetMinMaxVelocity(0, nStep, CWDirectionEntity, 0, errCode)
         If errCode <> 0 Then ErrorMsg(SwApp, "Failed to get velocity results")
         Debug.Print("  Algebraic Min/Max Velocities (Node, Min, Node, Max):")
         For i = 0 To UBound(Velocity)
             Debug.Print("  * " & Velocity(i))
         Next
         Debug.Print("")

         'Get algebraic minimum/maximum accelerations
         Acceleration = CWFeatObj5.GetMinMaxAcceleration(0, nStep, CWDirectionEntity, 0, errCode)
         If errCode <> 0 Then ErrorMsg(SwApp, "Failed to get acceleration results")
         Debug.Print("  Algebraic Min/Max Accelerations (Node, Min, Node, Max):")
         For i = 0 To UBound(Acceleration)
             Debug.Print("  * " & Acceleration(i))
         Next

         'Reaction forces and moments for entire model and selected face at solution step 40
         forces2 = CWFeatObj5.GetReactionForcesAndMomentsWithSelections(40, Nothing, swsForceUnit_e.swsForceUnitNOrNm, (DispArray1), selectedAndModelReactionFM, selectedOnlyReactionFM, errCode)
         If errCode <> 0 Then ErrorMsg(SwApp, "Failed to get reaction forces and moments")
         Debug.Print("  Reaction forces (N) and moments (N-m) for selected face ")
         Debug.Print("  {xcoord_force, ycoord_force, zcoord_force, resultant_force, ")
         Debug.Print("   xcoord_moment, ycoord_moment, zcoord_moment, resultant_moment}:")
         For i = 0 To UBound(selectedOnlyReactionFM)
             Debug.Print("  * " & selectedOnlyReactionFM(i))
         Next

     End Sub

     Sub ErrorMsg(ByVal SwApp As SldWorks, ByVal Message As String)
         SwApp.SendMsgToUser2(Message, 0, 0)
         SwApp.RecordLine("'*** WARNING - General")
         SwApp.RecordLine("'*** " & Message)
         SwApp.RecordLine("")
     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
