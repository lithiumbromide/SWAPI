---
title: "Create Linear Dynamic Study Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Dynamic_Harmonic_Study_Example_CSharp.htm"
---

# Create Linear Dynamic Study Example (C#)

This example shows how to create a linear harmonic dynamic study.

NOTE: To get persistent reference identifiers (PIDs) for model selections, you can use [pidcollector.exe](GettingStarted-swsimulationapi.html) or IModelDocExtension::GetPersistReference3.

```vb
//---------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
 // 3. Ensure that the specified file to open exists.
 // 4. Ensure that the c:\temp folder exists.
 //
 // Postconditions:
 // 1. Opens the specified file.
 // 2. Creates a linear harmonic dynamic study.
 // 3. Runs an analysis.
 // 4. Prints the study options and results to the Immediate window.
 // 5. Saves the solution step, displacement, velocity,
 //    and stress result files to c:\temp.
 // 6. Right-click the Stress1 or Displacement1 plot in the Results folder
 //    and click Show to plot the results in color in the graphics area.
 //
 // NOTE: Because the model is used elsewhere, do not save any changes.
 //---------------------------------------------------------------------------

 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.swconst;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.cosworks;
 using System.Runtime.InteropServices;
 namespace CreateDynHarmStudy_CSharp.csproj
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
             CWShellManager ShellMgr = default(CWShellManager);
             CWMaterial ShellMat = default(CWMaterial);
             CWLoadsAndRestraintsManager LBCMgr = default(CWLoadsAndRestraintsManager);
             CWBaseExcitation CWBaseExcitationU = default(CWBaseExcitation);
             CWDistributedMass CWDistribMass = default(CWDistributedMass);
             object CWBaseExcitationEntity = null;
             object CWDirectionEntity = null;
             int longstatus = 0;
             int longwarnings = 0;
             int errCode = 0;
             bool boolstatus = false;
             int nStep = 0;
             object pDisp5 = null;
             object[] DispArray1 = new object[1];
             object[] DispArray3 = new object[1];
             object[] Disp = null;
             object[] Stress = null;
             object[] Velocity = null;
             object[] Acceleration = null;
             string sStudyName = null;
             CWStudyResultOptions ResultOptions = default(CWStudyResultOptions);
             CWDampingOptions DampingOptions = default(CWDampingOptions);
             object[] DampingRatios = new object[9];
             int i = 0;

             //Tolerances and baselines
             const double MeshEleSize = 26.5868077635828;
             const double MeshTol = 1.32934038817914;

             //Open document
             Part = swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\lineardynamic.SLDPRT", (int)swDocumentTypes_e.swDocPART, (int) swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref longstatus, ref longwarnings);
             if (Part == null)
                 ErrorMsg(swApp, "Failed to open lineardynamic.SLDPRT");

             //Add-in callback
             CWAddinCallBack = (CwAddincallback)swApp.GetAddInObject("CosmosWorks.CosmosWorks");
             if (CWAddinCallBack == null)
                 ErrorMsg(swApp, "Failed to get CwAddincallback object");
             COSMOSWORKS = CWAddinCallBack.CosmosWorks;
             if (COSMOSWORKS == null)
                 ErrorMsg(swApp, "Failed to get CosmosWorks object");

             //Get active document
             ActDoc = COSMOSWORKS.ActiveDoc;
             if (ActDoc == null)
                 ErrorMsg(swApp, "Failed to get active document");

             //Create a dynamic harmonic study
             StudyMngr = ActDoc.StudyManager;
             if (StudyMngr == null)
                 ErrorMsg(swApp, "Failed to get study manager object");

             sStudyName = "Dynamic_Harmonic";
             Study = StudyMngr.CreateNewStudy3(sStudyName, (int)swsAnalysisStudyType_e.swsAnalysisStudyTypeDynamic, (int)swsDynamicAnalysisSubType_e.swsDynamicAnalysisSubTypeHarmonic, out errCode);

             Debug.Print("Linear dynamic study with harmonic analysis");
             Debug.Print("");
             Debug.Print("Study configuration name is " + Study.ConfigurationName);
             Debug.Print("Dynamic analysis subtype as defined in swsAnalysisStudyType_e is " + Study.DynamicAnalysisSubType);
             Debug.Print("Dynamic study options...");

             CWDynamicStudyOptions DynStudyOptions = default(CWDynamicStudyOptions);
             DynStudyOptions = Study.DynamicStudyOptions;
             int freqOption = 0;
             double freqValue = 0;
             bool bChecked = false;
             errCode = DynStudyOptions.GetFrequencyOption2(out freqOption, out freqValue);
             Debug.Print("  Frequency option (0=number of frequencies, 1=upper bound): " + freqOption);
             Debug.Print("  No. of frequencies or upper-bound frequency: " + freqValue);
             errCode = DynStudyOptions.GetFrequencyShiftOption2(out bChecked, out freqValue);
             Debug.Print("  Is frequency shift enabled (0=no, 1=yes)? " + bChecked);
             Debug.Print("  Frequency shift: " + freqValue);
             errCode = DynStudyOptions.SetIncompatibleBondingOption2(0); // automatic
             errCode = DynStudyOptions.SetUseSoftSpring3(0); // do not use soft springs to stabilize model
             errCode = DynStudyOptions.SetResultFolderPath2("c:\\temp");
             DynStudyOptions.SolverType = 2; // FFEPlus

             double harmbandwidth = 0;
             errCode = DynStudyOptions.GetHarmonicBandwidth2(out harmbandwidth);
             Debug.Print("  Harmonic bandwidth: " + harmbandwidth);
             double freqLowerLimit = 0;
             errCode = DynStudyOptions.GetHarmonicFrequencyLowerLimit2(out freqLowerLimit);
             Debug.Print("  Harmonic frequency lower limit: " + freqLowerLimit);
             double freqUpperLimit = 0;
             errCode = DynStudyOptions.GetHarmonicFrequencyUpperLimit2(out freqUpperLimit);
             Debug.Print("  Harmonic frequency upper limit: " + freqUpperLimit);
             int freqUnits = 0;
             errCode = DynStudyOptions.GetHarmonicFrequencyUnits2(out freqUnits);
             Debug.Print("  Harmonic frequency units (0=rad/sec, 1=Hz): " + freqUnits);
             int interpolation = 0;
             errCode = DynStudyOptions.GetHarmonicInterpolation2(out interpolation);
             Debug.Print("  Harmonic interpolation (0=logarithmic, 1=linear): " + interpolation);
             int points = 0;
             errCode = DynStudyOptions.GetHarmonicNoOfPoints2(out points);
             Debug.Print("  Harmonic number of points for each frequency: " + points);
             Debug.Print("");

             //Set study result options
             Debug.Print("Study result options...");
             ResultOptions = Study.StudyResultOptions;
             ResultOptions.SaveResultsForSolutionStepsOption = 1; // save solution step results
             ResultOptions.SaveDisplacementsAndVelocitiesOption = 1; // save displacements and velocities
             boolstatus = ResultOptions.SetSaveStressAndReactionsOptions2(-1, 0); // save stresses and reactions for all stress components

             //Solution step set #1
             errCode = ResultOptions.SetSolutionStepsSetInformation(1, 10, 100, 3);
             Debug.Print("  Set solution steps set #1 (10-100, inc=3)? (0=success): " + errCode);
             //Solution step set #3
             errCode = ResultOptions.SetSolutionStepsSetInformation(3, 100, 1000, 5);
             Debug.Print("  Set solution steps set #3 (100-1000, inc=5)? (0=success): " + errCode);
             Debug.Print("");

             //Set damping options
             DampingOptions = Study.DampingOptions;
             DampingOptions.DampingType = 0; //modal damping
            DampingOptions.ComputeFromMaterialDamping2 = 0; // do not use material damping ratios
             DampingOptions.ClearAllDampingRatios();
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

             object PID = null;
             object SelObj = null;
             object obj = null;

             //Get face by persistent ID
             boolstatus = Part.Extension.SelectByID2("", "FACE", 0.367377178180561, 0.0153999999998859, -0.443699715030164, false, 0, null, 0);
             obj = ((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(1, -1);
             PID = Part.Extension.GetPersistReference3(obj);
             SelObj = Part.Extension.GetObjectByPersistReference3((PID), out errCode);
             DispArray1[0] = SelObj; //Face

             //Get edge by persistent ID
             boolstatus = Part.Extension.SelectByID2("", "EDGE", 0.473843326221299, 0.0160904480509885, -0.000690335842989498, false, 0, null, 0);
             obj = ((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(1, -1);
             PID = Part.Extension.GetPersistReference3(obj);
             CWBaseExcitationEntity = Part.Extension.GetObjectByPersistReference3((PID), out errCode);
             DispArray3[0] = CWBaseExcitationEntity; //Edge

             //Get Axis1 reference geometry by persistent ID
             boolstatus = Part.Extension.SelectByID2("Axis1", "AXIS", -0.0320045390890095, 0.0639408825367532, -0.0319259521004658, false, 0, null, 0);
             obj = ((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(1, -1);
             PID = Part.Extension.GetPersistReference3(obj);
             CWDirectionEntity = Part.Extension.GetObjectByPersistReference3((PID), out errCode);
             pDisp5 = CWDirectionEntity;

             //Add materials
             ShellMgr = Study.ShellManager;
             if (ShellMgr == null)
                 ErrorMsg(swApp, "Failed to get shell manager object");

             CWShell CWFeatObj1 = default(CWShell);
             CWFeatObj1 = ShellMgr.GetShellAt(0, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to get shell component");
             ShellMat = CWFeatObj1.GetDefaultMaterial();
             ShellMat.MaterialUnits = 0;
             ShellMat.SetPropertyByName("EX", 2000000000000.0, 0);
             ShellMat.SetPropertyByName("NUXY", 0.25, 0);
             errCode = CWFeatObj1.SetShellMaterial(ShellMat);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to apply material");

             CWFeatObj1.ShellBeginEdit();
             CWFeatObj1.Formulation = 1;  // thick shell
             CWFeatObj1.ShellUnit = 1;  // centimeters
             CWFeatObj1.ShellThickness = 5;  // 5 cm
             CWFeatObj1.ShellOffsetOption = 3; // specify reference surface
             CWFeatObj1.ShellOffsetValue = 0.3;
             errCode = CWFeatObj1.ShellEndEdit();
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to create shell");
             CWFeatObj1 = null;

             //Get loads and restraints manager
             LBCMgr = Study.LoadsAndRestraintsManager;
             if (LBCMgr == null)
                 ErrorMsg(swApp, "Failed to get loads and restraints manager");

             //Create normal pressure
             CWPressure CWFeatObj2 = default(CWPressure);
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
             CWFeatObj2 = null;
             Debug.Print(" ");

             //Add a restraint
             CWRestraint CWFeatObj3 = default(CWRestraint);
             CWFeatObj3 = LBCMgr.AddRestraint(0, (DispArray3), pDisp5, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to create restraint");
             CWFeatObj3.RestraintBeginEdit();
             CWFeatObj3.SetTranslationComponentsValues(0, 0, 1, 0.0, 0.0, 0.0);
             CWFeatObj3.SetRotationComponentsValues(0, 0, 0, 0.0, 0.0, 0.0);
             CWFeatObj3.Unit = 2;
             errCode = CWFeatObj3.RestraintEndEdit();
             if (errCode != 0)
                 ErrorMsg(swApp, "Restraint end-edit failed");

             //Add uniform base excitation
             CWBaseExcitationU = LBCMgr.AddUniformBaseExcitation2((int)swsBaseExcitationType_e.swsBaseExcitationType_Acceleration, CWBaseExcitationEntity, (int)swsAccelerationUnit_e.swsAccelerationUnit_InchesPerSquareSec, -1, 2.3, -1, 3.4, -1, 4.5, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Adding uniform base excitation failed");
             Debug.Print("Uniform base excitation type (0=Disp, 1=Vel, 2=Acc): " + CWBaseExcitationU.BaseExcitationType);
             int bdir1 = 0;
             int bdir2 = 0;
             int bdir3 = 0;
             int bang = 0;
             CWBaseExcitationU.GetExcitationDirections2(out bdir1, out bdir2, out bdir3);
             Debug.Print(" Excitation in...");
             Debug.Print("   Direction 1 (-1=true)? " + bdir1);
             Debug.Print("   Direction 2 (-1=true)? " + bdir2);
             Debug.Print("   Direction 3 (-1=true)? " + bdir3);
             double dval1 = 0;
             double dval2 = 0;
             double dval3 = 0;
             CWBaseExcitationU.GetExcitationDirectionValues(out dval1, out dval2, out dval3);
             CWBaseExcitationU.GetExcitationReverseDirections2(out bdir1, out bdir2, out bdir3, out bang);
             Debug.Print(" Excitation values...");
             Debug.Print(" Units as defined in swsAccelerationUnit_e: " + CWBaseExcitationU.Unit);
             Debug.Print("   Direction 1: " + dval1);
             Debug.Print("     Reversed? (-1=true) " + bdir1);
             Debug.Print("   Direction 2: " + dval2);
             Debug.Print("     Reversed? (-1=true) " + bdir2);
             Debug.Print("   Direction 3: " + dval3);
             Debug.Print("     Reversed? (-1=true) " + bdir3);
             Debug.Print("   Phase angle (-1 if not set): " + CWBaseExcitationU.PhaseAngle);
             Debug.Print("     Reversed? (-1=true) " + bang);
             Debug.Print("     Units as defined in swsPhaseAngleUnit_e: " + CWBaseExcitationU.PhaseAngleUnit);
             object[] curveData = null;
             curveData = (object[])CWBaseExcitationU.GetTimeOrFrequencyCurve();
             //variation with frequency data
             Debug.Print(" Acceleration excitation variation with frequency data");
             Debug.Print(" (number of points, x1, y1, x2, y2...xn, yn):");
             for (i = 0; i <= curveData.GetUpperBound(0); i++)
             {
                 Debug.Print("  * " + curveData[i]);
             }
             Debug.Print("");

             //Add distributed mass
             CWDistribMass = LBCMgr.AddDistributedMass((DispArray1), 0, 1, ref errCode);
             Debug.Print("Total distributed mass: " + CWDistribMass.TotalMass);
             Debug.Print("  Units in swsUnitSystem_e units: " + CWDistribMass.Units);
             Debug.Print("");

             //Create mesh
             CWMesh CWFeatObj4 = default(CWMesh);
             CWFeatObj4 = Study.Mesh;
             if (CWFeatObj4 == null)
                 ErrorMsg(swApp, "Failed to create mesh object");
             CWFeatObj4.MesherType = 0;
             CWFeatObj4.Quality = 1;

             errCode = Study.CreateMesh(0, MeshEleSize, MeshTol);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to create mesh");
             Debug.Print("Worst Jacobian ratio for the mesh: " + CWFeatObj4.GetWorstJacobianRatio());
             Debug.Print("");

             //Run analysis
             Debug.Print("Running the analysis");
             Debug.Print("");
             errCode = Study.RunAnalysis();
             if (errCode != 0)
                 ErrorMsg(swApp, "Analysis failed with error code as defined in swsRunAnalysisError_e:" + errCode);

             //Get results
             CWResults CWFeatObj5 = default(CWResults);
             CWFeatObj5 = Study.Results;
             if (CWFeatObj5 == null)
                 ErrorMsg(swApp, "Failed to get Results object");

             Debug.Print("Study results...");
             nStep = CWFeatObj5.GetMaximumAvailableSteps();
             Debug.Print("  Maximum available steps: " + nStep);

             //Get algebraic minimum/maximum resultant displacements
             Disp = (object[])CWFeatObj5.GetMinMaxDisplacement(3, nStep, null, 0, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to get displacement results");
             Debug.Print("  Min/Max URES Resultant Displacements (Node, Min, Node, Max):");
             for (i = 0; i <= Disp.GetUpperBound(0); i++)
             {
                 Debug.Print("  * " + Disp[i]);
             }
             Debug.Print("");

             //Get algebraic minimum/maximum von Mises stresses
             Stress = (object[])CWFeatObj5.GetMinMaxStress(9, 0, nStep, null, 3, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to get stress results");
             Debug.Print("  Algebraic Min/Max von Mises Stresses (Node, Min, Node, Max):");
             for (i = 0; i <= Stress.GetUpperBound(0); i++)
             {
                 Debug.Print("  * " + Stress[i]);
             }
             Debug.Print("");

             //Get algebraic minimum/maximum velocities
             Velocity = (object[])CWFeatObj5.GetMinMaxVelocity(0, nStep, CWDirectionEntity, 0, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to get velocity results");
             Debug.Print("  Algebraic Min/Max Velocities (Node, Min, Node, Max):");
             for (i = 0; i <= Velocity.GetUpperBound(0); i++)
             {
                 Debug.Print("  * " + Velocity[i]);
             }
             Debug.Print("");

             //Get algebraic minimum/maximum accelerations
             Acceleration = (object[])CWFeatObj5.GetMinMaxAcceleration(0, nStep, CWDirectionEntity, 0, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to get acceleration results");
             Debug.Print("  Algebraic Min/Max Accelerations (Node, Min, Node, Max):");
             for (i = 0; i <= Acceleration.GetUpperBound(0); i++)
             {
                 Debug.Print("  * " + Acceleration[i]);
             }

            Debug.Print("");

             object[] forces2 = null;
             object selectedAndModelReactionFM = null;
             object selectedOnlyReactionFM = null;
             // Reaction forces and moments for entire model and selected face at solution step 59
             forces2 = (object[])CWFeatObj5.GetReactionForcesAndMomentsWithSelections(59, null, (int)swsForceUnit_e.swsForceUnitNOrNm, (DispArray1), out selectedAndModelReactionFM, out selectedOnlyReactionFM, out errCode);
             object[] selFM = (object[])selectedOnlyReactionFM;
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to get reaction forces and moments");
             Debug.Print("  Reaction forces (N) and moments (N-m) for selected face ");
             Debug.Print("  {xcoord_force, ycoord_force, zcoord_force, resultant_force, ");
             Debug.Print("   xcoord_moment, ycoord_moment, zcoord_moment, resultant_moment}:");
             for (i = 0; i <= selFM.GetUpperBound(0); i++)
             {
                 Debug.Print("  * " + selFM[i]);
             }

         }

         public void ErrorMsg(SldWorks SwApp, string Message)
         {
             SwApp.SendMsgToUser2(Message, 0, 0);
             SwApp.RecordLine("'*** WARNING - General");
             SwApp.RecordLine("'*** " + Message);
             SwApp.RecordLine("");
         }

         public SldWorks swApp;

     }

 }
```
