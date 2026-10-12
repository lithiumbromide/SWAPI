---
title: "Convert Study Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Convert_Study_Example_CSharp.htm"
---

# Convert Study Example (C#)

This example shows how to convert a static study to a linear dynamic harmonic study.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
 // 3. Open  public_documents\samples\Simulation Examples\tutor1.sldprt.
 //
 // Postconditions:
 // 1. Converts the Ready study to the LinDynHarmonic study.
 // 2. Sets damping options for, meshes, and analyzes LinDynHarmonic.
 // 3. Inspect the Simulation study tree.
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
 namespace ConvertStudy_CSharp.csproj
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
             CWResults CWResult = default(CWResults);
             CWDampingOptions DampingOptions = default(CWDampingOptions);
             object[] DampingRatios = new object[9];

             int errCode = 0;
             double el = 0;
             double tl = 0;

             CWAddinCallBack = (CwAddincallback)swApp.GetAddInObject("CosmosWorks.CosmosWorks");
             if (CWAddinCallBack == null)
                 ErrorMsg(swApp, "No CWAddinCallBack object");
             COSMOSWORKS = CWAddinCallBack.CosmosWorks;
             if (COSMOSWORKS == null)
                 ErrorMsg(swApp, "No CosmosWorks object");

             //Get active document
             ActDoc = COSMOSWORKS.ActiveDoc;
             if (ActDoc == null)
                 ErrorMsg(swApp, "No active document");

             //Get Ready study
             StudyMngr = ActDoc.StudyManager;
             if (StudyMngr == null)
                 ErrorMsg(swApp, "No CWStudyManager object");
             StudyMngr.ActiveStudy = 0;
             Study = StudyMngr.GetStudy(0);
             if (Study == null)
                 ErrorMsg(swApp, "No CWStudy object");

             //Convert study
             Study = StudyMngr.ConvertStudy2("Ready", (int)swsAnalysisStudyType_e.swsAnalysisStudyTypeStatic, "LinDynHarmonic", (int)swsAnalysisStudyType_e.swsAnalysisStudyTypeDynamic, "Default", (int)swsDynamicAnalysisSubType_e.swsDynamicAnalysisSubTypeHarmonic, false, false, out errCode);
             if (Study == null)
                 ErrorMsg(swApp, "Study not converted");

             //Set damping options
             DampingOptions = Study.DampingOptions;
             DampingOptions.DampingType = 0; //modal damping
             DampingOptions.ComputeFromMaterialDamping = 0; //do not use material damping ratios
             DampingOptions.ClearAllDampingRatios();
             DampingRatios[0] = 1;
             DampingRatios[1] = 5;
             DampingRatios[2] = 3.45;
             DampingRatios[3] = 6;
             DampingRatios[4] = 15;
             DampingRatios[5] = 15;
             DampingRatios[6] = 16;
             DampingRatios[7] = 25;
             DampingRatios[8] = 34.5;
             errCode = DampingOptions.SetDampingRatios(3, (DampingRatios));

             //Mesh the converted study
             CWMesh = Study.Mesh;
             if (CWMesh == null)
                 ErrorMsg(swApp, "No CWMesh object");
             CWMesh.Quality = 0;
             CWMesh.GetDefaultElementSizeAndTolerance(0, out el, out tl);
             errCode = Study.CreateMesh(0, el, tl);
             if (errCode != 0)
                 ErrorMsg(swApp, "Mesh failed");

             //Analyze the converted study
             errCode = Study.RunAnalysis();
             if (errCode != 0)
                 ErrorMsg(swApp, "Analysis failed");

             CWResult = Study.Results;
             if (CWResult == null)
                 ErrorMsg(swApp, "No CWResults object");

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
