---
title: "Create Nonlinear Study and Apply Materials Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Nonlinear_Study_and_Apply_Materials_Example_CSharp.htm"
---

# Create Nonlinear Study and Apply Materials Example (C#)

This example shows how to create a nonlinear study and apply user-defined and SOLIDWORKS materials to assembly components.

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
// 2. Creates a  nonlinear study.
// 3. Applies user-defined material to the first assembly component
//    and SOLIDWORKS material to the remaining components.
// 4. To verify, expand the Parts folder in the Simulation Study tree,
//    which is located beneath the FeatureManager design tree, and
//    observe the names of the materials applied to holder-1 and pipe-1.
//
// NOTE: Because the assembly document is used elsewhere, do not save changes.
//----------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using SolidWorks.Interop.cosworks;
using System;
using System.Diagnostics;
using System.Windows.Forms;
 namespace CreateNonlinearStudyApplyMaterials
 {
     partial class SolidWorksMacro
     {
         public void Main()
         {
             dynamic COSMOSWORKS = default(dynamic);
             dynamic COSMOSObject = default(dynamic);
             CWModelDoc ActDoc = default(CWModelDoc);
             CWStudyManager StudyMngr = default(CWStudyManager);
             CWStudy Study = default(CWStudy);
             CWSolidManager SolidMgr = default(CWSolidManager);
             CWSolidComponent SolidComponent = default(CWSolidComponent);
             CWSolidBody SolidBody = default(CWSolidBody);
             string SName = null;
             int errors = 0;
             int warnings = 0;
             int errorCode = 0;
             int errCode = 0;
             int CompCount = 0;
             int j = 0;
             CWMaterial CWMat = null;
             int iApp = 0;
             bool bApp = false;

             // Determine host SOLIDWORKS version
             int swVersion = Convert.ToInt32(swApp.RevisionNumber().Substring(0, 2));
             // Calculate the correct Simulation ProgID for this version of SOLIDWORKS
             int cwVersion = swVersion - 15;
             String cwProgID = String.Format("SldWorks.Simulation.{0}", cwVersion);
             Debug.Print(cwProgID);

             // Get the SOLIDWORKS Simulation object
             COSMOSObject = swApp.GetAddInObject(cwProgID);
             if (COSMOSObject == null) ErrorMsg(swApp, "COSMOSObject object not found", true);
             COSMOSWORKS = COSMOSObject.CosmosWorks;
             if (COSMOSWORKS == null) ErrorMsg(swApp, "COSMOSWORKS object not found", true);

             // Open and get the active document
             swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2019\\samples\\Simulation Examples\\Nonlinear\\nl_pipe_holder.sldasm", (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
             ActDoc = (CWModelDoc)COSMOSWORKS.ActiveDoc;
             if (ActDoc == null) ErrorMsg(swApp, "No active document", true);

             // Create new nonlinear study
             StudyMngr = (CWStudyManager)ActDoc.StudyManager;
             if (StudyMngr == null) ErrorMsg(swApp, "CWStudyManager object not created", true);
             Study = (CWStudy)StudyMngr.CreateNewStudy("Nonlinear", (int)swsAnalysisStudyType_e.swsAnalysisStudyTypeNonlinear, (int)swsMeshType_e.swsMeshTypeSolid, out errCode);
             if (Study == null) ErrorMsg(swApp, "Study not created", true);

             // Get number of solid components
             SolidMgr = (CWSolidManager)Study.SolidManager;
             if (SolidMgr == null) ErrorMsg(swApp, "CWSolidManager object not created", true);
             CompCount = SolidMgr.ComponentCount;
             SolidComponent = SolidMgr.GetComponentAt(0, out errorCode);
             if (SolidComponent == null) ErrorMsg(swApp, "CWSolidComponent object not created", true);

             // Get name of solid component
             SName = SolidComponent.ComponentName;

             // Apply user-defined material to the first component in the tree
             SolidBody = (CWSolidBody)SolidComponent.GetSolidBodyAt(0, out errCode);
             if (errCode != 0) ErrorMsg(swApp, "No solid body", true);
             if (SolidBody == null) ErrorMsg(swApp, "CWSolidBody object not created", true);
             CWMat = (CWMaterial)SolidBody.GetDefaultMaterial();
             CWMat.MaterialUnits = 0;
             if (CWMat == null) ErrorMsg(swApp, "No default material object", true);
             CWMat.MaterialName = "Alloy Steel";
             CWMat.SetPropertyByName("EX", 210000000000.0, 0);
             CWMat.SetPropertyByName("NUXY", 0.28, 0);
             CWMat.SetPropertyByName("GXY", 79000000000.0, 0);
             CWMat.SetPropertyByName("DENS", 7700, 0);
             CWMat.SetPropertyByName("SIGXT", 723825600, 0);
             CWMat.SetPropertyByName("SIGYLD", 620422000, 0);
             CWMat.SetPropertyByName("ALPX", 1.3E-05, 0);
             CWMat.SetPropertyByName("KX", 50, 0);
             CWMat.SetPropertyByName("C", 460, 0);
             errCode = SolidBody.SetSolidBodyMaterial(CWMat);
             if (errCode != 0) ErrorMsg(swApp, "Failed to apply material", true);

             //Apply SOLIDWORKS library material to rest of components
             SolidBody = null;
             SolidComponent = null;
             for (j = 1; j <= (CompCount - 1); j++)
             {
                 SolidComponent = (CWSolidComponent)SolidMgr.GetComponentAt(j, out errorCode);
                 SName = SolidComponent.ComponentName;
                 SolidBody = (CWSolidBody)SolidComponent.GetSolidBodyAt(0, out errCode);
                 if (errCode != 0) ErrorMsg(swApp, "No solid body", true);
                 bApp = SolidBody.SetLibraryMaterial2("C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\\english\\sldmaterials\\solidworks materials.sldmat", "Gray Cast Iron (SN)");
                 if (bApp == false) ErrorMsg(swApp, "No material applied", true);
                 SolidBody = null;
             }
         }

         public void ErrorMsg(SldWorks SwApp, string Message, bool EndTest)
         {
             MessageBox.Show(Message);
             MessageBox.Show("'*** WARNING - General");
             MessageBox.Show("'*** " + Message);
             MessageBox.Show("");
             if (EndTest)
             {
             }
         }
         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>
         public SldWorks swApp;
     }
 }
```
