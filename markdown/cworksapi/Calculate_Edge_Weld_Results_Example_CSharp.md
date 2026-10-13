---
title: "Calculate Edge Weld Results Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Calculate_Edge_Weld_Results_Example_CSharp.htm"
---

# Calculate Edge Weld Results Example (C#)

This example shows how to calculate the edge weld results for a specific edge weld connector.

```vb
//---------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
 // 3. Open the Immediate window.
 // 4. Verify that the specified model exists.
 //
 // Postconditions:
 // 1. Opens the part document.
 // 2. Meshes the part.
 // 3. Sets the solver type.
 // 4. Runs the analysis.
 // 5. Gets the edge weld results for Edge Weld Connector-1.
 // 6. Prints the edge weld results to the Immediate window.
 //
 // NOTE: Because this part document is used elsewhere,
 // do not save any changes when closing the document.
 //----------------------------------------------------------------------------

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using SolidWorks.Interop.cosworks;
 using System.Diagnostics;

 namespace EdgeWeld.csproj
 {
     public partial class SolidWorksMacro
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
             string ConnectorName = null;
             CWResults Results = default(CWResults);
             bool PassFail = false;
             object[] EdgeResult = null;

             //Tolerances and baselines
             const double MeshEleSize = 1.4769; //mm
             const double MeshTol = 0.073847; //mm

             //Open document
             fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\tjoint.sldprt";
             Part = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, 1, "", ref errors, ref warnings);
             //Part = (ModelDoc2)SwApp.ActiveDoc;

             //Add-in callback
             CWAddinCallBack = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
             COSMOSWORKS = (CosmosWorks)CWAddinCallBack.CosmosWorks;

             //Get active document
             ActDoc = (CWModelDoc)COSMOSWORKS.ActiveDoc;

             //Get study
             StudyMngr = (CWStudyManager)ActDoc.StudyManager;
             Study = (CWStudy)StudyMngr.GetStudy(0);
             Study.ActivateConfiguration();
             StudyMngr.ActiveStudy = 0;

             //Mesh
             CWFeatObj = (CWMesh)Study.Mesh;
             CWFeatObj.MesherType = 0;
             CWFeatObj.Quality = 0;
             errCode = Study.CreateMesh(0, MeshEleSize, MeshTol);
             CWFeatObj = null;

             //Set solver type as FFEPlus
             StaticOptions = Study.StaticStudyOptions;
             StaticOptions.SolverType = 2;

             //Run analysis
             errCode = (int)Study.RunAnalysis();

             Results = Study.Results;

             //Get edge weld results
             ConnectorName = "Edge Weld Connector-1";
             EdgeResult = (object[])Results.GetEdgeWeldResults(ConnectorName, (int)swsUnit_e.swsUnitSI, out PassFail, out errCode);

             //Print results to Immediate window
             long i = 0;
             Debug.Print("Results: ");
             for (i = 0; i < (EdgeResult.Length - 1); i++)
             {
                 Debug.Print("  " + EdgeResult[i]);
             }

             //Delete study
             StudyMngr.DeleteStudy(Study.Name);

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;
     }
 }
```
