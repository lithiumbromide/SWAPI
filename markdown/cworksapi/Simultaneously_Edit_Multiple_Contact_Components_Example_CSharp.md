---
title: "Simultaneously Edit Multiple Component Contacts Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Simultaneously_Edit_Multiple_Contact_Components_Example_CSharp.htm"
---

# Simultaneously Edit Multiple Component Contacts Example (C#)

This example shows how to add multiple component contacts to a frequency study and simultaneously edit them.

NOTE: To get persistent reference identifiers (PIDs) for model selections, you can use [pidcollector.exe](GettingStarted-swsimulationapi.html) or IModelDocExtension::GetPersistReference3.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 //  1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //     Tools > Add-ins > SOLIDWORKS Simulation > OK).
 //  2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //     (in the IDE, click Project > Add Reference > .NET >
 //     SolidWorks.Interop.cosworks > OK).
  //  3. Ensure that the specified material library exists.
  //  4. Ensure that the specified model document exists.
 //  5. Open the Immediate window.
 //
 // Postconditions:
 //  1. Opens the model.
 //  2. Creates Frequency 1 study.
 //  3. Uses a soft spring to stabilize the model.
 //  4. Adds Component Contact-1 and Component Contact-2 to the
  //     Component Contacts folder in the Simulation study tree.
 //  5. Edits simultaneously both component contacts.
 //  6. Applies ductile iron to the model.
 //  7. Meshes the model.
 //  8. Analyzes Frequency 1.
  //  9. Prints the resonant frequencies of each mode to the Immediate window.
  // 10. Inspect the Immediate window, the Simulation study tree, and the
 //     graphics area.
 //
  // NOTE: Because the model is used elsewhere, do not save changes.
  //----------------------------------------------------------------------------
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
 namespace EditMultipleCompContacts_CSharp.csproj
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
             CWSolidManager SolidMgr = default(CWSolidManager);
             CWSolidComponent SolidComponent = default(CWSolidComponent);
             CWSolidBody SolidBody = default(CWSolidBody);
             CWMesh CwMesh = default(CWMesh);
             CWResults CWResult = default(CWResults);
             ModelDoc2 Part = default(ModelDoc2);
             CWContactManager ContactMgr = default(CWContactManager);
             CWContactComponent CWComponentContact = default(CWContactComponent);
             object pDisp3 = null;
             object pDisp4 = null;
             byte[] var20 = null;
             byte[] var21 = null;
             object[] Freq = null;
             int bApp = 0;
             string str3 = null;
             string str4 = null;
             int longstatus = 0;
             int longwarnings = 0;
             int errCode = 0;
             double el = 0;
             double tl = 0;
             int i = 0;

             swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2017\\Simulation Examples\\Contact\\quartereyebar.sldasm", (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref longstatus, ref longwarnings);
             Part = (ModelDoc2)swApp.ActiveDoc;

             COSMOSObject = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
             if (COSMOSObject == null)
                 ErrorMsg(swApp, "Failed to get Simulation add-in");

             COSMOSWORKS = COSMOSObject.CosmosWorks;
             if (COSMOSWORKS == null)
                 ErrorMsg(swApp, "Failed to get COSMOSWORKS");

             ActDoc = COSMOSWORKS.ActiveDoc;
             if (ActDoc == null)
                 ErrorMsg(swApp, "Failed to get active document");

             // Create new frequency study
             StudyMngr = ActDoc.StudyManager;
             if (StudyMngr == null)
                 ErrorMsg(swApp, "Failed to get study manager");

             Study = StudyMngr.CreateNewStudy3("Frequency 1", (int)swsAnalysisStudyType_e.swsAnalysisStudyTypeFrequency, 0, out errCode);
             if (Study == null)
                 ErrorMsg(swApp, "Failed to create frequency study");

             ICWFrequencyStudyOptions StudyOptions = default(ICWFrequencyStudyOptions);
             StudyOptions = Study.FrequencyStudyOptions;
             StudyOptions.UseSoftSpring = 1;

             str3 = "64,31,0,0,4,0,0,0,255,254,255,29,81,0,117,0,97,0,114,0,116,0,101,0,114,0,69,0,121,0,101,0,66,0,97,0,114,0,45,0,49,0,64,0,113,0,117,0,97,0,114,0,116,0,101,0,114,0,101,0,121,0,101,0,98,0,97,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,9,0,0,0,3,0,0,0,103,0,0,0,102,0,0,0,101,0,0,0";
             StringtoArray(str3, ref var20);
             pDisp3 = Part.Extension.GetObjectByPersistReference3((var20), out longstatus);

             str4 = "64,31,0,0,5,0,0,0,255,254,255,27,81,0,117,0,97,0,114,0,116,0,101,0,114,0,66,0,111,0,108,0,116,0,45,0,49,0,64,0,113,0,117,0,97,0,114,0,116,0,101,0,114,0,101,0,121,0,101,0,98,0,97,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,11,0,0,0";
             StringtoArray(str4, ref var21);
             pDisp4 = Part.Extension.GetObjectByPersistReference3((var21), out longstatus);

             ContactMgr = Study.ContactManager;
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to get contact manager");

             ContactMgr.DeleteContactComponent("Global Contact");

             // Add bonded component contacts
             CWComponentContact = ContactMgr.CreateContactComponent((int)swsContactType_e.swsContactTypeBonded, (int)swsMeshCompatibility_e.swsMeshCompatibilityCompatible, pDisp3, out errCode);
             CWComponentContact = ContactMgr.CreateContactComponent((int)swsContactType_e.swsContactTypeBonded, (int)swsMeshCompatibility_e.swsMeshCompatibilityCompatible, pDisp4, out errCode);

             // Simultaneously edit both component contacts
             CWMultipleComponentContactsEditManager multCCEM = default(CWMultipleComponentContactsEditManager);
             multCCEM = Study.MultipleComponentContactsEditManager;
             errCode = multCCEM.AddContactComponent("Component Contact-1");
             errCode = multCCEM.AddContactComponent("Component Contact-2");
             Debug.Print("Number of contact components to edit simultaneously: " + multCCEM.GetContactComponentsCount());
             multCCEM.MultipleComponentContactsBeginEdit();
             Debug.Print("  Setting default component contact to Component Contact-1");
             errCode = multCCEM.SetAsDefaultComponentContact("Component Contact-1");
             Debug.Print("  Setting contact type to Allow Penetration");
             Debug.Print("");
             errCode = multCCEM.SetContactType((int)swsContactType_e.swsContactTypeFreeOrInsulated);
             multCCEM.MultipleComponentContactsEndEdit();

             // Apply material to model
             SolidMgr = Study.SolidManager;
             if (SolidMgr == null)
                 ErrorMsg(swApp, "No solid manager");

             SolidComponent = SolidMgr.GetComponentAt(0, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "No solid component");

             SolidBody = SolidComponent.GetSolidBodyAt(0, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "No solid body");

             bApp = SolidBody.SetLibraryMaterial("c:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\\english\\sldmaterials\\solidworks materials.sldmat", "Ductile Iron");
             if (bApp == 0)
                 ErrorMsg(swApp, "No material applied");

             SolidComponent = SolidMgr.GetComponentAt(1, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "No solid component");

             SolidBody = SolidComponent.GetSolidBodyAt(0, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "No solid body");

             bApp = SolidBody.SetLibraryMaterial("c:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\\english\\sldmaterials\\solidworks materials.sldmat", "Ductile Iron");
             if (bApp == 0)
                 ErrorMsg(swApp, "No material applied");

             // Mesh model
             CwMesh = Study.Mesh;
             if (CwMesh == null)
                 ErrorMsg(swApp, "Failed to get mesh object");

             CwMesh.Quality = 1;
             CwMesh.GetDefaultElementSizeAndTolerance((int)swsLinearUnit_e.swsLinearUnitMillimeters, out el, out tl);

             errCode = Study.CreateMesh((int)swsLinearUnit_e.swsLinearUnitMillimeters, el, tl);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to create mesh");

             // Run analysis
             errCode = Study.RunAnalysis();
             if (errCode != 0)
                 ErrorMsg(swApp, "Analysis failed with error code as defined in swsRunAnalysisError_e: " + errCode);

             // Get resonant frequencies for each mode
             CWResult = Study.Results;
             if (CWResult == null)
                 ErrorMsg(swApp, "Failed to get results object");

             Freq = (object[])CWResult.GetResonantFrequencies(out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to get resonant frequencies");

             Debug.Print("Resonant frequencies (mode number, radians/second, cycles/second, period in seconds):");
             for (i = 0; i <= Freq.GetUpperBound(0); i++)
             {
                 Debug.Print("  " + Freq[i]);
             }
         }

         public void ErrorMsg(SldWorks SwApp, string Message)
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
