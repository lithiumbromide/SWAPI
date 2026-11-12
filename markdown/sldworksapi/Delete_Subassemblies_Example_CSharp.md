---
title: "Delete Subassemblies Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Delete_Subassemblies_Example_CSharp.htm"
---

# Delete Subassemblies Example (C#)

This example shows how to delete the subassembly in which the selected subassembly is a component.

```
//------------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified assembly exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the assembly.
// 2. Selects and deletes the [Assem4^Assem3_assemSubAssems]<1>
//    subassembly and the subassembly in which it is a component.
// 3. Examine the FeatureManager design tree and Immediate
//    window.
//
// NOTE: Because the assembly is used elsewhere, do not save
// changes.
//------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace Macro1.CSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            AssemblyDoc swAssembly = default(AssemblyDoc);
            bool status = false;
            int errors = 0;
            int warnings = 0;
            string fileName = null;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\assemSubAssems.sldasm";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swAssembly = (AssemblyDoc)swModel;
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("Assem3^assemSubAssems-1@assemSubAssems/Assem4^Assem3_assemSubAssems-1@Assem3^assemSubAssems", "COMPONENT", 0, 0, 0, false, 0, null, 0);
            status = swAssembly.DeleteSelections((int)swAssemblyDeleteOptions_e.swDelete_SubAssembly);
            Debug.Print("Selected subassembly and the subassembly in which it is a component deleted? " + status);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
