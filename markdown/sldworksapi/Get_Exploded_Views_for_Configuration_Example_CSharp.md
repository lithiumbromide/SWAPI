---
title: "Get Exploded Views for Configuration Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Exploded_Views_for_Configuration_Example_CSharp.htm"
---

# Get Exploded Views for Configuration Example (C#)

This example shows how to get:

- number of exploded views for a configuration.
- name of each exploded view for a configuration.
- name of the configuration for each exploded view.
- name of the exploded view shown in the model.

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\pdmworks\speaker.sldasm.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Gets the name of the active configuration.
// 2. Creates five exploded views for the active configuration.
// 3. Gets the number of exploded views for the active configuration.
// 4. Gets the name of:
//    * each exploded view for the active configuration
//    * configuration for each exploded view
//    and shows each exploded view.
// 5. Gets the name of the exploded view shown in the model.
// 6. Examine the Immediate window.
//
// NOTE: Because the assembly is used elsewhere, do not save changes.
//----------------------------------------------------------------------------
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
            AssemblyDoc swAssembly = default(AssemblyDoc);
            ConfigurationManager swConfigMgr = default(ConfigurationManager);
            Configuration swConfig = default(Configuration);
            string activeConfigName = null;
            string[] viewNames = null;
            string viewName = null;
            int i = 0;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swAssembly = (AssemblyDoc)swModel;

            //Get active configuration name
            swConfigMgr = (ConfigurationManager)swModel.ConfigurationManager;
            swConfig = (Configuration)swConfigMgr.ActiveConfiguration;
            activeConfigName = swConfig.Name;

            Debug.Print("Active configuration name: " + activeConfigName);

            //Create five exploded views in the active configuration
            for (i = 0; i <= 4; i++)
            {
                swAssembly.CreateExplodedView();
            }

            //Get the number of exploded views in the active configuration name
            Debug.Print("  Number of exploded views created: " + swAssembly.GetExplodedViewCount2(activeConfigName));

            //Get the name of each exploded view in the active configuration,
            //get the name of the configuration for each exploded view, and
            //show each exploded view
            viewNames = (string[])swAssembly.GetExplodedViewNames2(activeConfigName);

            for (i = 0; i < viewNames.Length; i++)
            {
                viewName = viewNames[i];
                Debug.Print("    Exploded view name: " + viewName);
                Debug.Print("      Name of configuration for exploded view: " + swAssembly.GetExplodedViewConfigurationName(viewName));
                swAssembly.ShowExploded2(true, viewName);

            }
```

```
            //Get the name of exploded view shown in model
            viewName = "";
            swModelDocExt = swModel.Extension;
            swModelDocExt.IsExploded(out viewName);
            Debug.Print("Name of exploded view shown in model: " + viewName);
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
