---
title: "Get Component State Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Component_State_Example_CSharp.htm"
---

# Get Component State Example (C#)

This example shows how to find out if the selected component is resolved or suppressed, hidden or visible, and whether or not it's a rigid or flexible subassembly. This example also gets the persistent ID of the selected component.

```
//---------------------------------------------------
// Preconditions:
// 1. Ensure that the specified assembly document
//    to open exists.
// 2. Open the Immediate window.
// 3. Run the macro.
//
// Postconditions:
// 1. Opens the assembly document.
// 2. Selects the subassembly.
// 3. Prints to the Immediate window:
//    * Paths to the assembly and subassembly documents
//    * Whether the component is hidden, fixed,
//      or suppressed
//    * Component's persistent ID
//    * Component's solving state
// 4. Examine the Immediate window.
//----------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace GetComponentStateCSharp.csproj
{

    partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            AssemblyDoc swAssy = default(AssemblyDoc);
            SelectionMgr swSelMgr = default(SelectionMgr);
            Component2 swComp = default(Component2);
            string fileName = null;
            bool status = false;
            int errors = 0;
            int warnings = 0;

            // Open assembly document
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\98food processor.sldasm";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            // Select subassembly
            status = swModelDocExt.SelectByID2("blade shaft-1@98food processor", "COMPONENT", 0, 0, 0, false, 0, null, 0);
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swAssy = (AssemblyDoc)swModel;
            swComp = (Component2)swSelMgr.GetSelectedObjectsComponent3(1, 0);

            // Print to the Immediate window the path and state of the
            // selected component
            Debug.Print("File = " + swModel.GetPathName());
            Debug.Print("  Component   = " + swComp.Name2);
            Debug.Print("    Path           = " + swComp.GetPathName());
            Debug.Print("    IsHidden       = " + swComp.IsHidden(true));
            Debug.Print("    IsFixed        = " + swComp.IsFixed());
            Debug.Print("    GetSuppression = " + swComp.GetSuppression());
            Debug.Print("    ID             = " + swComp.GetID());
            // 0 =  if subassembly is rigid
            // 1 =  if subassembly is flexible
            // -1 = selected component is a part component
            Debug.Print("    Solving        = " + swComp.Solving);
        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>

        public SldWorks swApp;

    }
}
```
