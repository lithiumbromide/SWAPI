---
title: "Create, Unlink, and Purge Display States in Part Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create,_Unlink,_and_Purge_Display_States_in_Part_Example_CSharp.htm"
---

# Create, Unlink, and Purge Display States in Part Example (C#)

This example shows how to create, unlink, and purge display states in a part document.

```
//---------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\multibody\multi-inter.sldprt,
//    whose Default configuration has two display states:
//    * PhotoWorks Display
//    * Display State 1
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Creates and unlinks Display State 2.
// 2. Attempts to purge any display states identical to
//    Display State 2.
// 3. Closes the part document without saving any changes.
// 4. Examine the Immediate window.
//-----------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
namespace AddAndPurgeDisplayStates_CSharp.csproj
{
    partial
 class SolidWorksMacro
    {
        public PartDoc swPart;

        public
 void Main()
```

```vb
        {
             ModelDoc2 swModel = default(ModelDoc2);
             Configuration swConfig = default(Configuration);
             ModelDocExtension swModelDocExt = default(ModelDocExtension);
             bool boolstatus = false;
             string modelName = null;
             swModel = (ModelDoc2)swApp.ActiveDoc;

            // Get Default configuration and create a display state
             swConfig = (Configuration)swModel.GetConfigurationByName("Default");
             boolstatus = swConfig.CreateDisplayState("Display State 2");
             if (boolstatus) Debug.Print("Display State 2 created.");
             swModel.ForceRebuild3(true);
            // If display is linked, unlink it
             swModelDocExt = swModel.Extension;
             Debug.Print("Is Display State 2 linked? " + swModelDocExt.LinkedDisplayState);
             swModelDocExt.LinkedDisplayState = false;
             Debug.Print("Is Display State 2 still linked? " + swModelDocExt.LinkedDisplayState);
            // Purge any display states identical to Display State 2
             boolstatus = swModelDocExt.PurgeDisplayState();
             Debug.Print("Identical display states to Display State 2 purged? " + boolstatus);
             swModel.ForceRebuild3(true);
            // Close the part without saving changes
             modelName = swModel.GetTitle();
             swApp.QuitDoc(modelName);
        }
        public SldWorks swApp;
    }
}
```
