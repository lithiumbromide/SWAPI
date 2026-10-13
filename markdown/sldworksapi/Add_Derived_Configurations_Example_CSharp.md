---
title: "Add Derived Configurations Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Derived_Configurations_Example_CSharp.htm"
---

# Add Derived Configurations Example (C#)

This example shows how to add a derived configuration for each existing configuration.

```vb
 //---------------------------------------------------------------------------
 // Preconditions: Open a part or assembly.
 //
 // Postconditions: For each configuration, adds and selects a derived
 // configuration.
 //
 // NOTE: IConfigurationManager::AddConfiguration returns
 // Nohting or null if the new configuration already exists.
 //---------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 namespace SelectConfiguration_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             string[] vConfigNameArr = null;

             Configuration swConf = default(Configuration);
             ConfigurationManager swConfMgr = default(ConfigurationManager);
             Configuration swDerivConf = default(Configuration);
             bool bRet = false;
             int i;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swConfMgr = swModel.ConfigurationManager;
             swConf = swConfMgr.ActiveConfiguration;

             vConfigNameArr = (string[])swModel.GetConfigurationNames();

             for (i = 0; i <= vConfigNameArr.GetUpperBound(0); i++)  {
                 swConf = (Configuration)swModel.GetConfigurationByName(vConfigNameArr[i]);

                 // Nothing or null if (derived) configuration already exists
                 swDerivConf = swConfMgr.AddConfiguration(swConf.Name + " Derived", "Derived comment", "Derived alternate name", 1, swConf.Name, "Derived description");
                 bRet = swDerivConf.Select2(true, null);
             }

         }

         public SldWorks swApp;

     }

 }
```
