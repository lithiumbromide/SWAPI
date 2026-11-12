---
title: "Create Drop Test Study Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Drop_Test_Study_Example_CSharp.htm"
---

# Create Drop Test Study Example (C#)

This example shows how to create a drop test study.

NOTE: To get persistent reference identifiers (PIDs) for model selections, you can use [pidcollector.exe](GettingStarted-swsimulationapi.html) or IModelDocExtension::GetPersistReference3.

```vb
//----------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
 // 3. Open public_documents\samples\tutorial\api\KeyPad_1.sldasm.
 //
 // Postconditions:
 //  1. Creates a default drop test study results plot.
 //  2. Creates drop test study, Study 2.
 //  3. Applies Nylon 101 SOLIDWORKS material to all components.
 //  4. Meshes the model.
 //  5. Sets drop height to 1000 mm.
 //  6. Runs the analysis.
 //  7. Validates the von Mises stress results.
 //  8. When the macro stops:
 //     a. Inspect the Immediate window for the 1000 mm drop test study's setup
 //        and result options.
 //     b. Inspect the default drop test study results plot.
 //     c. Press F5 to continue.
 //  9. Changes drop height to 2000 mm.
 // 10. Re-runs the analysis.
 // 11. Inspect the results folder.
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
 namespace DropTest_CSharp.csproj
 {
     partial class SolidWorksMacro
     {
         ModelDoc2 Part;
         CosmosWorks COSMOSWORKS;
         CwAddincallback CWAddinCallBack;
         CWModelDoc ActDoc;
         CWStudyManager StudyMngr;
         CWStudy Study;
         CWMesh CWMesh;
         CWResults CWFeatObj;
         CWSolidManager SolidMgr;
         CWSolidComponent SolidComponent;
         CWSolidBody Solidbody;
         CWDropTestSetup Setup;
         CWDropTestResultOptions ResultOptions;
         CWDropTestStudyOptions StudyOptions;

         object Selection;
         string CosmosFolder;
         string sLibWithPathname;
         string sMaterialName;
         string sName;
         int errCode;
         int nStep;
         double VMS1000;
         double VMS2000;
         object[] Stress = new object[4];
         int CompCount;
         int j;
         double Height;
         int bApp;
         Hashtable PIDCollection = new Hashtable();
         double Tol;
         double A;
         double B;

         public void Main()
         {
             PIDCollection = PIDInitializer();

             Tol = 0.25;
             //25% tolerance
             VMS1000 = 7314431;
             //maximum von Mises stress at step 25 for drop height = 1000 mm
             VMS2000 = 10389063;
             //maximum von Mises stress at step 25 for drop height = 2000 mm

             if (swApp == null)
                 return;

             CosmosFolder = swApp.GetExecutablePath();
             Part = (ModelDoc2)swApp.ActiveDoc;

             CWAddinCallBack = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
             COSMOSWORKS = CWAddinCallBack.CosmosWorks;

             ActDoc = COSMOSWORKS.ActiveDoc;
```

```vb
            // Add a default drop test study results plot
             bApp = ActDoc.AddDefaultDropTestStudyPlot((int)swsDropTestStudyResultType_e.swsDropTestResultElementalStress, (int)swsStressComponent_e.swsStressComponentVON);
```

