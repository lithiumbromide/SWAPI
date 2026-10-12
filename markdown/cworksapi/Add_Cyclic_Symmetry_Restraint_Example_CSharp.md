---
title: "Add Cyclic Symmetry Restraint Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Add_Cyclic_Symmetry_Restraint_Example_CSharp.htm"
---

# Add Cyclic Symmetry Restraint Example (C#)

This example shows how to add a cyclic symmetry restraint to a static study.

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
 //
 // Postconditions:
 // 1. Opens the specified model document.
 // 2. Gets study, Partial-Solids.
 // 3. Adds the Cyclic Symmetry-1 fixture to Partial-Solids.
 // 4. Meshes the model.
 // 5. Analyzes Partial-Solids.
  // 6. Inspect the Simulation study tree and the graphics area.
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
 namespace AddCyclicSymmetricRestraint_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Part;
         CosmosWorks COSMOSWORKS;
         CwAddincallback CWAddinCallBack;
         CWModelDoc ActDoc;
         CWStudyManager StudyMngr;
         CWStudy Study;
         CWLoadsAndRestraintsManager LBCMgr;
         CWRestraint Restraint;
         int errCode;
         int longstatus;
         int longwarnings;
         object Axis1;
         object Face1;
         object Face2;

         const double MeshEleSize = 4.48279654351123;
         const double MeshTol = 0.224139827175561;
         const double Tol1 = 0.05;

         public void Main()
         {

             Part = swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2017\\Simulation Examples\\pressurevessel.sldprt", 1, 0, "", ref longstatus, ref longwarnings);
             Part = (ModelDoc2)swApp.ActiveDoc;

             Hashtable PIDCollection = new Hashtable();
             PIDCollection = PIDInitializer();

             Axis1 = SelectByPID(Part, "selection1", PIDCollection); // axis of revolution
             Face1 = SelectByPID(Part, "selection2", PIDCollection); // first face
             Face2 = SelectByPID(Part, "selection3", PIDCollection); // second face

             CWAddinCallBack = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
             if (CWAddinCallBack == null)
                 ErrorMsg(swApp, "Failed to get Simulation add-in");
             COSMOSWORKS = CWAddinCallBack.CosmosWorks;
             if (COSMOSWORKS == null)
                 ErrorMsg(swApp, "Failed to get COSMOSWORKS");

             ActDoc = COSMOSWORKS.ActiveDoc;
             if (ActDoc == null)
                 ErrorMsg(swApp, "Failed to get active document");

             //Get the static study
             StudyMngr = ActDoc.StudyManager;
             if (StudyMngr == null)
                 ErrorMsg(swApp, "No CWStudyManager object");
             Study = StudyMngr.GetStudy(1);
             if (Study == null)
                 ErrorMsg(swApp, "Failed to get study");
             StudyMngr.ActiveStudy = 1;

             //Add a cyclic symmetric restraint
             LBCMgr = Study.LoadsAndRestraintsManager;
             if (LBCMgr == null)
                 ErrorMsg(swApp, "No CWLoadsAndRestraintsManager object");

             Restraint = LBCMgr.AddCyclicSymmetryRestraint(Face1, Face2, Axis1, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Adding cyclic symmetry restraint failed with error as defined in swsCyclicRestraintError_e: " + errCode);

             //Mesh the model
             CWMesh CWMeshObj = default(CWMesh);
             CWMeshObj = Study.Mesh;
             if (CWMeshObj == null)
                 ErrorMsg(swApp, "No CWMesh object");
             CWMeshObj.MesherType = 0;
             CWMeshObj.Quality = 0;
             errCode = Study.CreateMesh(0, MeshEleSize, MeshTol);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to create mesh");
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
             string selection1 = null;
             string selection2 = null;
             string selection3 = null;

             //Axis1
             selection1 = "234,35,0,0,1,0,0,0,255,254,255,0,0,0,0,0,49,0,0,0";
             selection1 = selection1 + ",Type=1";

             //First face
             selection2 = "234,35,0,0,3,0,0,0,255,254,255,0,0,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,10,0,0,0,0,2,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,85,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,32,0,67,0,111,0,114,0,112,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,92,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,112,0,114,0,101,0,115,0,115,0,117,0,114,0,101,0,118,0,101,0,115,0,115,0,101,0,108,0,46,0,115,0,108,0,100,0,112,0,114,0,116,0,9,128,255,254,255,14,112,0,114";
             selection2 = selection2 + ",0,101,0,115,0,115,0,117,0,114,0,101,0,118,0,101,0,115,0,115,0,101,0,108,0,2,0,0,148,98,134,61,255,254,255,0,255,254,255,0,0,224,22,28,65,1,0,0,0,0,0,0,0,1,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,224,22,28,65,44,0,0,0,178,133,134,61,0,0,0,0,2,0,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,44,0,0,0,178,133,134,61,3,0,0,0,3,128,0,0,5,128,8,0,44,0,0,0,178,133,134,61,1,0,0,0,2,0,0,0,12,128,0,0,5,128,8,0,44,0,0,0,178,133,134,61,33,0,0,0,12,128,0,0,5,128,8,0,44,0,0,0,178,133,134,61,32,0,0,0,12,128,0,0,5,128,8,0,44,0,0,0,178,133,134,61,31,0,0,0,3,128,0,0,5,128,8,0,44,0,0,0,178,133,134,61,1,0,0,0,2,0,0,0,12,128,0,0,5,128,8,0,44,0,0,0,178,133,134,61,29,0,0,0,12,128,0,0,5,128,8,0,44,0,0,0,178,133,134,61,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0";
             selection2 = selection2 + ",Type=1";

             //Second Face
             selection3 = "234,35,0,0,3,0,0,0,255,254,255,0,0,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,10,0,0,0,0,2,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,85,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,32,0,67,0,111,0,114,0,112,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,92,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,112,0,114,0,101,0,115,0,115,0,117,0,114,0,101,0,118,0,101,0,115,0,115,0,101,0,108,0,46,0,115,0,108,0,100,0,112,0,114,0,116,0,9,128,255,254,255,14,112,0,114";
             selection3 = selection3 + ",0,101,0,115,0,115,0,117,0,114,0,101,0,118,0,101,0,115,0,115,0,101,0,108,0,2,0,0,148,98,134,61,255,254,255,0,255,254,255,0,0,224,22,28,65,1,0,0,0,0,0,0,0,1,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,224,22,28,65,44,0,0,0,178,133,134,61,1,0,0,0,2,0,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,44,0,0,0,178,133,134,61,3,0,0,0,12,128,0,0,5,128,8,0,44,0,0,0,178,133,134,61,2,0,0,0,12,128,0,0,5,128,8,0,44,0,0,0,178,133,134,61,29,0,0,0,3,128,0,0,5,128,8,0,44,0,0,0,178,133,134,61,0,0,0,0,2,0,0,0,12,128,0,0,5,128,8,0,44,0,0,0,178,133,134,61,31,0,0,0,12,128,0,0,5,128,8,0,44,0,0,0,178,133,134,61,32,0,0,0,12,128,0,0,5,128,8,0,44,0,0,0,178,133,134,61,33,0,0,0,3,128,0,0,5,128,8,0,44,0,0,0,178,133,134,61,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0";
             selection3 = selection3 + ",Type=1";

             //Store constants in a collection
             PIDCollection.Add("selection1", selection1);
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
