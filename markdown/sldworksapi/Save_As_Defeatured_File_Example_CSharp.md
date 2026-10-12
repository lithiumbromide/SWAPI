---
title: "Save as De-Featured File Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Save_As_Defeatured_File_Example_CSharp.htm"
---

# Save as De-Featured File Example (C#)

This example shows how to de-feature an assembly and save it as a part.

```vb
//-----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\floxpress\ball valve\ball_valve.sldasm.
 // 2. Verify that c:\temp exists.
 //
 // Postconditions:
 // 1. Saves the assembly as a de-featured part.
 // 2. Open c:\temp\ball_valve.sldprt to verify.
 //------------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
namespace SaveFileAsDeFeaturedPart_CSharp.csproj
{
    partial class SolidWorksMacro
    {
        ModelDoc2 swModel;
         bool boolstatus;
        public void Main()
         {
            swModel= (ModelDoc2)swApp.ActiveDoc;
             boolstatus = swModel.Extension.SaveDeFeaturedFile("C:\\temp\\ball_valve.sldprt");
        }
        public SldWorks swApp;
    }
}
```
