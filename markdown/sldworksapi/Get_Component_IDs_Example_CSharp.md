---
title: "Get Component IDs Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Component_IDs_Example_CSharp.htm"
---

# Get Component IDs Example (C#)

This example shows how to get the component IDs of the components in an assembly and subassemblies.

```
//--------------------------------------------------------------------------
// Preconditions:
// 1. Open an assembly document containing nested subassemblies.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Traverses the assembly and subassemblies.
// 2. Gets the name and component ID of each component in the assembly and
//    subassemblies.
// 3. Examine the Immediate window.
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
            ConfigurationManager swConfMgr = default(ConfigurationManager);
            Configuration swConf = default(Configuration);
            Component2 swRootComp = default(Component2);

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swConfMgr = (ConfigurationManager)swModel.ConfigurationManager;
            swConf = (Configuration)swConfMgr.ActiveConfiguration;
            swRootComp = (Component2)swConf.GetRootComponent3(true);
            Debug.Print("File = " + swModel.GetPathName());
            if (swModel.GetType() == (int)swDocumentTypes_e.swDocASSEMBLY)
            {
                TraverseComponent(swRootComp, 1);
            }

        }

        public void TraverseComponent(Component2 swComp, int nLevel)
        {
            object[] vChildComp = null;
            Component2 swChildComp = default(Component2);
            string sPadStr = "";
            int i = 0;

            for (i = 0; i <= nLevel - 1; i++)
            {
                sPadStr = sPadStr + "  ";
            }
            vChildComp = (object[])swComp.GetChildren();
            for (i = 0; i <= vChildComp.Length - 1; i++)
            {
                swChildComp = (Component2)vChildComp[i];
                Debug.Print(sPadStr + "Component name: " + swChildComp.Name2 + ", Component ID: " + swChildComp.GetID());
                TraverseComponent(swChildComp, nLevel + 1);
            }
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
