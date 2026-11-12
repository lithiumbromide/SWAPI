---
title: "Simultaneously Edit Multiple Contact Sets Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Simultaneously_Edit_Multiple_Contact_Sets_Example_CSharp.htm"
---

# Simultaneously Edit Multiple Contact Sets Example (C#)

This example shows how to add multiple contact sets to a frequency study and simultaneously edit them.

NOTE: To get persistent reference identifiers (PIDs) for model selections, you can use [pidcollector.exe](GettingStarted-swsimulationapi.html) or IModelDocExtension::GetPersistReference3.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in  (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
  // 3. Ensure that the specified model document exists.
 // 4. Open the Immediate window.
 //
 // Postconditions:
 // 1. Opens the model.
 // 2. Gets the Ready study.
 // 3. Adds two contact sets.
  // 4. Simultaneously edits the contact sets to change types
 //    from Bonded to Allow Penetration.
 // 5. Creates a mesh.
 // 6. Runs an analysis.
  // 7. Inspect the Immediate window and the Simulation Study tree.
 //
  // NOTE: Because the model is used elsewhere, do not save changes.
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

 namespace EditContactSets_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {

             CosmosWorks COSMOSWORKS = default(CosmosWorks);
             CwAddincallback COSMOSObject = default(CwAddincallback);
             CWModelDoc ActDoc = default(CWModelDoc);
             CWStudyManager StudyMngr = default(CWStudyManager);
             CWStudy Study = default(CWStudy);
             CWMesh CwMesh = default(CWMesh);
             CWResults CWResult = default(CWResults);
             ModelDoc2 Part = default(ModelDoc2);
             CWContactManager ContactMgr = default(CWContactManager);
             CWContactSet CWContactSet = default(CWContactSet);
             object pDisp1 = null;
             object pDisp2 = null;
             object pDisp3 = null;
             byte[] var8 = null;
             byte[] var9 = null;
             byte[] var10 = null;
             object[] Freq = null;
             string str1 = null;
             string str2 = null;
             string str3 = null;
             int longstatus = 0;
             int longwarnings = 0;
             int errCode = 0;
             double el = 0;
             double tl = 0;
             int i = 0;

             swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2017\\Simulation Examples\\shaft.sldasm", (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref longstatus, ref longwarnings);
             Part = (ModelDoc2)swApp.ActiveDoc;

             COSMOSObject = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
             if (COSMOSObject == null)
                 ErrorMsg(swApp, "COSMOSObject object not found");

             COSMOSWORKS = COSMOSObject.CosmosWorks;
             if (COSMOSWORKS == null)
                 ErrorMsg(swApp, "COSMOSWORKS object not found");

             ActDoc = COSMOSWORKS.ActiveDoc;
             if (ActDoc == null)
                 ErrorMsg(swApp, "No active document");

             // Gets the Ready study
             StudyMngr = ActDoc.StudyManager;
             if (StudyMngr == null)
                 ErrorMsg(swApp, "No CWStudyManager object");

             Study = StudyMngr.GetStudy(0);
             if (Study == null)
                 ErrorMsg(swApp, "No study found");

             // Get selections for multiple contact sets

             // Shaft source
             str1 = "189,35,0,0,3,0,0,0,255,254,255,23,111,0,118,0,101,0,114,0,101,0,110,0,100,0,101,0,114,0,32,0,115,0,104,0,97,0,102,0,116,0,45,0,49,0,64,0,115,0,104,0,97,0,102,0,116,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,13,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,58,67,0,58,0,92,0,67,0,79,0,83,0,77,0,79,0,83,0,68,0,111,0,99,0,115,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,95,0,102,0,111,0,114,0,67,0,117,0,115,0,116,0,111,0,109,0,101,0,114,0,115,0,92,0,111,0,118,0,101,0,114,0,101,0,110,0,100,0,101,0,114,0,32,0,115,0,104,0,97,0,102,0,116,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,";
             str1 = str1 + "9,128,255,254,255,15,111,0,118,0,101,0,114,0,101,0,110,0,100,0,101,0,114,0,32,0,115,0,104,0,97,0,102,0,116,0,2,0,0,5,73,58,52,255,254,255,0,0,123,22,28,65,1,0,0,0,0,0,0,0,35,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,45,0,0,0,0,0,0,0,123,22,28,65,10,0,0,0,65,73,58,52,1,0,0,0,255,255,1,0,19,0,109,111,70,105,108,108,101,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,13,0,0,0,97,73,58,52,1,0,0,0,0,0,12,128,0,0,5,128,8,0,14,0,0,0,108,73,58,52,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0";
             StringtoArray(str1, ref var8);
             pDisp1 = Part.Extension.GetObjectByPersistReference3((var8), out longstatus);

             // Bore 1 target
             str2 = "189,35,0,0,3,0,0,0,255,254,255,28,112,0,98,0,32,0,98,0,101,0,97,0,114,0,105,0,110,0,103,0,95,0,49,0,46,0,53,0,48,0,32,0,98,0,111,0,114,0,101,0,45,0,50,0,64,0,115,0,104,0,97,0,102,0,116,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,21,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,63,67,0,58,0,92,0,67,0,79,0,83,0,77,0,79,0,83,0,68,0,111,0,99,0,115,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,95,0,102,0,111,0,114,0,67,0,117,0,115,0,116,0,111,0,109,0,101,0,114,0,115,0,92,0,112,0,98,0,32,0,98,0,101,0,97,0,114,0,105,0,110,0,103,0,95,0,49,0,46,0,53,0,48,0,32,0,98,0,111,0,114,0,101,0,46,0,8";
             str2 = str2 + "3,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,20,112,0,98,0,32,0,98,0,101,0,97,0,114,0,105,0,110,0,103,0,95,0,49,0,46,0,53,0,48,0,32,0,98,0,111,0,114,0,101,0,2,0,0,130,66,58,52,255,254,255,0,0,144,22,28,65,1,0,0,0,0,0,0,0,34,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,52,0,0,0,0,0,0,0,144,22,28,65,15,0,0,0,58,68,58,52,1,0,0,0,255,255,255,255,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,15,0,0,0,58,68,58,52,1,0,0,0,0,0,12,128,0,0,5,128,8,0,19,0,0,0,141,68,58,52,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0";
             StringtoArray(str2, ref var9);
             pDisp2 = Part.Extension.GetObjectByPersistReference3((var9), out longstatus);

             // Bore 2 target
             str3 = "189,35,0,0,3,0,0,0,255,254,255,28,112,0,98,0,32,0,98,0,101,0,97,0,114,0,105,0,110,0,103,0,95,0,49,0,46,0,53,0,48,0,32,0,98,0,111,0,114,0,101,0,45,0,49,0,64,0,115,0,104,0,97,0,102,0,116,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,20,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,63,67,0,58,0,92,0,67,0,79,0,83,0,77,0,79,0,83,0,68,0,111,0,99,0,115,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,95,0,102,0,111,0,114,0,67,0,117,0,115,0,116,0,111,0,109,0,101,0,114,0,115,0,92,0,112,0,98,0,32,0,98,0,101,0,97,0,114,0,105,0,110,0,103,0,95,0,49,0,46,0,53,0,48,0,32,0,98,0,111,0,114,0,101,0,46,0,8";
             str3 = str3 + "3,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,20,112,0,98,0,32,0,98,0,101,0,97,0,114,0,105,0,110,0,103,0,95,0,49,0,46,0,53,0,48,0,32,0,98,0,111,0,114,0,101,0,2,0,0,130,66,58,52,255,254,255,0,0,144,22,28,65,1,0,0,0,0,0,0,0,34,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,52,0,0,0,0,0,0,0,144,22,28,65,15,0,0,0,58,68,58,52,1,0,0,0,255,255,255,255,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,15,0,0,0,58,68,58,52,1,0,0,0,0,0,12,128,0,0,5,128,8,0,19,0,0,0,141,68,58,52,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0";
             StringtoArray(str3, ref var10);
             pDisp3 = Part.Extension.GetObjectByPersistReference3((var10), out longstatus);

             // Create arrays
             object[] varArray3 = { pDisp1 };
             object[] varArray4 = { pDisp2 };
             object[] varArray5 = { pDisp3 };

             // Add bonded contact sets
             ContactMgr = Study.ContactManager;
             if (errCode != 0)
                 ErrorMsg(swApp, "No ContactManager object");
             CWContactSet = ContactMgr.CreateContactSet2((int)swsContactType_e.swsContactTypeBonded, 0, (varArray3), (varArray4), out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "No CWContactSet object");

             CWContactSet = ContactMgr.CreateContactSet2((int)swsContactType_e.swsContactTypeBonded, 0, (varArray3), (varArray5), out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "No CWContactSet object");

             // Simultaneously edit both contact sets
             CWMultipleContactSetsEditManager multCSEM = default(CWMultipleContactSetsEditManager);
             multCSEM = Study.MultipleContactSetsEditManager;
             errCode = multCSEM.AddContactSet("Contact Set-1");
             errCode = multCSEM.AddContactSet("Contact Set-2");
             Debug.Print("Number of contact sets added: " + multCSEM.GetContactSetCount());
             multCSEM.MultipleContactSetsBeginEdit();
             errCode = multCSEM.SetAsDefaultContactSet("Contact Set-1");
             errCode = multCSEM.SetContactType((int)swsContactType_e.swsContactTypeFreeOrInsulated);
             multCSEM.MultipleContactSetsEndEdit();

             // Mesh
             CwMesh = Study.Mesh;
             if (CwMesh == null)
                 ErrorMsg(swApp, "No CWMesh object");

             CwMesh.Quality = 1;
             CwMesh.GetDefaultElementSizeAndTolerance((int)swsLinearUnit_e.swsLinearUnitMillimeters, out el, out tl);

             errCode = Study.CreateMesh((int)swsLinearUnit_e.swsLinearUnitMillimeters, el, tl);
             if (errCode != 0)
                 ErrorMsg(swApp, "Mesh failed");

             // Run analysis
             errCode = Study.RunAnalysis();
             if (errCode != 0)
                 ErrorMsg(swApp, "Analysis failed with error code as defined in swsRunAnalysisError_e: " + errCode);

             // Get results
             CWResult = Study.Results;
             if (CWResult == null)
                 ErrorMsg(swApp, "No CWResults object");

             Freq = (object[])CWResult.GetResonantFrequencies(out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "No frequency result");

             Debug.Print("Resonant frequencies:");

             for (i = 0; i <= Freq.GetUpperBound(0); i++)
             {
                 Debug.Print(Freq[i].ToString());
             }
         }

         private void ErrorMsg(SldWorks SwApp, string Message)
         {

             SwApp.SendMsgToUser2(Message, 0, 0);
             SwApp.RecordLine("'*** WARNING - General");
             SwApp.RecordLine("'*** " + Message);
             SwApp.RecordLine("");

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

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```
