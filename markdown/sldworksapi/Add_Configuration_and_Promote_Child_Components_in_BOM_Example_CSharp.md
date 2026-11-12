---
title: "Add Configuration and Promote Child Components in BOM Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Configuration_and_Promote_Child_Components_in_BOM_Example_CSharp.htm"
---

# Add Configuration and Promote Child Components in BOM Example (C#)

This example shows how to add a configuration to an assembly and promote its child components one level in a BOM.

```
//----------------------------------------
// Preconditions:
// 1. Specified assembly document exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified assembly document.
// 2. Adds a new configuration named Config2.
// 3. Sets the option to dissolve the assembly's
//    configuration when it appears in a BOM and
//    promote all of its child components one level.
// 4. To verify, examine the option value printed to
//    the Immediate window.
//
// NOTE: Because this assembly document is used
// elsewhere, do not save changes when closing it.
//----------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace ChildComponentDisplayInBOMCSharp.csproj
{
    public partial class SolidWorksMacro
    {
        AssemblyDoc swAssembly;
        ModelDoc2 swModel;
        ModelDocExtension swModelDocExt;
        Configuration swConfig;
        string fileName;
        bool status;
        int errors;
        int warnings;

        public void Main()
        {
            //Open assembly document
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\bowl and chute.sldasm";
            swAssembly = (AssemblyDoc)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModel = (ModelDoc2)swAssembly;

            //Add configuration named Config2
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("bowl and chute.SLDASM", "COMPONENT", 0, 0, 0, false, 0, null, 0);
            swModel.ClearSelection2(true);
            swConfig = (Configuration)swModel.AddConfiguration3("Config2", "", "", (int)swConfigurationOptions2_e.swConfigOption_DoDisolveInBOM + (int)swConfigurationOptions2_e.swConfigOption_DontShowPartsInBOM);

            //Dissolve the assembly's configuration
            //when it appears in a BOM and promote all of
            //its child components one level
            swConfig.ChildComponentDisplayInBOM = (int)swChildComponentInBOMOption_e.swChildComponent_Promote;
            Debug.Print("Child component display option in BOM: " + swConfig.ChildComponentDisplayInBOM);
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
