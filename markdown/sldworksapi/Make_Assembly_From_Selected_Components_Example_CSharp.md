---
title: "Make Assembly from Selected Components Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Make_Assembly_From_Selected_Components_Example_CSharp.htm"
---

# Make Assembly from Selected Components Example (C#)

This example shows how to create a new assembly using the selected components of the active assembly.

//---------------------------------------------------------------------
// Preconditions:
// 1. Open `public_documents`**\samples\tutorial\motionstudies\valve_cam2.sldasm**
// 2. Ensure that the **Save new components to external files** check box
// on the **Tools > Options > Assemblies** dialog is selected.
// Otherwise, the selected components are saved as virtual components
// and not as external files.
// 3. Select **valve<1>** and **valve_guide<1>** components.
//
// Postconditions:
// 1. Creates `public_documents`**\samples\tutorial\motionstudies\MyTestValveAssembly.sldasm**,
// which is made up of the **valve<1>** and **valve_guide<1>** components.
// 2. Replaces the **valve<1>** and **valve_guide<1>** components with
// **MyTestValveAssembly** subassembly.
// 3. Examine the FeatureManager design tree and
// `public_documents`**\samples\tutorial\motionstudies**.
// 4. Clear the S**ave new components to external files** check box
// on the **Tools > Options > Assemblies** dialog if you selected
// it for this example.
//
// NOTE: Because the assembly is used elsewhere, do not save changes.
//-----------------------------------------------------------------------

```vb
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
namespace MakeAssemblyFromSelectedComponents_CSharp.csproj
{
    partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            AssemblyDoc swAssy = default(AssemblyDoc);
            string tmpPath = null;
            swModel = (ModelDoc2)swApp.ActiveDoc;
            string strCompModelname = null;
            strCompModelname = "MyTestValveAssembly.sldasm";
            // Save the new assembly in the same folder as the original assembly
            tmpPath = swModel.GetPathName();
            tmpPath = tmpPath.Substring(0, tmpPath.Length - 17);
            Debug.Print( tmpPath);
            swAssy = (AssemblyDoc)swModel;
            // Create a new assembly using the selected components
            swAssy.MakeAssemblyFromSelectedComponents(tmpPath + strCompModelname);
        }
        public SldWorks swApp;
    }
}
```
