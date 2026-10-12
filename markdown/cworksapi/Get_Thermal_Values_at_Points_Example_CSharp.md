---
title: "Get Thermal Values at Points Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Get_Thermal_Values_at_Points_Example_CSharp.htm"
---

# Get Thermal Values at Points Example (C#)

## Get Thermal Values Example (C#)

This example shows how to get thermal values in a thermal study.

```vb
  //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
 // 3. Ensure that the specified model exists.
 // 4. Modify the path to solidworks materials.sldmat if needed.
  // 5. Uncomment the thermal method whose return values you want to see.
 // 6. Open the Immediate window.
 //
 // Postconditions:
 // 1.  Opens document.
 // 2.  Creates Thermal_One study.
 // 3.  Applies user-defined and SOLIDWORKS materials to components.
  // 4.  Gets objects by persistent reference and populates input arrays.
 // 5.  Sets thermal study options.
  // 6.  Assigns initial temperatures to assembly components.
  // 7.  Adds heat power and convection to assembly components.
  // 8.  Assigns thermostat location and the temperature range.
 // 9.  Meshes the assembly.
 // 10. Analyzes the study.
  // 11. Prints thermal values at solution step 60 to the Immediate window.
 //
 // NOTES:
 //  * To get persistent reference identifiers (PIDs) for model selections,
 //    use pidcollector.exe or IModelDocExtension::GetPersistReference3.
  //  * Solving this study can take some time. Examine the Immediate window
  //    to monitor the macro's progress. Done! indicates that the macro
 //    has finished.
  //  * Because this assembly document is used by a SOLIDWORKS Simulation
 //    online tutorial, do not save any changes.
  //--------------------------------------------------------------------
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
 namespace GetThermalValues_CSharp.csproj
 {
     partial class SolidWorksMacro
     {
         public void Main()
         {
             CosmosWorks COSMOSWORKS = default(CosmosWorks);
             CwAddincallback CWObject = default(CwAddincallback);
             CWModelDoc ActDoc = default(CWModelDoc);
             CWStudyManager StudyMngr = default(CWStudyManager);
             CWStudy Study = default(CWStudy);
             CWSolidManager SolidMgr = default(CWSolidManager);
             CWSolidComponent SolidComp = default(CWSolidComponent);
             CWSolidBody SolidBody = default(CWSolidBody);
             CWThermalStudyOptions ThermalOptions = default(CWThermalStudyOptions);
             CWConvection CWConv = default(CWConvection);
             CWHeatPower CWHeatPower = default(CWHeatPower);
             CWMesh CwMesh = default(CWMesh);
             CWResults CWResult = default(CWResults);
             CWMaterial CWMat = default(CWMaterial);
             CWTemperature CWTemp = default(CWTemperature);
             ModelDoc2 Part = default(ModelDoc2);
             CWLoadsAndRestraintsManager LBCMgr = default(CWLoadsAndRestraintsManager);
             object oselect1 = null;
             object oselect2 = null;
             object oselect3 = null;
             object oselect4 = null;
             object oselect5 = null;
             object oselect6 = null;
             object oselect7 = null;
             object oselect8 = null;
             object oselect9 = null;
             object oselect10 = null;
             object therm1 = null;
             byte[] var1 = null;
             byte[] var2 = null;
             byte[] var3 = null;
             byte[] var4 = null;
             byte[] var5 = null;
             byte[] var6 = null;
             byte[] var7 = null;
             byte[] var8 = null;
             byte[] var9 = null;
             byte[] var10 = null;
             byte[] var11 = null;
             object[] Temp = null;
             string selection1 = null;
             string selection2 = null;
             string selection3 = null;
             string selection4 = null;
             string selection5 = null;
             string selection6 = null;
             string selection7 = null;
             string selection8 = null;
             string selection9 = null;
             string selection10 = null;
             string selection11 = null;
             int longstatus = 0;
             int longwarnings = 0;
             int errCode = 0;
             double el = 0;
             double tl = 0;
             int nStep = 0;

             // Open document
             Debug.Print("Opening document...");
             Part = swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2017\\Simulation Examples\\Thermal\\CoffeeJar.SLDASM", (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref longstatus, ref longwarnings);

             if (Part == null)
                 ErrorMsg(swApp, "Failed to open document", true);

             // Get the SOLIDWORKS Simulation add-in object
             CWObject = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
             if (CWObject == null)
                 ErrorMsg(swApp, "No CwAddincallback object", true);

             COSMOSWORKS = CWObject.CosmosWorks;
             if (COSMOSWORKS == null)
                 ErrorMsg(swApp, "No CosmosWorks object", true);

             // Get active document
             ActDoc = COSMOSWORKS.ActiveDoc;
             if (ActDoc == null)
                 ErrorMsg(swApp, "No active document", true);

             // Create new thermal study
             Debug.Print("Creating thermal study...");

             StudyMngr = ActDoc.StudyManager;
             if (StudyMngr == null)
                 ErrorMsg(swApp, "No study manager object", true);

             Study = StudyMngr.CreateNewStudy3("Thermal_One", (int)swsAnalysisStudyType_e.swsAnalysisStudyTypeThermal, (int)swsMeshType_e.swsMeshTypeSolid, out errCode);
             if (Study == null)
                 ErrorMsg(swApp, "No study", true);

             // Get first solid component
             SolidMgr = Study.SolidManager;
             if (SolidMgr == null)
                 ErrorMsg(swApp, "No solid manager object", true);

             SolidComp = SolidMgr.GetComponentAt(0, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "No solid component", true);

             SolidBody = SolidComp.GetSolidBodyAt(0, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "No solid body", true);

             // Add material
             CWMat = SolidBody.GetDefaultMaterial();
             if (CWMat == null)
                 ErrorMsg(swApp, "No default material", true);

             CWMat.MaterialName = "Coffee";

             CWMat.SetPropertyByName("DENS", 1000, 0);
             CWMat.SetPropertyByName("KX", 40, 0);
             CWMat.SetPropertyByName("C", 4200.0, 0);

             errCode = SolidBody.SetSolidBodyMaterial(CWMat);
             if (errCode != 0)
                 ErrorMsg(swApp, "Solid body material not set", true);

             // Get second solid component
             SolidComp = SolidMgr.GetComponentAt(1, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "No solid component", true);

             SolidBody = SolidComp.GetSolidBodyAt(0, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "No solid body", true);

             // Add material
             errCode = SolidBody.SetLibraryMaterial("C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\\english\\sldmaterials\\solidworks materials.sldmat", "Glass");
             if (errCode == 0)
                 ErrorMsg(swApp, "No glass material applied", true);

             // Get third solid component
             SolidComp = SolidMgr.GetComponentAt(2, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "No solid component", true);

             SolidBody = SolidComp.GetSolidBodyAt(0, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "No solid body", true);

             // Add material
             errCode = SolidBody.SetLibraryMaterial("C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\\english\\sldmaterials\\solidworks materials.sldmat", "Nylon 6/10");
             if (errCode == 0)
                 ErrorMsg(swApp, " No Nylon 6/10 material applied", true);

             // CoffeePot
             selection1 = "216,14,0,0,5,0,0,0,255,254,255,21,67,0,111,0,102,0,102,0,101,0,101,0,80,0,111,0,116,0,45,0,49,0,64,0,67,0,111,0,102,0,102,0,101,0,101,0,74,0,97,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,11,0,0,0";
             StringtoArray(selection1, ref var1);
             oselect1 = Part.Extension.GetObjectByPersistReference3((var1), out longstatus);

             // Coffee
             selection2 = "216,14,0,0,5,0,0,0,255,254,255,18,67,0,111,0,102,0,102,0,101,0,101,0,45,0,49,0,64,0,67,0,111,0,102,0,102,0,101,0,101,0,74,0,97,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,12,0,0,0";
             StringtoArray(selection2, ref var2);
             oselect2 = Part.Extension.GetObjectByPersistReference3((var2), out longstatus);

             // Top
             selection3 = "216,14,0,0,5,0,0,0,255,254,255,15,84,0,111,0,112,0,45,0,49,0,64,0,67,0,111,0,102,0,102,0,101,0,101,0,74,0,97,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,13,0,0,0";
             StringtoArray(selection3, ref var3);
             oselect3 = Part.Extension.GetObjectByPersistReference3((var3), out longstatus);

             // Get the four coffee faces that make up the surface of coffee in the coffee pot
             // Face 1
             selection4 = "216,14,0,0,3,0,0,0,255,254,255,18,67,0,111,0,102,0,102,0,101,0,101,0,45,0,49,0,64,0,67,0,111,0,102,0,102,0,101,0,101,0,74,0,97,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,12,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,18,0,109,111,80,76,105,110,101,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,14,0,109,111,79,98,106,70,105,108,101,68,101,102,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,6,99,0,111,0,102,0,102,0,101,0,101,0,126,253,47,63,11,128,255,254,255,57,67,0,58,0,92,0,67,0,79,0,83,0,77,0,79,0,83,0,68,0,111,0,99,0,115,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,95,0,102,0,111,0,114,0,67,0,117,0,115,0,116,0,111,0,109,0,101,0,114,0,115,0,92,0,84,0,104,0,101,0,114,0,109,0,97,0,10";
             selection4 = selection4 + "8,0,92,0,99,0,111,0,102,0,102,0,101,0,101,0,46,0,115,0,108,0,100,0,112,0,114,0,116,0,90,14,28,65,0,0,0,0,2,0,1,0,0,0,0,0,0,0,4,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,0,0,92,0,0,0,241,69,48,63,3,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,1,0,0,0,5,0,0,0,255,255,1,0,18,0,109,111,80,76,105,110,101,80,114,111,106,73,100,82,101,112,95,99,0,0,5,128,8,0,90,0,0,0,219,69,48,63,16,128,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,1,0,0,0,19,128,0,0,5,128,8,0,92,0,0,0,241,69,48,63,3,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,16,128,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,1,0,0,0,1,0,0,0,16,128,0,0,5,128,8,0,88,0,0,0,135,69,48,63,11,0,0,0,0,0,0,0,0,0";
             StringtoArray(selection4, ref var4);
             oselect4 = Part.Extension.GetObjectByPersistReference3((var4), out longstatus);

             // Face 2
             selection5 = "216,14,0,0,3,0,0,0,255,254,255,18,67,0,111,0,102,0,102,0,101,0,101,0,45,0,49,0,64,0,67,0,111,0,102,0,102,0,101,0,101,0,74,0,97,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,12,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,18,0,109,111,80,76,105,110,101,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,14,0,109,111,79,98,106,70,105,108,101,68,101,102,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,6,99,0,111,0,102,0,102,0,101,0,101,0,126,253,47,63,11,128,255,254,255,57,67,0,58,0,92,0,67,0,79,0,83,0,77,0,79,0,83,0,68,0,111,0,99,0,115,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,95,0,102,0,111,0,114,0,67,0,117,0,115,0,116,0,111,0,109,0,101,0,114,0,115,0,92,0,84,0,104,0,101,0,114,0,109,0,97,0,";
             selection5 = selection5 + "108,0,92,0,99,0,111,0,102,0,102,0,101,0,101,0,46,0,115,0,108,0,100,0,112,0,114,0,116,0,90,14,28,65,0,0,0,0,2,0,1,0,0,0,0,0,0,0,4,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,0,0,92,0,0,0,241,69,48,63,3,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,1,0,0,0,6,0,0,0,255,255,1,0,18,0,109,111,80,76,105,110,101,80,114,111,106,73,100,82,101,112,95,99,0,0,5,128,8,0,92,0,0,0,241,69,48,63,3,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,16,128,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,1,0,0,0,1,0,0,0,19,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,16,128,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,1,0,0,0,16,128,0,0,5,128,8,0,88,0,0,0,135,69,48,63,11,0,0,0,0,0,0,0,0,0";
             StringtoArray(selection5, ref var5);
             oselect5 = Part.Extension.GetObjectByPersistReference3((var5), out longstatus);

             // Face 3
             selection6 = "216,14,0,0,3,0,0,0,255,254,255,18,67,0,111,0,102,0,102,0,101,0,101,0,45,0,49,0,64,0,67,0,111,0,102,0,102,0,101,0,101,0,74,0,97,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,12,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,18,0,109,111,80,76,105,110,101,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,14,0,109,111,79,98,106,70,105,108,101,68,101,102,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,6,99,0,111,0,102,0,102,0,101,0,101,0,126,253,47,63,11,128,255,254,255,57,67,0,58,0,92,0,67,0,79,0,83,0,77,0,79,0,83,0,68,0,111,0,99,0,115,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,95,0,102,0,111,0,114,0,67,0,117,0,115,0,116,0,111,0,109,0,101,0,114,0,115,0,92,0,84,0,104,0,101,0,114,0,109,0,97,0,";
             selection6 = selection6 + "108,0,92,0,99,0,111,0,102,0,102,0,101,0,101,0,46,0,115,0,108,0,100,0,112,0,114,0,116,0,90,14,28,65,0,0,0,0,2,0,1,0,0,0,0,0,0,0,4,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,0,0,92,0,0,0,241,69,48,63,3,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,2,0,0,0,2,0,0,0,255,255,1,0,18,0,109,111,80,76,105,110,101,80,114,111,106,73,100,82,101,112,95,99,0,0,5,128,8,0,92,0,0,0,241,69,48,63,3,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,16,128,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,2,0,0,0,1,0,0,0,16,128,0,0,5,128,8,0,88,0,0,0,135,69,48,63,11,0,0,0,19,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,16,128,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,1,0,0,0,0,0,0,0,0,0";
             StringtoArray(selection6, ref var6);
             oselect6 = Part.Extension.GetObjectByPersistReference3((var6), out longstatus);

             // Face 4
             selection7 = "216,14,0,0,3,0,0,0,255,254,255,18,67,0,111,0,102,0,102,0,101,0,101,0,45,0,49,0,64,0,67,0,111,0,102,0,102,0,101,0,101,0,74,0,97,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,12,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,18,0,109,111,80,76,105,110,101,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,14,0,109,111,79,98,106,70,105,108,101,68,101,102,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,6,99,0,111,0,102,0,102,0,101,0,101,0,126,253,47,63,11,128,255,254,255,57,67,0,58,0,92,0,67,0,79,0,83,0,77,0,79,0,83,0,68,0,111,0,99,0,115,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,95,0,102,0,111,0,114,0,67,0,117,0,115,0,116,0,111,0,109,0,101,0,114,0,115,0,92,0,84,0,104,0,101,0,114,0,109,0,97,0,";
             selection7 = selection7 + "108,0,92,0,99,0,111,0,102,0,102,0,101,0,101,0,46,0,115,0,108,0,100,0,112,0,114,0,116,0,90,14,28,65,0,0,0,0,2,0,1,0,0,0,0,0,0,0,4,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,0,0,92,0,0,0,241,69,48,63,3,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,2,0,0,0,1,0,0,0,16,128,0,0,5,128,8,0,88,0,0,0,135,69,48,63,11,0,0,0,255,255,1,0,18,0,109,111,80,76,105,110,101,80,114,111,106,73,100,82,101,112,95,99,0,0,5,128,8,0,92,0,0,0,241,69,48,63,3,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,16,128,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,2,0,0,0,1,0,0,0,21,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,16,128,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,1,0,0,0,0,0,0,0,0,0";
             StringtoArray(selection7, ref var7);
             oselect7 = Part.Extension.GetObjectByPersistReference3((var7), out longstatus);

             // Get the selections for convection
             // Top-outer face of coffee pot
             selection8 = "216,14,0,0,3,0,0,0,255,254,255,21,67,0,111,0,102,0,102,0,101,0,101,0,80,0,111,0,116,0,45,0,49,0,64,0,67,0,111,0,102,0,102,0,101,0,101,0,74,0,97,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,11,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,14,0,109,111,79,98,106,70,105,108,101,68,101,102,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,9,67,0,111,0,102,0,102,0,101,0,101,0,80,0,111,0,116,0,174,232,47,63,11,128,255,254,255,60,67,0,58,0,92,0,67,0,79,0,83,0,77,0,79,0,83,0,68,0,111,0,99,0,115,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,95,0,102,0,111,0,114,0,67,0,117,0,115,0,116,0,111,0,109,0,101,0,";
             selection8 = selection8 + "114,0,115,0,92,0,84,0,104,0,101,0,114,0,109,0,97,0,108,0,92,0,67,0,111,0,102,0,102,0,101,0,101,0,80,0,111,0,116,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,153,14,28,65,0,0,0,0,2,0,1,0,0,0,0,0,0,0,5,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,0,0,39,0,0,0,234,237,47,63,3,0,0,0,3,128,0,0,5,128,8,0,39,0,0,0,234,237,47,63,2,0,0,0,0,0,3,128,0,0,5,128,8,0,39,0,0,0,234,237,47,63,4,0,0,0,0,0,0,0,0,0";
             StringtoArray(selection8, ref var8);
             oselect8 = Part.Extension.GetObjectByPersistReference3((var8), out longstatus);

             // Lower-outer face of coffee pot
             selection9 = "216,14,0,0,3,0,0,0,255,254,255,21,67,0,111,0,102,0,102,0,101,0,101,0,80,0,111,0,116,0,45,0,49,0,64,0,67,0,111,0,102,0,102,0,101,0,101,0,74,0,97,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,11,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,14,0,109,111,79,98,106,70,105,108,101,68,101,102,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,9,67,0,111,0,102,0,102,0,101,0,101,0,80,0,111,0,116,0,174,232,47,63,11,128,255,254,255,60,67,0,58,0,92,0,67,0,79,0,83,0,77,0,79,0,83,0,68,0,111,0,99,0,115,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,95,0,102,0,111,0,114,0,67,0,117,0,115,0,116,0,111,0,109,0,101,";
             selection9 = selection9 + "0,114,0,115,0,92,0,84,0,104,0,101,0,114,0,109,0,97,0,108,0,92,0,67,0,111,0,102,0,102,0,101,0,101,0,80,0,111,0,116,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,153,14,28,65,0,0,0,0,2,0,1,0,0,0,0,0,0,0,5,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,0,0,39,0,0,0,234,237,47,63,2,0,0,0,3,128,0,0,5,128,8,0,39,0,0,0,234,237,47,63,3,0,0,0,0,0,3,128,0,0,5,128,8,0,39,0,0,0,234,237,47,63,1,0,0,0,0,0,0,0,0,0";
             StringtoArray(selection9, ref var9);
             oselect9 = Part.Extension.GetObjectByPersistReference3((var9), out longstatus);

             // Get the selections for heat power
             // Vertex located on the top of the bottom face of the coffee pot
             selection10 = "216,14,0,0,3,0,0,0,255,254,255,18,67,0,111,0,102,0,102,0,101,0,101,0,45,0,49,0,64,0,99,0,111,0,102,0,102,0,101,0,101,0,106,0,97,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,12,0,0,0,255,255,1,0,13,0,109,111,86,101,114,116,101,120,82,101,102,95,99,255,255,255,255,255,255,255,255,8,0,0,0,0,2,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,18,0,109,111,80,76,105,110,101,80,114,111,106,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,";
             selection10 = selection10 + "1,0,14,0,109,111,79,98,106,70,105,108,101,68,101,102,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,6,99,0,111,0,102,0,102,0,101,0,101,0,126,253,47,63,11,128,255,254,255,57,67,0,58,0,92,0,67,0,79,0,83,0,77,0,79,0,83,0,68,0,111,0,99,0,115,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,95,0,102,0,111,0,114,0,67,0,117,0,115,0,116,0,111,0,109,0,101,0,114,0,115,0,92,0,84,0,104,";
             selection10 = selection10 + "0,101,0,114,0,109,0,97,0,108,0,92,0,99,0,111,0,102,0,102,0,101,0,101,0,46,0,115,0,108,0,100,0,112,0,114,0,116,0,90,14,28,65,0,0,0,0,2,0,1,0,0,0,0,0,0,0,4,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,0,0,92,0,0,0,241,69,48,63,255,255,1,0,18,0,109,111,80,76,105,110,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,90,0,0,0,219,69,48,63,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,";
             selection10 = selection10 + "110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,1,0,0,0,1,0,0,0,3,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,17,128,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,1,0,0,0,3,128,0,0,5,128,8,0,92,0,0,0,241,69,48,63,14,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,17,128,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,2,0,0,0,1,0,0,0,3,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,17,128,0,0,5,128,8,0,88,0,0,0,";
             selection10 = selection10 + "135,69,48,63,5,0,0,0,1,0,0,0,14,128,0,0,5,128,8,0,92,0,0,0,241,69,48,63,14,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,17,128,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,1,0,0,0,5,0,0,0,14,128,0,0,5,128,8,0,92,0,0,0,241,69,48,63,14,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,17,128,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,2,0,0,0,1,0,0,0,14,128,0,0,5,128,8,0,92,0,0,0,241,69,48,63,14,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,17,128,0,0,";
             selection10 = selection10 + "5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,2,0,0,0,2,0,0,0,14,128,0,0,5,128,8,0,92,0,0,0,241,69,48,63,14,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,17,128,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,1,0,0,0,6,0,0,0,4,0,0,0,0,0,0,0";
             StringtoArray(selection10, ref var10);
             therm1 = Part.Extension.GetObjectByPersistReference3((var10), out longstatus);

             // Vertex where sensor (thermostat) is located
             selection11 = "216,14,0,0,3,0,0,0,255,254,255,21,67,0,111,0,102,0,102,0,101,0,101,0,80,0,111,0,116,0,45,0,49,0,64,0,67,0,111,0,102,0,102,0,101,0,101,0,74,0,97,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,11,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,3,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,14,0,109,111,79,98,106,70,105,108,101,68,101,102,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,9,67,0,111,0,102,0,102,0,101,0,101,0,80,0,111,0,116,0,174,232,47,63,11,128,255,254,255,60,67,0,58,0,92,0,67,0,79,0,83,0,77,0,79,0,83,0,68,0,111,0,99,0,115,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,95,0,102,0,111,0,114,0,67,0,117,0,115,0,116,0,111,0,109,0,101,0,";
             selection11 = selection11 + "114,0,115,0,92,0,84,0,104,0,101,0,114,0,109,0,97,0,108,0,92,0,67,0,111,0,102,0,102,0,101,0,101,0,80,0,111,0,116,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,153,14,28,65,0,0,0,0,2,0,1,0,0,0,0,0,0,0,5,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,0,0,39,0,0,0,234,237,47,63,1,0,0,0,3,128,0,0,5,128,8,0,39,0,0,0,234,237,47,63,2,0,0,0,0,0,0,0,0,0";
             StringtoArray(selection11, ref var11);
             oselect10 = Part.Extension.GetObjectByPersistReference3((var11), out longstatus);

             // Create arrays
             object[] varArray1 = {
             oselect1,
             oselect3
             };
             object[] varArray2 = { oselect2 };
             object[] varArray3 = {
             oselect4,
             oselect5,
             oselect6,
             oselect7
             };
             object[] varArray4 = {
             oselect8,
             oselect9
             };
             object[] varArray5 = { therm1 };
             object[] varArray6 = { oselect10 };
             object[] varArray7 = {
             -19.63,
             31.23,
             173.15
             };

             // Set transient thermal study with solver type FFEPlus
             Debug.Print("Setting transient thermal study with solver type FFEPlus...");
             ThermalOptions = Study.ThermalStudyOptions;
             Study.ThermalStudyOptions.SolutionType = 0;
             if (ThermalOptions == null)
                 ErrorMsg(swApp, "No thermal options", false);

             ThermalOptions.SolverType = 2;
             ThermalOptions.TotalTime = 3600;
             ThermalOptions.TimeIncrement = 60;

             // Apply initial temperature to coffee pot and top
             Debug.Print("Applying initial temperature to coffee pot and top...");

             LBCMgr = Study.LoadsAndRestraintsManager;
             if (LBCMgr == null)
                 ErrorMsg(swApp, "No loads and restraints manager", false);

             CWTemp = LBCMgr.AddTemperature((varArray1), out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "No temperature applied", true);

             CWTemp.TemperatureBeginEdit();
             CWTemp.TemperatureType = 0;
             CWTemp.Unit = 1;
             CWTemp.TemperatureValue = 72;

             errCode = CWTemp.TemperatureEndEdit();
             if (errCode != 0)
                 ErrorMsg(swApp, "No temperature applied", true);

             // Apply initial temperature to coffee
             Debug.Print("Applying initial temperature to coffee...");

             CWTemp = LBCMgr.AddTemperature((varArray2), out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "No temperature applied", true);

             CWTemp.TemperatureBeginEdit();
             CWTemp.TemperatureType = 0;
             CWTemp.Unit = 1;
             CWTemp.TemperatureValue = 195;

             errCode = CWTemp.TemperatureEndEdit();
             if (errCode != 0)
                 ErrorMsg(swApp, "No temperature applied", true);

             // Create convection for coffee component
             Debug.Print("Creating convection for coffee component...");

             CWConv = LBCMgr.AddConvection((varArray3), out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "No convection added", true);

             CWConv.ConvectionBeginEdit();
             CWConv.Unit = 1;
             CWConv.ConvectionCoefficient = 8.5E-06;
             CWConv.BulkAmbientTemperature = 72;

             errCode = CWConv.ConvectionEndEdit();
             if (errCode != 0)
                 ErrorMsg(swApp, "Convection end-edit failed for coffee", true);

             // Create convection for coffee pot component
             Debug.Print("Creating convection for coffee pot component...");
             CWConv = LBCMgr.AddConvection((varArray4), out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "No convection added", true);

             CWConv.ConvectionBeginEdit();
             CWConv.Unit = 1;
             CWConv.ConvectionCoefficient = 6.1E-05;
             CWConv.BulkAmbientTemperature = 72;

             errCode = CWConv.ConvectionEndEdit();
             if (errCode != 0)
                 ErrorMsg(swApp, "Convection end-edit failed for coffee pot", true);

             // Create heat power for face
             Debug.Print("Creating heat power for face...");

             CWHeatPower = LBCMgr.AddHeatPower((varArray6), out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "No heat power created", true);

             CWHeatPower.HeatPowerBeginEdit();
             CWHeatPower.Unit = 0;
             CWHeatPower.HPValue = 2000;

             // Set thermostat to a vertex
             Debug.Print("Setting thermostat to a vertex...");
             CWHeatPower.IncludeThermostat = 1;
             CWHeatPower.SetThermostat(therm1);
             CWHeatPower.ThermostatUnits = 1;
             CWHeatPower.SetCutOffTemperatures(190, 200);
             errCode = CWHeatPower.HeatPowerEndEdit();
             if (errCode != 0)
                 ErrorMsg(swApp, "Heat power not updated", true);

             // Create mesh
             Debug.Print("Creating mesh...");
             CwMesh = Study.Mesh;
             if (CwMesh == null)
                 ErrorMsg(swApp, "No mesh object", false);
             CwMesh.Quality = 1;
             CwMesh.GetDefaultElementSizeAndTolerance(0, out el, out tl);
             errCode = Study.CreateMesh(0, el, tl);
             if (errCode != 0)
                 ErrorMsg(swApp, "Mesh failed", true);

             // Run analysis
             Debug.Print("Running analysis...");
             errCode = Study.RunAnalysis();
             if (errCode != 0)
                 ErrorMsg(swApp, "Analysis failed", true);

             // Get thermal results
             Debug.Print("Getting thermal results...");
             CWResult = Study.Results;
             if (CWResult == null)
                 ErrorMsg(swApp, "No results object", false);

             nStep = CWResult.GetMaximumAvailableSteps(); // solution step 60

             // Get temperature value at point {-19.63, 31.23, 173.15} at solution step 60
             Temp = (object[])CWResult.GetThermalValuesAtPoints((int)swsThermalComponent_e.swsThermalComponentTEMP, nStep, null, (varArray7), (int)swsTemperatureUnit_e.swsTemperatureUnitKelvin, out errCode);

             // Get temperature values at all nodes at solution step 60
             //Temp = CWResult.GetThermalValues(nStep, Nothing, swsTemperatureUnitKelvin, errCode)

             // Get heat energy values for the specified vertex at solution step 60
             //Temp = CWResult.GetHeatPowerOrEnergy2(-1, (varArray6), swsUnitSI, 1, nStep, errCode) ' Heat energy

             // Get temperature values for all steps at node 9236
             //Temp = CWResult.GetThermalComponentForAllStepsAtNode(swsThermalComponentTEMP, 9236, Nothing, swsTemperatureUnitKelvin, errCode)

             // Get temperature values for the specified entities at solution step 60
             //Temp = CWResult.GetThermalForEntities(swsThermalComponentTEMP, nStep, Nothing, (varArray4), swsTemperatureUnitKelvin, errCode)

             if (errCode != 0)
                 ErrorMsg(swApp, "No temperature result", true);

             // Print out the contents of Temp
             // See the Simulation API Help for information about the contents of the returned array
             int i = 0;
             for (i = 0; i <= Temp.GetUpperBound(0); i++)
             {
                 Debug.Print(Temp[i].ToString());
             }

             Debug.Print("Done!");

         }

         public void ErrorMsg(SldWorks swApp, string Message, bool EndTest)
         {
             swApp.SendMsgToUser2(Message, 0, 0);
             swApp.RecordLine("'*** WARNING - General");
             swApp.RecordLine("'*** " + Message);
             swApp.RecordLine("");
         }

         private void StringtoArray(string inputSTR, ref byte[] varEntity)
         {
             string[] PIDArray = null;
             byte[] PID = null;
             int i;

             // Parse string into an array
             PIDArray = inputSTR.Split(new char[] { ',' });

             //Convert string array to byte array
             int sizeArray = PIDArray.Length;
             PID = new byte[sizeArray];
             for (i = 0; i < PIDArray.Length; i++)
             {
                 PID[i] = Convert.ToByte(PIDArray[i]);
             }

             varEntity = PID;
         }

         public SldWorks swApp;

     }

 }
```
