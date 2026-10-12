---
title: "Apply Material to Selected Entities Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Apply_Material_to_Selected_Entities_Example_CSharp.htm"
---

# Apply Material to Selected Entities Example (C#)

This example shows how to apply SOLIDWORKS-defined materials to selected entities.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
 // 3. Verify that Solidworks materials.sldmat exists.
 // 4. Open public_documents\samples\Simulation Examples\actuator.sldasm.
 // 5. Click the Ready study tab.
  // 6. In the Simulation Study tree, expand the Parts folder and multi-select
 //    actuator_casing-1 and actuator_piston-1.
 //
 // Postconditions:
 // 1. Applies 2024 Alloy (SN) material to the selected components.
  // 2. Inspect the Simulation Study tree to verify step 1.
 //
  // NOTE: Because the assembly is used elsewhere, do not save changes.
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
 namespace ApplyMaterialSelectedEntities_CSharp.csproj
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
             int returnValue = 0;

             // Get SOLIDWORKS Simulation object
             COSMOSObject = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
             if (COSMOSObject == null)
                 ErrorMsg(swApp, "COSMOSObject object not found");

             COSMOSWORKS = COSMOSObject.CosmosWorks;
             if (COSMOSWORKS == null)
                 ErrorMsg(swApp, "COSMOSWORKS object not found");

             ActDoc = COSMOSWORKS.ActiveDoc;
             if (ActDoc == null)
                 ErrorMsg(swApp, "No active document");

             // Get the Ready study
             StudyMngr = ActDoc.StudyManager;
             if (StudyMngr == null)
                 ErrorMsg(swApp, "CWStudyManager object not found");
             Study = StudyMngr.GetStudy(0);
             if (Study == null)
                 ErrorMsg(swApp, "Study not found");

             SolidMgr = Study.SolidManager;
             if (SolidMgr == null)
                 ErrorMsg(swApp, "CWSolidManager object not created");

             // Apply a SOLIDWORKS material to selected components
             returnValue = SolidMgr.SetLibraryMaterialToSelectedEntities("solidworks materials.sldmat", "2024 Alloy (SN)");
             if (returnValue == 1)
                 ErrorMsg(swApp, "No material applied");

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