```vb
             StudyMngr = ActDoc.StudyManager;

             //Create a drop test study
             Study = StudyMngr.CreateNewStudy3("Study 2", 6, 0, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to create a drop test study");

             StudyOptions = Study.DropTestStudyOptions;
             Debug.Print("Study results folder: " + StudyOptions.ResultFolder);
             Debug.Print("Study displacement formulation (true = large): " + StudyOptions.LargeDisplacement2);
             ResultOptions = Study.DropTestResultOptions;
             Debug.Print("Number of graph steps: " + ResultOptions.NoOfGraphSteps);
             Debug.Print("Number of plots: " + ResultOptions.NoOfPlots);
             Debug.Print("Save results from starting time (sec): " + ResultOptions.SaveResultsStartingTime);
             Debug.Print("Time to solve after impact (sec): " + ResultOptions.SolutionTimeAfterImpact);

             //Create mesh
             CWMesh = Study.Mesh;
             CWMesh.MesherType = 0;
             //standard mesh = 0, CB mesh = 1
             CWMesh.Quality = 0;
             //draft = 0, high quality = 1
             errCode = Study.CreateMesh(0, 2, 0.05);
             //create mesh, 0-1-2-3-4 : mm-cm-m-in-ft

             //Apply material
             sLibWithPathname = CosmosFolder + "\\lang\\english\\sldmaterials\\solidworks materials.sldmat";
             sMaterialName = "Nylon 101";
             //Nylon 101 SOLIDWORKS material
             SolidMgr = Study.SolidManager;
             CompCount = SolidMgr.ComponentCount;
             //Apply material to all solid components
             for (j = 0; j <= (CompCount - 1); j++)
             {
                 SolidComponent = SolidMgr.GetComponentAt(j,  out errCode);
                 sName = SolidComponent.ComponentName;
                 Solidbody = SolidComponent.GetSolidBodyAt(0,  out errCode);
                 bApp = Solidbody.SetLibraryMaterial(sLibWithPathname, sMaterialName);
                 Solidbody = null;
             }

             //Assign drop test setup
             Selection = SelectByPID(Part, "selection1", PIDCollection);
             Setup = Study.AddDropTestSetup(Selection,  out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to create DropTestSetup object");
             if (Setup == null)
                 ErrorMsg(swApp, "Failed to get DropTestSetup object");
             Height = Setup.DropHeight;
             if (Height != 1000)
                 ErrorMsg(swApp, "Failed to validate drop height = 1000 mm from original Study 1");

             Debug.Print("Critical damping ratio: " + Setup.CriticalDampingRatio);
             Debug.Print("Drop height (mm): " + Setup.DropHeight);
             Debug.Print("Drop height type (swsDropHeightType_e): " + Setup.DropHeightType);
             Debug.Print("Drop height units (swsLinearUnit_e): " + Setup.DropHeightUnit);
             Debug.Print("Drop type (swsDropType_e): " + Setup.DropType);
             Debug.Print("Reverse gravity direction? (true = yes) " + Setup.FlipGravityDirection2);
             Debug.Print("Reverse velocity direction? (true = yes) " + Setup.FlipVelocityDirection2);
             Debug.Print("Coefficient of friction: " + Setup.FrictionCoefficient);
             Debug.Print("Gravity magnitude: " + Setup.Gravity);
             Debug.Print("Gravity units (swsAccelerationUnit_e): " + Setup.GravityUnit);
             Debug.Print("Mass density of impact layer: " + Setup.MassDensity);
             Debug.Print("Stiffness per unit area normal to impact plane: " + Setup.NormalStiffness);
             Debug.Print("Units of stiffness (swsUnitSystem_e): " + Setup.StiffnessUnit);
             Debug.Print("Stiffness per unit area parallel to the impact plane: " + Setup.TangentialStiffness);
             Debug.Print("Orientation of impact plane (swsDropTargetOrientationType_e): " + Setup.TargetOrientationType);
             Debug.Print("Stiffness type (swsDropTargetStiffnessType_e): " + Setup.TargetStiffnessType);
             Debug.Print("Thickness of the impact layer: " + Setup.TargetThickness);
             Debug.Print("Units of thickness (swsLinearUnit_e): " + Setup.ThicknessUnit);
             Debug.Print("Velocity at impact: " + Setup.Velocity);
             Debug.Print("Units of velocity (swsVelocityUnit_e): " + Setup.VelocityUnit);

             //Run study for drop height = 1000 mm
             errCode = Study.RunAnalysis();
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to run study (drop height = 1000 mm)");
             CWFeatObj = Study.Results;
             if (CWFeatObj == null)
                 ErrorMsg(swApp, "Failed to get Result Object (drop height = 1000 mm)");
             nStep = CWFeatObj.GetMaximumAvailableSteps();
             //nStep = last step of study
             if (nStep != 25)
                 ErrorMsg(swApp, "Total number of steps in result is incorrect (drop height = 1000 mm)");
             Stress = (object[])CWFeatObj.GetMinMaxStress(9, 0, nStep, null, 0, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to get von Mises stress result for drop height = 1000 mm");
             A = (float)Stress[3];
             B = VMS1000;
             if (ResultsVer(A, B, Tol) == true)
             {
                 ErrorMsg(swApp, "The von Mises stress result for drop height = 1000 mm has % error = " + ResultsError(A, B, Tol));
             }

             //Change drop height from 1000 mm to 2000 mm
             Setup.DropTestSetupBeginEdit();
             Setup.DropType = 0;
             Setup.DropHeightType = 0;
             Setup.DropHeight = 2000;
             Setup.DropHeightUnit = 0;
             errCode = Setup.DropTestSetupEndEdit();

             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to make change to drop height");
             Height = Setup.DropHeight;
             if (Height != 2000)
                 ErrorMsg(swApp, "Failed to correctly change drop height to 2000 mm");

             System.Diagnostics.Debugger.Break();
             // Inspect results for drop height = 1000 mm

             //Run study for drop height = 2000 mm
             errCode = Study.RunAnalysis();
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to run study (drop height = 2000 mm)");
             CWFeatObj = Study.Results;
             if (CWFeatObj == null)
                 ErrorMsg(swApp, "Failed to get Result Object (drop height = 2000 mm)");
             nStep = CWFeatObj.GetMaximumAvailableSteps();
             //nStep = last step of study
             if (nStep != 25)
                 ErrorMsg(swApp, "Total number of steps in result is incorrect (drop height = 2000 mm)");
             Stress = (object[])CWFeatObj.GetMinMaxStress(9, 0, nStep, null, 0, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to get von Mises stress result for drop height = 2000 mm");
             A = (float)Stress[3];
             B = VMS2000;
             if (A < VMS1000 | A == VMS1000)
                 ErrorMsg(swApp, "The von Mises stress result for drop height = 2000 mm is less than or equal to drop height = 1000 mm");
             if (ResultsVer(A, B, Tol) == true)
             {
                 ErrorMsg(swApp, "The von Mises stress result for drop height = 2000 mm has % error = " + ResultsError(A, B, Tol));
             }

         }

         public bool ResultsVer(double ActualResult, double ReferenceResult, double Tolerance)
         {
             return (ActualResult < (1 - Tolerance) * ReferenceResult) | (ActualResult > (1 + Tolerance) * ReferenceResult);
         }

         public double ResultsError(double ActualResult, double ReferenceResult, double Tolerence)
         {
             return (ActualResult - ReferenceResult) / ReferenceResult * 100;
         }

         public void ErrorMsg(SldWorks SwApp, string Message)
         {
             SwApp.SendMsgToUser2(Message, 0, 0);
             SwApp.RecordLine("'*** WARNING - General");
             SwApp.RecordLine("'*** " + Message);
             SwApp.RecordLine("");
         }

         public object SelectByPID(ModelDoc2 nPart, string PIDName, Hashtable PIDCollection)
         {
             object functionReturnValue = null;
             byte[] PID = null;
             string[] PIDVariant = null;
             string PIDString = null;
             int i = 0;
             object SelObj = null;

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
             SelObj = nPart.Extension.GetObjectByPersistReference3((PID), out errCode);
             functionReturnValue = SelObj;
             return functionReturnValue;
         }

         public Hashtable PIDInitializer()
         {
             Hashtable PIDCollection = new Hashtable();
             string selection1 = null;

            selection1 = "230,35,0,0,3,0,0,0,255,254,255,17,112,0,97,0,100,0,95,0,49,0,45,0,49,0,64,0,107,0,101,0,121,0,32,0,112,0,97,0,100,0,95,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,51,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,6,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,55,92,0,92,0,112,0,117,0,110,0,45,0,113,0,97,0,115,0,118,0,114,0,45,0,112,0,108,0,112,0,92,0,81,0,97,0,95,0,100,0,111,0,99,0,117,0,109,0,101,0,110,0,116,0,115,0,92,0,77,0,111,0,98,0,105,0,108,0,101,0,72,0,97,0,110,0,100,0,115,0,101,0,116,0,92,0,80,0,97,0,100,0,95,0,49,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,5,80,0,97,0,100,0,95,0,49,0,2,0,0,0,86,29,67,255,254,2";
            selection1 = selection1 + "55,0,255,254,255,0,0,56,86,29,67,0,0,0,0,0,0,0,0,3,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,56,86,29,67,26,0,0,0,56,86,29,67,0,0,0,0,0,0,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,26,0,0,0,56,86,29,67,1,0,0,0,12,128,0,0,5,128,8,0,26,0,0,0,56,86,29,67,2,0,0,0,12,128,0,0,5,128,8,0,26,0,0,0,56,86,29,67,3,0,0,0,12,128,0,0,5,128,8,0,26,0,0,0,56,86,29,67,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0";
            selection1 = selection1 + ",Type=1";

             //Store constants in a collection
             PIDCollection.Add("selection1", selection1);

             return PIDCollection;
         }

         public SldWorks swApp;

     }

 }
```
