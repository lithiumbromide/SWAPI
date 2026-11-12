---
title: "Apply Material to Bodies Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Apply_Material_to_Bodies_Example_CSharp.htm"
---

# Apply Material to Bodies Example (C#)

This example shows how to apply user-defined and SOLIDWORKS-defined materials to different bodies.

```vb
//---------------------------------------------------------------------------
// Preconditions:
// 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
//    Tools > Add-ins > SOLIDWORKS Simulation > OK).

// 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference

//    (in the IDE, click Project > Add Reference > .NET >
//    SolidWorks.Interop.cosworks > OK).
// 3. Verify that the specified material library exists.
// 4. Verify that the specified assembly exists.
//
// Postconditions:
// 1. Opens the assembly.
// 2. Creates a nonlinear study.
// 3. Gets the number of components.
// 4. Applies materials to all components.
// 5. Expand the Parts folder in the Simulation Study tree
//    to verify step 4.
//
// NOTE: Because this assembly is used elsewhere, do not save changes.
//-------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using SolidWorks.Interop.cosworks;
using System;
using System.Diagnostics;
namespace SimulationApplyMaterialsBodiesCSharp.csproj
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
            int errorCode = 0;
            int status = 0;
            int warnings = 0;
            int errCode = 0;
            int CompCount = 0;
            int j = 0;
            CWMaterial CWMat = default(CWMaterial);
            int returnValue = 0;
            string SName = null;
            int materialProperty = 0;

            // Get SOLIDWORKS Simulation object>
            COSMOSObject = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
            if (COSMOSObject == null) ErrorMsg("No CwAddincallback object");
            COSMOSWORKS = (CosmosWorks)COSMOSObject.CosmosWorks;
            if (COSMOSWORKS == null) ErrorMsg("No COSMOSWORKS object");

            // Open and get document
            swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2017\\Simulation Examples\\basketball_hoop.sldasm", (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref status, ref warnings);
            ActDoc = (CWModelDoc)COSMOSWORKS.ActiveDoc;
            if (ActDoc == null) ErrorMsg("No active document");

            // Create new nonlinear study
            StudyMngr = (CWStudyManager)ActDoc.StudyManager;
            if (StudyMngr == null) ErrorMsg("No CWStudyManager object");
            Study = (CWStudy)StudyMngr.CreateNewStudy("Nonlinear", (int)swsAnalysisStudyType_e.swsAnalysisStudyTypeNonlinear, (int)swsMeshType_e.swsMeshTypeSolid, out errCode);
            if (Study == null) ErrorMsg("No CWStudy object");

            // Get number of solid components
            SolidMgr = (CWSolidManager)Study.SolidManager;
            if (SolidMgr == null) ErrorMsg("No CWSolidManager object");
            CompCount = SolidMgr.ComponentCount;
            SolidComponent = (CWSolidComponent)SolidMgr.GetComponentAt(0, out errorCode);
            if (SolidComponent == null) ErrorMsg("No CWSolidComponent object");

            // Get name of solid component
            SName = SolidComponent.ComponentName;

            // Apply user-defined material for the first component in the tree
            SolidBody =(CWSolidBody) SolidComponent.GetSolidBodyAt(0, out errCode);
            if (errCode != 0) ErrorMsg("No solid body");
            if (SolidBody == null) ErrorMsg("No CWSolidBody object");
            CWMat = (CWMaterial)SolidBody.GetDefaultMaterial();
            CWMat.MaterialUnits = 0;
            if (CWMat == null) ErrorMsg("No CWMaterial object");
            CWMat.MaterialName = "Alloy Steel";
            CWMat.SetPropertyByName("EX", 210000000000.0, 0);
            Debug.Print("Property EX: " + CWMat.GetPropertyByName((int)swsUnitSystem_e.swsUnitSystemSI, "EX", out materialProperty));
            CWMat.SetPropertyByName("NUXY", 0.28, 0);
            CWMat.SetPropertyByName("GXY", 79000000000.0, 0);
            CWMat.SetPropertyByName("DENS", 7700, 0);
            CWMat.SetPropertyByName("SIGXT", 723825600, 0);
            CWMat.SetPropertyByName("SIGYLD", 620422000, 0);
            CWMat.SetPropertyByName("ALPX", 1.3E-05, 0);
            CWMat.SetPropertyByName("KX", 50, 0);
            CWMat.SetPropertyByName("C", 460, 0);
            errCode = SolidBody.SetSolidBodyMaterial(CWMat);
            if (errCode != 0) ErrorMsg("Failed to apply material");

            // Apply a different SOLIDWORKS Simulation library material to rest of components
            SolidBody = null;
            SolidComponent = null;
            for (j = 1; j <= (CompCount - 1); j++)
            {
                SolidComponent = (CWSolidComponent)SolidMgr.GetComponentAt(j, out errorCode);
                SName = SolidComponent.ComponentName;
                SolidBody = (CWSolidBody)SolidComponent.GetSolidBodyAt(0, out errCode);
                if (errCode != 0) ErrorMsg("No CWSolidBody object");
                returnValue = SolidBody.SetLibraryMaterial("c:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\\english\\sldmaterials\\solidworks materials.sldmat", "2024 Alloy (SN)");
                if (returnValue == 0) ErrorMsg("No material applied");
                SolidBody = null;
            }
        }

        // Error function
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
