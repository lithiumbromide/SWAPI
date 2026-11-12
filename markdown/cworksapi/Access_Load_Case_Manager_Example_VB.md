---
title: "Access Load Case Manager Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Access_Load_Case_Manager_Example_VB.htm"
---

# Access Load Case Manager Example (VBA)

This example shows how to access the Load Case Manager to define load cases and load case combinations.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click  Tools > References > SOLIDWORKS Simulation version type library).
 ' 3. Ensure that the specified model exists.
 '
 ' Postconditions:
 ' 1. Gets the Ready study.
 ' 2. Opens the Load Case Manager.
 ' 3. Adds primary load cases and load case combinations.
 ' 4. Analyzes Ready using all primary load cases and load case combinations.
 ' 5. Creates a results displacement plot.
 ' 6. Click on each primary load case and load case combination in the
 '    Results View tab of the Load Case Manager. Inspect the result data
 '    in the graphics area after each click.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 ' ---------------------------------------------------------------------------
 Option Explicit
Dim SwApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim COSMOSWORKS As CosmosWorksLib.COSMOSWORKS
 Dim CWAddinCallBack As CosmosWorksLib.CWAddinCallBack
 Dim ActDoc As CosmosWorksLib.CWModelDoc
 Dim StudyMngr As CosmosWorksLib.CWStudyManager
 Dim Study As CosmosWorksLib.CWStudy
Dim CWMesh As CosmosWorkLib.CWMesh
 Dim LoadCaseManager As CosmosWorksLib.CWLoadCaseManager
 Dim CWResult As CosmosWorksLib.CWResults
 Dim CWCFf As CosmosWorksLib.CWPlot
 Dim bLoaded As Long
 Dim errCode As Long
 Dim longstatus As Long, longwarnings As Long
 Dim bSuccess As Boolean
 Dim PrimaryCases As Variant, SecondaryCases As Variant
 Dim varBOOLVals As Variant, varLoadVals As Variant
 Dim varRetBOOLVals As Variant, varRetLoadVals As Variant
 Dim strCombination As String, retStrCombination As String
Dim e1 As Double, t1 As Double

Sub main()
     Set SwApp = Application.SldWorks

     Set Part = SwApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2024\samples\Simulation Examples
 \Tutor1.sldprt", swDocPART, 1, "", longstatus, longwarnings)
     If Part Is Nothing Then ErrorMsg SwApp, "Failed to open Tutor1.sldprt"
     Set CWAddinCallBack = SwApp.GetAddInObject("CosmosWorks.CosmosWorks")
     If CWAddinCallBack Is Nothing Then ErrorMsg SwApp, "Simulation add-in not loaded"
     Set COSMOSWORKS = CWAddinCallBack.COSMOSWORKS
     If COSMOSWORKS Is Nothing Then ErrorMsg SwApp, "No COSMOSWORKS object"

     Set ActDoc = COSMOSWORKS.ActiveDoc()
     If ActDoc Is Nothing Then ErrorMsg SwApp, "No active document"
     Set StudyMngr = ActDoc.StudyManager()
     If StudyMngr Is Nothing Then ErrorMsg SwApp, "No CWStudyManager object"
     Set Study = StudyMngr.GetStudy(0)
     StudyMngr.ActiveStudy = 0
     If Study Is Nothing Then ErrorMsg SwApp, "No study"

     Set LoadCaseManager = Study.LoadCaseManager()
     If LoadCaseManager Is Nothing Then ErrorMsg SwApp, "No CWLoadCaseManager object"

     bSuccess = LoadCaseManager.OpenLoadCaseManager()
