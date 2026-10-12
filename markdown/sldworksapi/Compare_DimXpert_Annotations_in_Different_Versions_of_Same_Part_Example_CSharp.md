---
title: "Compare DimXpert Annotations in Different Versions of Same Part Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Compare_DimXpert_Annotations_in_Different_Versions_of_Same_Part_Example_CSharp.htm"
---

# Compare DimXpert Annotations in Different Versions of Same Part Example (C#)

This example shows how to compare the DimXpert annotations in different versions of the same part.

```
//-------------------------------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\api\block.sldprt.
//    a. Click DimXpertManager > Auto Dimension Scheme > OK.
//    b. Save the part as block1.sldprt.
//    c. Right-click TXD2@Scheme2, change 0.25mm to 0.5mm, and click OK.
//    d. Save the part as block2.sldprt.
//    e. Open block1.sldprt.
// 2. Verify that c:\temp exists.
// 3. Open the Immediate window.
//
// Postconditions:
// 1. Compares the DimXpert annotations in the parts and creates
//    the report and bitmap image files.
// 2. Examine the Immediate window.
// 3. Open and examine the files in c:\temp\CompareBlocks.
//----------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            bool status = false;
            string referenceDocument = null;
            string modifiedDocument = null;
            string reportName = null;
            string reportFolderPath = null;
            int reportSaveOptions = 0;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            referenceDocument = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\block1.sldprt";
            modifiedDocument = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\block2.sldprt";
            reportName = "CompareBlocks";
            reportFolderPath = "c:\\temp";
            reportSaveOptions = (int)sw3DPMISaveOptions_e.swDimXpertData + (int)sw3DPMISaveOptions_e.swReferenceData;
            status = swModelDocExt.Compare3DPMI(referenceDocument, modifiedDocument, reportName, reportFolderPath, reportSaveOptions);
            Debug.Print("Method executed: " + status);
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
