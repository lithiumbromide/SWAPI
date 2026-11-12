---
title: "Create Linear Dynamic Time History Study Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Dynamic_Time_History_Study_Example_CSharp.htm"
---

# Create Linear Dynamic Time History Study Example (C#)

This example shows how to create a linear dynamic study with a modal time history analysis and get some study options.

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
  // 2. Creates a linear dynamic study for modal time history analysis.
 // 3. Runs the analysis.
  // 4. Prints some study options and results to the Immediate window.
  // 5. Saves the solution step, displacement, velocity,
 //    and stress result files to c:\temp.
 //
  // NOTE: Because the model is used elsewhere, do not save any changes.
  //---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.cosworks;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace CreateDynTimeHistStudy_CSharp.csproj
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
             CWDynamicStudyOptions DynStudyOptions = default(CWDynamicStudyOptions);
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
             int i = 0;
             int freqOption = 0;
             double freqValue = 0;
             bool bChecked = false;
             object forces2 = null;
             object selectedAndModelReactionFM = null;
             object selectedOnlyReactionFM = null;
             CWShell CWFeatObj1 = default(CWShell);
             CWRestraint CWFeatObj3 = default(CWRestraint);
             CWMesh CWFeatObj4 = default(CWMesh);
             CWResults CWFeatObj5 = default(CWResults);
             CWDynamicInitialCondition CWFeatObj6 = default(CWDynamicInitialCondition);
             int param = 0;
             string sParam = "";
             double dParam = 0;
             double dStartTime = 0;
             double dEndTime = 0;
             double dTimeInc = 0;

             //Tolerances and baselines
             const double MeshEleSize = 26.5868077635828;
             const double MeshTol = 1.32934038817914;

             //Open document
             Part = swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\lineardynamic.SLDPRT", (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref longstatus, ref longwarnings);
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

             //Create a dynamic random vibration study
             StudyMngr = ActDoc.StudyManager;
             if (StudyMngr == null)
                 ErrorMsg(swApp, "Failed to get study manager object");
             sStudyName = "Dynamic_Modal_Time_History";
             Study = StudyMngr.CreateNewStudy3(sStudyName, (int)swsAnalysisStudyType_e.swsAnalysisStudyTypeDynamic, (int)swsDynamicAnalysisSubType_e.swsDynamicAnalysisSubTypeTransient, out errCode);
             Debug.Print("Linear dynamic study with modal time history analysis");
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
             errCode = DynStudyOptions.SetIncompatibleBondingOption2(0); // automatic
             errCode = DynStudyOptions.SetUseSoftSpring2(0); // do not use soft springs to stabilize model
             errCode = DynStudyOptions.SetResultFolderPath2("c:\\temp");
             DynStudyOptions.SolverType = 2;  // FFEPlus
             errCode = DynStudyOptions.GetTimeHistoryDeadLoadOptions2(out bChecked, out sParam, out dParam);
             Debug.Print("  Get dead loads from a static study (true to get them, false to not): " + bChecked);
             Debug.Print("  Name of static study from which to get dead loads: " + sParam);
             Debug.Print("  Multiplication factor: " + dParam);
             errCode = DynStudyOptions.GetTimeHistoryFirstIntegrationParameter2(out dParam);
             Debug.Print("  First integration parameter: " + dParam);
             errCode = DynStudyOptions.GetTimeHistoryIntegrationMethod2(out param);
             Debug.Print("  Integration method as defined in swsTimeIntegrationMethod_e: " + param);
             errCode = DynStudyOptions.GetTimeHistorySecondIntegrationParameter2(out dParam);
             Debug.Print("  Second integration parameter): " + dParam);
             errCode = DynStudyOptions.GetTimeHistoryTimeRangeValues2(out dStartTime, out dEndTime, out dTimeInc);
             Debug.Print("  Use the material damping ratio? (1 to use, 0 to not): " + dStartTime);
             Debug.Print("  Use the material damping ratio? (1 to use, 0 to not): " + dEndTime);
             Debug.Print("  Use the material damping ratio? (1 to use, 0 to not): " + dTimeInc);
             errCode = DynStudyOptions.GetTimeHistoryWilsonTheta2(out dParam);
             Debug.Print("  Theta value: " + param);
             Debug.Print("");

             //Set study result options
             Debug.Print("Study result options...");
             ResultOptions = Study.StudyResultOptions;
             ResultOptions.SaveResultsForSolutionStepsOption = 1; // save solution step results
             ResultOptions.SaveDisplacementsAndVelocitiesOption = 1; // save displacements and velocities
             ResultOptions.SaveStresses = 1;  // save stresses

             //Solution step set #1
             errCode = ResultOptions.SetSolutionStepsSetInformation(1, 10, 100, 3);
             Debug.Print("  Set solution steps set #1 (10-100, inc=3)? (0=success): " + errCode);

             //Solution step set #3
             errCode = ResultOptions.SetSolutionStepsSetInformation(3, 100, 1000, 5);
             Debug.Print("  Set solution steps set #3 (100-1000, inc=5)? (0=success): " + errCode);
             Debug.Print("");
             object PID = null;
             object SelObj = null;
             object obj = null;

             //Get face by persistent ID
             boolstatus = Part.Extension.SelectByID2("", "FACE", 0.367377178180561, 0.0153999999998859, -0.443699715030164, false, 0, null, 0);
             obj = ((SelectionMgr)Part.SelectionManager).GetSelectedObject6(1, -1);
             PID = Part.Extension.GetPersistReference3(obj);
             SelObj = Part.Extension.GetObjectByPersistReference3((PID), out errCode);
             DispArray1[0] = SelObj;

             //Get edge by persistent ID
             boolstatus = Part.Extension.SelectByID2("", "EDGE", 0.473843326221299, 0.0160904480509885, -0.000690335842989498, false, 0, null, 0);
             obj = ((SelectionMgr)Part.SelectionManager).GetSelectedObject6(1, -1);
             PID = Part.Extension.GetPersistReference3(obj);
             CWBaseExcitationEntity = Part.Extension.GetObjectByPersistReference3((PID), out errCode);
             DispArray3[0] = CWBaseExcitationEntity;

             //Get Axis1 reference geometry by persistent ID
             boolstatus = Part.Extension.SelectByID2("Axis1", "AXIS", -0.0320045390890095, 0.0639408825367532, -0.0319259521004658, false, 0, null, 0);
             obj = ((SelectionMgr)Part.SelectionManager).GetSelectedObject6(1, -1);
             PID = Part.Extension.GetPersistReference3(obj);
             CWDirectionEntity = Part.Extension.GetObjectByPersistReference3((PID), out errCode);
             pDisp5 = CWDirectionEntity;

             //Add materials
             ShellMgr = Study.ShellManager;
             if (ShellMgr == null)
                 ErrorMsg(swApp, "Failed to get shell manager object");
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
             CWFeatObj1.Formulation = 1; // thick shell
             CWFeatObj1.ShellUnit = 1; // centimeters
             CWFeatObj1.ShellThickness = 5;  // 5 cm
             CWFeatObj1.ShellOffsetOption = 3;  // specify reference surface
             CWFeatObj1.ShellOffsetValue = 0.3;
             errCode = CWFeatObj1.ShellEndEdit();
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to create shell");
             CWFeatObj1 = null;

             //Get loads and restraints manager
             LBCMgr = Study.LoadsAndRestraintsManager;
             if (LBCMgr == null)
                 ErrorMsg(swApp, "Failed to get loads and restraints manager.");
             Debug.Print(" ");

             //Add a restraint
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
             //Apply an initial (time = 0) condition to the face in DispAarray1 using the direction reference edge in CWBaseExcitationEntity
             CWFeatObj6 = LBCMgr.AddInitialConditionForDynamicStudy2((int)swsDynamicInitialConditionType_e.swsDynamicInitialConditionType_Displacement, (int)swsSelectionType_e.swsSelectionFaceEdgeVertexPoint, (DispArray1), CWBaseExcitationEntity, (int)swsLinearUnit_e.swsLinearUnitMillimeters, 0, 0, 0, 0, -1,
                 10.0, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to add initial condition");
             int bval1 = 0;
             int bval2 = 0;
             int bval3 = 0;
             int bdir1 = 0;
             int bdir2 = 0;
             int bdir3 = 0;
             double dval1 = 0;
             double dval2 = 0;
             double dval3 = 0;
             CWFeatObj6.GetDirections2(out bdir1, out bdir2, out bdir3);
             CWFeatObj6.GetValues(out dval1, out dval2, out dval3);
             CWFeatObj6.GetReverseDirections2(out bval1, out bval2, out bval3);
             Debug.Print("Initial condition:");
             Debug.Print("  Type as defined in swsDynamicInitialConditionType_e: " + CWFeatObj6.InitialConditionType);
             if (CWFeatObj6.InitialConditionType == 0)
             {
                 Debug.Print("  Units as defined in swsLinearUnit_e: " + CWFeatObj6.Units);
             }
             Debug.Print("  Direction reference is an edge.");
             Debug.Print("    Apply initial condition along the edge? (-1=yes, 0=no) " + bdir3);
             Debug.Print("        Value: " + dval3);
             Debug.Print("        Reverse? (-1=yes, 0=no) " + bval3);

             //Create mesh
             CWFeatObj4 = Study.Mesh;
             if (CWFeatObj4 == null)
                 ErrorMsg(swApp, "Failed to create mesh object");
             CWFeatObj4.MesherType = 0; // standard
             CWFeatObj4.Quality = 1;  // high
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
                 ErrorMsg(swApp, "Analysis failed with error code as defined in swsRunAnalysisError_e: " + errCode);

             //Get results
             CWFeatObj5 = Study.Results;
             if (CWFeatObj5 == null)
                 ErrorMsg(swApp, "Failed to get results object");
             Debug.Print("Study results...");
             nStep = CWFeatObj5.GetMaximumAvailableSteps();
             Debug.Print("  Maximum available steps: " + nStep);

             //Get algebraic minimum/maximum resultant displacements
             Disp = (object[])CWFeatObj5.GetMinMaxDisplacement(3, nStep, null, 0, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to get displacement results");
             Debug.Print("  Min/max URES resultant displacements (Node, Min, Node, Max):");
             for (i = 0; i <= Disp.GetUpperBound(0); i++)
             {
                 Debug.Print("  * " + Disp[i]);
             }
             Debug.Print("");

             //Get algebraic minimum/maximum von Mises stresses
             Stress = (object[])CWFeatObj5.GetMinMaxStress(9, 0, nStep, null, 3, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to get stress results");
             Debug.Print("  Algebraic min/max von Mises stresses (Node, Min, Node, Max):");
             for (i = 0; i <= Stress.GetUpperBound(0); i++)
             {
                 Debug.Print("  * " + Stress[i]);
             }
             Debug.Print("");

             //Get algebraic minimum/maximum velocities
             Velocity = (object[])CWFeatObj5.GetMinMaxVelocity(0, nStep, CWDirectionEntity, 0, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to get velocity results");
             Debug.Print("  Algebraic min/max velocities (Node, Min, Node, Max):");
             for (i = 0; i <= Velocity.GetUpperBound(0); i++)
             {
                 Debug.Print("  * " + Velocity[i]);
             }
             Debug.Print("");

             //Get algebraic minimum/maximum accelerations
             Acceleration = (object[])CWFeatObj5.GetMinMaxAcceleration(0, nStep, CWDirectionEntity, 0, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to get acceleration results");
             Debug.Print("  Algebraic min/max accelerations (Node, Min, Node, Max):");
             for (i = 0; i <= Acceleration.GetUpperBound(0); i++)
             {
                 Debug.Print("  * " + Acceleration[i]);
             }

             //Reaction forces and moments for entire model and selected face at solution step 31
             forces2 = CWFeatObj5.GetReactionForcesAndMomentsWithSelections(31, null, (int)swsForceUnit_e.swsForceUnitNOrNm, (DispArray1), out selectedAndModelReactionFM, out selectedOnlyReactionFM, out errCode);
             object[] selFM = (object[])selectedOnlyReactionFM;
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to get reaction forces and moments");
             Debug.Print("  Reaction forces (N) and moments (N-m) for selected face at solution step 1 ");
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

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```