```

Dim StudyOptions As CosmosWorksLib.CWStaticStudyOptions

Set StudyOptions = Study.**StaticStudyOptions**

StudyOptions.**AdaptiveMethodType** = 2

StudyOptions.**PAdaptiveConvergenceCriteria** = 0

StudyOptions.**PAdaptiveErrorLimit** = 1#

StudyOptions.**PAdaptiveMaxIterations** = 4

StudyOptions.**PAdaptiveMaxPOrder** = 5

StudyOptions.**PAdaptiveStartingPOrder** = 2

StudyOptions.**PAdaptiveStrainEnergyErrorLimit** = 2#

StudyOptions.**IncludeRemarkInReport** = 1

StudyOptions.**RemarkComment** = "Remark comment"

StudyOptions.**NoPenetration** = 1

StudyOptions.**IgnoreClearanceForSurfaceContact** = 1

StudyOptions.**IncompatibleBondingOption** = swsIncompatibleBondingOption_Automatic

StudyOptions.**IncludeGlobalFriction** = 1

StudyOptions.**FrictionCoefficient** = 0.5

'Mesh

Set CWMesh = Study.**Mesh**

CWMesh.**Quality** = 1

CWMesh.**GetDefaultElementSizeAndTolerance** 0, el, tl

errCode = Study.**CreateMesh**(0, el, tl)

'Run analysis

errCode = Study.**RunAnalysis**

'Get results

Set CWResult = Study.**Results**

```vb
     bSuccess = LoadCaseManager.AddNewPrimaryLoadCase("My Load Case1")
     If bSuccess = False Then ErrorMsg SwApp, "Primary load case not created"
     bSuccess = LoadCaseManager.AddNewPrimaryLoadCase("My Load Case2")
     If bSuccess = False Then ErrorMsg SwApp, "Primary load case not created"
     bSuccess = LoadCaseManager.AddNewPrimaryLoadCase("My Load Case3")
     If bSuccess = False Then ErrorMsg SwApp, "Primary load case not created"

     bSuccess = LoadCaseManager.DeletePrimaryLoadCase("My Load Case3")
     If bSuccess = False Then ErrorMsg SwApp, "Primary load case not deleted"

     bSuccess = LoadCaseManager.SuppressOrUnSuppressPrimaryLoadCase("My Load Case2", True)
     If bSuccess = False Then ErrorMsg SwApp, "Primary load case not suppressed"

     bSuccess = LoadCaseManager.SuppressOrUnSuppressPrimaryLoadCase("My Load Case2", False)
     If bSuccess = False Then ErrorMsg SwApp, "Primary load case not unsuppressed"

     bSuccess = LoadCaseManager.RenamePrimaryLoadCase("My Load Case2", "Live Load2")
     If bSuccess = False Then ErrorMsg SwApp, "Primary load case not renamed"

     varBOOLVals = Array(False)
     varLoadVals = Array(3.5)
     errCode = LoadCaseManager.SetLoadDataForPrimaryLoadCase("My Load Case1", "Pressure-1", (varBOOLVals), (varLoadVals))
     If errCode > 0 Then ErrorMsg SwApp, "Load data of Pressure-1 not applied to My Load Case1"

     varBOOLVals = Array(True)
     varLoadVals = Array(-1)
     errCode = LoadCaseManager.SetLoadDataForPrimaryLoadCase("My Load Case1", "Restraint-1", (varBOOLVals), (varLoadVals))
     If errCode > 0 Then ErrorMsg SwApp, "Load data of Restraint-1 not applied to My Load Case1"

     varBOOLVals = Array(False)
     varLoadVals = Array(-1)
     errCode = LoadCaseManager.SetLoadDataForPrimaryLoadCase("My Load Case1", "Restraint-1", (varBOOLVals), (varLoadVals))
     If errCode > 0 Then ErrorMsg SwApp, "Load data of Restraint-1 not applied to My Load Case1"

     varBOOLVals = Array(False)
     varLoadVals = Array(6.5)
     errCode = LoadCaseManager.SetLoadDataForPrimaryLoadCase("Live Load2", "Pressure-1", (varBOOLVals), (varLoadVals))
     If errCode > 0 Then ErrorMsg SwApp, "Load data of Pressure-1 not applied to Live Load2"

     varRetLoadVals = LoadCaseManager.GetLoadDataForPrimaryLoadCase("Live Load2", "Pressure-1", varRetBOOLVals)

     strCombination = """My Load Case1"" + ""Live Load2"""
     errCode = LoadCaseManager.AddNewLoadCaseCombination("Load Case Combination1", strCombination)
     If errCode > 0 Then ErrorMsg SwApp, "Load Case Combination1 not added"

     strCombination = "2*(sin(30)*""My Load Case1""*(1 + 1) + (4 - 2)*""Live Load2""*cos(60))"
     errCode = LoadCaseManager.AddNewLoadCaseCombination("Load Case Combination2", strCombination)
     If errCode > 0 Then ErrorMsg SwApp, "Load Case Combination2 not added"

     strCombination = """My Load Case1"" + ""Live Load2"""
     errCode = LoadCaseManager.AddNewLoadCaseCombination("Load Case Combination3", strCombination)
     If errCode > 0 Then ErrorMsg SwApp, "Load Case Combination3 not added"

     strCombination = """My Load Case1"" + ""Live Load2"""
     errCode = LoadCaseManager.AddNewLoadCaseCombination("Load Case Combination4", strCombination)
     If errCode > 0 Then ErrorMsg SwApp, "Load Case Combination4 not added"

     bSuccess = LoadCaseManager.DeleteLoadCaseCombination("Load Case Combination3")
     If bSuccess = False Then ErrorMsg SwApp, "Load Case Combination3 not deleted"

     bSuccess = LoadCaseManager.DeleteLoadCaseCombination("Load Case Combination4")
     If bSuccess = False Then ErrorMsg SwApp, "Load Case Combination4 cannot be deleted"

     strCombination = """My Load Case1"" + ""Live Load2"""
     errCode = LoadCaseManager.AddNewLoadCaseCombination("Load Case Combination3", strCombination)
     If errCode > 0 Then ErrorMsg SwApp, "Load Case Combination3 not added"

     bSuccess = LoadCaseManager.SuppressOrUnSuppressLoadCaseCombination("Load Case Combination2", True)
     If bSuccess = False Then ErrorMsg SwApp, "Load Case Combination2 not suppressed"

     bSuccess = LoadCaseManager.SuppressOrUnSuppressLoadCaseCombination("Load Case Combination2", False)
     If bSuccess = False Then ErrorMsg SwApp, "Load Case Combination2 not unsuppressed"

     bSuccess = LoadCaseManager.SuppressOrUnSuppressLoadCaseCombination("Load Case Combination3", True)
     If bSuccess = False Then ErrorMsg SwApp, "Load Case Combination3 not suppressed"

     bSuccess = LoadCaseManager.RenameLoadCaseCombination("Load Case Combination2", "My Combination2")
     If bSuccess = False Then ErrorMsg SwApp, "Load Case Combination2 not renamed"

     bSuccess = LoadCaseManager.RenameLoadCaseCombination("My Combination2", "Load Case Combination2")
     If bSuccess = False Then ErrorMsg SwApp, "Load Case Combination2 not renamed"

     strCombination = """My Load Case1"" * ""Live Load2"""
     errCode = LoadCaseManager.SetEquationForLoadCaseCombination("Load Case Combination1", strCombination)
     If errCode = 0 Then ErrorMsg SwApp, "Load Case Combination1 equation not set"

     strCombination = "(""My Load Case1""*2 + ""Live Load2""*2)/2"
     errCode = LoadCaseManager.SetEquationForLoadCaseCombination("Load Case Combination1", strCombination)
     If errCode > 0 Then ErrorMsg SwApp, "Load Case Combination1 equation not set"

     retStrCombination = LoadCaseManager.GetEquationForLoadCaseCombination("Load Case Combination1")
     errCode = StrComp(retStrCombination, strCombination)
     If errCode < 0 Or errCode > 0 Then ErrorMsg SwApp, "Load Case Combination1 equation not returned"

     PrimaryCases = LoadCaseManager.GetAllPrimaryLoadCaseNames()
     SecondaryCases = LoadCaseManager.GetAllLoadCaseCombinationNames()

     errCode = LoadCaseManager.RunLoadCases(True, True)
     If errCode > 0 Then ErrorMsg SwApp, "Load cases failed to run"

     LoadCaseManager.ShowLoadCaseViewTab

     bSuccess = LoadCaseManager.ShowResultsViewTab()
     If bSuccess = False Then ErrorMsg SwApp, "Cannot display Results View tab"

     bSuccess = LoadCaseManager.LoadResultsOfPrimaryLoadCase("My Load Case1")
     If bSuccess = False Then ErrorMsg SwApp, "My Load Case1 results not loaded"

     Set CWResult = Study.Results
     If CWResult Is Nothing Then ErrorMsg SwApp, "No CWResults object"

     Set CWCFf = CWResult.CreatePlot(swsResultDisplacementOrAmplitude, swsStaticDisplacement_URES, swsUnitSI, False, errCode)

     bSuccess = LoadCaseManager.LoadResultsOfPrimaryLoadCase("Live Load2")
     If bSuccess = False Then ErrorMsg SwApp, "Live Load2 results not loaded"

     bSuccess = LoadCaseManager.LoadResultsOfLoadCaseCombination("Load Case Combination1")
     If bSuccess = False Then ErrorMsg SwApp, "Load Case Combination1 results not loaded"

     bSuccess = LoadCaseManager.LoadResultsOfLoadCaseCombination("Load Case Combination2")
     If bSuccess = False Then ErrorMsg SwApp, "Load Case Combination2 results not loaded"

     'LoadCaseManager.CloseLoadCaseManager
     'LoadCaseManager.DeleteAllDataAndClose
End Sub

Sub ErrorMsg(SwApp As SldWorks.SldWorks, Message As String)
     SwApp.SendMsgToUser2 Message, 0, 0
     SwApp.RecordLine "'*** WARNING - General"
     SwApp.RecordLine "'*** " & Message
     SwApp.RecordLine ""
 End Sub
```
