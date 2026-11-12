---
title: "Get Top-level Components Using Component IDs Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Top-level_Component_Using_Component_IDs_Example_CSharp.htm"
---

# Get Top-level Components Using Component IDs Example (C#)

This example shows how to get the top-level components in an assembly using their component IDs.

```
//--------------------------------------------------------------------------
// Preconditions:
// 1. Open an assembly document containing subassemblies.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Traverses the assembly.
// 2. Gets the name and component ID of each top-level component
//    in the assembly.
// 3. Adds each component ID to an array and traverses the array.
//    a. Gets each top-level component using its component ID.
//    b. Gets the name and component ID of each top-level component
//       in the assembly.
// 4. Examine the Immediate window and FeatureManager design tree.
//---------------------------------------------------------------------------
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
            AssemblyDoc swAssemblyDoc = default(AssemblyDoc);
            ConfigurationManager swConfMgr = default(ConfigurationManager);
            Configuration swConf = default(Configuration);
            Component2 swRootComp = default(Component2);
            object[] vChildComp = null;
            Component2 swChildComp = default(Component2);
            int i = 0;
            int compID = 0;
            int[] compIDs = null;
            int nbrComp = 0;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swAssemblyDoc = (AssemblyDoc)swModel;
            swConfMgr = (ConfigurationManager)swModel.ConfigurationManager;
            swConf = (Configuration)swConfMgr.ActiveConfiguration;
            swRootComp = (Component2)swConf.GetRootComponent3(true);

            Debug.Print("Get top-level components by traversing assembly:");
            vChildComp = (object[])swRootComp.GetChildren();
            nbrComp = vChildComp.Length;
            compIDs = new int[nbrComp + 1];
            for (i = 0; i < nbrComp; i++)
            {
                swChildComp = (Component2)vChildComp[i];
                compID = swChildComp.GetID();
                Debug.Print("  Component name: " + swChildComp.Name2 + ", Component ID: " + compID);
                // Add component ID to an array
                compIDs[i] = compID;
            }

            Debug.Print("");

            Debug.Print("Get top-level components using component IDs:");
            swChildComp = null;
            for (i = 0; i < compIDs.Length - 1; i++)
            {
                compID = compIDs[i];
                swChildComp = (Component2)swAssemblyDoc.GetComponentByID(compID);
                Debug.Print("  Component name: " + swChildComp.Name2 + ", Component ID: " + swChildComp.GetID());
            }

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
