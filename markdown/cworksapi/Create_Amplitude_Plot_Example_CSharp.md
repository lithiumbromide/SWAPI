---
title: "Create Amplitude Plot and Set Mode Shape Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Amplitude_Plot_Example_CSharp.htm"
---

# Create Amplitude Plot and Set Mode Shape Example (C#)

This example shows how to create an amplitude plot and set its mode shape number.

```vb
//---------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
 // 3. Open public_documents\samples\Simulation Examples\tutor1.sldprt.
 // 4. Create a frequency study and apply material to the model.
 //
 // Postconditions:
 // 1. Activates the Frequency1 study.
 // 2. Meshes and analyzes the study.
 // 3. Creates one or more default resultant amplitude plots, depending on your
 //    Tools > Simulation > Options > Default Options > Frequency/Buckling Study
 //    Results settings.
 // 4. Creates another resultant amplitude plot and sets its mode shape number
 //    to 4.
 // 5. Gets the minimum and maximum resultant amplitudes for the last plot.
 // 6. Click OK to close any error dialog boxes.
 //
 // NOTE: Because the model is used elsewhere, do not save changes.
 // --------------------------------------------------------------------------
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
 namespace CreatePlot_Frequency_CSharp.csproj
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

             int errCode = 0;
             double el = 0;
             double tl = 0;
             object[] Disp = null;

             const double DispMax = 1.424;
             const double DispMin = 0.1;

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

             //Get Frequency1 study
             StudyMngr = ActDoc.StudyManager;
             if (StudyMngr == null)
                 ErrorMsg(swApp, "No CWStudyManager object");
             StudyMngr.ActiveStudy = 1;
             Study = StudyMngr.GetStudy(1);
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

             //Create resultant amplitude plot
             CWCFf = CWResult.CreatePlot((int)swsPlotResultTypes_e.swsResultDisplacementOrAmplitude, (int)swsFrequencyBucklingResultDisplacementComponentTypes_e.swsFrequencyBucklingDisplacement_URES, (int)swsUnit_e.swsUnitSI, false, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failure to create plot");

             //Set mode shape number of plot to 4
             errCode = CWCFf.SetModeShape(4);
             if (errCode != 0)
                 ErrorMsg(swApp, "Plot is not set for specified mode shape");

             errCode = CWCFf.ActivatePlot();
             if (errCode != 0)
                 ErrorMsg(swApp, "Plot is not activated");

             //Get min/max resultant amplitudes from plot
             Disp = (object[])CWCFf.GetMinMaxResultValues(out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "No amplitude values");

             if ((Convert.ToDouble(Disp[1]) < 0.95 * DispMin) | (Convert.ToDouble(Disp[1]) > 1.05 * DispMin))
             {
                 ErrorMsg(swApp, " Minimum amplitude % error = " + (((Convert.ToDouble(Disp[1]) - DispMin) / DispMin) * 100));
             }

             if ((Convert.ToDouble(Disp[3]) < 0.95 * DispMax) | (Convert.ToDouble(Disp[3]) > 1.05 * DispMax))
             {
                 ErrorMsg(swApp, "Maximum amplitude % error = " + (((Convert.ToDouble(Disp[3]) - DispMax) / DispMax) * 100));
             }

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
