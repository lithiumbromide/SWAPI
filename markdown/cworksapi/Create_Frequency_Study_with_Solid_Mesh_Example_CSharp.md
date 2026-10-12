---
title: "Create Frequency Study with Solid Mesh Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Frequency_Study_with_Solid_Mesh_Example_CSharp.htm"
---

# Create Frequency Study with Solid Mesh Example (C#)

This example shows how to create a frequency study with solid mesh.

```vb
//--------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in  (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
 // 3. Ensure that the specified model exists.
 // 4. Ensure that the specified material library exists.
 // 5. Open the Immediate window.
 //
 // Postconditions:
 // 1. Opens the assembly.
 // 2. Specifies the default frequency study results plots.
 // 3. Creates a frequency study.
 // 4. Applies the same material to all bodies.
 // 5. Creates a mesh with default global size and tolerance parameters.
 // 6. Sets the number of frequencies.
 // 7. Runs the analysis.
 // 8. Gets the result frequencies and mass participation factors.
 // 9. Inspect the results plots and the Immediate window.
 //
 // NOTE: Because the model is used elsewhere, do not save any changes.
 // -----------------------------------------------------------------
```

```vb
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using SolidWorks.Interop.cosworks;
using System;
namespace CreateFrequencyStudySolidMeshCSharp.csproj
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
            CWFrequencyStudyOptions FrequencyOptions = default(CWFrequencyStudyOptions);
            int status = 0;
            int warnings = 0;
            int errCode = 0;
            int errorCode = 0;
            int CompCount = 0;
            int BodyCount = 0;
            int j = 0;
            int i = 0;
            int returnValue = 0;
            object Freq = null;
            object MassPart = null;
            double el = 0;
            double tl = 0;

            // Get SOLIDWORKS Simulation object
            COSMOSObject = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
            if (COSMOSObject == null) ErrorMsg("COSMOSObject object not found");
            COSMOSWORKS = (CosmosWorks)COSMOSObject.CosmosWorks;
            if (COSMOSWORKS == null) ErrorMsg("COSMOSWORKS object not found");

            // Get active document
            swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2017\\Simulation Examples\\shaft.sldasm", (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref status, ref warnings);
            ActDoc = (CWModelDoc)COSMOSWORKS.ActiveDoc;
            if (ActDoc == null) ErrorMsg("No active document");
```

```vb
            // Add default frequency study result plot of resultant amplitude
             errCode = ActDoc.AddDefaultFrequencyOrBucklingStudyPlot(true, 0, true, (int)swsFrequencyBucklingResultDisplacementComponentTypes_e.swsFrequencyBucklingDisplacement_URES);
```

