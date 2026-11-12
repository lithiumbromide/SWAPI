---
title: "Create Nonlinear Dynamic Plots Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Nonlinear_Dynamic_Plots_Example_CSharp.htm"
---

# Create Nonlinear Dynamic Plots Example (C#)

This example shows how to a create a plot of a specific solution step of a nonlinear dynamic study.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
 // 3. Open public_documents\samples\Simulation Examples\tutor1.sldprt.
 //
 // Postconditions:
 // 1. Activates Nonlinear1 study.
 // 2. Meshes and analyzes the study.
 // 3. Creates displacement, stress, and strain plots of solution step 72.
 // 4. Gets the min/max values for the result plots.
 // 5. Click OK to close any error dialog boxes.
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
 namespace CreatePlot_NL_Dynamic_CSharp.csproj
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
             object[] Stress = null;
             object[] Strn = null;

             const double URESMax = 11.26;   //nm
             const double URESMin = 0.0;     //nm
             const double VONMax = 0.00319;  //MPa
             const double VONMin = 8.95E-06; //MPa

             const double MaxStrn = 3.95E-08;
             const double MinStrn = 3.3E-11;

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

             //Get the Nonlinear1 study
             StudyMngr = ActDoc.StudyManager;
             if (StudyMngr == null)
                 ErrorMsg(swApp, "No study manager object");
             StudyMngr.ActiveStudy = 1;
             Study = StudyMngr.GetStudy(1);
             if (Study == null)
                 ErrorMsg(swApp, "No study object");

             //Mesh
             CWMesh = Study.Mesh;
             if (CWMesh == null)
                 ErrorMsg(swApp, "No mesh object");
             CWMesh.Quality = 0;
             CWMesh.GetDefaultElementSizeAndTolerance(0, out el, out tl);
             errCode = Study.CreateMesh(0, el, tl);
             if (errCode != 0)
                 ErrorMsg(swApp, "Mesh failed");

             //Run analysis
             errCode = Study.RunAnalysis();
             if (errCode != 0)
                 ErrorMsg(swApp, "Analysis failed");

             //Get results
             CWResult = Study.Results;
             if (CWResult == null)
                 ErrorMsg(swApp, "No result object");

             //Create resultant displacement plot
             CWCFf = CWResult.CreatePlot((int)swsPlotResultTypes_e.swsResultDisplacementOrAmplitude, (int)swsStaticResultDisplacementComponentTypes_e.swsStaticDisplacement_URES, (int)swsUnit_e.swsUnitSI, false, out errCode);
             if (CWCFf == null)
                 ErrorMsg(swApp, "Failure to create plot");

             //Display plot of step 72
             errCode = CWCFf.SetPlotStepNumber(72);
             if (errCode != 0)
                 ErrorMsg(swApp, "Plot is not activated for the given step");

             errCode = CWCFf.ActivatePlot();
             if (errCode != 0)
                 ErrorMsg(swApp, "Plot is not activated");

             //Get min/max resultant displacements from plot
             Disp = (object[])CWCFf.GetMinMaxResultValues(out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "No displacement results");

             if ((Convert.ToDouble(Disp[1]) < 0.95 * URESMin) | (Convert.ToDouble(Disp[1]) > 1.05 * URESMin))
             {
                 ErrorMsg(swApp, "URES minimum % error = " + (((Convert.ToDouble(Disp[1]) - URESMin) / URESMin) * 100));
             }

             if ((Convert.ToDouble(Disp[3]) < 0.95 * URESMax) | (Convert.ToDouble(Disp[3]) > 1.05 * URESMax))
             {
                 ErrorMsg(swApp, "URES maximum % error = " + (((Convert.ToDouble(Disp[3]) - URESMax) / URESMax) * 100));
             }

             //Create stress plot
             CWCFf = CWResult.CreatePlot((int)swsPlotResultTypes_e.swsResultStress, (int)swsStaticResultNodalStressComponentTypes_e.swsStaticNodalStress_VON, (int)swsUnit_e.swsUnitSI, false, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failure to create plot");

             //Display plot of step 72
             errCode = CWCFf.SetPlotStepNumber(72);
             if (errCode != 0)
                 ErrorMsg(swApp, "Plot is not activated for the given step");

             errCode = CWCFf.ActivatePlot();
             if (errCode != 0)
                 ErrorMsg(swApp, "Plot is not activated");

             //Get min/max von Mises stresses from plot
             Stress = (object[])CWCFf.GetMinMaxResultValues(out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "No stress results");

             if ((Convert.ToDouble(Stress[1]) < 0.95 * VONMin) | (Convert.ToDouble(Stress[1]) > 1.05 * VONMin))
             {
                 ErrorMsg(swApp, " Minimum von Mises stress % error = " + (((Convert.ToDouble(Stress[1]) - VONMin) / VONMin) * 100));
             }

             if ((Convert.ToDouble(Stress[3]) < 0.95 * VONMax) | (Convert.ToDouble(Stress[3]) > 1.05 * VONMax))
             {
                 ErrorMsg(swApp, "Maximum von Mises stress % error = " + (((Convert.ToDouble(Stress[3]) - VONMax) / VONMax) * 100));
             }

             //Create equivalent elemental strain plot
             CWCFf = CWResult.CreatePlot((int)swsPlotResultTypes_e.swsResultStrain, (int)swsStaticResultElementalStrainComponentTypes_e.swsStaticElementalStrain_ESTRN, (int)swsUnit_e.swsUnitSI, true, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failure to create plot");

             //Display plot of step 72
             errCode = CWCFf.SetPlotStepNumber(72);
             if (errCode != 0)
                 ErrorMsg(swApp, "Plot is not activated for the given step");

             errCode = CWCFf.ActivatePlot();
             if (errCode != 0)
                 ErrorMsg(swApp, "Plot is not activated");

             //Get min/max strains from plot
             Strn = (object[])CWCFf.GetMinMaxResultValues(out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "No strain results");

             if ((Convert.ToDouble(Strn[1]) < 0.95 * MinStrn) | (Convert.ToDouble(Strn[1]) > 1.05 * MinStrn))
             {
                 ErrorMsg(swApp, "Minimum strain % error = " + (((Convert.ToDouble(Strn[1]) - MinStrn) / MinStrn) * 100));
             }

             if ((Convert.ToDouble(Strn[3]) < 0.95 * MaxStrn) | (Convert.ToDouble(Strn[3]) > 1.05 * MaxStrn))
             {
                 ErrorMsg(swApp, "Maximum strain % error = " + (((Convert.ToDouble(Strn[3]) - MaxStrn) / MaxStrn) * 100));
             }

         }

         public void ErrorMsg(SldWorks SwApp, string Message)
         {
             SwApp.SendMsgToUser2(Message, 0, 0);
             SwApp.RecordLine("'*** WARNING - General");
             SwApp.RecordLine("'*** " + Message);
             SwApp.RecordLine("");
         }

         public SldWorks swApp;

     }
 }
```
