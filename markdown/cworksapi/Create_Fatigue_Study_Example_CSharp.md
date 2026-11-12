---
title: "Create Fatigue Study Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Fatigue_Study_Example_CSharp.htm"
---

# Create Fatigue Study Example (C#)

This example shows how to create a fatigue study.

NOTE: To get persistent reference identifiers (PIDs) for model selections, you can use [pidcollector.exe](GettingStarted-swsimulationapi.html) or IModelDocExtension::GetPersistReference3.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
  // 3. Open, rebuild, and fix as needed public_documents\samples\tutorial\api\
 //     landing_gear.sldasm.
 // 4. Activate Ready_Static.
 // 5. Right-click BearingLoads-1 and click Edit Definition.
 // 6. Select load-bearing faces that are concentric with the Z-axis of the
 //    selected coordinate system and click the green check mark.
 // 7. Mesh the study.
 // 8. Run the study.
 // 9. Open an Immediate window.
 //
 // Postconditions:
 // 1. A default fatigue study results plot is created.
 // 2. Two fatigue studies are created and analyzed:
 //    * Fatigue_StudyAPIConst (constant amplitude fatigue study)
 //    * Fatigue_StudyAPIVariable (variable amplitude fatigue study)
 // 3. Inspect the Immediate window for fatigue study options, fatigue events,
 //    and fatigue study analysis results.
 // 4. Inspect the fatigue results plots.
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
 namespace CreateFatigueStudy_CSharp.csproj
 {
     partial class SolidWorksMacro
     {
         public void ErrorMsg(string Message)
         {
             swApp.SendMsgToUser2(Message, 0, 0);
             swApp.RecordLine("'*** WARNING - General");
             swApp.RecordLine("'*** " + Message);
             swApp.RecordLine("");
         }

         public object SelectByPID(ModelDoc2 Part, string PIDName, Hashtable PIDCollection)
         {
             object functionReturnValue = null;
             byte[] PID = null;
             string[] PIDVariant = null;
             string PIDString = null;
             int i = 0;
             object SelObj = null;
             int errCode = 0;

             //Get the value mapped to the PIDName key from the hashtable
             PIDString =  "";
             IDictionaryEnumerator enumerator = (IDictionaryEnumerator)PIDCollection.GetEnumerator();
             enumerator.Reset();
             while (enumerator.MoveNext())
             {
                 if ((string)enumerator.Key == PIDName)
                 {
                     PIDString = (string)enumerator.Value;
                     break;
                 }
             }

             //Parse the string into an array
             PIDVariant = PIDString.Split(new char[] { ',' });
             int sizeArray = PIDVariant.Length;
             PID = new byte[sizeArray];

             //Change to a byte array
             for (i = 0; i < PIDVariant.Length - 1; i++)
             {
                 PID[i] = Convert.ToByte(PIDVariant[i]);
             }

             //Select the entity
             SelObj = Part.Extension.GetObjectByPersistReference3((PID),  out errCode);
             functionReturnValue = SelObj;
             SelObj = null;
             return functionReturnValue;
         }

         public Hashtable PIDInitializer()
         {
             Hashtable PIDCollection = new Hashtable();
             string selection1 = null;

             //Constants
             selection1 =   "255,18,0,0,3,0,0,0,255,254,255,27,85,0,112,0,112,0,114,0,115,0,119,0,97,0,121,0,95,0,108,0,110,0,107,0,45,0,49,0,64,0,108,0,97,0,110,0,100,0,105,0,110,0,103,0,95,0,103,0,101,0,97,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,57,0,0,0,255,255,1,0,13,0,109,111,86,101,114,116,101,120,82,101,102,95,99,255,255,255,255,255,255,255,255,3,0,0,0,0,2,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,104,67,0,58,0,92,0,68,0,111,0,99,0,117,0,109,0,101,0,110,0,116,0,115,0,32,0,97,0,110,0,100,0,32,0,83,0,101,0,116,0,116,0,105,0,110,0,103,0,115,0,92,0,97,0,116,0,114,0,105,0,118,0,101,0,100,0,105,0,92,0,77,0,121,0,32,0,68,0,111,0,99,0,117,0,109,0,101,0,110,0,116,0,115,0,92,0,99,";
             selection1 = selection1 +  "0,111,0,115,0,109,0,111,0,115,0,95,0,115,0,117,0,112,0,112,0,111,0,114,0,116,0,92,0,50,0,48,0,48,0,54,0,98,0,101,0,116,0,97,0,92,0,76,0,97,0,110,0,100,0,105,0,110,0,103,0,32,0,71,0,101,0,97,0,114,0,92,0,85,0,112,0,112,0,114,0,115,0,119,0,97,0,121,0,95,0,108,0,110,0,107,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,12,85,0,112,0,112,0,114,0,115,0,119,0,97,0,121,0,95,0,108,0,110,0,107,0,2,0,0,247,212,198,52,0,138,187,76,66,1,0,0,0,0,0,0,0,18,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,32,0,0,0,0,0,0,0,138,187,76,66,8,0,0,0,166,214,198,52,14,0,0,0,3,128,0,0,5,128,8,0,8,0,0,0,166,214,198,52,13,0,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,8,0,0,0,166,214,198,52,1,0,0,0,255,255,255,255,0,0,0,0,0,0,0,0";
             selection1 = selection1 +  ",Type=1";

             //Store constants in a collection
             PIDCollection.Add("selection1",  selection1);

             return PIDCollection;
         }

         public string ProcErrCode(int errCode)
         {
             string functionReturnValue = null;
             switch (errCode)
             {
                 case 0:
                     functionReturnValue =  "Successful.";
                     break;
                 case 1: // TODO: to 21
                     functionReturnValue = "Incorrect input conditions.";
                     break;
                 case 22:
                     functionReturnValue =  "Authorization failed for this analysis type.";
                     break;
                 case 23:
                     functionReturnValue =  "Mesh not found. Create mesh first.";
                     break;
                 case 24:
                     functionReturnValue =  "Analysis failed.";
                     break;
                 default:
                     functionReturnValue =  "Unknown error condition.";
                     break;
             }
             return functionReturnValue;
         }

         public void Main()
         {
             ModelDoc2 Part = default(ModelDoc2);
             CosmosWorks COSMOSWORKS = default(CosmosWorks);
             CwAddincallback CWAddinCallBack = default(CwAddincallback);
             CWModelDoc ActDoc = default(CWModelDoc);
             CWStudyManager StudyMngr = default(CWStudyManager);
             CWStudy Study = default(CWStudy);
             CWStudy Study2 = default(CWStudy);
             CWResults CWFeatObj = default(CWResults);
             CWFatigueStudyOptions FatigueOptions = default(CWFatigueStudyOptions);
             CWFatigueEvent FatigueEvent = default(CWFatigueEvent);
             CWFatigueStudyOptions FatigueOptions2 = default(CWFatigueStudyOptions);
             CWFatigueEvent FatigueEvent2 = default(CWFatigueEvent);
             object[] PointsX = new object[11];
             object[] PointsY = new object[11];
             object[] PointsX_2 = new object[13];
             object[] PointsY_2 = new object[13];
             int errCode = 0;
             object[] Disp = null;
             object VarStudyNames = null;
             object VarScales = null;
             object VarSteps = null;
             int AssocCounts = 0;
             object VarNewStudyNames = null;
             object VarNewScales = null;
             object VarNewSteps = null;
             object VarVertices = null;

             Hashtable PIDCollection = new Hashtable();
             PIDCollection = PIDInitializer();

             Part = (ModelDoc2)swApp.ActiveDoc;

             VarVertices = SelectByPID(Part, "selection1", PIDCollection);

             CWAddinCallBack = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
             if (CWAddinCallBack == null)
                 ErrorMsg("CWAddinCallBack object not found.");
             COSMOSWORKS = CWAddinCallBack.CosmosWorks;
             if (COSMOSWORKS == null)
                 ErrorMsg("COSMOSWORKS object not found.");

             ActDoc = COSMOSWORKS.ActiveDoc;
             if (ActDoc == null)
                 ErrorMsg("Failed to get active document.");
```

```vb
            // Add default fatigue study results plot
             errCode = ActDoc.AddDefaultFatigueStudyPlot((int)swsFatigueStudyResultType_e.swsFatigueStudy_DamagePlot);
```

```vb
             StudyMngr = ActDoc.StudyManager;
             if (StudyMngr == null)
                 ErrorMsg("Failed to get StudyManager object.");

             //Create constant amplitude fatigue study
             Debug.Print("Creating constant amplitude fatigue study Fatigue_StudyAPIConst...");
             Study = StudyMngr.CreateNewStudy3("Fatigue_StudyAPIConst", (int)swsAnalysisStudyType_e.swsAnalysisStudyTypeFatigue, 0, out errCode);
             if (Study == null)
                 ErrorMsg("Failed to create new study.");

             errCode = Study.SetFatigueResultOptions(1,  null);

             FatigueOptions = Study.FatigueStudyOptions;
             if (FatigueOptions == null)
                 ErrorMsg("Failed to get FatigueStudyOptions object.");

             FatigueEvent = FatigueOptions.AddFatigueEventForConstantAmplitude("Ready_Static", -0.002, 1, out errCode);
             FatigueEvent.SuppressUnSuppress();
             //suppress event
             FatigueEvent.SuppressUnSuppress();
             //unsuppress event

             AssocCounts = FatigueEvent.GetStudyAssociationData(out VarStudyNames, out VarScales, out VarSteps);

             FatigueEvent.FatigueEventBeginEdit();
             FatigueEvent.Cycles2 = 500.0;
             FatigueEvent.LoadingRatio = 8.9;
             FatigueEvent.LoadingType = 2;
             // Loading ratio
             VarNewScales = 5.6;
             VarNewStudyNames = "Ready_Static";
             VarNewSteps = 9;
             errCode = FatigueEvent.SetStudyAssociationData(1, (VarNewStudyNames), (VarNewScales), (VarNewSteps));
             errCode = FatigueEvent.FatigueEventEndEdit();

             CWFatigueEvent fatEv = default(CWFatigueEvent);
             fatEv = FatigueOptions.GetFatigueEvent(0,  out errCode);
             Debug.Print("  Name of constant amplitude fatigue event is: " + fatEv.Name);
             Debug.Print("  Number of loading events in this fatigue study: " + FatigueOptions.LoadingEventCount);
             Debug.Print("  Result folder: " + FatigueOptions.ResultFolder);
             Debug.Print("  Shell face option as defined in swsShellFace_e: " + FatigueOptions.ShellFace);
             int bchecked = 0;
             double dcycles = 0;
             FatigueOptions.GetInfiniteLifeSettings2(out bchecked, out dcycles);
             Debug.Print("  Fatigue study infinite life settings checked? (-1 = yes) " + bchecked);
             Debug.Print("  Number of cycles to use: " + dcycles);
             Debug.Print("  Event interaction type as defined in swsFatigueEventInteraction_e: " + FatigueOptions.ConstantAmplitudeEventInteractionOption);
             Debug.Print("  Computing alternating stress option as defined in swsFatigueAlternatingStressOption_e: " + FatigueOptions.ComputingAlternatingStressOption);
             Debug.Print("  Fatigue strength reduction factor: " + FatigueOptions.FatigueStrengthReductionFactor);
             Debug.Print("  Mean stress correction option as defined in swsFatigueMeanStressCorrectionType_e: " + FatigueOptions.MeanStressCorrectionOption);

             errCode = Study.RunAnalysis();
             if (errCode != 0)
                 ErrorMsg("Analysis failed with error code " + errCode +  " - " + ProcErrCode(errCode));

             //Create variable amplitude fatigue study
             Debug.Print("");
             Debug.Print("Creating variable amplitude fatigue study Fatigue_StudyAPIVariable...");
             Study2 = StudyMngr.CreateNewStudy3("Fatigue_StudyAPIVariable", (int)swsAnalysisStudyType_e.swsAnalysisStudyTypeFatigue, 1, out errCode);
             if (Study2 == null)
                 ErrorMsg("Failed to create new study.");

             errCode = Study2.SetFatigueResultOptions(1, (VarVertices));

             FatigueOptions2 = Study2.FatigueStudyOptions;
             if (FatigueOptions2 == null)
                 ErrorMsg("Failed to get FatigueStudyOptions Object.");

             PointsX[0] = 0;
             PointsX[1] = 1;
             PointsX[2] = 2;
             PointsX[3] = 3;
             PointsX[4] = 4;
             PointsX[5] = 5;
             PointsX[6] = 6.25714;
             PointsX[7] = 7;
             PointsX[8] = 8.3846;
             PointsX[9] = 9;
             PointsX[10] = 10;

             PointsY[0] = 0;
             PointsY[1] = 11;
             PointsY[2] = 21;
             PointsY[3] = 33;
             PointsY[4] = 44;
             PointsY[5] = 21;
             PointsY[6] = 66.25714;
             PointsY[7] = 77;
             PointsY[8] = 88.3846;
             PointsY[9] = 99;
             PointsY[10] = 109;

             FatigueEvent2 = FatigueOptions2.AddFatigueEventForVariableAmplitude("Ready_Static", -0.002, 1, (PointsX), (PointsY), 0, 1.0, out errCode);

             fatEv = FatigueOptions2.GetFatigueEvent(0,  out errCode);
             Debug.Print("  Name of variable amplitude fatigue event is " + fatEv.Name);
             Debug.Print("  Number of repeats: " + FatigueEvent2.NoOfRepeats);
             Debug.Print("  Start times: " + FatigueEvent2.StartTimes);

             FatigueEvent2.FatigueEventBeginEdit();

             PointsX_2[0] = 0;
             PointsX_2[1] = 1;
             PointsX_2[2] = 2;
             PointsX_2[3] = 3;
             PointsX_2[4] = 4;
             PointsX_2[5] = 5;
             PointsX_2[6] = 6.25714;
             PointsX_2[7] = 7;
             PointsX_2[8] = 8.3846;
             PointsX_2[9] = 9;
             PointsX_2[10] = 10;
             PointsX_2[11] = 11;
             PointsX_2[12] = 20;

             PointsY_2[0] = 0;
             PointsY_2[1] = 11;
             PointsY_2[2] = 21;
             PointsY_2[3] = 33;
             PointsY_2[4] = 44;
             PointsY_2[5] = 21;
             PointsY_2[6] = 66.25714;
             PointsY_2[7] = 77;
             PointsY_2[8] = 88.3846;
             PointsY_2[9] = 99;
             PointsY_2[10] = 109;
             PointsY_2[11] = 66;
             PointsY_2[12] = 12;

             errCode = FatigueEvent2.SetLoadHistoryCurve((PointsX_2), (PointsY_2), 2, 1.8);
             errCode = FatigueEvent2.FatigueEventEndEdit();

             object[] lhCurve = null;
             int ntype = 0;
             double dsamplingrate = 0;
             lhCurve = (object[])FatigueEvent2.GetLoadHistoryCurve(out ntype, out dsamplingrate);
             Debug.Print("  Type of load history curve as defined in swsFatigueLoadHistoryCurveType_e: " + ntype);
             Debug.Print("  Sampling rate in seconds: " + dsamplingrate);
             Debug.Print("  Number of pairs of load history curve data: " + lhCurve[0]);
             Debug.Print("  Load history curve [time, amplitude] data:");
             Debug.Print("  " + lhCurve[1] + ", " + lhCurve[2]);
             Debug.Print("  " + lhCurve[3] + ", " + lhCurve[4]);
             Debug.Print("  " + lhCurve[5] + ", " + lhCurve[6]);
             Debug.Print("  " + lhCurve[7] + ", " + lhCurve[8]);
             Debug.Print("  " + lhCurve[9] + ", " + lhCurve[10]);
             Debug.Print("  " + lhCurve[11] + ", " + lhCurve[12]);
             Debug.Print("  " + lhCurve[13] + ", " + lhCurve[14]);
             Debug.Print("  " + lhCurve[15] + ", " + lhCurve[16]);
             Debug.Print("  " + lhCurve[17] + ", " + lhCurve[18]);
             Debug.Print("  " + lhCurve[19] + ", " + lhCurve[20]);
             Debug.Print("  " + lhCurve[21] + ", " + lhCurve[22]);
             Debug.Print("  " + lhCurve[23] + ", " + lhCurve[24]);
             Debug.Print("  " + lhCurve[25] + ", " + lhCurve[26]);

             Debug.Print("  Number of loading events in this fatigue study: " + FatigueOptions2.LoadingEventCount);
             Debug.Print("  Result folder: " + FatigueOptions2.ResultFolder);
             Debug.Print("  Shell face option as defined in swsShellFace_e: " + FatigueOptions2.ShellFace);

             FatigueOptions2.GetInfiniteLifeSettings(out bchecked, out dcycles);
             int nnoofbins = 0;
             int npercentfilterloadcycles = 0;
             FatigueOptions2.GetVariableAmplitudeEventOptions(out nnoofbins, out npercentfilterloadcycles);
             Debug.Print("  Fatigue study infinite life settings checked? (1 = yes) " + bchecked);
             Debug.Print("  Number of cycles to use: " + dcycles);
             Debug.Print("  Number of equally spaced buckets in which to distribute the load: " + nnoofbins);
             Debug.Print("  Filter load cycles below this percentage of maximum load: " + npercentfilterloadcycles);
             Debug.Print("  Computing alternating stress option as defined in swsFatigueAlternatingStressOption_e: " + FatigueOptions2.ComputingAlternatingStressOption);
             Debug.Print("  Fatigue strength reduction factor: " + FatigueOptions2.FatigueStrengthReductionFactor);
             Debug.Print("  Mean stress correction option as defined in swsFatigueMeanStressCorrectionType_e: " + FatigueOptions2.MeanStressCorrectionOption);

             errCode = Study2.RunAnalysis();
             if (errCode != 0)
                 ErrorMsg("Analysis failed with error code " + errCode +  " - " + ProcErrCode(errCode));

             CWFeatObj = Study2.Results;
             if (CWFeatObj == null)
                 ErrorMsg("Failed to get result object.");

             //Get Min,Max Fatigue
             Disp = (object[])CWFeatObj.GetMinMaxFatigue(0, out errCode);
             Debug.Print("  Minimum fatigue is " + Disp[1] +  " at node " + Disp[0]);
             Debug.Print("  Maximum fatigue is " + Disp[3] +  " at node " + Disp[2]);
         }

         public SldWorks swApp;

     }

 }
```