```vb
            // Create new frequency study
            StudyMngr = (CWStudyManager)ActDoc.StudyManager;
            if (StudyMngr == null) ErrorMsg("No CWStudyManager object");
            Study = (CWStudy)StudyMngr.CreateNewStudy3("Frequency", (int)swsAnalysisStudyType_e.swsAnalysisStudyTypeFrequency, (int)swsMeshType_e.swsMeshTypeSolid, out errCode);
            if (Study == null) ErrorMsg("Study not created");

            // Get number of solid components
            SolidMgr = (CWSolidManager)Study.SolidManager;
            if (SolidMgr == null) ErrorMsg("No CWSolidManager object");
            CompCount = SolidMgr.ComponentCount;

            // Apply SOLIDWORKS material to rest of components
            SolidBody = null;
            SolidComponent = null;
            for (j = 0; j <= (CompCount - 1); j++)
            {
                SolidComponent = (CWSolidComponent)SolidMgr.GetComponentAt(j, out errorCode);
                BodyCount = SolidComponent.SolidBodyCount;
                for (i = 0; i <= (BodyCount - 1); i++)
                {
                    SolidBody = (CWSolidBody)SolidComponent.GetSolidBodyAt(i, out errCode);
                    if (errCode != 0) ErrorMsg("No solid body");
                    returnValue = SolidBody.SetLibraryMaterial("c:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\\english\\sldmaterials\\solidworks materials.sldmat", "Ductile Iron (SN)");
                    if (returnValue != 1) ErrorMsg("No material applied");
                    SolidBody = null;
                }
            }

            // Set meshing
            CwMesh = (CWMesh)Study.Mesh;
            if (CwMesh == null) ErrorMsg("No mesh object");
            CwMesh.Quality = 1;
            CwMesh.GetDefaultElementSizeAndTolerance(0, out el, out tl);
            errCode = Study.CreateMesh(0, el, tl);
            if (errCode != 0) ErrorMsg("Mesh failed");

             // Set frequency study options
             FrequencyOptions = Study.FrequencyStudyOptions;
             if (FrequencyOptions == null)
                     ErrorMsg("No CWFrequencyStudyOptions object");

             FrequencyOptions.Options = (int)swsFrequencyStudyOption_e.swsFrequencyStudyOptionNumberFrequencies;
             FrequencyOptions.NoOfFrequencies = 8;

             Debug.Print("Study: " + Study.Name);
             Debug.Print("  Option as defined in swsFrequencyStudyOption_e: " + FrequencyOptions.Options);
             if (FrequencyOptions.Options == 1)
             {
                     Debug.Print("  Upper-bound frequency: " + FrequencyOptions.UpperBoundFrequency);
             }
             else if (FrequencyOptions.Options == 0)
             {
                     Debug.Print("  Number of frequencies: " + FrequencyOptions.NoOfFrequencies);
                     Debug.Print("  Calculate frequencies around a specified frequency? (true=yes, false=no): " + FrequencyOptions.UseLowerBoundFrequency2);
                     if (FrequencyOptions.UseLowerBoundFrequency2)
                     {
                         Debug.Print("    Lower bound frequency: " + FrequencyOptions.LowerBoundFrequency);
                     }
             }

             Debug.Print("  Result folder: " + FrequencyOptions.ResultFolder);
             Debug.Print("  Solver type as defined in swsSolverType_e: " + FrequencyOptions.SolverType);
             Debug.Print("  Use soft spring to stabilize the model? (true=yes, false=no): " + FrequencyOptions.UseSoftSpring2);
             double zeroStrainTemp = 0;
             int tempUnit = 0;
             FrequencyOptions.GetZeroStrainTemperature(out zeroStrainTemp, out tempUnit);
             Debug.Print("  Flow/Thermal Effects:");
             Debug.Print("    Temperature source as defined in swsThermalOption_e: " + FrequencyOptions.ThermalResults);
             Debug.Print("    Temperature source:");
             if (FrequencyOptions.ThermalResults == 1)
             {
                     Debug.Print("        Thermal study: " + FrequencyOptions.ThermalStudyName);
                     Debug.Print("        Time step of transient thermal study: " + FrequencyOptions.TimeStep);
             }
             else if (FrequencyOptions.ThermalResults == 2)
             {
                     Debug.Print("        SOLIDWORKS Flow Simulation results file: " + FrequencyOptions.FlowTemperatureFile);
             }
             else
             {
                     Debug.Print("        Model");
             }
             Debug.Print("    Reference temperature at zero strain: " + zeroStrainTemp);
             Debug.Print("    Import fluid pressure loads from SOLIDWORKS Flow Simulation? (true=yes, false=no): " + FrequencyOptions.CheckFlowPressure2);
             if (FrequencyOptions.CheckFlowPressure2)
             {
                     Debug.Print("        SOLIDWORKS Flow Simulation results file: " + FrequencyOptions.FlowPressureFile);
                     Debug.Print("        Use reference pressure offset from Flow Simulation? (1=yes, 0=no): " + FrequencyOptions.ReferencePressureOption);
                     if (FrequencyOptions.ReferencePressureOption == 1)
                     {
                         Debug.Print("          Reference pressure offset: " + FrequencyOptions.DefinedReferencePressure);
                     }
                     Debug.Print("        Run as legacy study and import only the normal component of the pressure load? (true=yes, false=no): " + FrequencyOptions.CheckRunAsLegacy2);
             }

            // Run analysis
            errCode = Study.RunAnalysis();
            if (errCode != 0) ErrorMsg("Analysis failed");

            // Get results: frequencies and mass participation factors
            CWResult = (CWResults)Study.Results;
            if (CWResult == null) ErrorMsg("No result object");
            Freq = CWResult.GetResonantFrequencies(out errCode);
            MassPart = CWResult.GetMassParticipation(out errCode);
        }

        private void ErrorMsg(string Message)
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
