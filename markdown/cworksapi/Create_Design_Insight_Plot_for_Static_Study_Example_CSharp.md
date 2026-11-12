---
title: "Create a Design Insight Plot for a Static Study Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Design_Insight_Plot_for_Static_Study_Example_CSharp.htm"
---

# Create a Design Insight Plot for a Static Study Example (C#)

This example shows how to create a Design Insight plot and set its load level.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
 // 3. Open public_documents\samples\Simulation Examples\actuator.sldasm.
 //
 // Postconditions:
  // 1. Deletes all default static study plots from the model document.
 // 2. Activates the Ready static study.
 // 3. Meshes and runs the study.
 // 4. Creates a Design Insight plot.
  // 5. Gets the Design Insight plot and sets its load level to 50.
 // 6. Inspect the graphics area.
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
 namespace CreateDesignInsight_CSharp.csproj
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
             CWPlot CWCFf = default(CWPlot);
             CWPlot plot = default(CWPlot);
             int errCode = 0;
             double el = 0;
             double tl = 0;

             CWAddinCallBack = (CwAddincallback)swApp.GetAddInObject("CosmosWorks.CosmosWorks");
             if (CWAddinCallBack == null)
                 ErrorMsg(swApp, "No CWAddincallback object");
             COSMOSWORKS = CWAddinCallBack.CosmosWorks;
             if (COSMOSWORKS == null)
                 ErrorMsg(swApp, "No CosmosWorks object");

             //Get active document
             ActDoc = COSMOSWORKS.ActiveDoc;
             if (ActDoc == null)
                 ErrorMsg(swApp, "No active document");

             //Delete all default static study plots from this model
             ActDoc.DeleteAllDefaultStaticStudyPlots();

             //Get Ready study
             StudyMngr = ActDoc.StudyManager;
             if (StudyMngr == null)
                 ErrorMsg(swApp, "No CWStudyManager object");
             StudyMngr.ActiveStudy = 0;
             Study = StudyMngr.GetStudy(0);
             if (Study == null)
                 ErrorMsg(swApp, "No CWStudy object");

             //Mesh
             CWMesh = Study.Mesh;
             if (CWMesh == null)
                 ErrorMsg(swApp, "No CWMesh object");
             CWMesh.Quality = 0;
             CWMesh.GetDefaultElementSizeAndTolerance(0, out el, out tl);
             errCode = Study.CreateMesh(0, el, tl);
             if (errCode != 0)
                 ErrorMsg(swApp, "Mesh failed");

             //Run analysis
             errCode = Study.RunAnalysis();
             if (errCode != 0)
                 ErrorMsg(swApp, "Analysis failed with error code as defined in swsRunAnalysisError_e: " + errCode);

             //Get results
             CWResult = Study.Results;
             if (CWResult == null)
                 ErrorMsg(swApp, "No CWResults object");

             //Create Design Insight plot of the results
             CWCFf = CWResult.CreatePlot((int)swsPlotResultTypes_e.swsResultDesignInsight, 0, (int)swsUnit_e.swsUnitSI, false, out errCode);
             if (CWCFf == null)
                 ErrorMsg(swApp, "Failed to create plot");

             //Get Design Insight plot
             plot = CWResult.GetPlot("Design Insight1", out errCode);

             //Set load level of Design Insight plot
             plot.IsoValue = 50;

             //Activate plot
             errCode = plot.ActivatePlot();
             if (errCode != 0)
                 ErrorMsg(swApp, "Plot is not activated");
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
