---
title: "Set Transparency of Unmodified Components in Large Design Review Assembly Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Transparency_of_Components_LDR_Mode_Example_CSharp.htm"
---

# Set Transparency of Unmodified Components in Large Design Review Assembly Example (C#)

This example shows how to:

- open an assembly in Large Design Review mode
- open, modify, save, and close an assembly component, and
- set the transparency level of unmodified components in the assembly.

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Create c:\temp\LDR.
// 2. Copy these files from public_documents\samples\tutorial\api to c:\temp\LDR:
//    * landing_gear.sldasm
//    * lwrsway_lnk.sldprt
//    * oleopiston.sldprt
//    * oleostrut.sldprt
//    * part4.sldprt
//    * upprsway_lnk.sldprt
//    * wheel_hub.sldprt
//    * wheelassy.sldasm
// 3. Open the Immediate window.
//
// Postconditions:
// 1. Click OK in the Large Design Review dialog.
// 2. Opens the assembly in Large Design Review mode.
// 3. Opens, modifies, saves, and closes the assembly component, oleostrut.sldprt.
//    a. When prompted to rebuild, click Rebuild and save the document.
//    b. If prompted to update the graphics data in Large Design Review,
//       click Yes.
// 4. Sets the transparency level of unmodified components in the assembly to 0.75.
// 5. Close the assembly and part documents.
// 6. Examine the Immediate window and graphics area.
//---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace LargeDesignReviewCSharp.csproj
{

    partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            AssemblyDoc swAssemblyDoc = default(AssemblyDoc);
            Dimension swDimension = default(Dimension);
            string fileName = null;
            bool status = false;
            int errors = 0;
            int warnings = 0;

            // Open an assembly in Large Design Review mode
            fileName = "C:\\temp\\LDR\\landing_gear.sldasm";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_ViewOnly, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swAssemblyDoc = (AssemblyDoc)swApp.ActiveDoc;

            // Open a component, modify it, and save it
            ModelDoc2 swCompModel = default(ModelDoc2);
            status = swModelDocExt.SelectByID2("oleostrut-1@landing_gear", "COMPONENT", 0, 0, 0, false, 0, null, 0);
            swApp.OpenDoc6("C:\\temp\LDR\\oleostrut.sldprt", 1, 0, "", ref errors, ref warnings);
            swApp.ActivateDoc3("oleostrut.sldprt", false, (int)swRebuildOnActivation_e.swUserDecision, ref errors);
            swCompModel = (ModelDoc2)swApp.ActiveDoc;
            swCompModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("Sketch9", "SKETCH", 0, 0, 0, false, 0, null, 0);
            swCompModel.EditSketch();
            swCompModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("D3@Sketch9@oleostrut.SLDPRT", "DIMENSION", 0.0792805491990847, -0.020779176201373, 0, false, 0, null, 0);
            swDimension = (Dimension)swCompModel.Parameter("D3@Sketch9");
            swDimension.SystemValue = 0.025;
            swCompModel.ClearSelection2(true);
            status = swCompModel.Save3((int)swSaveAsOptions_e.swSaveAsOptions_SaveReferenced, ref errors, ref warnings);
            swApp.CloseDoc("oleostrut.sldprt");

            // Set the transparency level of unmodified components in the assembly
            swAssemblyDoc.LargeDesignReviewTransparencyLevelDynamic = true;
            swAssemblyDoc.LargeDesignReviewTransparencyLevelEnabled = true;
            swAssemblyDoc.LargeDesignReviewTransparencyLevel = 0.75;
            Debug.Print("Transparency level: " + swAssemblyDoc.LargeDesignReviewTransparencyLevel);
            Debug.Print("  Enabled = " + swAssemblyDoc.LargeDesignReviewTransparencyLevelEnabled);
            Debug.Print("  Dynamic = " + swAssemblyDoc.LargeDesignReviewTransparencyLevelDynamic);

        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>

        public SldWorks swApp;

    }
}
```
