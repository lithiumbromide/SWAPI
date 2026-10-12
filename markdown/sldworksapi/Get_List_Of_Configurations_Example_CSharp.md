---
title: "Get List of Configurations Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_List_Of_Configurations_Example_CSharp.htm"
---

# Get List of Configurations Example (C#)

This example shows how to get a list of configuration names for the active document.

```
//------------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified assembly document exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified assembly document.
// 2. Gets the name of the file, name of the active configuration,
//    and the names of all configurations.
// 3. Examine the Immediate window.
//
// NOTE: Because the assembly is used elsewhere, do not save changes.
//-------------------------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace Macro1.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            string[] configNames = null;
            string configName = null;
            Configuration swConfig = default(Configuration);
            int i = 0;
            int errors = 0;
            int warnings = 0;
            string fileName = null;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\smartcomponents\\pillow_block.sldasm";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

            //Get and print active model path and name
            Debug.Print("File = " + swModel.GetPathName());
            Debug.Print("");
            //Get and print name of active configuration
            swConfig = (Configuration)swModel.GetActiveConfiguration();
            Debug.Print("  Name of active configuration = " + swConfig.Name);
            Debug.Print("");

            //Get and print names of all configurations
            configNames = (string[])swModel.GetConfigurationNames();
            for (i = 0; i < configNames.Length; i++)
            {
                configName = (string)configNames[i];
                swConfig = (Configuration)swModel.GetConfigurationByName(configName);
                Debug.Print("  Name of configuration(" + i + ") = " + configName);
                Debug.Print("    Use alternate name in BOM  = " + swConfig.UseAlternateNameInBOM);
                Debug.Print("    Alternate name             = " + swConfig.AlternateName);
                Debug.Print("    Comment                    = " + swConfig.Comment);
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
