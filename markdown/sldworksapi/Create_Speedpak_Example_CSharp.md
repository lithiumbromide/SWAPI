---
title: "Create a SpeedPak Configuration Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Speedpak_Example_CSharp.htm"
---

# Create a SpeedPak Configuration Example (C#)

This example shows how to create a SpeedPak configuration for the active configuration.

```
//----------------------------------------------------------------------------
// Preconditions: Open an assembly.
//
// Postconditions:
// 1. Adds active_configuration (Default_speedpak) is added
//    ConfigurationManager.
// 2. Click the ConfigurationManager tab and expand Default.
//---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;

namespace SpeedpakConfigurationCSharp.csproj
{

    partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            bool boolstatus = false;
            ConfigurationManager swConfigMgr = default(ConfigurationManager);

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swConfigMgr = (ConfigurationManager)swModel.ConfigurationManager;

            // Add a SpeedPak configuration with a part/body
            // selection threshold of 0.5 to the active configuration
            swConfigMgr.AddSpeedPak2(1, 0.5);
            boolstatus = swModel.ForceRebuild3(false);

        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>

        public SldWorks swApp;

    }
}
```
