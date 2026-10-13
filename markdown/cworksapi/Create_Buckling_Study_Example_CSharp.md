---
title: "Create Buckling Study Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Buckling_Study_Example_CSharp.htm"
---

# Create Buckling Study Example (C#)

This example shows how to create and analyze a buckling study.

NOTE: To get persistent reference identifiers (PIDs) for model selections, you can use [pidcollector.exe](GettingStarted-swsimulationapi.html) or IModelDocExtension::GetPersistReference3.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
  // 3. Ensure that the specified model document exists.
  // 4. Ensure that the specified materials library exists.
 // 5. Open an Immediate window.
 //
 // Postconditions:
 // 1. Opens the specified model document.
 // 2. Creates new study, Buckling1.
 // 3. Prints the study options of Buckling1 to the Immediate window.
 // 4. Adds AISI 1020 steel to the solid bodies in the model.
 // 5. Adds Fixed-1 restraint to Buckling1.
 // 6. Adds Pressure-1 load  to Buckling1.
 // 7. Meshes the bodies in the model.
 // 8. Analyzes Buckling1.
  // 9. Inspect the Immediate window, the Simulation study tree, and the
 //    graphics area.
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
 namespace CreateBucklingStudy_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Part;
         CosmosWorks COSMOSWORKS;
         CwAddincallback CWAddinCallBack;
         CWModelDoc ActDoc;
         CWStudyManager StudyMngr;
         CWStudy Study;
         CWSolidManager SolidMgr;
         CWSolidComponent SolidComp;
         CWSolidBody SolidBody;
         CWLoadsAndRestraintsManager LBCMgr;
         CWPressure CWPressureLoad;
         int errCode;
         int intStatus;
         int longstatus;
         int longwarnings;
         object[] DispArray2 = new object[1];
         object[] DispArray3 = new object[1];
         const double MeshEleSize = 4.48279654351123;
         const double MeshTol = 0.224139827175561;
         const double Tol1 = 0.05;

         public void Main()
         {
             Part = swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2017\\Simulation Examples\\Educational Examples\\spider.sldasm", 2, 0, "", ref longstatus, ref longwarnings);
             Part = (ModelDoc2)swApp.ActiveDoc;

             Hashtable PIDCollection = new Hashtable();
             PIDCollection = PIDInitializer();

             string strMaterialLib = null;
             strMaterialLib = swApp.GetExecutablePath() + "\\lang\\english\\sldmaterials\\solidworks materials.sldmat";

             DispArray2[0] = new DispatchWrapper(SelectByPID(Part, "selection2", PIDCollection)); // cylindrical face
             DispArray3[0] = new DispatchWrapper(SelectByPID(Part, "selection3", PIDCollection)); // arm

             CWAddinCallBack = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
             if (CWAddinCallBack == null)
                 ErrorMsg(swApp, "Failed to get Simulation add-in");
             COSMOSWORKS = CWAddinCallBack.CosmosWorks;
             if (COSMOSWORKS == null)
                 ErrorMsg(swApp, "Failed to get CosmosWorks");

             ActDoc = COSMOSWORKS.ActiveDoc;
             if (ActDoc == null)
                 ErrorMsg(swApp, "Failed to get active document");

             //Create new buckling study
             StudyMngr = ActDoc.StudyManager;
             if (StudyMngr == null)
                 ErrorMsg(swApp, "Failed to get the study manager");
             Study = StudyMngr.CreateNewStudy3("Buckling1", (int)swsAnalysisStudyType_e.swsAnalysisStudyTypeBuckling, 0, out errCode);
             if (Study == null)
                 ErrorMsg(swApp, "Failed to create new study");

             //Buckling study options
             CWBucklingStudyOptions bsOptions = default(CWBucklingStudyOptions);
             bsOptions = Study.BucklingStudyOptions;
             Debug.Print("");
             Debug.Print("Buckling study options");
             Debug.Print("  Number of buckling modes: " + bsOptions.BucklingModes);
             double zeroStrainTemp = 0;
             int tempUnit = 0;
             bsOptions.GetZeroStrainTemperature(out zeroStrainTemp, out tempUnit);
             Debug.Print("  Flow/Thermal Effects:");
             Debug.Print("    Temperature source as defined in swsThermalOption_e: " + bsOptions.ThermalResults);
             Debug.Print("    Temperature source:");
             if (bsOptions.ThermalResults == 1)
             {
                 Debug.Print("        Thermal study: " + bsOptions.ThermalStudyName);
                 Debug.Print("        Time step of transient thermal study: " + bsOptions.TimeStep);
             }
             else if (bsOptions.ThermalResults == 2)
             {
                 Debug.Print("        SOLIDWORKS Flow Simulation results file: " + bsOptions.FlowTemperatureFile);
             }
             else
             {
                 Debug.Print("        Model");
             }
             Debug.Print("    Reference temperature at zero strain: " + zeroStrainTemp);

             Debug.Print("    Import fluid pressure loads from SOLIDWORKS Flow Simulation? (true=yes, false=no): " + bsOptions.CheckFlowPressure2);
             if (bsOptions.CheckFlowPressure == 1)
             {
                 Debug.Print("        SOLIDWORKS Flow Simulation results file: " + bsOptions.FlowPressureFile);
                 Debug.Print("        Use reference pressure offset from Flow Simulation? (1=yes, 0=no): " + bsOptions.ReferencePressureOption);
                 if (bsOptions.ReferencePressureOption == 0)
                 {
                     Debug.Print("          Reference pressure offset: " + bsOptions.DefinedReferencePressure);
                 }
                 Debug.Print("        Run as legacy study and import only the normal component of the pressure load? (true=yes, false=no): " + bsOptions.CheckRunAsLegacy2);
             }
             Debug.Print("  Result folder: " + bsOptions.ResultFolder);
             Debug.Print("  Solver type as defined in swsSolverType_e: " + bsOptions.SolverType);
             Debug.Print("  Use soft spring to stabilize the model? (true=yes, false=no): " + bsOptions.UseSoftSpring2);

             //Add materials
             SolidMgr = Study.SolidManager;
             if (SolidMgr == null)
                 ErrorMsg(swApp, "Failed to get solid manager");
             SolidComp = SolidMgr.GetComponentAt(0, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to get component");
             SolidBody = SolidComp.GetSolidBodyAt(0, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to get solid body");
             intStatus = SolidBody.SetLibraryMaterial(strMaterialLib, "AISI 1020");
             if (intStatus != 1)
                 ErrorMsg(swApp, "Failed to apply material");

             SolidComp = SolidMgr.GetComponentAt(1, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to get component");
             SolidBody = SolidComp.GetSolidBodyAt(0, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to get solid body");
             intStatus = SolidBody.SetLibraryMaterial(strMaterialLib, "AISI 1020");
             if (intStatus != 1)
                 ErrorMsg(swApp, "Failed to apply material");

             SolidComp = SolidMgr.GetComponentAt(2, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to get component");
             SolidBody = SolidComp.GetSolidBodyAt(0, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to get solid body");
             intStatus = SolidBody.SetLibraryMaterial(strMaterialLib, "AISI 1020");
             if (intStatus != 1)
                 ErrorMsg(swApp, "Failed to apply material");

             LBCMgr = Study.LoadsAndRestraintsManager;
             if (LBCMgr == null)
                 ErrorMsg(swApp, "Failed to get the loads and restraints manager");

             //Add a restraint
             CWRestraint restraint = default(CWRestraint);
             restraint = LBCMgr.AddRestraint((int)swsRestraintType_e.swsRestraintTypeFixed, (DispArray2), null, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to add a restraint");

             //Add a pressure load
             CWPressureLoad = LBCMgr.AddPressure((int)swsPressureType_e.swsPressureTypeNormal, (DispArray3), null, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to create a pressure load");

             //Create mesh
             CWMesh CWMeshObj = default(CWMesh);
             CWMeshObj = Study.Mesh;
             if (CWMeshObj == null)
                 ErrorMsg(swApp, "Failed to get the mesh object");
             CWMeshObj.MesherType = 0;
             CWMeshObj.Quality = 0;
             errCode = Study.CreateMesh(0, MeshEleSize, MeshTol);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to create the mesh");
             CWMeshObj = null;

             //Run analysis
             errCode = Study.RunAnalysis();
             if (errCode != 0)
                 ErrorMsg(swApp, "Analysis failed with error as defined in swsRunAnalysisError_e: " + errCode);

         }

         public void ErrorMsg(SldWorks SwApp, string Message)
         {
             SwApp.SendMsgToUser2(Message, 0, 0);
             SwApp.RecordLine("'*** WARNING - General");
             SwApp.RecordLine("'*** " + Message);
             SwApp.RecordLine("");
         }

         public object SelectByPID(ModelDoc2 Part, string PIDName, Hashtable PIDCollection)
         {
             object functionReturnValue = null;
             byte[] PID = null;
             string[] PIDVariant = null;
             string PIDString = null;
             int i = 0;
             object SelObj = null;

             //Get the value mapped to the PIDName key from the hashtable
             PIDString = "";
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
             SelObj = Part.Extension.GetObjectByPersistReference3((PID), out errCode);
             functionReturnValue = SelObj;
             return functionReturnValue;

         }

         public Hashtable PIDInitializer()
         {

             Hashtable PIDCollection = new Hashtable();

             string selection2 = null;
             string selection3 = null;

             //Cylindrical face
             selection2 = "64,31,0,0,3,0,0,0,255,254,255,14,115,0,104,0,97,0,102,0,116,0,45,0,49,0,64,0,115,0,112,0,105,0,100,0,101,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,10,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,97,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,32,0,67,0,111,0,114,0,112,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,92,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,69,0,100,0,117,0,99,0,97,0,11";
             selection2 = selection2 + "6,0,105,0,111,0,110,0,97,0,108,0,32,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,115,0,104,0,97,0,102,0,116,0,46,0,115,0,108,0,100,0,112,0,114,0,116,0,9,128,255,254,255,5,115,0,104,0,97,0,102,0,116,0,2,0,0,155,126,163,53,0,165,25,208,59,1,0,0,0,0,0,0,0,5,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,63,0,0,0,0,0,0,0,7,50,149,70,12,0,0,0,171,126,163,53,1,0,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,12,0,0,0,171,126,163,53,1,0,0,0,255,255,255,255,0,0,12,128,0,0,5,128,8,0,12,0,0,0,171,126,163,53,0,0,0,0,255,255,255,255,0,0,0,0,0,0,0,0,0,0";
             selection2 = selection2 + ",Type=1";

             //Arm
             selection3 = "64,31,0,0,3,0,0,0,255,254,255,15,115,0,112,0,105,0,100,0,101,0,114,0,45,0,49,0,64,0,115,0,112,0,105,0,100,0,101,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,9,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,8,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,98,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,32,0,67,0,111,0,114,0,112,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,92,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,69,0,100,0,117,0,99,0,9";
             selection3 = selection3 + "7,0,116,0,105,0,111,0,110,0,97,0,108,0,32,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,115,0,112,0,105,0,100,0,101,0,114,0,46,0,115,0,108,0,100,0,112,0,114,0,116,0,9,128,255,254,255,6,115,0,112,0,105,0,100,0,101,0,114,0,2,0,0,149,119,163,53,0,73,0,71,0,1,0,0,0,0,0,0,0,3,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,142,0,0,0,0,0,0,0,13,50,149,70,28,0,0,0,119,124,163,53,10,0,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,107,0,0,0,227,104,166,53,1,0,0,0,255,255,255,255,255,255,1,0,19,0,109,111,70,105,108,108,101,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,139,0,0,0,68,107,166,53,4,0,0,0,15,128,0,0,5,128,8,0,141,0,0,0,83,107,166,53,4,0,0,0,15,128,0,0,5,128,8,0,139,0,0,0,68,107,166,53,3,0,0,0,0,0,12,128,0,0,5,128,8,0,48,0,0,0,82,125,163,53,1,0,0,0,255,255,255,255,0,0,0,0,0,0,0,0,0,0";
             selection3 = selection3 + ",Type=1";

             //Store constants in a hashtable
             PIDCollection.Add("selection2", selection2);
             PIDCollection.Add("selection3", selection3);

             return PIDCollection;
         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }

 }
```
