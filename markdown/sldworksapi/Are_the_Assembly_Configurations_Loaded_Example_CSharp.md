---
title: "Are the Assembly Configurations Loaded Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Are_the_Assembly_Configurations_Loaded_Example_CSharp.htm"
---

# Are the Assembly Configurations Loaded Example (C#)

This example shows how to find out if the configurations in an assembly are loaded, whether the configurations need to be updated and rebuilt, and the configuration types.

```
//-----------------------------------------------------------------------
// Preconditions:
// 1. Verify that the assembly document to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Loads all configurations.
// 2. Examine the Immediate window to see the states of the
//    configurations.
//
// NOTE: Because the specified assembly document is used elsewhere,
// do not save the document when you close it.
// ---------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
namespace IsLoadedConfigurationCSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {

            ModelDoc2 swModel = default(ModelDoc2);
            Configuration swConfiguration = default(Configuration);
            ConfigurationManager swConfigurationMgr = default(ConfigurationManager);
            object[] ConfNameArr = null;
            string ConfName = null;
            const string DocFilename = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\pdmworks\\speaker.sldasm";
            bool boolstatus = false;
            int Errors = 0;
            int Warnings = 0;
            int i;

            swModel = (ModelDoc2)swApp.OpenDoc6(DocFilename, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref Errors, ref Warnings);
            if (swModel == null)
            {
                return;
            }
            else
            {
                Debug.Print("File = " + swModel.GetPathName());
                Debug.Print("");
            }

            swConfigurationMgr = (ConfigurationManager)swModel.ConfigurationManager;
            swConfiguration = (Configuration)swConfigurationMgr.ActiveConfiguration;
            ConfNameArr = (object[])swModel.GetConfigurationNames();
            Debug.Print("Traverse assembly without activating other configurations...");
            for (i = 0; i < ConfNameArr.Length; i++)
            {
                ConfName = (string)ConfNameArr[i];
                swConfiguration = (Configuration)swModel.GetConfigurationByName(ConfName);
                Debug.Print(" Name of the configuration: " + swConfiguration.Name);
                Debug.Print("     Is the configuration loaded? " + swConfiguration.IsLoaded());
                Debug.Print("     Does the configuration need to be updated? " + swConfiguration.IsDirty());
                Debug.Print("     Does the configuration need to be rebuilt? " + swConfiguration.NeedsRebuild);
                Debug.Print("     What is the configuration type? ? " + swConfiguration.Type);
            }

            Debug.Print("");

            // Traverse the assembly again, but this time activate all
            // configurations, which loads them
            Debug.Print("Traverse assembly and activate all configurations...");
            for (i = 0; i < ConfNameArr.Length; i++)
            {
                ConfName = (string)ConfNameArr[i];
                swConfiguration = (Configuration)swModel.GetConfigurationByName(ConfName);
                boolstatus = swModel.ShowConfiguration2(ConfName);
                swConfiguration = (Configuration)swConfigurationMgr.ActiveConfiguration;
                Debug.Print(" Name of the configuration: " + swConfiguration.Name);
                Debug.Print("     Is the configuration loaded? " + swConfiguration.IsLoaded());
                Debug.Print("     Does the configuration need to be updated? " + swConfiguration.IsDirty());
                Debug.Print("     Does the configuration need to be rebuilt? " + swConfiguration.NeedsRebuild);
                Debug.Print("     What is the configuration type? ? " + swConfiguration.Type);
            }
        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
