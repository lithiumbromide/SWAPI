---
title: "Access Load Case Manager Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Access_Load_Case_Manager_Example_CSharp.htm"
---

# Access Load Case Manager Example (C#)

This example shows how to access the Load Case Manager to define load cases and load case combinations.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
 // 3. Ensure that the specified model exists.
 //
 // Postconditions:
 // 1. Gets the Ready study.
 // 2. Opens the Load Case Manager.
  // 3. Adds primary load cases and load case combinations.
 // 4. Analyzes Ready using all primary load cases and load case combinations.
 // 5. Creates a results displacement plot.
  // 6. Click each primary load case and load case combination in the
  //    Results View tab of the Load Case Manager. Inspect the result data
 //    in the graphics area after each click.
 //
  // NOTE: Because the model is used elsewhere, do not save changes.
  // ---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using SolidWorks.Interop.cosworks;
 using System.Runtime.InteropServices;
 namespace LoadCaseManager_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Part;
         CosmosWorks COSMOSWORKS;
         CwAddincallback CWAddinCallBack;
         CWModelDoc ActDoc;
         CWStudyManager StudyMngr;
         CWStudy Study;
        CWMesh Mesh;
         CWLoadCaseManager LoadCaseManager;
         CWResults CWResult;
         CWPlot CWCFf;
        CWStaticStudyOptions StudyOptions;

         int errCode;
         int longstatus;
         int longwarnings;

         bool bSuccess;

         object PrimaryCases;
         object SecondaryCases;
         object[] varBOOLVals = new object[1];
         object[] varLoadVals = new object[1];
         object[] varRetBOOLVals = new object[1];
         object[] varRetLoadVals = new object[1];
         string strCombination;
         string retStrCombination;
           double e1;
           double e2;

         public void Main()
         {
             Part = swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2024\\Simulation Examples\\Tutor1.sldprt", (int)swDocumentTypes_e.swDocPART, 1, "", ref longstatus, ref longwarnings);
             if (Part == null)
                 ErrorMsg(swApp, "Failed to open Tutor1.sldprt");

             CWAddinCallBack = (CwAddincallback)swApp.GetAddInObject("CosmosWorks.CosmosWorks");
             if (CWAddinCallBack == null)
                 ErrorMsg(swApp, "Simulation add-in not loaded");
             COSMOSWORKS = CWAddinCallBack.CosmosWorks;
             if (COSMOSWORKS == null)
                 ErrorMsg(swApp, "No COSMOSWORKS object");

             ActDoc = COSMOSWORKS.ActiveDoc;
             if (ActDoc == null)
                 ErrorMsg(swApp, "No active document");

             StudyMngr = ActDoc.StudyManager;
             if (StudyMngr == null)
                 ErrorMsg(swApp, "No CWStudyManager object");
             Study = StudyMngr.GetStudy(0);
             StudyMngr.ActiveStudy = 0;
             if (Study == null)
                 ErrorMsg(swApp, "No study");

             LoadCaseManager = Study.LoadCaseManager;
             if (LoadCaseManager == null)
                 ErrorMsg(swApp, "No Load Case Manager");

             bSuccess = LoadCaseManager.OpenLoadCaseManager();
```

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

CWMesh = (CWMesh)Study.**Mesh**

CWMesh.**Quality** = 1

CWMesh.**GetDefaultElementSizeAndTolerance**(0, out el, out tl)

errCode = Study.**CreateMesh**(0, el, tl)

'Run analysis

errCode = Study.**RunAnalysis()**

'Get results

CWResult = (CWResults)Study.**Results**

```vb
             bSuccess = LoadCaseManager.AddNewPrimaryLoadCase("My Load Case1");
             if (bSuccess == false)
                 ErrorMsg(swApp, "Primary load case not created");
             bSuccess = LoadCaseManager.AddNewPrimaryLoadCase("My Load Case2");
             if (bSuccess == false)
                 ErrorMsg(swApp, "Primary load case not created");
             bSuccess = LoadCaseManager.AddNewPrimaryLoadCase("My Load Case3");
             if (bSuccess == false)
                 ErrorMsg(swApp, "Primary load case not created");

             bSuccess = LoadCaseManager.DeletePrimaryLoadCase("My Load Case3");
             if (bSuccess == false)
                 ErrorMsg(swApp, "Primary load case not deleted");

             bSuccess = LoadCaseManager.SuppressOrUnSuppressPrimaryLoadCase("My Load Case2", true);
             if (bSuccess == false)
                 ErrorMsg(swApp, "Primary load case not suppressed");

             bSuccess = LoadCaseManager.SuppressOrUnSuppressPrimaryLoadCase("My Load Case2", false);
             if (bSuccess == false)
                 ErrorMsg(swApp, "Primary load case not unsuppressed");

             bSuccess = LoadCaseManager.RenamePrimaryLoadCase("My Load Case2", "Live Load2");
             if (bSuccess == false)
                 ErrorMsg(swApp, "Primary load case not renamed");

             varBOOLVals[0] = false;
             varLoadVals[0] = 3.5;
             errCode = LoadCaseManager.SetLoadDataForPrimaryLoadCase("My Load Case1", "Pressure-1", (varBOOLVals), (varLoadVals));
             if (errCode > 0)
                 ErrorMsg(swApp, "Load data of Pressure-1 not applied to My Load Case1");

             varBOOLVals[0] = true;
             varLoadVals[0] = -1;
             errCode = LoadCaseManager.SetLoadDataForPrimaryLoadCase("My Load Case1", "Restraint-1", (varBOOLVals), (varLoadVals));
             if (errCode > 0)
                 ErrorMsg(swApp, "Load data of Restraint-1 not applied to My Load Case1");

             varBOOLVals[0] = false;
             varLoadVals[0] = -1;
             errCode = LoadCaseManager.SetLoadDataForPrimaryLoadCase("My Load Case1", "Restraint-1", (varBOOLVals), (varLoadVals));
             if (errCode > 0)
                 ErrorMsg(swApp, "Load data of Restraint-1 not applied to My Load Case1");

             varBOOLVals[0] = false;
             varLoadVals[0] = 6.5;
             errCode = LoadCaseManager.SetLoadDataForPrimaryLoadCase("Live Load2", "Pressure-1", (varBOOLVals), (varLoadVals));
             if (errCode > 0)
                 ErrorMsg(swApp, "Load data of Pressure-1 not applied to Live Load2");

             varRetLoadVals = (object[])LoadCaseManager.GetLoadDataForPrimaryLoadCase("Live Load2", "Pressure-1", out varRetBOOLVals[0]);

             strCombination = "\"My Load Case1\" + \"Live Load2\"";
             errCode = LoadCaseManager.AddNewLoadCaseCombination("Load Case Combination1", strCombination);
             if (errCode > 0)
                 ErrorMsg(swApp, "Load Case Combination1 not added");

             strCombination = "2*(sin(30)*\"My Load Case1\"*(1 + 1) + (4 - 2)*\"Live Load2\"*cos(60))";
             errCode = LoadCaseManager.AddNewLoadCaseCombination("Load Case Combination2", strCombination);
             if (errCode > 0)
                 ErrorMsg(swApp, "Load Case Combination2 not added");

             strCombination = "\"My Load Case1\" + \"Live Load2\"";
             errCode = LoadCaseManager.AddNewLoadCaseCombination("Load Case Combination3", strCombination);
             if (errCode > 0)
                 ErrorMsg(swApp, "Load Case Combination3 not added");

             strCombination = "\"My Load Case1\" + \"Live Load2\"";
             errCode = LoadCaseManager.AddNewLoadCaseCombination("Load Case Combination4", strCombination);
             if (errCode > 0)
                 ErrorMsg(swApp, "Load Case Combination4 not added");

             bSuccess = LoadCaseManager.DeleteLoadCaseCombination("Load Case Combination3");
             if (bSuccess == false)
                 ErrorMsg(swApp, "Load Case Combination3 not deleted");

             bSuccess = LoadCaseManager.DeleteLoadCaseCombination("Load Case Combination4");
             if (bSuccess == false)
                 ErrorMsg(swApp, "Load Case Combination4 cannot be deleted");

             strCombination = "\"My Load Case1\" + \"Live Load2\"";
             errCode = LoadCaseManager.AddNewLoadCaseCombination("Load Case Combination3", strCombination);
             if (errCode > 0)
                 ErrorMsg(swApp, "Load Case Combination3 not added");

             bSuccess = LoadCaseManager.SuppressOrUnSuppressLoadCaseCombination("Load Case Combination2", true);
             if (bSuccess == false)
                 ErrorMsg(swApp, "Load Case Combination2 not suppressed");

             bSuccess = LoadCaseManager.SuppressOrUnSuppressLoadCaseCombination("Load Case Combination2", false);
             if (bSuccess == false)
                 ErrorMsg(swApp, "Load Case Combination2 not unsuppressed");

             bSuccess = LoadCaseManager.SuppressOrUnSuppressLoadCaseCombination("Load Case Combination3", true);
             if (bSuccess == false)
                 ErrorMsg(swApp, "Load Case Combination3 not suppressed");

             bSuccess = LoadCaseManager.RenameLoadCaseCombination("Load Case Combination2", "My Combination2");
             if (bSuccess == false)
                 ErrorMsg(swApp, "Load Case Combination2 not renamed");

             bSuccess = LoadCaseManager.RenameLoadCaseCombination("My Combination2", "Load Case Combination2");
             if (bSuccess == false)
                 ErrorMsg(swApp, "Load Case Combination2 not renamed");

             strCombination = "\"My Load Case1\" * \"Live Load2\"";
             errCode = LoadCaseManager.SetEquationForLoadCaseCombination("Load Case Combination1", strCombination);
             if (errCode == 0)
                 ErrorMsg(swApp, "Load Case Combination1 equation not set");

             strCombination = "(\"My Load Case1\"*2 + \"Live Load2\"*2)/2";
             errCode = LoadCaseManager.SetEquationForLoadCaseCombination("Load Case Combination1", strCombination);
             if (errCode > 0)
                 ErrorMsg(swApp, "Load Case Combination1 equation not set");

             retStrCombination = LoadCaseManager.GetEquationForLoadCaseCombination("Load Case Combination1");
             errCode = retStrCombination.CompareTo(strCombination);
             if (errCode < 0 | errCode > 0)
                 ErrorMsg(swApp, "Load Case Combination1 equation not returned");

             PrimaryCases = LoadCaseManager.GetAllPrimaryLoadCaseNames();
             SecondaryCases = LoadCaseManager.GetAllLoadCaseCombinationNames();

             errCode = LoadCaseManager.RunLoadCases(true, true);
             if (errCode > 0)
                 ErrorMsg(swApp, "Load cases failed to run");

             LoadCaseManager.ShowLoadCaseViewTab();

             bSuccess = LoadCaseManager.ShowResultsViewTab();
             if (bSuccess == false)
                 ErrorMsg(swApp, "Cannot display Results View tab");

             bSuccess = LoadCaseManager.LoadResultsOfPrimaryLoadCase("My Load Case1");
             if (bSuccess == false)
                 ErrorMsg(swApp, "My Load Case1 results not loaded");

             CWResult = Study.Results;
             if (CWResult == null)
                 ErrorMsg(swApp, "No CWResults object");

            CWCFf = CWResult.CreatePlot((int)swsPlotResultTypes_e.swsResultDisplacementOrAmplitude, (int)swsStaticResultDisplacementComponentTypes_e.swsStaticDisplacement_URES, (int     swsUnit_e.swsUnitSI, false, out errCode);

             bSuccess = LoadCaseManager.LoadResultsOfPrimaryLoadCase("Live Load2");
             if (bSuccess == false)
                 ErrorMsg(swApp, "Live Load2 results not loaded");

             bSuccess = LoadCaseManager.LoadResultsOfLoadCaseCombination("Load Case Combination1");
             if (bSuccess == false)
                 ErrorMsg(swApp, "Load Case Combination1 results not loaded");

             bSuccess = LoadCaseManager.LoadResultsOfLoadCaseCombination("Load Case Combination2");
             if (bSuccess == false)
                 ErrorMsg(swApp, "Load Case Combination2 results not loaded");

             //LoadCaseManager.CloseLoadCaseManager
             //LoadCaseManager.DeleteAllDataAndClose

         }

         public void ErrorMsg(SldWorks SwApp, string Message)
         {
             SwApp.SendMsgToUser2(Message, 0, 0);
             SwApp.RecordLine("'*** WARNING - General");
             SwApp.RecordLine("'*** " + Message);
             SwApp.RecordLine("");
         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }

 }
```
