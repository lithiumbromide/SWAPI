---
title: "Get Linked Display States Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_Linked_Display_States_Example_CSharp.htm"
---

# Get Linked Display States Example (C#)

This example gets an assembly and reports on its active configuration and display states.

```vb
// -------------------------------------------------------------------------
 // Preconditions:
 // 1. Read the SOLIDWORKS Document Manager API
 //    Getting Started topic in the API help
 //    and ensure that the required DLLs have been registered.
 // 2. Open SOLIDWORKS and copy the code below to a C# macro.
 // 3. Ensure that the latest SolidWorks.Interop.swdocumentmgr.dll
 //    interop assembly is loaded in your project. (Right-click your
 //    project in Project Explorer, click Add Reference,
 //    click the interop assembly in the .NET tab, or browse
 //    for the DLL in install_dir\api\redist).
 // 4. Substitute your license key for your_license_key in the code.
 // 5. Open the Immediate window.
 //
 // Postconditions: Examine the Immediate Window for output.
 //--------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using SolidWorks.Interop.swdocumentmgr;
using System;
using System.Diagnostics;

    partial class SolidWorksMacro
    {
        public SldWorks swApp;
        public void Main()
        {
            SwDMClassFactory swCf = default(SwDMClassFactory);
            swCf = new SwDMClassFactory();
            SwDMApplication swDocMgr = default(SwDMApplication);
            swDocMgr = swCf.GetApplication("your_license_key");
            int i = 0;
            int j = 0;
            SwDMDocument14 swDoc12 = default(SwDMDocument14);
            SwDmDocumentOpenError res = default(SwDmDocumentOpenError);
            SwDmDocumentType dt = default(SwDmDocumentType);
            dt = SwDmDocumentType.swDmDocumentAssembly;
            string filename;

            Debug.Print("Opening an assembly...");
            filename = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\motor casing.sldasm";
            swDoc12 = (SwDMDocument14)swDocMgr.GetDocument(filename, dt, false, out res);
            if (swDoc12 == null | (res != SwDmDocumentOpenError.swDmDocumentOpenErrorNone))
            {
                Debug.Print("Error opening file....");
                return;
            }
            SwDMConfiguration12 activeConfig = default(SwDMConfiguration12);
            string activeConfigName = null;
            SwDMConfigurationMgr configMgr = default(SwDMConfigurationMgr);
            configMgr = swDoc12.ConfigurationManager;
            activeConfigName = configMgr.GetActiveConfigurationName();
            Debug.Print("Getting the active configuration: " + activeConfigName);
            activeConfig = (SwDMConfiguration12)configMgr.GetConfigurationByName(activeConfigName);
            if (activeConfig == null)
            {
                Debug.Print("Error getting the active configuration...");
                return;
            }
            Debug.Print("ID of " + activeConfig.Name2 + ": " + activeConfig.GetID());
            Debug.Print("");

            int numLinkedDisplayStates = 0;
            String[] ldsVariant = null;
            string lds = null;
            Boolean[] compVisibleList = null;
            string[] compFileDirectory = null;
            Object ldsObject = null;

            numLinkedDisplayStates = activeConfig.GetLinkedDisplayStates(out ldsObject);
            Debug.Print("Number of linked display states of " + activeConfigName + ": " + numLinkedDisplayStates);

            // Getting all the components for one linked display state
            ldsVariant = (String[])ldsObject;
            Object vis = null;
            Object fd = null;
            lds = ldsVariant[0];
            activeConfig.GetComponentVisibleByDisplayStateName(lds, out vis, out fd);
            Debug.Print("");
            Debug.Print("Getting the paths and file names of all of the components in the linked display state, " + lds + ": ");
            Debug.Print("");
            compVisibleList = (Boolean[])vis;
            compFileDirectory = (String[])fd;
            for (j = 0; j <= compFileDirectory.GetUpperBound(0); j++)
            {
                Debug.Print("Component: " + compFileDirectory[j]);
                Debug.Print(" Is visible? " + compVisibleList[j]);
            }
            //Getting all the components in the configuration
            Debug.Print("");
            Debug.Print("Getting the names of all of the components in the FeatureManager design tree in C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\api\\redist\ " + activeConfig.Name2 + ": ");
            Debug.Print("");
            Object[] vComponents = null;
            vComponents = (Object[])activeConfig.GetComponents();
            if (!((vComponents == null)))
            {
                SwDMComponent11 swDmComponent = default(SwDMComponent11);
                for (i = 0; i <= vComponents.GetUpperBound(0); i++)
                {
                    swDmComponent = (SwDMComponent11)vComponents[i];
                    Debug.Print(" Component name: " + swDmComponent.Name3);
                    Debug.Print(" For a selective open with OpenDoc7, use: " + swDmComponent.SelectName2);
                }
            }
            swDoc12.CloseDoc();
        }
    }
```
