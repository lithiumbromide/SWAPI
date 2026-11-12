---
title: "Access Load Case Manager Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Access_Load_Case_Manager_Example_VBNET.htm"
---

# Access Load Case Manager Example (VB.NET)

This example shows how to access the Load Case Manager to define load cases and load case combinations.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 '    (in the IDE, click Project > Add Reference > .NET >
 '    SolidWorks.Interop.cosworks > OK).
 ' 3. Ensure that the specified model exists.
 '
 ' Postconditions:
 ' 1. Gets the Ready study.
 ' 2. Opens the Load Case Manager.
  ' 3. Adds primary load cases and load case combinations.
 ' 4. Analyzes Ready using all primary load cases and load case combinations.
 ' 5. Creates a results displacement plot.
  ' 6. Click each primary load case and load case combination in the
  '    Results View tab of the Load Case Manager. Inspect the result data
 '    in the graphics area after each click.
 '
  ' NOTE: Because the model is used elsewhere, do not save changes.
  ' ---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.cosworks
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Dim Part As ModelDoc2
     Dim COSMOSWORKS As CosmosWorks
     Dim CWAddinCallBack As CwAddincallback
     Dim ActDoc As CWModelDoc
     Dim StudyMngr As CWStudyManager
     Dim Study As CWStudy
     Dim LoadCaseManager As CWLoadCaseManager
     Dim CWResult As CWResults
    Dim CWMesh As CWMesh
     Dim CWCFf As CWPlot

     Dim errCode As Integer
     Dim longstatus As Integer
     Dim longwarnings As Integer

     Dim bSuccess As Boolean

     Dim PrimaryCases As Object
     Dim SecondaryCases As Object
     Dim varBOOLVals As Object() = New Object(0) {}
     Dim varLoadVals As Object() = New Object(0) {}
     Dim varRetBOOLVals As Object() = New Object(0) {}
     Dim varRetLoadVals As Object() = New Object(0) {}
     Dim strCombination As String
     Dim retStrCombination As String
      Dim e1 As Double, t1 As Double

     Sub main()

         Part = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2024\samples\Simulation Examples\Tutor1.sldprt", swDocumentTypes_e.swDocPART, 1, "", longstatus, longwarnings)
         If Part Is Nothing Then ErrorMsg(SwApp, "Failed to open Tutor1.sldprt")

         CWAddinCallBack = SwApp.GetAddInObject("CosmosWorks.CosmosWorks")
         If CWAddinCallBack Is Nothing Then ErrorMsg(SwApp, "Simulation add-in not loaded")
         COSMOSWORKS = CWAddinCallBack.COSMOSWORKS
         If COSMOSWORKS Is Nothing Then ErrorMsg(SwApp, "No COSMOSWORKS object")

         ActDoc = COSMOSWORKS.ActiveDoc()
         If ActDoc Is Nothing Then ErrorMsg(SwApp, "No active document")

         StudyMngr = ActDoc.StudyManager()
         If StudyMngr Is Nothing Then ErrorMsg(SwApp, "No CWStudyManager object")
         Study = StudyMngr.GetStudy(0)
         StudyMngr.ActiveStudy = 0
         If Study Is Nothing Then ErrorMsg(SwApp, "No study")

         LoadCaseManager = Study.LoadCaseManager()
         If LoadCaseManager Is Nothing Then ErrorMsg(SwApp, "No Load Case Manager")

         bSuccess = LoadCaseManager.OpenLoadCaseManager()
