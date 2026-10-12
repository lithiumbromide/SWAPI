---
title: "Get Whether Components Are Loaded Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Whether_Components_Are_Loaded_Example_CSharp.htm"
---

# Get Whether Components Are Loaded Example (C#)

This example gets whether the components in an assembly document are loaded.

```vb
//---------------------------------------
 // Preconditions:
 // 1. Verify that the specified assembly document exists.
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. Loads the Magnet-1 component.
 // 2. Examine the Immediate window.
 //
 // NOTE: Because this assembly document is used elsewhere,
 // do not save changes.
 //---------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;

namespace IsLoadedComponent2CSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
        ModelDoc2 swModel;
        DocumentSpecification swDocSpecification;
        string[] sComponents = new string[1];
        object[] Components;
        Component2 swComponent = default(Component2);
        string sName;
        AssemblyDoc swAssembly;
        int longstatus;
        int longwarnings;
        int i;
        ConfigurationManager swConfigMgr;
        Configuration swConfig;

        // Selectively open speaker.sldasm
        // Load only Magnet-1
        swDocSpecification = (DocumentSpecification)swApp.GetOpenDocSpec("C:\\Users\\Public\\Documents\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\pdmworks\\speaker.sldasm");
        sComponents[0] = "Magnet-1@speaker";
        Components = (object[])sComponents;
        swDocSpecification.ComponentList = Components;
        swDocSpecification.Selective = true;
        sName = swDocSpecification.FileName;
        swDocSpecification.DocumentType = (int)swDocumentTypes_e.swDocASSEMBLY;
        swDocSpecification.DisplayState = "Default_Display State-1";
        swDocSpecification.UseLightWeightDefault = true;
        swDocSpecification.LightWeight = true;
        swDocSpecification.Silent = true;
        swDocSpecification.IgnoreHiddenComponents = true;
        swModel = (ModelDoc2)swApp.OpenDoc7(swDocSpecification);
        longstatus = swDocSpecification.Error;
        longwarnings = swDocSpecification.Warning;

        // Get whether the components in the
        // assembly document are loaded and suppressed; only
        // Magnet-1 should be loaded and not suppressed
        swAssembly = (AssemblyDoc)swModel;
        swConfigMgr = (ConfigurationManager)swModel.ConfigurationManager;
        swConfig = (Configuration)swConfigMgr.ActiveConfiguration;
        Components = (object[])swAssembly.GetComponents(true);
        for (i = 0; i < Components.Length; i++)
        {
            swComponent = (Component2)Components[i];
            if ((swComponent.IsLoaded()))
            {
                Debug.Print("Component: " + swComponent.Name + " is loaded.");
            }
            else
            {
                Debug.Print("Component: " + swComponent.Name + " is not loaded.");
            }

            Debug.Print ("  Suppressed: " + swConfig.GetComponentSuppressionState(swComponent.Name));
            Debug.Print ("");
        }
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
