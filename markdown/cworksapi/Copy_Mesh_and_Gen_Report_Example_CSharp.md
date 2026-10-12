---
title: "Copy Mesh and Generate Report Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Copy_Mesh_and_Gen_Report_Example_CSharp.htm"
---

# Copy Mesh and Generate Report Example (C#)

This example shows how to copy the mesh from one study to another and generate a report.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
 // 3. Open public_documents\samples\Simulation Examples\Verification\buckling2.sldprt.
 //
 // Postconditions:
 // 1. Meshes the Quality and Draft studies.
  // 2. Copies the mesh from the Quality study to the Draft study.
 // 3. Click OK to close any dialog boxes.
 // 4. Generates a report for the Draft study in c:\temp.
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
 namespace CopyMesh_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             CosmosWorks COSMOSWORKS = default(CosmosWorks);
             CwAddincallback CWAddinCallBack = default(CwAddincallback);
             CWModelDoc ActDoc = default(CWModelDoc);
             CWStudyManager StudyMngr = default(CWStudyManager);
             CWStudy Study = default(CWStudy);
             CWMesh CWMesh = default(CWMesh);

             int errCode = 0;
             int n = 0;
             double el = 0;
             double tl = 0;

             const double NoOfElements1 = 712;
             const double NoOfElements2 = 2686;

             CWAddinCallBack = (CwAddincallback)swApp.GetAddInObject("CosmosWorks.CosmosWorks");
             if (CWAddinCallBack == null)
                 ErrorMsg(swApp, "No CwAddincallback object");
             COSMOSWORKS = CWAddinCallBack.CosmosWorks;
             if (COSMOSWORKS == null)
                 ErrorMsg(swApp, "No CosmosWorks object");

             //Get active document
             ActDoc = COSMOSWORKS.ActiveDoc;
             if (ActDoc == null)
                 ErrorMsg(swApp, "No active document");

             //Get the first study
             StudyMngr = ActDoc.StudyManager;
             if (StudyMngr == null)
                 ErrorMsg(swApp, "No CWStudyManager object");
             StudyMngr.ActiveStudy = 0;
             Study = StudyMngr.GetStudy(0);
             if (Study == null)
                 ErrorMsg(swApp, "No CWStudy object");

             //Mesh the first study
             CWMesh = Study.Mesh;
             if (CWMesh == null)
                 ErrorMsg(swApp, "No CWMesh object");
             CWMesh.Quality = 1;
             CWMesh.GetDefaultElementSizeAndTolerance(0, out el, out tl);
             errCode = Study.CreateMesh(0, el, tl);
             if (errCode != 0)
                 ErrorMsg(swApp, "Mesh failed");

             n = CWMesh.NodeCount;

             if ((n < 0.95 * NoOfElements2) | (n > 1.05 * NoOfElements2))
             {
                 ErrorMsg(swApp, " % error = " + (((n - NoOfElements2) / NoOfElements2) * 100));
             }

             //Get the second study
             StudyMngr.ActiveStudy = 1;
             Study = StudyMngr.GetStudy(1);
             if (Study == null)
                 ErrorMsg(swApp, "No CWStudy object");

             //Mesh the second study
             CWMesh = Study.Mesh;
             if (CWMesh == null)
                 ErrorMsg(swApp, "No CWMesh object");
             CWMesh.Quality = 0;
             CWMesh.GetDefaultElementSizeAndTolerance(0, out el, out tl);
             errCode = Study.CreateMesh(0, el, tl);
             if (errCode != 0)
                 ErrorMsg(swApp, "Mesh failed");

             n = CWMesh.NodeCount;
             if ((n < 0.95 * NoOfElements1) | (n > 1.05 * NoOfElements1))
             {
                 ErrorMsg(swApp, " % error = " + (((n - NoOfElements1) / NoOfElements1) * 100));
             }

             //Copy mesh from the first study to the second study
             errCode = Study.CopyMeshFromStudy("Quality");
             if (errCode != 0)
                 ErrorMsg(swApp, "Mesh failed to copy");

             n = CWMesh.NodeCount;
             if ((n < 0.95 * NoOfElements2) | (n > 1.05 * NoOfElements2))
             {
                 ErrorMsg(swApp, " % error = " + (((n - NoOfElements2) / NoOfElements2) * 100));
             }

             //Generate Report
             errCode = Study.GenerateReport("C:\\temp", "report");
             if (errCode != 1)
                 ErrorMsg(swApp, "Failed to generate report");

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
