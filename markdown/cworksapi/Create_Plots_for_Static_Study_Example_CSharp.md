---
title: "Create Plots for a Static Study Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Plots_for_Static_Study_Example_CSharp.htm"
---

# Create Plots for a Static Study Example (C#)

This example shows how to create plots of displacement, stress, and strain results in a static study.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 //  1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //     Tools > Add-ins > SOLIDWORKS Simulation > OK).
 //  2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
  //     (in the IDE, click Project > Add Reference > .NET >
  //     SolidWorks.Interop.cosworks > OK).
 //  3. Ensure that c:\temp exists.
 //  4. Open public_documents\samples\Simulation Examples\tutor1.sldprt.
 //  5. Open the Immediate window.
 //
 // Postconditions:
  //  1. Deletes all default static study plots from the model document.
 //  2. Activates the Ready static study.
 //  3. Meshes and runs the study.
 //  4. Creates Displacement1 plot.
 //  5. Changes the units of the displacement plot.
 //  6. Creates and activates Stress2 plot.
  //  7. Probes and annotates Stress2 and saves the probed  result plot to
 //     c:\temp\tutor1-Ready-Image-1.png.
 //  8. Creates Strain1 plot.
 //  9. Applies a view orientation to each plot.
  // 10. Gets the minimum and maximum values for the result plots.
 // 11. Click OK to close each message box.
 // 12. Detect stress hot spots and singularities.
 // 13. Creates the Stress Hot Spot1 plot and gets hot spot nodes and elements.
 // 14. Inspect c:\temp\tutor1-Ready-Image-1.png.
  // 15. Inspect the Immediate window.
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
 using System.Runtime.InteropServices;
 using SolidWorks.Interop.cosworks;
 namespace CreatePlotsForStaticStudy_CSharp.csproj
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
             CWResultsProbeManager CWProbeResultsManager = default(CWResultsProbeManager);

             int errCode = 0;
             double el = 0;
             double tl = 0;
             object[] Disp = null;
             object[] Stress = null;
             object[] Strn = null;

             const double URESMax = 1004928; //nm
             const double URESMin = 0.0;     //nm
             const double VONMax = 284;      //MPa
             const double VONMin = 0.797;    //MPa
             const double MaxStrn = 0.00352;
             const double MinStrn = 2.94E-06;

             CWAddinCallBack = (CwAddincallback)swApp.GetAddInObject("CosmosWorks.CosmosWorks");
             if (CWAddinCallBack == null)
                 ErrorMsg(swApp, "No CWAddinCallBack object", true);
             COSMOSWORKS = CWAddinCallBack.CosmosWorks;
             if (COSMOSWORKS == null)
                 ErrorMsg(swApp, "No CosmosWorks object", true);

             //Get active document
             ActDoc = COSMOSWORKS.ActiveDoc;
             if (ActDoc == null)
                 ErrorMsg(swApp, "No active document", true);

             //Delete all default static study plots from this model
             ActDoc.DeleteAllDefaultStaticStudyPlots();

             //Get Ready study
             StudyMngr = ActDoc.StudyManager;
             if (StudyMngr == null)
                 ErrorMsg(swApp, "No study manager object", true);
             StudyMngr.ActiveStudy = 0;
             Study = StudyMngr.GetStudy(0);
             if (Study == null)
                 ErrorMsg(swApp, "Study not created", true);

             //Set static study options
             CWStaticStudyOptions StudyOptions;
             StudyOptions = Study.StaticStudyOptions;
             StudyOptions.AdaptiveMethodType = 2;
             StudyOptions.PAdaptiveConvergenceCriteria = 0;
             StudyOptions.PAdaptiveErrorLimit = 1.0;
             StudyOptions.PAdaptiveMaxIterations = 4;
             StudyOptions.PAdaptiveMaxPOrder = 5;
             StudyOptions.PAdaptiveStartingPOrder = 2;
             StudyOptions.PAdaptiveStrainEnergyErrorLimit = 2.0;
             StudyOptions.IncludeRemarkInReport = 1;
             StudyOptions.RemarkComment = "Remark comment";
             StudyOptions.NoPenetration = 1;
             StudyOptions.IgnoreClearanceForSurfaceContact = 1;
             StudyOptions.IncompatibleBondingOption = (int)swsIncompatibleBondingOption_e.swsIncompatibleBondingOption_Automatic;
             StudyOptions.IncludeGlobalFriction = 1;
             StudyOptions.FrictionCoefficient = 0.5;

             //Mesh
             CWMesh = Study.Mesh;
             if (CWMesh == null)
                 ErrorMsg(swApp, "No mesh object", false);
             CWMesh.Quality = 1;
             CWMesh.GetDefaultElementSizeAndTolerance(0, out el, out tl);
             errCode = Study.CreateMesh(0, el, tl);
             if (errCode != 0)
                 ErrorMsg(swApp, "Mesh failed", true);

             //Run analysis
             errCode = Study.RunAnalysis();
             if (errCode != 0)
                 ErrorMsg(swApp, "Analysis failed", true);

             //Get results
             CWResult = Study.Results;
             if (CWResult == null)
                 ErrorMsg(swApp, "No result object", false);

             Debug.Print("Time taken in seconds for input phase: " + Study.GetTimeTakenForInputPhase());
             Debug.Print("Time taken in seconds to solve this study: " + Study.GetTotalSolutionTime());

             //Create displacement plot
             CWCFf = CWResult.CreatePlot((int)swsPlotResultTypes_e.swsResultDisplacementOrAmplitude, (int)swsDisplacementComponent_e.swsDisplacementComponentURES, (int)swsUnit_e.swsUnitSI, false, out errCode);
             if (CWCFf == null)
                 ErrorMsg(swApp, "Failed to create plot", false);

             //Change the units from cm to in
             errCode = CWCFf.SetComponentUnitAndValueByElem((int)swsDisplacementComponent_e.swsDisplacementComponentURES, (int)swsLinearUnit_e.swsLinearUnitInches, false);

             //Apply top view orientation
             errCode = CWCFf.ApplyNameViewOrientation2((int)swsNameViewOrientation_e.swsNameViewOrientation_Top);

             //Activate plot
             errCode = CWCFf.ActivatePlot();
             if (errCode != 0)
                 ErrorMsg(swApp, "Plot is not activated", true);

             //Get min/max resultant displacements from plot
             Disp = (object[])CWCFf.GetMinMaxResultValues(out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "No displacement results", true);

             double Disp1 = Convert.ToDouble(Disp[1]);
             double Disp3 = Convert.ToDouble(Disp[3]);

             if ((Disp1 < 0.95 * URESMin) | (Disp1 > 1.05 * URESMin))
             {
                 ErrorMsg(swApp, "URES minimum % error = " + (((Disp1 - URESMin) / URESMin) * 100), false);
             }

             if ((Disp3 < 0.95 * URESMax) | (Disp3 > 1.05 * URESMax))
             {
                 ErrorMsg(swApp, "URES maximum % error = " + (((Disp3 - URESMax) / URESMax) * 100), false);
             }

             //Create stress plot
             CWCFf = CWResult.CreatePlot((int)swsPlotResultTypes_e.swsResultStress, (int)swsStaticResultNodalStressComponentTypes_e.swsStaticNodalStress_VON, (int)swsUnit_e.swsUnitSI, false, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to create plot", true);

             //Apply bottom view orientation
             errCode = CWCFf.ApplyNameViewOrientation2((int)swsNameViewOrientation_e.swsNameViewOrientation_Bottom);

             //Activate plot
             errCode = CWCFf.ActivatePlot();
             if (errCode != 0)
                 ErrorMsg(swApp, "Plot is not activated", true);

             //Get min/max von Mises stresses from plot
             Stress = (object[])CWCFf.GetMinMaxResultValues(out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "No stress results", true);

             double Stress1 = Convert.ToDouble(Stress[1]);
             double Stress3 = Convert.ToDouble(Stress[3]);

             if ((Stress1 < 0.95 * VONMin) | (Stress1 > 1.05 * VONMin))
             {
                 ErrorMsg(swApp, " Minimum von Mises stress % error = " + (((Stress1 - VONMin) / VONMin) * 100), false);
             }

             if ((Stress3 < 0.95 * VONMax) | (Stress3 > 1.05 * VONMax))
             {
                 ErrorMsg(swApp, "Maximum von Mises stress % error = " + (((Stress3 - VONMax) / VONMax) * 100), false);
             }

             // Probe stress plot at two locations
             CWProbeResultsManager = CWCFf.GetResultsProbeManager(out errCode);
             int[] SelNodeElemVariant = { 1033, 924 };
             object SelNodeElemWarnings;

             errCode = CWProbeResultsManager.BeginProbing();
             CWProbeResultsManager.ClearSelectionAndAnnotations();
             CWProbeResultsManager.ProbingOption = (int)swsProbePostResultOption_e.swsProbePostResultOption_AtNodeElemNumber;
            errCode = CWProbeResultsManager.ShowAnnotationOnSelNodeElems((SelNodeElemVariant), out SelNodeElemWarnings);
             if (errCode == 14)
                 ErrorMsg(swApp, "Not all specified nodes or elements are annotated", true);
             errCode = CWProbeResultsManager.CaptureProbedResultPlotAsPNGImage("c:\\temp\\", "tutor1-Ready-Image-1");
             errCode = CWProbeResultsManager.EndProbing();

             //Create strain plot
             CWCFf = CWResult.CreatePlot((int)swsPlotResultTypes_e.swsResultStrain, (int)swsStaticResultElementalStrainComponentTypes_e.swsStaticElementalStrain_ESTRN, (int)swsUnit_e.swsUnitEnglish, true, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to create plot", true);

             //Apply left view orientation
             errCode = CWCFf.ApplyNameViewOrientation2((int)swsNameViewOrientation_e.swsNameViewOrientation_Left);

             //Activate plot
             errCode = CWCFf.ActivatePlot();
             if (errCode != 0)
                 ErrorMsg(swApp, "Plot is not activated", true);

             //Get min/max strains from plot
             Strn = (object[])CWCFf.GetMinMaxResultValues(out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "No strain results", true);

             double Strn1 = Convert.ToDouble(Strn[1]);
             double Strn3 = Convert.ToDouble(Strn[3]);

             if ((Strn1 < 0.95 * MinStrn) | (Strn1 > 1.05 * MinStrn))
             {
                 ErrorMsg(swApp, "Minimum strain % error = " + (((Strn1 - MinStrn) / MinStrn) * 100), false);
             }

             if ((Strn3 < 0.95 * MaxStrn) | (Strn3 > 1.05 * MaxStrn))
             {
                 ErrorMsg(swApp, "Maximum strain % error = " + (((Strn3 - MaxStrn) / MaxStrn) * 100), false);
             }

             //Detect stress hot spots and singularities
             Boolean hotSpotsFound;
             Boolean singularitiesFound;
             object nodeArray;
             object elemArray;
             errCode = CWResult.RunStressHotSpotDiagnostics(25, true, 3, 0.6, 1.5, 0, out hotSpotsFound, out singularitiesFound);

             //Create stress hot spot plot and get detected hot spots
             if (hotSpotsFound == true) {
                 errCode = CWResult.GetDetectedHotSpotNodes(out nodeArray);
                 errCode = CWResult.GetDetectedHotSpotElements(out elemArray);
                 CWCFf = CWResult.CreateStressHotSpotPlot(true, true, out errCode);
             }

         }

         public void ErrorMsg(SldWorks SwApp, string Message, bool EndTest)
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
