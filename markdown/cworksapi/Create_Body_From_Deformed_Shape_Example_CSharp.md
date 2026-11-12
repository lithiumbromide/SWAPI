---
title: "Create Body From Deformed Shape Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Body_From_Deformed_Shape_Example_CSharp.htm"
---

# Create Body From Deformed Shape Example (C#)

This example shows how to save the deformed shape that results from running a static study.

```vb
  //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
 // 3. Ensure that c:\temp exists.
 // 4. Ensure that the specified model exists.
 // 5. Open an Immediate window.
 //
 // Postconditions:
 //  1. Opens the model document.
 //  2. Adds a default elemental strain plot.
 //  3. Gets the static study.
 //  4. Meshes the model.
 //  5. Sets the solver type.
 //  6. Analyzes the study.
 //  7. Creates the Strain1 plot.
 //  8. Saves only the SOLIDWORKS body from the deformed shape in
 //     c:\temp\deformedBody.sldprt.
 //  9. Gets the size of the deform coordinate array.
 // 10. Gets the plot definition of Strain1.
 // 11. Inspect the Immediate window and c:\temp.
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
 using System.Runtime.InteropServices;
 namespace CreateDeformedBody_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 Part = default(ModelDoc2);
             string fileName = null;
             int errors = 0;
             int warnings = 0;
             int errCode = 0;
             CosmosWorks COSMOSWORKS = default(CosmosWorks);
             CwAddincallback CWAddinCallBack = default(CwAddincallback);
             CWModelDoc ActDoc = default(CWModelDoc);
             CWStudyManager StudyMngr = default(CWStudyManager);
             CWStudy Study = default(CWStudy);
             CWStaticStudyOptions StaticOptions = default(CWStaticStudyOptions);
             CWMesh CWFeatObj = default(CWMesh);
             CWResults res = default(CWResults);

             const double MeshEleSize = 1.4769;
             const double MeshTol = 0.073847;

             fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\tjoint.sldprt";
             Part = swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, 1, "", ref errors, ref warnings);

             CWAddinCallBack = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
             COSMOSWORKS = CWAddinCallBack.CosmosWorks;

             ActDoc = COSMOSWORKS.ActiveDoc;
             errCode = ActDoc.AddDefaultStaticStudyPlot((int)swsDefaultStaticResultTypes_e.swsStaticResultElementalStrain, (int)swsStaticResultElementalStrainComponentTypes_e.swsStaticElementalStrain_ENERGY);

             StudyMngr = ActDoc.StudyManager;
             Study = StudyMngr.GetStudy(1);
             Study.ActivateConfiguration();
             StudyMngr.ActiveStudy = 1;

             //Mesh
             CWFeatObj = Study.Mesh;
             CWFeatObj.MesherType = 0;
             CWFeatObj.Quality = 0;
             errCode = Study.CreateMesh(0, MeshEleSize, MeshTol);
             CWFeatObj = null;

             //Set solver type to FFEPlus
             StaticOptions = Study.StaticStudyOptions;
             StaticOptions.SolverType = 2;

             //Run analysis
             errCode = Study.RunAnalysis();

             res = Study.Results;

             //Save only the SOLIDWORKS body from the deformed shape
             errCode = res.CreateDeformedBody2((int)swsCreateDeformedBodyOption_e.swsCreateDeformedBodyAsPart, (int)swsCreateDeformedBodyAdvancedOption_e.swsCreateDeformedBodyAdvanced_OutputBodyOnly, 1, "deformedBody", "c:\\temp");
             Debug.Print("Create deformed body result code as defined in swsCreateDeformedBodyError_e: " + errCode);
             Debug.Print("Option to use when the deformed body fails to sew into a solid object as defined in swsCreateDeformedBodyFailedSewOption_e: " + res.GetDeformedBodyFailedSewOption());

             object[] vCoord = null;
             int plotType = 0;
             string nComp = "";
             bool bNodal = false;
             bool bDeformed = false;
             double dScaleFactor = 0;
             vCoord = (object[])res.GetDeformedCoord("Strain1", out errCode);
             Debug.Print("Deformed coordinate array size: " + vCoord.GetUpperBound(0));

             errCode = res.GetPlotDefinition("Strain1", out plotType, out nComp, out bNodal, out bDeformed, out dScaleFactor);
             Debug.Print("Plot definition");
             Debug.Print("  Name: Strain1");
             Debug.Print("  Type as defined in swsPlotResultTypes_e: " + plotType);
             Debug.Print("  Component name: " + nComp);
             Debug.Print("  Nodal? (True = nodal, False = elemental) " + bNodal);
             Debug.Print("  Deformed? " + bDeformed);
             Debug.Print("  Scale factor: " + dScaleFactor);

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }

 }
```
