---
title: "Rebuild All Configurations Without Activating Each Configuration Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Rebuild_All_Configurations_Without_Activating_Each_Configuration_Example_CSharp.htm"
---

# Rebuild All Configurations Without Activating Each Configuration Example (C#)

This example shows how to rebuild only those features that need to be rebuilt in all configurations without activating each configuration.

```
//-------------------------------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\pdmworks\speaker.sldasm.
// 2. Right-click membrane<1> and click Suppress in the active
//    configuration, Dual Speaker.
// 3. Click Don't Save.
// 4. Click the ConfigurationManager tab and right-click Single
//    Speaker Glueable and click Show Configuration to make this
//    configuration the active configuration.
// 5. Open the Immediate window.
//
// Postconditions:
// 1. Gets whether each configuration needs to be rebuilt.
// 2. Rebuilds only those features that need to be rebuilt in all
//    configurations without activating each configuration.
// 3. Gets whether each configuration needs to be rebuilt.
// 4. Examine the Immediate window.
//
// NOTE: Because the assembly is used elsewhere, do not save changes.
//-------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {

        ModelDoc2 swModel;
        ModelDocExtension swModelDocExt;
        Configuration swConfiguration;
        string[] vConfNameArr;
        string vConfName;

        public void Main()

        {
            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            //Get whether each configuration needs to be rebuilt
            Debug.Print("Traverse assembly without activating other configurations...");
            TraverseConfigurations(swModel);

            //Rebuild only those features that need to be rebuilt in all configurations
            //without activating each configuration
            swModelDocExt.EditRebuildAll();

            //Get whether each configuration needs to be rebuilt
            Debug.Print("Traverse assembly without activating other configurations...");
            TraverseConfigurations(swModel);

        }

        public void TraverseConfigurations(ModelDoc2 swModel)
        {
            vConfNameArr = (string[])swModel.GetConfigurationNames();
            foreach (string config in vConfNameArr)
            {
                vConfName = (string)config;
                swConfiguration = (Configuration)swModel.GetConfigurationByName(vConfName);
                Debug.Print("  Name of the configuration: " + swConfiguration.Name);
                Debug.Print("    Does the configuration need to be rebuilt? " + swConfiguration.NeedsRebuild);
            }
            Debug.Print("");

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
