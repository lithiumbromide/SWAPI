---
title: "Add Bearing Load Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Add_Bearing_Load_Example_CSharp.htm"
---

# Add Bearing Load Example (C#)

This example shows how to add a bearing load to a static study and get its properties.

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
  // 4. Ensure that the specified material library exists.
 // 5. Open an Immediate window.
 //
 // Postconditions:
 //  1. Opens the specified model document.
 //  2. Inserts Axis2 in the FeatureManager design tree.
 //  3. Inserts Coordinate System1 in the FeatureManager design tree.
 //  4. Creates new study, Static1.
 //  5. Applies AISI 1020 steel to the solid bodies in the model.
 //  6. Adds BearingLoads-1 to Static1.
 //  7. Adds Link Connector-1 to Static1.
 //  8. Prints the properties of BearingLoads-1 to the Immediate window.
 //  9. Meshes the bodies in the model.
 // 10. Sets the study options for Static1.
 // 11. Analyzes Static1.
 // 12. Inspect the Immediate window, FeatureManager design tree, and
 //     Simulation study tree.
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
 namespace AddBearingLoad_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Part;
         Feature coordSys;
         CosmosWorks COSMOSWORKS;
         CwAddincallback CWAddinCallBack;
         CWModelDoc ActDoc;
         CWStudyManager StudyMngr;
         CWStudy Study;
         CWSolidManager SolidMgr;
         CWSolidComponent SolidComp;
         CWSolidBody SolidBody;
         CWLoadsAndRestraintsManager LBCMgr;
         CWBearingLoad CWBearingLoad;
         CWLinkConnector CWLinkConnector;
         int errCode;
         int intStatus;
         bool boolstatus;
         int longstatus;
         int longwarnings;
         CWStaticStudyOptions StaticOptions;
         object DispArray1;
         object Vert1;
         object Vert2;
         object[] DispArray2 = new object[1];
         const double MeshEleSize = 4.48279654351123;
         const double MeshTol = 0.224139827175561;
         const double Tol1 = 0.05;

         public void Main()
         {
             Part = swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2017\\Simulation Examples\\Educational Examples\\spider.sldasm", 2, 0, "", ref longstatus, ref longwarnings);
             Part = (ModelDoc2)swApp.ActiveDoc;

             //Create Axis2
             boolstatus = Part.Extension.SelectByID2("", "FACE", 0.0073775062512027, 0.00602478435399689, 0.0537262605714091, true, 0, null, 0);
             boolstatus = Part.InsertAxis2(true);

             //Create Coordinate System1
             boolstatus = Part.Extension.SelectByID2("", "EDGE", 0.00252708736488216, 0.03884014356629, -0.0155712463055693, false, 2, null, 0);
             boolstatus = Part.Extension.SelectByID2("Axis2", "AXIS", 0, 0, 0, true, 8, null, 0);

             coordSys = Part.FeatureManager.InsertCoordinateSystem(false, false, false);

             Hashtable PIDCollection = new Hashtable();
             PIDCollection = PIDInitializer();

             string strMaterialLib = null;
             strMaterialLib = swApp.GetExecutablePath() + "\\lang\\english\\sldmaterials\\solidworks materials.sldmat";

             DispArray1 = SelectByPID(Part, "selection1", PIDCollection); // coordinate system
             DispArray2[0] = new DispatchWrapper(SelectByPID(Part, "selection2", PIDCollection)); // cylindrical face

            Vert1 = SelectByPID(Part, "selection3", PIDCollection); // link connector first location
             Vert2 = SelectByPID(Part, "selection4", PIDCollection); // link connector second location

             CWAddinCallBack = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
             if (CWAddinCallBack == null)
                 ErrorMsg(swApp, "Failed to get Simulation add-in");
             COSMOSWORKS = CWAddinCallBack.CosmosWorks;
             if (COSMOSWORKS == null)
                 ErrorMsg(swApp, "Failed to get CosmosWorks");

             ActDoc = COSMOSWORKS.ActiveDoc;
             if (ActDoc == null)
                 ErrorMsg(swApp, "Failed to get active document");

             //Create new static study
             StudyMngr = (CWStudyManager)ActDoc.StudyManager;
             if (StudyMngr == null)
                 ErrorMsg(swApp, "Failed to get the study manager");
             Study = StudyMngr.CreateNewStudy3("Static1", (int)swsAnalysisStudyType_e.swsAnalysisStudyTypeStatic, 0, out errCode);
             if (Study == null)
                 ErrorMsg(swApp, "Failed to create new study");

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

             //Add a bearing load
             LBCMgr = Study.LoadsAndRestraintsManager;
             if (LBCMgr == null)
                 ErrorMsg(swApp, "Failed to get the loads and restraints manager");

             CWBearingLoad = LBCMgr.AddBearingLoad(DispArray1, (DispArray2), ref errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to create a bearing load");

             CWBearingLoad.BearingLoadBeginEdit();
             CWBearingLoad.Direction = 1;
             CWBearingLoad.YDirectionValue = 1;
             CWBearingLoad.BearingLoadEndEdit();
             Debug.Print("Bearing load properties:");
             Debug.Print("  Unit system as defined in swsUnit_e: " + CWBearingLoad.BearingLoadUnit);
             Debug.Print("  Distribution type as defined in swsBearingLoadDistributionType_e: " + CWBearingLoad.DistributionType);
             Debug.Print("  Use time curve? (false = no, true = yes): " + CWBearingLoad.UseTimeCurve2);
             Debug.Print("  Bearing load values:");
             Debug.Print("    X direction: " + CWBearingLoad.XDirectionValue);
             Debug.Print("       Reverse? (false = no, true = yes): " + CWBearingLoad.XDirectionReverse2);
             Debug.Print("    Y direction: " + CWBearingLoad.YDirectionValue);
             Debug.Print("       Reverse? (false = no, true = yes): " + CWBearingLoad.YDirectionReverse2);

             //Add a link connector
             CWLinkConnector = LBCMgr.AddLinkConnector(Vert1, Vert2, out errCode);
             if (errCode != 0) ErrorMsg(swApp, "Failed to add a link connector");

             //Create mesh
             CWMesh CWMeshObj = default(CWMesh);
             CWMeshObj = Study.Mesh;
             if (CWMeshObj == null)
                 ErrorMsg(swApp, "Failed to create mesh object");
             CWMeshObj.MesherType = 0;
             CWMeshObj.Quality = 0;
             errCode = Study.CreateMesh(0, MeshEleSize, MeshTol);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to create mesh");
             CWMeshObj = null;

             //Set static study options
             StaticOptions = Study.StaticStudyOptions;
             if (StaticOptions == null)
                 ErrorMsg(swApp, "Failed to get static study options");
             StaticOptions.SolverType = 1;
             StaticOptions.UseSoftSpring = 1;
             StaticOptions.LargeDisplacement = 0;

             Debug.Print( "    Flow/Thermal Effects:");
             Debug.Print( "       Thermal options:");
             Debug.Print( "          Temperature source as defined in swsThermalOption_e: " + StaticOptions.ThermalResults);
             Debug.Print("          Temperature source:");
             if (StaticOptions.ThermalResults == 1) {
                 Debug.Print("          Thermal study: " +StaticOptions.ThermalStudyName);
                 Debug.Print( "              Time step (for transient thermal study only): " + StaticOptions.TimeStep);
             } else if  ( StaticOptions.ThermalResults == 2 ) {
                 Debug.Print( "               SOLIDWORKS Flow Simulation results file " + StaticOptions.FlowTemperatureFile);
             }
             else
                 Debug.Print( "               The current model");

             Debug.Print("       Fluid pressure option:");
             Debug.Print( "          Import fluid pressure loads from SOLIDWORKS Flow Simulation? (1=yes, 0=no): " + StaticOptions.CheckFlowPressure);
             if (StaticOptions.CheckFlowPressure == 1 ) {
                 Debug.Print( "           SOLIDWORKS Flow Simulation results file: " + StaticOptions.FlowPressureFile);
                 Debug.Print( "           Use reference pressure offset from Flow Simulation? (1=yes, 0=no): " + StaticOptions.ReferencePressureOption);
                 if (StaticOptions.ReferencePressureOption == 0 ) {
                     Debug.Print( "             Reference pressure offset: " + StaticOptions.DefinedReferencePressure);
                 }
                 Debug.Print( "          Run as legacy study and import only the normal component of the pressure load? (1=yes, 0=no): " + StaticOptions.CheckRunAsLegacy);
             }

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
             string selection1 = null;
             string selection2 = null;
             string selection3 = null;
             string selection4 = null;

             //Coordinate system
             selection1 = "181,35,0,0,1,0,0,0,255,254,255,0,0,0,0,0,35,2,0,0";
             selection1 = selection1 + ",Type=1";

             //Cylindrical face
             selection2 = "64,31,0,0,3,0,0,0,255,254,255,14,115,0,104,0,97,0,102,0,116,0,45,0,49,0,64,0,115,0,112,0,105,0,100,0,101,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,10,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,97,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,32,0,67,0,111,0,114,0,112,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,92,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,69,0,100,0,117,0,99,0,97,0,11";
             selection2 = selection2 + "6,0,105,0,111,0,110,0,97,0,108,0,32,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,115,0,104,0,97,0,102,0,116,0,46,0,115,0,108,0,100,0,112,0,114,0,116,0,9,128,255,254,255,5,115,0,104,0,97,0,102,0,116,0,2,0,0,155,126,163,53,0,165,25,208,59,1,0,0,0,0,0,0,0,5,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,63,0,0,0,0,0,0,0,7,50,149,70,12,0,0,0,171,126,163,53,1,0,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,12,0,0,0,171,126,163,53,1,0,0,0,255,255,255,255,0,0,12,128,0,0,5,128,8,0,12,0,0,0,171,126,163,53,0,0,0,0,255,255,255,255,0,0,0,0,0,0,0,0,0,0";
             selection2 = selection2 + ",Type=1";

             //Vertex 1
             selection3 = "189,35,0,0,3,0,0,0,255,254,255,15,115,0,112,0,105,0,100,0,101,0,114,0,45,0,49,0,64,0,115,0,112,0,105,0,100,0,101,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,9,0,0,0,255,255,1,0,13,0,109,111,86,101,114,116,101,120,82,101,102,95,99,255,255,255,255,255,255,255,255,3,0,0,0,0,2,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,19,0,109,111,70,105,108,108,101,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,98,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,32,0,67,0,111,0,114,0,112,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,92,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,69,0,100,0";
             selection3 = selection3 + ",117,0,99,0,97,0,116,0,105,0,111,0,110,0,97,0,108,0,32,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,115,0,112,0,105,0,100,0,101,0,114,0,46,0,115,0,108,0,100,0,112,0,114,0,116,0,9,128,255,254,255,6,115,0,112,0,105,0,100,0,101,0,114,0,2,0,0,149,119,163,53,255,254,255,0,0,184,241,44,76,1,0,0,0,0,0,0,0,5,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,142,0,0,0,0,0,0,0,13,50,149,70,141,0,0,0,83,107,166,53,4,0,0,0,3,128,0,0,5,128,8,0,139,0,0,0,68,107,166,53,4,0,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,28,0,0,0,119,124,163,53,0,0,0,0,255,255,255,255,0,0,0,0,0,0,0,0,0,0,0,0";
             selection3 = selection3 + ",Type=1";

             //Vertex 2
             selection4 = "189,35,0,0,3,0,0,0,255,254,255,15,115,0,112,0,105,0,100,0,101,0,114,0,45,0,49,0,64,0,115,0,112,0,105,0,100,0,101,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,9,0,0,0,255,255,1,0,13,0,109,111,86,101,114,116,101,120,82,101,102,95,99,255,255,255,255,255,255,255,255,3,0,0,0,0,2,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,98,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,32,0,67,0,111,0,114,0,112,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,92,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0";
             selection4 = selection4 + ",92,0,69,0,100,0,117,0,99,0,97,0,116,0,105,0,111,0,110,0,97,0,108,0,32,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,115,0,112,0,105,0,100,0,101,0,114,0,46,0,115,0,108,0,100,0,112,0,114,0,116,0,9,128,255,254,255,6,115,0,112,0,105,0,100,0,101,0,114,0,2,0,0,149,119,163,53,255,254,255,0,0,184,241,44,76,1,0,0,0,0,0,0,0,5,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,142,0,0,0,0,0,0,0,13,50,149,70,28,0,0,0,119,124,163,53,6,0,0,0,255,255,1,0,19,0,109,111,70,105,108,108,101,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,141,0,0,0,83,107,166,53,5,0,0,0,12,128,0,0,5,128,8,0,139,0,0,0,68,107,166,53,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0";
             selection4 = selection4 + ",Type=1";

             //Store constants in a collection
             PIDCollection.Add("selection1", selection1);
             PIDCollection.Add("selection2", selection2);
             PIDCollection.Add("selection3", selection3);
             PIDCollection.Add("selection4", selection4);

             return PIDCollection;

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```
