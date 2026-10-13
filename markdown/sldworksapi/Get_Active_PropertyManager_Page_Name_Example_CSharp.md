---
title: "Get Active PropertyManager Page Name Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Active_PropertyManager_Page_Name_Example_CSharp.htm"
---

# Get Active PropertyManager Page Name Example (C#)

This example shows how to get the name of the active PropertyManager page.

```vb
 //--------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\fillets\knob.sldprt.
 // 2. In SOLIDWORKS Design, click Insert > Features > Fillet/Round.
 // 3. Open the Immediate window.
 //
 // Postconditions:
 // 1. Gets the name of the active PropertyManager page.
 // 2. Examine the Immediate window.
 // 3. In the SOLIDWORKS Design user-interface:
 //    a. Close the PropertyManager page.
 //    b. Close the part document.
 //
 // NOTE: Because the part is used elsewhere, do not
 // save changes.
 //----------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;

 namespace Macro1CSharp.csproj
 {
     partial  class  SolidWorksMacro
     {

         public  void Main()
         {

             ModelDoc2 swModel = default(ModelDoc2);
             ModelDocExtension swModelDocExt = default(ModelDocExtension);
             string pageName = null;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swModelDocExt = (ModelDocExtension)swModel.Extension;

             // Print the name of the active PropertyManager page in the Immediate window
             pageName = swModelDocExt.GetActivePropertyManagerPage();

             Debug.Print("Name of active PropertyManager page: " + pageName);
         }

         ///  <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>
         public SldWorks swApp;

     }
 }
```
