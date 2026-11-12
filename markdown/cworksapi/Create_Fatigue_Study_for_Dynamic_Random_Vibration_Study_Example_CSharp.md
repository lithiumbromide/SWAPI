---
title: "Create Fatigue Study for Dynamic Random Vibration Study Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Fatigue_Study_for_Dynamic_Random_Vibration_Study_Example_CSharp.htm"
---

# Create Fatigue Study for Dynamic Random Vibration Study Example (C#)

This example shows how to create a fatigue study for a linear dynamic random vibration study.

```vb
  //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
 // 3. Ensure that the specified part and material library exist.
 // 4. Open an Immediate window.
 //
 // Postconditions:
 //  1. Opens the specified file.
 //  2. Creates and analyzes study, Dynamic_Random_Vibration.
 //  3. Creates a default fatigue study damage plot.
 //  4. Creates study, RandomVibrationFatigue.
  //  5. Adds a fatigue event of duration 60 seconds to RandomVibrationFatigue.
  //  6. Modifies the fatigue S-N curve equation for the model's material.
 //  7. Analyzes RandomVibrationFatigue and displays message boxes with damage
  //     percentage errors for each of the following computational methods:
 //     * Narrow Band
 //     * Steinberg
 //     * Wirsching
 //  8. Click OK to close each message box.
  //  9. Inspect the Immediate window for the Narrow Band method
 //     minimum and maximum fatigue.
 // 10. Inspect the damage plot.
 //
  // NOTE: Because the model is used elsewhere, do not save any changes.
  //---------------------------------------------------------------------------
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

 namespace RandomVibrationFatigue_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 Part = default(ModelDoc2);
             CosmosWorks COSMOSWORKS = default(CosmosWorks);
             CwAddincallback CWAddinCallBack = default(CwAddincallback);
             CWModelDoc ActDoc = default(CWModelDoc);
             CWStudyManager StudyMngr = default(CWStudyManager);
             CWStudy Study = default(CWStudy);
             CWMaterial SolidMat = default(CWMaterial);
             CWLoadsAndRestraintsManager LBCMgr = default(CWLoadsAndRestraintsManager);
             CWDynamicStudyOptions DynStudyOptions = default(CWDynamicStudyOptions);
             object CWDirectionEntity = null;
             int longstatus = 0;
             int longwarnings = 0;
             int errCode = 0;
             bool boolstatus = false;
             object pDisp5 = null;
             object[] DispArray1 = new object[1];
             object[] DispArray3 = new object[1];
             string sStudyName = null;
             CWStudyResultOptions ResultOptions = default(CWStudyResultOptions);
             CWDampingOptions DampingOptions = default(CWDampingOptions);
             object[] DampingRatios = new object[9];
             int freqOption = 0;
             double freqValue = 0;
             bool bChecked = false;
             CWResults CWFeatObj = default(CWResults);
             CWPressure CWFeatObj2 = default(CWPressure);
             CWRestraint CWFeatObj3 = default(CWRestraint);
             CWMesh CWFeatObj4 = default(CWMesh);
             CWResults CWFeatObj5 = default(CWResults);
             int param = 0;
             double dParam = 0;
             double inRadius = 0;
             double outRadius = 0;
             CWFatigueStudyOptions FatigueOptions = default(CWFatigueStudyOptions);
             CWFatigueEvent FatigueEvent = default(CWFatigueEvent);
             object[] Damage = null;

             const double Tol = 0.05; //5% - damage tolerance
             const double DamageMax_NarrowBand = 1305.36; //baseline percentage
             const double DamageMax_Steinberg = 741.951; //baseline percentage
             const double DamageMax_Wirsching = 907.23; //baseline percentage
             const double MeshEleSize = 26.5868077635828; //mm
             const double MeshTol = 1.32934038817914; //mm

             Part = swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\block.SLDPRT", (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref longstatus, ref longwarnings);
             if (Part == null)
                 ErrorMsg(swApp, "Failed to open block.SLDPRT");

             CWAddinCallBack = (CwAddincallback)swApp.GetAddInObject("CosmosWorks.CosmosWorks");
             if (CWAddinCallBack == null)
                 ErrorMsg(swApp, "Failed to get CwAddincallback object");
             COSMOSWORKS = CWAddinCallBack.CosmosWorks;
             if (COSMOSWORKS == null)
                 ErrorMsg(swApp, "Failed to get CosmosWorks object");

             ActDoc = COSMOSWORKS.ActiveDoc;
             if (ActDoc == null)
                 ErrorMsg(swApp, "Failed to get active document");

             // Create a dynamic random vibration study
             StudyMngr = ActDoc.StudyManager;
             if (StudyMngr == null)
                 ErrorMsg(swApp, "Failed to get CWStudyManager object");

             sStudyName = "Dynamic_Random_Vibration";
             Study = StudyMngr.CreateNewStudy3(sStudyName, (int)swsAnalysisStudyType_e.swsAnalysisStudyTypeDynamic, (int)swsDynamicAnalysisSubType_e.swsDynamicAnalysisSubTypeRandom, out errCode);

             Debug.Print("Linear dynamic study with random vibration analysis");
             Debug.Print("");
             Debug.Print("Study configuration name is " + Study.ConfigurationName);
             Debug.Print("Dynamic analysis subtype as defined in swsAnalysisStudyType_e is " + Study.DynamicAnalysisSubType);
             Debug.Print("Dynamic study options...");

             DynStudyOptions = Study.DynamicStudyOptions;

             errCode = DynStudyOptions.GetFrequencyOption2(out freqOption, out freqValue);
             Debug.Print("  Frequency option (0=number of frequencies, 1=upper bound): " + freqOption);
             Debug.Print("  No. of frequencies or upper-bound frequency: " + freqValue);
             errCode = DynStudyOptions.GetFrequencyShiftOption2(out bChecked, out freqValue);
             Debug.Print("  Is frequency shift enabled (0=no, 1=yes)? " + bChecked);
             Debug.Print("  Frequency shift: " + freqValue);

             errCode = DynStudyOptions.SetIncompatibleBondingOption2((int)swsIncompatibleBondingOption_e.swsIncompatibleBondingOption_Automatic);
             errCode = DynStudyOptions.SetUseSoftSpring2(0); // Not using a soft spring to stabilize model
             errCode = DynStudyOptions.SetResultFolderPath2("c:\\temp");

             DynStudyOptions.SolverType = (int)swsSolverType_e.swsSolverTypeFFEPlus;

             errCode = DynStudyOptions.GetRandomVibrationAnalysisMethod2(out param);
             Debug.Print("  Analysis method as defined in swsRandomVibrationAnalysisMethod_e: " + param);
             errCode = DynStudyOptions.GetRandomVibrationBiasingParameter2(out dParam);
             Debug.Print("  Biasing parameter: " + param);
             errCode = DynStudyOptions.GetRandomVibrationCorrelationOption2(out param);
             Debug.Print("  Correlation option as defined in swsRandomVibrationCorrelationOption_e: " + param);
             errCode = DynStudyOptions.GetRandomVibrationCrossModeCutOffRatio2(out dParam);
             Debug.Print("  Cross-mode cut-off ratio: " + param);
             errCode = DynStudyOptions.GetRandomVibrationFrequencyLowerLimit2(out dParam);
             Debug.Print("  Operating frequency lower limit: " + param);
             errCode = DynStudyOptions.GetRandomVibrationFrequencyUnits2(out param);
             Debug.Print("  Units of operating frequency as defined in swsFrequencyUnit_e: " + param);
             errCode = DynStudyOptions.GetRandomVibrationFrequencyUpperLimit2(out dParam);
             Debug.Print("  Operating frequency upper limit: " + param);
             errCode = DynStudyOptions.GetRandomVibrationGaussIntegrationOrder2(out param);
             Debug.Print("  Gauss integration order as defined in swsGaussIntegrationOrder_e: " + param);
             errCode = DynStudyOptions.GetRandomVibrationNoOfFrequencyPoints2(out param);
             Debug.Print("  Number of frequency points: " + param);
             errCode = DynStudyOptions.GetRandomVibrationPartialCorrelationDetails2(out param, out inRadius, out outRadius);
             Debug.Print("  Partially correlated units as defined in swsLinearUnit_e: " + param);
             Debug.Print("  Inside radius: " + inRadius);
             Debug.Print("  Outside radius: " + outRadius);

             Debug.Print("");

             // Set study result options
             Debug.Print("Study result options...");
             ResultOptions = Study.StudyResultOptions;
             ResultOptions.SaveResultsForSolutionStepsOption = (int)swsSaveResultsOption_e.swsSaveResultsOption_ForAllSolutionSteps;
             ResultOptions.SaveDisplacementsAndVelocitiesOption = (int)swsResultsDisplacementAndVelocityOption_e.swsResultsDisplacementAndVelocityOption_Absolute;
             ResultOptions.SaveStresses = 1;  // Save stress results

             // Set damping options
             DampingOptions = Study.DampingOptions;
             DampingOptions.DampingType = (int)swsDampingType_e.swsDampingType_Modal;
             DampingRatios[0] = 1;
             DampingRatios[1] = 5;
             DampingRatios[2] = 3.45;
             DampingRatios[3] = 6;
             DampingRatios[4] = 15;
             DampingRatios[5] = 15;
             DampingRatios[6] = 16;
             DampingRatios[7] = 25;
             DampingRatios[8] = 34.5;
             errCode = DampingOptions.SetDampingRatios(3, (DampingRatios));
             DampingOptions.ComputeFromMaterialDamping = 0; // Not using the material damping ratio to calculate modal damping ratios

             object PID = null;
             object SelObj = null;
             object obj = null;
             object fixtureEntity = null;

             // Get a face to which to apply a pressure
             boolstatus = Part.Extension.SelectByID2("", "FACE", -0.00795509158535879, 0, -0.0113043904061669, false, 0, null, 0);
             obj = ((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(1, -1);
             PID = Part.Extension.GetPersistReference3(obj);
             SelObj = Part.Extension.GetObjectByPersistReference3((PID), out errCode);
             DispArray1[0] = SelObj;

             // Get a face to use as a fixture
             boolstatus = Part.Extension.SelectByID2("", "FACE", -0.0207435908961884, -0.0134200983288792, -0.00999045700837087, false, 0, null, 0);
             obj = ((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(1, -1);
             PID = Part.Extension.GetPersistReference3(obj);
             fixtureEntity = Part.Extension.GetObjectByPersistReference3((PID), out errCode);
             DispArray3[0] = fixtureEntity;

             // Get a face to use as a reference entity
             boolstatus = Part.Extension.SelectByID2("", "FACE", 0.0180913769526114, -0.0129337958455835, -0.0101226987114842, false, 0, null, 0);
             obj = ((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(1, -1);
             PID = Part.Extension.GetPersistReference3(obj);
             CWDirectionEntity = Part.Extension.GetObjectByPersistReference3((PID), out errCode);
             pDisp5 = CWDirectionEntity;

             // Add a material
             CWSolidManager SolidMgr = default(CWSolidManager);
             CWSolidComponent SolidComponent = default(CWSolidComponent);
             string SName = null;
             CWSolidBody SolidBody = default(CWSolidBody);

             SolidMgr = Study.SolidManager;
             SolidComponent = SolidMgr.GetComponentAt(0, out errCode);
             SName = SolidComponent.ComponentName;

             SolidBody = SolidComponent.GetSolidBodyAt(0, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "No solid body");

             longstatus = SolidBody.SetLibraryMaterial("C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\\english\\sldmaterials\\solidworks materials.sldmat", "Ductile Iron (SN)");
             if (longstatus == 0)
                 ErrorMsg(swApp, "No material applied");

             // Get loads and restraints manager
             LBCMgr = Study.LoadsAndRestraintsManager;
             if (LBCMgr == null)
                 ErrorMsg(swApp, "Failed to get loads and restraints manager");

             // Apply pressure normal to the selected face
             CWFeatObj2 = LBCMgr.AddPressure((int)swsPressureType_e.swsPressureTypeNormal, (DispArray1), null, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to create normal pressure");
             CWFeatObj2.PressureBeginEdit();
             Debug.Print("Normal pressure values...");
             Debug.Print("  Pressure unit in swsStrengthUnit_e units: " + CWFeatObj2.Unit);
             Debug.Print("  Pressure value: " + CWFeatObj2.Value);
             Debug.Print("  Pressure phase angle (-1 if not set): " + CWFeatObj2.PhaseAngle);
             Debug.Print("  Pressure phase angle unit in swsPhaseAngleUnit_e units: " + CWFeatObj2.PhaseAngleUnit);
             errCode = CWFeatObj2.PressureEndEdit();
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to apply normal pressure value");

             Debug.Print(" ");

             // Add a fixture
             CWFeatObj3 = LBCMgr.AddRestraint((int)swsRestraintType_e.swsRestraintTypeFixed, (DispArray3), pDisp5, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to create restraint");
             CWFeatObj3.RestraintBeginEdit();
             CWFeatObj3.SetTranslationComponentsValues(0, 0, 1, 0.0, 0.0, 0.0);
             CWFeatObj3.SetRotationComponentsValues(0, 0, 0, 0.0, 0.0, 0.0);
             CWFeatObj3.Unit = (int)swsLinearUnit_e.swsLinearUnitMeters;
             errCode = CWFeatObj3.RestraintEndEdit();
             if (errCode != 0)
                 ErrorMsg(swApp, "Restraint end-edit failed");

             // Create mesh
             CWFeatObj4 = Study.Mesh;
             if (CWFeatObj4 == null)
                 ErrorMsg(swApp, "Failed to create mesh object");
             CWFeatObj4.MesherType = (int)swsMesherType_e.swsMesherTypeStandard;
             CWFeatObj4.Quality = (int)swsMeshQuality_e.swsMeshQualityHigh;

             errCode = Study.CreateMesh((int)swsLinearUnit_e.swsLinearUnitMillimeters, MeshEleSize, MeshTol);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to create mesh");
             Debug.Print("Worst Jacobian ratio for the mesh: " + CWFeatObj4.GetWorstJacobianRatio());
             Debug.Print("");

             // Run analysis
             Debug.Print("Running the analysis");
             Debug.Print("");
             errCode = Study.RunAnalysis();
             if (errCode != 0)
                 ErrorMsg(swApp, "Analysis failed with error code as defined in swsRunAnalysisError_e:" + errCode);
             CWFeatObj5 = Study.Results;
             if (CWFeatObj5 == null)
                 ErrorMsg(swApp, "Failed to get results object");

             // Add default fatigue study results plot
             errCode = ActDoc.AddDefaultFatigueStudyPlot((int)swsFatigueStudyResultType_e.swsFatigueStudy_DamagePlot);

             StudyMngr = ActDoc.StudyManager;
             if (StudyMngr == null)
                 ErrorMsg(swApp, "Failed to get CWStudyManager object");

             // Create random vibration fatigue study
             Debug.Print("Creating RandomVibrationFatigue study...");
             Study = StudyMngr.CreateNewStudy3("RandomVibrationFatigue", (int)swsAnalysisStudyType_e.swsAnalysisStudyTypeFatigue, 3, out errCode);
             if (Study == null)
                 ErrorMsg(swApp, "Failed to create new study");

             errCode = Study.SetFatigueResultOptions((int)swsFatigueCalculationsOption_e.swsFatigueCalculationsOption_SurfaceOnly, null);

             FatigueOptions = Study.FatigueStudyOptions;
             if (FatigueOptions == null)
                 ErrorMsg(swApp, "Failed to get CWFatigueStudyOptions object");

             FatigueEvent = FatigueOptions.AddFatigueEventForRandomVibration("Dynamic_Random_Vibration", 60, 0, out errCode);

             SolidMgr = Study.SolidManager;
             SolidComponent = SolidMgr.GetComponentAt(0, out errCode);
             SName = SolidComponent.ComponentName;

             SolidBody = SolidComponent.GetSolidBodyAt(0, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "No solid body");

             longstatus = SolidBody.SetLibraryMaterial("C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\\english\\sldmaterials\\solidworks materials.sldmat", "Ductile Iron (SN)");
             if (longstatus == 0)
                 ErrorMsg(swApp, "No material applied");

             SolidMat = SolidBody.GetSolidBodyMaterial();

             SolidMat.SNCurveSource = (int)swsMaterialSNCurveSource_e.swsMaterialSNCurveSourceEquation;
             SolidMat.SNCurveEstimateConstants = 0; // Specify Basquin Equation constants, B and m
             SolidMat.SNCurveSpecificConstantBUnit = 3; // N/mm^2
             SolidMat.SNCurveSpecificConstantB = 2E+20; // B constant
             SolidMat.SNCurveSlopeM = 0.5; // Slope m

             errCode = SolidBody.SetSolidBodyMaterial(SolidMat);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to apply material");

             FatigueOptions.RandomVibrationComputationalMethod = 0; // Narrow Band computational method
             errCode = Study.RunAnalysis();
             if (errCode != 0)
                 ErrorMsg(swApp, "Narrow Band analysis failed with error code as defined in swsRunAnalysisError_e: " + errCode);

             CWFeatObj = Study.Results;
             if (CWFeatObj == null)
                 ErrorMsg(swApp, "Failed to get CWResults object");

             // Get minimum and maximum damage
             Damage = (object[])CWFeatObj.GetMinMaxFatigue((int)swsFatigueComponent_e.swsFatigueComponent_Damage, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to get minimum and maximum damage for Narrow Band analysis. Error code as defined in swsResultsError_e: " + errCode);

             double dam3;
             double dam1;
             dam1 = (float)Damage[1];
             dam3 = (float)Damage[3];

             // Compare maximum damage percentage with baseline and report errors
             if ((dam3 < (1 - Tol) * DamageMax_NarrowBand) | dam3 > (1 + Tol) * DamageMax_NarrowBand)
             {
                 ErrorMsg(swApp, "Narrow Band damage % error = " + (((dam3 - DamageMax_NarrowBand) / DamageMax_NarrowBand) * 100));
             }

             Debug.Print("Narrow Band computational method...");
             Debug.Print("  Minimum fatigue is " + dam1 + " at node " + Damage[0]);
             Debug.Print("  Maximum fatigue is " + dam3 + " at node " + Damage[2]);

             FatigueOptions.RandomVibrationComputationalMethod = 1; // Steinberg computational method
             errCode = Study.RunAnalysis();
             if (errCode != 0)
                 ErrorMsg(swApp, "Steinberg analysis failed with error code as defined in swsRunAnalysisError_e: " + errCode);

             CWFeatObj = Study.Results;
             if (CWFeatObj == null)
                 ErrorMsg(swApp, "Failed to get CWResults object");

             // Get minimum and maximum damage
             Damage = (object[])CWFeatObj.GetMinMaxFatigue((int)swsFatigueComponent_e.swsFatigueComponent_Damage, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to get minimum and maximum damage for Steinberg analysis. Error code as defined in swsResultsError_e: " + errCode);

             dam1 = (float)Damage[1];
             dam3 = (float)Damage[3];

             // Compare maximum damage percentage with baseline and report errors
             if ((dam3 < (1 - Tol) * DamageMax_Steinberg) | (dam3 > (1 + Tol) * DamageMax_Steinberg))
             {
                 ErrorMsg(swApp, "Steinberg damage % error = " + (((dam3 - DamageMax_Steinberg) / DamageMax_Steinberg) * 100));
             }

             FatigueOptions.RandomVibrationComputationalMethod = 2; // Wirsching computational method
             errCode = Study.RunAnalysis();
             if (errCode != 0)
                 ErrorMsg(swApp, "Wirsching analysis failed with error code as defined in swsRunAnalysisError_e: " + errCode);

             CWFeatObj = Study.Results;
             if (CWFeatObj == null)
                 ErrorMsg(swApp, "Failed to get CWResults object");

             // Get minimum and maximum damage
             Damage = (object[])CWFeatObj.GetMinMaxFatigue((int)swsFatigueComponent_e.swsFatigueComponent_Damage, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to get minimum and maximum damage for Wirsching analysis. Error code as defined in swsResultsError_e: " + errCode);

             dam1 = (float)Damage[1];
             dam3 = (float)Damage[3];

             // Compare maximum damage percentage with baseline and report errors
             if ((dam3 < (1 - Tol) * DamageMax_Wirsching) | (dam3 > (1 + Tol) * DamageMax_Wirsching))
             {
                 ErrorMsg(swApp, "Wirsching damage % error = " + (((dam3 - DamageMax_Wirsching) / DamageMax_Wirsching) * 100));
             }

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
