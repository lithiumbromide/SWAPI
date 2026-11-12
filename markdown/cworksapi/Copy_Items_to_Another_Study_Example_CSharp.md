---
title: "Copy Items to Another Study Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Copy_Items_to_Another_Study_Example_CSharp.htm"
---

# Copy Items to Another Study Example (C#)

This example shows how to copy contact sets and fixtures from one study to another.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
 // 3. Ensure the specified model exists.
 // 4. Open the Immediate window.
 //
 // Postconditions:
 // 1. Opens the assembly document.
 // 2. Copies fixtures and contact sets from Ready to Partial.
 // 3. Activates Partial.
 // 4. Meshes Partial.
 // 5. Analyzes Partial.
  // 6. Inspect the Immediate window, the Simulation study tree, and the
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
 namespace CopyItems_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             CosmosWorks COSMOSWORKS = null;
             CwAddincallback COSMOSObject = default(CwAddincallback);
             CWModelDoc ActDoc = default(CWModelDoc);
             CWStudyManager StudyMngr = default(CWStudyManager);
             CWStudy Study = default(CWStudy);
             CWMesh CwMesh = default(CWMesh);
             CWLoadsAndRestraintsManager lrMngr = default(CWLoadsAndRestraintsManager);
             CWLoadsAndRestraints Fixture = default(CWLoadsAndRestraints);
             CWContactManager ContactMgr = default(CWContactManager);
             CWContactSet ContactSet = default(CWContactSet);
             int errCode = 0;
             int errors = 0;
             int warnings = 0;
             object[] contactSets = new object[1];
             object[] fixtures = new object[3];
             int i = 0;

             const string fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2017\\Simulation Examples\\Contact\\slider_locker_mechanism.sldasm";

             COSMOSObject = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
             if (COSMOSObject == null)
                 ErrorMsg(swApp, "No Simulation add-in");
             COSMOSWORKS = COSMOSObject.CosmosWorks;
             if (COSMOSWORKS == null)
                 ErrorMsg(swApp, "No COSMOSWORKS object");

             swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
             ActDoc = COSMOSWORKS.ActiveDoc;
             if (ActDoc == null)
                 ErrorMsg(swApp, "No active document");

             StudyMngr = ActDoc.StudyManager;
             if (StudyMngr == null)
                 ErrorMsg(swApp, "No CWStudyManager object");
             Study = StudyMngr.GetStudy(0);
             StudyMngr.ActiveStudy = 0;
             if (Study == null)
                 ErrorMsg(swApp, "No CWStudy object");
             if ((Study.Name != "Ready"))
                 ErrorMsg(swApp, "Wrong study");
             Debug.Print("Name of study: " + Study.Name);

             // Create array of names of contact sets to copy
             ContactMgr = Study.ContactManager;
             for (i = 0; i <= (ContactMgr.ContactSetCount - 1); i++)
             {
                 ContactSet = ContactMgr.GetContactSetAt(i);
                 contactSets[i] = ContactSet.ContactName;
             }

             // Create array of names of fixtures to copy
             lrMngr = Study.LoadsAndRestraintsManager;
             for (i = 0; i <= (lrMngr.Count - 1); i++)
             {
                 Fixture = lrMngr.GetLoadsAndRestraints(i, out errCode);
                 fixtures[i] = Fixture.Name;
             }

             // Copy fixtures and contact sets from Ready study to Partial study
             errCode = ContactMgr.CopyContactsToStudy("Partial", contactSets);
             errCode = lrMngr.CopyLoadsAndRestraintsToStudy("Partial", fixtures);

             // Activate Partial study
             Study = StudyMngr.GetStudy(1);
             StudyMngr.ActiveStudy = 1;

             CwMesh = Study.Mesh;
             if (CwMesh == null)
                 ErrorMsg(swApp, "No CWMesh object");

             // Set type of mesh to curvature-based
             CwMesh.MesherType = (int)swsMesherType_e.swsMesherTypeAlternate;

             // Set mesh parameters
             CwMesh.GrowthRatio = 1.6;
             CwMesh.MinElementsInCircle = 8;

             // Create mesh
             errCode = Study.CreateMesh((int)swsLinearUnit_e.swsLinearUnitMillimeters, 20, 1);

             if (errCode != 0)
                 ErrorMsg(swApp, "Mesh failed with error code as defined in swsStudyMeshError_e: " + errCode);

             errCode = Study.RunAnalysis();

             if (errCode != 0)
                 ErrorMsg(swApp, "Analysis failed with error code as defined in swsRunAnalysisError_e: " + errCode);

         }
         public void ErrorMsg(SldWorks swApp, string Message)
         {
             swApp.SendMsgToUser2(Message, 0, 0);
             swApp.RecordLine("'*** WARNING - General");
             swApp.RecordLine("'*** " + Message);
             swApp.RecordLine("");
         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }

 }
```
