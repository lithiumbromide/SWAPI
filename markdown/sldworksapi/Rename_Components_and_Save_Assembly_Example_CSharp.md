---
title: "Rename Components and Save Assembly Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Rename_Components_and_Save_Assembly_Example_CSharp.htm"
---

# Rename Components and Save Assembly Example (C#)

This example shows how to rename components in an assembly and returns an error when attempting to save the assembly without first saving its references.

```
//--------------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified assembly exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified assembly.
// 2. Selects a component.
// 3. Renames the selected component and the other component with the
//    the same name.
// 4. Attempts to save the assembly.
// 5. Gets whether the assembly has renamed components.
// 6. Examine the Immediate window.
//
// NOTE: Because the assembly is used elsewhere, do not save changes.
//--------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

Namespace Macro1CSharp.csproj
{
    Partial Public Class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            bool status = false;
            int errors = 0;
            int warnings = 0;
            string fileName = null;
            int errorsRename = 0;
            int errorsSave = 0;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\beam_boltconnection.sldasm";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            status = swModelDocExt.SelectByID2("beam with holes-2@beam_boltconnection", "COMPONENT", 0, 0, 0, false, 0, null, 0);
            errorsRename = swModelDocExt.RenameDocument("Renamed_beam_with_holes");
            Debug.Print("Rename document errors: " + errorsRename);
            status = swModel.Save3((int)swSaveAsOptions_e.swSaveAsOptions_Silent, ref errorsSave, ref warnings);
            if (status == false)
            {
                Debug.Print("Save errors (8192 = Saving an assembly with renamed components requires saving the references): " + errorsSave);
            }
            status = swModelDocExt.HasRenamedDocuments();
            Debug.Print("Assembly document has renamed components: " + status);

            swModel.ClearSelection2(true);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
