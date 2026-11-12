---
title: "Create SpeedPak for Subassemblies Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_SpeedPak_for_Subassemblies_Example_CSharp.htm"
---

# Create SpeedPak for Subassemblies Example (C#)

This example shows how to:

- create SpeedPak configurations for subassemblies.
- switch between the SpeedPak configuration and the parent configuration of the SpeedPak configuration.

```
//-------------------------------------------------------------------
// Preconditions:
//  1. Verify that the specified assembly to open exists.
//  2. Open the Immediate window.
//
// Postconditions:
//  1. Opens the specified assembly.
//  2. Deletes the Coordinate System1 feature to avoid errors.
//  3. Selects the arm1 and arm2 subassemblies.
//  4. Checks to see if either component has a SpeedPak configuration.
//  5. Creates graphics-only SpeedPak for each selected component.
//  6. At System.Diagnostics.Debugger.Break, examine the FeatureManager
//     design tree to verify that the icons for arm1 and arm2 indicate
//     SpeedPak, then press F5.
//  7. Switches SpeedPak to each selected component's parent configuration.
//  8. At System.Diagnostics.Debugger.Break, examine the FeatureManager
//     design tree to verify that SpeedPak switched to the parent configuration
//     of arm1 and arm2, then press F5.
//  9. Switches each component back to SpeedPak.
// 10. Examine the Immediate window and FeatureManager design tree to verify
//     that arm1 and arm2 are SpeedPak.
//
// NOTE: Because the assembly is used elsewhere, do not save changes.
//--------------------------------------------------------------------
using System;
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System.Diagnostics;

namespace Macro1CSharp.csproj
{
    partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel;
            ModelDocExtension swModelDocExt;
            AssemblyDoc swAssembly;
            SelectionMgr swSelMgr;
            Component2 swComponent;
            bool status = false;
            int errors = 0;
            int warnings = 0;
            string fileName;
            object[] selComponents = new object[2];
            int i = 0;
            int count = 0;
            bool speedPakExists = false;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\wrench.sldasm";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swAssembly = (AssemblyDoc)swModel;
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;

            //Select and delete Coordinate System1 to avoid errors
            status = swModelDocExt.SelectByID2("Coordinate System1", "COORDSYS", 0, 0, 0, false, 0, null, 0);
            swModel.EditDelete();

            //Select the two subassemblies for which to create SpeedPak configurations
            status = swModelDocExt.SelectByID2("arm1-1@wrench", "COMPONENT", 0, 0, 0, false, 0, null, 0);
            selComponents[0] = swSelMgr.GetSelectedObject6(1, -1);
            status = swModelDocExt.SelectByID2("arm2-1@wrench", "COMPONENT", 0, 0, 0, true, 0, null, 0);
            selComponents[1] = swSelMgr.GetSelectedObject6(2, -1);
            count = swSelMgr.GetSelectedObjectCount2(-1);

            //Get whether any of the selected components already
            //have SpeedPak configurations
            for (i = 0; i <= count - 1; i++)
            {
                swComponent = (Component2)selComponents[i];
                speedPakExists = swComponent.IsSpeedPak;
                if ((speedPakExists))
                {
                    Debug.Print("SpeedPak already exists for component(" + i + ")");
                }
            }

            //Create graphics-only SpeedPak for the selected components
            status = swAssembly.CreateSpeedPak(2);
            Debug.Print("SpeedPak created for selected components? " + status);

            System.Diagnostics.Debugger.Break();
            //Examine the FeatureManager design tree to verify that the
            //icons for arm1 and arm2 indicate SpeedPak, then press F5

            //Switch SpeedPak to the parent configurations of each selected components
            status = swModelDocExt.SelectByID2("arm1-1@wrench", "COMPONENT", 0, 0, 0, false, 0, null, 0);
            status = swModelDocExt.SelectByID2("arm2-1@wrench", "COMPONENT", 0, 0, 0, true, 0, null, 0);
            status = swAssembly.SetSpeedPakToParent();
            Debug.Print("SpeedPak switched to the parent configuration of each selected component? " + status);

            System.Diagnostics.Debugger.Break();
            //Examine the FeatureManager design tree to verify
            //that SpeedPak switched to the parent configurations of arm1 and
            //arm2

            //Switch the selected components to SpeedPak
            status = swModelDocExt.SelectByID2("arm1-1@wrench", "COMPONENT", 0, 0, 0, false, 0, null, 0);
            status = swModelDocExt.SelectByID2("arm2-1@wrench", "COMPONENT", 0, 0, 0, true, 0, null, 0);
            status = swAssembly.UseSpeedPak();
            Debug.Print("Switched the selected components to SpeedPak? " + status);
        }
        public SldWorks swApp;
    }
}
```
