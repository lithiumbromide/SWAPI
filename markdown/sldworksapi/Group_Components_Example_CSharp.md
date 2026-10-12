---
title: "Group and Ungroup Components Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Group_Components_Example_CSharp.htm"
---

# Group and Ungroup Components Example (C#)

This example shows how to:

- group the same components in the same configuration in an assembly into a folder in the FeatureManager design tree.
- ungroup the grouped components.

```
//---------------------------------------------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\advdrawings\98food processor.sldasm.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Groups the rubber feet components into rubber feet(Default)(5).
// 2. Examine the Immediate window and FeatureManager design tree.
// 3. Press F5.
// 4. Ungroups rubber feet(Default)(5).
// 5. Examine the Immediate window and FeatureManager design tree.
//
// NOTE: Because the assembly is used elsewhere, do not save changes.
//---------------------------------------------------------------------------------
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
            FeatureManager swFeatureManager = default(FeatureManager);
 	    ModelDocExtension swModelDocExt = default(ModelDocExtension);
	    AssemblyDoc swAssemblyDoc = default(AssemblyDoc);
	    bool status = false;

            swModel = (ModelDoc2)swApp.ActiveDoc;
```

```
    	    //Group rubber feet components into rubber feet(Default)(5)
            swFeatureManager = (FeatureManager)swModel.FeatureManager;
            swFeatureManager.GroupComponentInstances = true;
            Debug.Print("Component instances grouped? " + swFeatureManager.GroupComponentInstances);
```

```
	    System.Diagnostics.Debugger.Break();
	    //Press F5

	    //Ungroup rubber feet(Default)(5)
	    swModelDocExt = (ModelDocExtension)swModel.Extension;
	    status = swModelDocExt.SelectByID2("rubber feet(Default)(5)", "FTRFOLDER", 0, 0, 0, false, 0, null, 0);
	    swAssemblyDoc = (AssemblyDoc)swModel;
	    status = swAssemblyDoc.UngroupComponents();
	    Debug.Print("Grouped components ungrouped? " + status);
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
