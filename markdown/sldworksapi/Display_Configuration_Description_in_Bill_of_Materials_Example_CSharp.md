---
title: "Display Configuration Description in Bill of Materials Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Display_Configuration_Description_in_Bill_of_Materials_Example_CSharp.htm"
---

# Display Configuration Description in Bill of Materials Example (C#)

This example shows how to traverse an assembly and display the description of each configuration in the bill of materials.

```
//--------------------------------------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\smartcomponents\pillow_block.sldasm.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Traverses the configurations.
// 2. Gets the name of each configuration and its description.
// 3. Sets and gets whether to display the description of each configuration
//    in the bill of materials.
// 4. Examine the Immediate window.
//
// NOTE: Because the assembly is used elsewhere, do not save changes.
//--------------------------------------------------------------------------
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
            string[] vConfigNameArr = null;
            Configuration swConfig = default(Configuration);
            Configuration swParentConfig = default(Configuration);
            ConfigurationManager swConfMgr = default(ConfigurationManager);
            object[] vChildConfigArr = null;
            Configuration swChildConfig = default(Configuration);

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swConfMgr = (ConfigurationManager)swModel.ConfigurationManager;
            Debug.Print("File = " + swModel.GetPathName());
            Debug.Print("");
            // Traverse configurations; always at least one configuration exists
            vConfigNameArr = (string[])swModel.GetConfigurationNames();
            foreach (string vConfigName in vConfigNameArr)
            {
                swConfig = (Configuration)swModel.GetConfigurationByName(vConfigName);
                Debug.Print("  Configuration name = " + swConfig.Name);
                Debug.Print("    Description = " + swConfig.Description);
                swConfig.UseDescriptionInBOM = true;
                Debug.Print("    Display description in bill of materials? " + swConfig.UseDescriptionInBOM);
                // Process parent
                swParentConfig = (Configuration)swConfig.GetParent();
                if ((swParentConfig != null))
                {
                    Debug.Print("      Parent = " + swParentConfig.Name);
                }
                // Process children
                vChildConfigArr = (object[])swConfig.GetChildren();
                if ((vChildConfigArr != null))
                {
                    foreach (object vChildConfig in vChildConfigArr)
                    {
                        swChildConfig = (Configuration)vChildConfig;
                        Debug.Print("      Child = " + swChildConfig.Name);
                    }
                }
                Debug.Print("");
            }

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
