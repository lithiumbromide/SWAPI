---
title: "Set and Get Paths of Interface Files Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Set_and_Get_Paths_of_Interface_Files_Example_CSharp.htm"
---

# Set and Get Paths of Interface Files Example (C#)

This example shows how to set and get the paths of interface files.

```
//--------------------------------------------------------------
// Preconditions:
// 1. Create a C# Windows console project.
// 2. Copy and paste this example into the C# IDE.
// 3. Add a reference to:
//    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
// 4. Add a reference to System.Windows.Forms.
// 5. Start DraftSight.
// 6. Press F5.
//
// Postconditions:
// 1. Connects to DraftSight.
// 2. Sets different alias, custom icon, customization, and
//    menu file paths.
// 3. Gets different alias, custom icon, customization, and
//    menu file paths. Click OK to close each message box.
//
// NOTE: To verify, you can also click Tools > Options >
// File Locations and expand Interface. Then expand and
// examine Alias File Location, Custom Icon Location,
// Customization File, and Menu Files.
//--------------------------------------------------------------
using System;
using DraftSight.Interop.dsAutomation;
using System.Runtime.InteropServices;
using System.Windows.Forms;

namespace InterfaceFilesCSharp
{
    class Program
    {
        public static void Main()
        {
            DraftSight.Interop.dsAutomation.Application dsApp;

            //Connect to DraftSight application
            dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");

            if (null == dsApp)
            {
                return;
            }

            //Abort any command currently running in DraftSight
            //to avoid nested commands
            dsApp.AbortRunningCommand();

            InterfaceFiles dsInterfaceFiles = dsApp.GetInterfaceFiles();
            if (null == dsInterfaceFiles)
            {
                MessageBox.Show("There are no valid interface files.");
                return;
            }

            //Set and get different file paths
            dsInterfaceFiles.AliasFilePath = "C:\\Program Files\\Dassault Systemes\\DraftSight\\Default Files\\Alias";

            dsInterfaceFiles.CustomIconPath = "";

            dsInterfaceFiles.CustomizationFilePath = "";

            dsInterfaceFiles.MenuFilesPath = "C:\\Program Files\\Dassault Systemes\\DraftSight\\Default Files\\StartupMenu\\english";

            MessageBox.Show("Alias file path: " + dsInterfaceFiles.AliasFilePath);
            MessageBox.Show("Custom icon path: " + dsInterfaceFiles.CustomIconPath);
            MessageBox.Show("Customization file path: " + dsInterfaceFiles.CustomizationFilePath);
            MessageBox.Show("Menu files path: " + dsInterfaceFiles.MenuFilesPath);

        }
    }
}
```
