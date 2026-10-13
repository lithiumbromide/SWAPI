---
title: "Get Display State Names and Visibilities of Components Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Display_State_Names_and_Visibilites_of_Components_Example_CSharp.htm"
---

# Get Display State Names and Visibilities of Components Example (C#)

This example shows how to get the names of the display states in an assembly and the visibilities of the assembly components in each display state.

```
//------------------------------------------------------------------------------
// Preconditions:
// 1. Open an assembly that contains multiple components
//    and display states.
// 2. Open the Immediate window.
//
// Postconditions: Examine the Immediate window.
//-----------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace DisplayStateComponentsCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            ConfigurationManager swConfigMgr = default(ConfigurationManager);
            Configuration swConfig = default(Configuration);
            object oComponents = null;
            object[] components = null;
            Component2 comp = null;
            int docType = 0;
            int i = 0;
            int j = 0;
            string[] displayStateNames = null;
            string displayStateName = null;
            int[] displayStateVisibilities = null;
            int displayStateVisibility = 0;
            string visibility = "";

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            docType = swModel.GetType();
            if (docType == (int)swDocumentTypes_e.swDocASSEMBLY)
            {
                swConfigMgr = (ConfigurationManager)swModel.ConfigurationManager;
                swConfig = (Configuration)swConfigMgr.ActiveConfiguration;
                displayStateNames = (string[])swConfig.GetDisplayStates();
                for (i = 0; i < displayStateNames.Length; i++)
                {
                    displayStateName = (string)displayStateNames[i];
                    Debug.Print("Display state name: " + displayStateName);
                    displayStateVisibilities = (int[])swConfig.GetDisplayStateComponentVisibility(displayStateName, false, false, out oComponents);
                    components = (object[])oComponents;
                    Debug.Print("  Display state visibility: ");
                    for (j = 0; j < displayStateVisibilities.Length; j++)
                    {
                        displayStateVisibility = (int)displayStateVisibilities[j];
                        switch (displayStateVisibility)
                        {
                            case 0:
                                visibility = "Hidden";
                                break;
                            case 1:
                                visibility = "Shown";
                                break;
                        }
                        comp = (Component2)components[j];
                        Debug.Print("    " + comp.Name2 + ": " + visibility);
                    }
                }
            }
            else
            {
                Debug.Print("Open an assembly document with multiple display states.");
                return;
            }

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
