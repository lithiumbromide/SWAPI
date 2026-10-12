---
title: "Make Component Independent Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Make_Component_Independent_Example_CSharp.htm"
---

# Make Component Independent Example (C#)

This example shows how to:

- make a selected component independent.
- save the selected component as a new part.
- reference the new part in the assembly.

```
//------------------------------------------------------------------------
// Preconditions:
// 1. Verify that c:\temp exists.
// 2. Copy these files from public_documents\samples\tutorial\driveworksxpress
//    to c:\temp:
//    * leg.sldprt
//    * mobile gantry.sldasm
//    * universal beam.sldpart
//
// Postconditions:
// 1. Opens the assembly.
// 2. Selects the leg<1> component.
// 3. Makes the selected component independent, saves the component as
//    a new part, c:\temp\my leg.sldprt, and references the new part in
//    the assembly.
// 4. Examine the FeatureManager design tree and c:\temp.
//------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            AssemblyDoc swAssembly = default(AssemblyDoc);
            string fileName = null;
            bool status = false;
            int errors = 0;
            int warnings = 0;

            fileName = "c:\\temp\\mobile gantry.sldasm";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swAssembly = (AssemblyDoc)swModel;

            //Select leg<1>
            status = swModelDocExt.SelectByID2("leg-1@mobile gantry", "COMPONENT", 0, 0, 0, false, 0, null, 0);

            //Make leg<1> independent, save it as a new part,
            //and reference the new part in the assembly
            status = swAssembly.MakeIndependent("c:\\temp\\my leg.sldprt");

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
