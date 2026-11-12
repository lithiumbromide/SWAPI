---
title: "Get Names and Show Model Break Views Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Names_and_Show_Model_Break_Views_Example_CSharp.htm"
---

# Get Names and Show Model Break Views Example (C#)

This example shows how to:

- get the names of the Model Break Views in the current configuration of an active model.
- show one of the Model Break Views.

```
//--------------------------------------
// Preconditions:
// 1. Open a part document with multiple
//    hidden Model Break Views.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Gets the number and names of the Model Break
//    Views in the current configuration of the
//    active model.
// 2. Shows one of the Model Break Views.
// 3. Examine the Immediate window and the
//    graphics area.
//----------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace ModelBreakViewsCSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel;
            ModelDocExtension swModelDocExt;
            object[] names = null;
            object oNames = null;
            int nbr;
            int i;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            //Get and print number and names of Model Break
            //Views in current configuration of the active
            //model
            nbr = swModelDocExt.GetModelBreakViewNames(out oNames);
            names = (object[])oNames;
            Debug.Print("Model Break Views:");
            Debug.Print("  Number: " + nbr);
            Debug.Print("  Names: ");
            for (i = 0; i <= nbr - 1; i++)
            {
                Debug.Print("    " + names[i]);
            }

            //Show Model Break View
            string name;
            name = (string)names[nbr - 1];
            swModelDocExt.ShowModelBreakView(true, name);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
