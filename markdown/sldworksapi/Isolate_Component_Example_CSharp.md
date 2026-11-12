---
title: "Isolate Component Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Isolate_Component_Example_CSharp.htm"
---

# Isolate Component Example (C#)

This example shows how to isolate a component and save the characteristics of the new display state.

```
//----------------------------------------------------------
// Preconditions: Verify that the assembly exists.
//
// Postconditions:
// 1. Opens the assembly.
// 2. Selects a component.
// 3. Isolates the selected component and changes the
//    display of all of the other components to wireframe.
// 4. Saves the display characteristics to a new display
//    state.
// 5. Exits isolate.
// 6. Click the ConfigurationManager tab and double-click
//    Test_Display_State.
//
// NOTE: Because the assembly is used elsewhere, do not
// save changes.
//----------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            AssemblyDoc swAssembly = default(AssemblyDoc);
            bool status = false;
            int errors = 0;
            int warnings = 0;
            string assemblyName = null;
            string componentToIsolate = null;

            assemblyName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\interferenceassem.sldasm";
            swModel = (ModelDoc2)swApp.OpenDoc6(assemblyName, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swAssembly = (AssemblyDoc)swModel;
            componentToIsolate = "squarepad_pink-1@interferenceassem";
            status = swModelDocExt.SelectByID2(componentToIsolate, "COMPONENT", 0, 0, 0, false, 0, null, 0);

            //Isolate selected component and set the
            //visibility of all of the other components to wireframe
            status = swAssembly.Isolate();
            swAssembly.SetIsolateVisibility((int)swIsolateVisibility_e.swIsolateVisibility_WIREFRAME);

            //Save the new display state as Test_Display_State
            status = swAssembly.SaveIsolate("Test_Display_State");

            //Exit isolate
            status = swAssembly.ExitIsolate();

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
