---
title: "Import STEP File Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Import_STEP_File_Example_CSharp.htm"
---

# Import STEP File Example (C#)

This example shows how to import and repair a STEP file.

```
//-------------------------------------------------------------------------------
// Preconditions: Verify that the specified SOLIDWORKS Design part document to open exists.
//
// Postconditions:
// 1. Opens the specified SOLIDWORKS Design part document.
// 2. Saves the part document as a STEP file.
// 3. Closes the part document.
// 4. Imports the STEP file created in step 2.
// 5. Runs import diagnostics on the STEP file and repairs any bad faces.
// 6. Creates Imported1 in the FeatureManager design tree.
//-------------------------------------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;

namespace ImportStepDataCSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
            PartDoc swPart = default(PartDoc);
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            ImportStepData swImportStepData = default(ImportStepData);
            bool status = false;
            int errors = 0;
            int warnings = 0;
            string fileName = null;
            string stepFileName = null;

            //Open the part document to export to a STEP file
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2019\\samples\\tutorial\\api\\db9 male.sldprt";
            swPart = (PartDoc)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModel = (ModelDoc2)swPart;
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            //Export the part document to a STEP file
            stepFileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2019\\samples\\tutorial\\api\\db9 male.STEP";
            status = swModelDocExt.SaveAs(stepFileName, 0, (int)swSaveAsOptions_e.swSaveAsOptions_Silent, null, ref errors, ref warnings);
            swPart = null;

            swApp.CloseDoc("db9 male.sldprt");

            //Get import information
            swImportStepData = (ImportStepData)swApp.GetImportFileData(stepFileName);

            //If ImportStepData::MapConfigurationData is not set, then default to
            //the environment setting swImportStepConfigData; otherwise, override
            //swImportStepConfigData with ImportStepData::MapConfigurationData
            swImportStepData.MapConfigurationData = true;

            //Import the STEP file
            swPart = (PartDoc)swApp.LoadFile4(stepFileName, "r", swImportStepData, ref errors);
            swModel = (ModelDoc2)swPart;
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            //Run diagnostics on the STEP file and repair any bad faces
            errors = swPart.ImportDiagnosis(true, false, true, 0);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
