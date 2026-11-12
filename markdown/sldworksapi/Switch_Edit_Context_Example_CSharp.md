---
title: "Switch Edit Context Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Switch_Edit_Context_Example_CSharp.htm"
---

# Switch Edit Context Example (C#)

This example shows how to switch back and forth between assembly and part when editing. It also shows how to fix and float an assembly component.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open:
 //    public_documents\samples\tutorial\api\assem2.sldasm
 // 2. Press F5 after each macro pause.
 //
 // Postconditions: None
 //
 // NOTE: Because the model is used elsewhere,
 // do not save changes when closing it.
 // ---------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 namespace AssemblyDocMethods_CSharp.csproj
 {
     partial class SolidWorksMacro
     {
         AssemblyDoc assem;
         ModelDoc2 Part;

         bool boolstatus;

         public void Main()
         {
             assem = (AssemblyDoc)swApp.ActiveDoc;
             Part = (ModelDoc2)assem;

             boolstatus = Part.Extension.SelectByID2("Part1^Assem2-1@assem2", "COMPONENT", 0, 0, 0, false, 0, null, 0);
             assem.FixComponent();
             // Part1^Assem2-1@assem2 is now fixed
             System.Diagnostics.Debugger.Break();

             Part.ClearSelection2(true);
             boolstatus = Part.Extension.SelectByID2("Part1^Assem2-1@assem2", "COMPONENT", 0, 0, 0, false, 0, null, 0);
             assem.UnfixComponent();
             // Part1^Assem2-1@assem2 is now floating
             System.Diagnostics.Debugger.Break();

             Part.ClearSelection2(true);
             boolstatus = Part.Extension.SelectByID2("Part1^Assem2-1@assem2", "COMPONENT", 0, 0, 0, false, 0, null, 0);
             int Info = 0;
             assem.EditPart2(true, true, ref Info);
             // Part1^Assem2-1@assem2 is being edited in the context of the assembly
             System.Diagnostics.Debugger.Break();

             Part.ClearSelection2(true);
             boolstatus = Part.Extension.SelectByID2("assem2.SLDASM", "COMPONENT", 0, 0, 0, false, 0, null, 0);
             assem.EditAssembly();
             // The assembly is being edited

         }

         public SldWorks swApp;

     }

 }
```
