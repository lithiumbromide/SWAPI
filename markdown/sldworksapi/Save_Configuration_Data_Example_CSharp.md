---
title: "Save Configuration Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Save_Configuration_Data_Example_CSharp.htm"
---

# Save Configuration Data Example (C#)

This example shows how to mark each configuration in a multi-configuration model as needing to be rebuilt and how to save its configuration data, including preview bitmaps, every time you save the model document.

```
//------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified file to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Activates each configuration in the model.
// 2. Sets each configuration's Rebuild/Save Mark to true, if it is false.
// 3. Saves each configuration's preview bitmap to disk.
// 4. Examine the Immediate window.
//
// NOTES:
// * In SOLIDWORKS 2013 and later, to mark each configuration
//   as needing to be rebuilt and to save its configuration data
//   every time you save the model:
//   1. Activate each configuration and set
//      IConfiguration::AddRebuildSaveMark to true.
//   2. Save the model.
// * Because this model is used elsewhere, do not
//   save changes.
//------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace AddRebuildSaveMarkCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {

            ModelDoc2 swModel = default(ModelDoc2);
            Configuration swConfig = default(Configuration);
            ConfigurationManager swConfMgr = default(ConfigurationManager);
            object[] configNameArr = null;
            string configName = null;
            string fileName = null;
            string bitmapName = null;
            string bitmapPathName = null;
            bool status = false;
            int errors = 0;
            int warnings = 0;
            int i = 0;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\multiconfig-part-2.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swConfMgr = (ConfigurationManager)swModel.ConfigurationManager;
            configNameArr = (object[])swModel.GetConfigurationNames();

            Debug.Print("Checking each configuration's Add Rebuild/Save Mark setting after opening the model document:");

            for (i = 0; i <= configNameArr.GetUpperBound(0); i++)
            {
                configName = (string)configNameArr[i];
                swConfig = (Configuration)swModel.GetConfigurationByName(configName);
                status = swModel.ShowConfiguration2(configName);
                Debug.Print("   " + configName + "'s" + " Add Rebuild/Save Mark = " + swConfig.AddRebuildSaveMark);
                if (swConfig.AddRebuildSaveMark == false)
                {
                    swConfig.AddRebuildSaveMark = true;
                    bitmapName = configName + ".bmp";
                    Debug.Print("      Resetting " + configName + "'s" + " Add Rebuild/Save Mark = " + swConfig.AddRebuildSaveMark);
                    bitmapPathName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\" + bitmapName;
                    status = swApp.GetPreviewBitmapFile(fileName, configName, bitmapPathName);
                    if (status)
                    {
                        Debug.Print("      " + configName + "'s " + "preview bitmap written to disk: " + bitmapPathName);
                    }
                }
            }

            //Save the model to save each configuration's data with the model
            //status = swModel.Save3(swSaveAsOptions_e.swSaveAsOptions_Silent, errors, warnings)

        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;

    }
}
```