```

Dim StudyOptions As CWStaticStudyOptions

StudyOptions = Study.**StaticStudyOptions**

StudyOptions.**AdaptiveMethodType** = 2

StudyOptions.**PAdaptiveConvergenceCriteria** = 0

StudyOptions.**PAdaptiveErrorLimit** = 1.0

StudyOptions.**PAdaptiveMaxIterations** = 4

StudyOptions.**PAdaptiveMaxPOrder** = 5

StudyOptions.**PAdaptiveStartingPOrder** = 2

StudyOptions.**PAdaptiveStrainEnergyErrorLimit** = 2.0

StudyOptions.**IncludeRemarkInReport** = 1

StudyOptions.**RemarkComment** = "Remark comment"

StudyOptions.**NoPenetration** = 1

StudyOptions.**IgnoreClearanceForSurfaceContact** = 1

StudyOptions.**IncompatibleBondingOption** = swsIncompatibleBondingOption_Automatic

StudyOptions.**IncludeGlobalFriction** = 1

StudyOptions.**FrictionCoefficient** = 0.5

'Mesh

CWMesh = Study.**Mesh**

CWMesh.**Quality** = 1

CWMesh.**GetDefaultElementSizeAndTolerance**(0, el, tl)

errCode = Study.**CreateMesh**(0, el, tl)

'Run analysis

errCode = Study.**RunAnalysis**

'Get results

CWResult = Study.**Results**

```vb
         bSuccess = LoadCaseManager.AddNewPrimaryLoadCase("My Load Case1")
         If bSuccess = False Then ErrorMsg(SwApp, "Primary load case not created")
         bSuccess = LoadCaseManager.AddNewPrimaryLoadCase("My Load Case2")
         If bSuccess = False Then ErrorMsg(SwApp, "Primary load case not created")
         bSuccess = LoadCaseManager.AddNewPrimaryLoadCase("My Load Case3")
         If bSuccess = False Then ErrorMsg(SwApp, "Primary load case not created")

         bSuccess = LoadCaseManager.DeletePrimaryLoadCase("My Load Case3")
         If bSuccess = False Then ErrorMsg(SwApp, "Primary load case not deleted")

         bSuccess = LoadCaseManager.SuppressOrUnSuppressPrimaryLoadCase("My Load Case2", True)
         If bSuccess = False Then ErrorMsg(SwApp, "Primary load case not suppressed")

         bSuccess = LoadCaseManager.SuppressOrUnSuppressPrimaryLoadCase("My Load Case2", False)
         If bSuccess = False Then ErrorMsg(SwApp, "Primary load case not unsuppressed")

         bSuccess = LoadCaseManager.RenamePrimaryLoadCase("My Load Case2", "Live Load2")
         If bSuccess = False Then ErrorMsg(SwApp, "Primary load case not renamed")

         varBOOLVals(0) = False
         varLoadVals(0) = 3.5
         errCode = LoadCaseManager.SetLoadDataForPrimaryLoadCase("My Load Case1", "Pressure-1", (varBOOLVals), (varLoadVals))
         If errCode > 0 Then ErrorMsg(SwApp, "Load data of Pressure-1 not applied to My Load Case1")

         varBOOLVals(0) = True
         varLoadVals(0) = -1
         errCode = LoadCaseManager.SetLoadDataForPrimaryLoadCase("My Load Case1", "Restraint-1", (varBOOLVals), (varLoadVals))
         If errCode > 0 Then ErrorMsg(SwApp, "Load data of Restraint-1 not applied to My Load Case1")

         varBOOLVals(0) = False
         varLoadVals(0) = -1
         errCode = LoadCaseManager.SetLoadDataForPrimaryLoadCase("My Load Case1", "Restraint-1", (varBOOLVals), (varLoadVals))
         If errCode > 0 Then ErrorMsg(SwApp, "Load data of Restraint-1 not applied to My Load Case1")

         varBOOLVals(0) = False
         varLoadVals(0) = 6.5
         errCode = LoadCaseManager.SetLoadDataForPrimaryLoadCase("Live Load2", "Pressure-1", (varBOOLVals), (varLoadVals))
         If errCode > 0 Then ErrorMsg(SwApp, "Load data of Pressure-1 not applied to Live Load2")

         varRetLoadVals = LoadCaseManager.GetLoadDataForPrimaryLoadCase("Live Load2", "Pressure-1", varRetBOOLVals(0))

         strCombination = """My Load Case1"" + ""Live Load2"""
         errCode = LoadCaseManager.AddNewLoadCaseCombination("Load Case Combination1", strCombination)
         If errCode > 0 Then ErrorMsg(SwApp, "Load Case Combination1 not added")

         strCombination = "2*(sin(30)*""My Load Case1""*(1 + 1) + (4 - 2)*""Live Load2""*cos(60))"
         errCode = LoadCaseManager.AddNewLoadCaseCombination("Load Case Combination2", strCombination)
         If errCode > 0 Then ErrorMsg(SwApp, "Load Case Combination2 not added")

         strCombination = """My Load Case1"" + ""Live Load2"""
         errCode = LoadCaseManager.AddNewLoadCaseCombination("Load Case Combination3", strCombination)
         If errCode > 0 Then ErrorMsg(SwApp, "Load Case Combination3 not added")

         strCombination = """My Load Case1"" + ""Live Load2"""
         errCode = LoadCaseManager.AddNewLoadCaseCombination("Load Case Combination4", strCombination)
         If errCode > 0 Then ErrorMsg(SwApp, "Load Case Combination4 not added")

         bSuccess = LoadCaseManager.DeleteLoadCaseCombination("Load Case Combination3")
         If bSuccess = False Then ErrorMsg(SwApp, "Load Case Combination3 not deleted")

         bSuccess = LoadCaseManager.DeleteLoadCaseCombination("Load Case Combination4")
         If bSuccess = False Then ErrorMsg(SwApp, "Load Case Combination4 cannot be deleted")

         strCombination = """My Load Case1"" + ""Live Load2"""
         errCode = LoadCaseManager.AddNewLoadCaseCombination("Load Case Combination3", strCombination)
         If errCode > 0 Then ErrorMsg(SwApp, "Load Case Combination3 not added")

         bSuccess = LoadCaseManager.SuppressOrUnSuppressLoadCaseCombination("Load Case Combination2", True)
         If bSuccess = False Then ErrorMsg(SwApp, "Load Case Combination2 not suppressed")

         bSuccess = LoadCaseManager.SuppressOrUnSuppressLoadCaseCombination("Load Case Combination2", False)
         If bSuccess = False Then ErrorMsg(SwApp, "Load Case Combination2 not unsuppressed")

         bSuccess = LoadCaseManager.SuppressOrUnSuppressLoadCaseCombination("Load Case Combination3", True)
         If bSuccess = False Then ErrorMsg(SwApp, "Load Case Combination3 not suppressed")

         bSuccess = LoadCaseManager.RenameLoadCaseCombination("Load Case Combination2", "My Combination2")
         If bSuccess = False Then ErrorMsg(SwApp, "Load Case Combination2 not renamed")

         bSuccess = LoadCaseManager.RenameLoadCaseCombination("My Combination2", "Load Case Combination2")
         If bSuccess = False Then ErrorMsg(SwApp, "Load Case Combination2 not renamed")

         strCombination = """My Load Case1"" * ""Live Load2"""
         errCode = LoadCaseManager.SetEquationForLoadCaseCombination("Load Case Combination1", strCombination)
         If errCode = 0 Then ErrorMsg(SwApp, "Load Case Combination1 equation not set")

         strCombination = "(""My Load Case1""*2 + ""Live Load2""*2)/2"
         errCode = LoadCaseManager.SetEquationForLoadCaseCombination("Load Case Combination1", strCombination)
         If errCode > 0 Then ErrorMsg(SwApp, "Load Case Combination1 equation not set")

         retStrCombination = LoadCaseManager.GetEquationForLoadCaseCombination("Load Case Combination1")
         errCode = StrComp(retStrCombination, strCombination)
         If errCode < 0 Or errCode > 0 Then ErrorMsg(SwApp, "Load Case Combination1 equation not returned")

         PrimaryCases = LoadCaseManager.GetAllPrimaryLoadCaseNames()
         SecondaryCases = LoadCaseManager.GetAllLoadCaseCombinationNames()

         errCode = LoadCaseManager.RunLoadCases(True, True)
         If errCode > 0 Then ErrorMsg(SwApp, "Load cases failed to run")

         LoadCaseManager.ShowLoadCaseViewTab()

         bSuccess = LoadCaseManager.ShowResultsViewTab()
         If bSuccess = False Then ErrorMsg(SwApp, "Cannot display Results View tab")

         bSuccess = LoadCaseManager.LoadResultsOfPrimaryLoadCase("My Load Case1")
         If bSuccess = False Then ErrorMsg(SwApp, "My Load Case1 results not loaded")

         CWResult = Study.Results
         If CWResult Is Nothing Then ErrorMsg(SwApp, "No CWResults object")

         CWCFf = CWResult.CreatePlot(swsPlotResultTypes_e.swsResultDisplacementOrAmplitude, swsStaticResultDisplacementComponentTypes_e.swsStaticDisplacement_URES, swsUnit_e.swsUnitSI, False, errCode)

         bSuccess = LoadCaseManager.LoadResultsOfPrimaryLoadCase("Live Load2")
         If bSuccess = False Then ErrorMsg(SwApp, "Live Load2 results not loaded")

         bSuccess = LoadCaseManager.LoadResultsOfLoadCaseCombination("Load Case Combination1")
         If bSuccess = False Then ErrorMsg(SwApp, "Load Case Combination1 results not loaded")

         bSuccess = LoadCaseManager.LoadResultsOfLoadCaseCombination("Load Case Combination2")
         If bSuccess = False Then ErrorMsg(SwApp, "Load Case Combination2 results not loaded")

         'LoadCaseManager.CloseLoadCaseManager
         'LoadCaseManager.DeleteAllDataAndClose

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
