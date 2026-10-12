---
title: "Create GTol Composite Frame Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Gtol_Composite_Frame_Example_CSharp.htm"
---

# Create GTol Composite Frame Example (C#)

This example shows how to create a composite frame for a geometric tolerance symbol.

```vb
 //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a document with a geometric tolerance (GTol) whose first two
 //    frames have the same symbol.
 // 2. Select the GTol in the graphics area.
 // 3. Open the Immediate window.
 //
 // Postconditions:
 // 1. Creates a composite frame for the symbol in the graphics area.
 // 2. Examine the graphics area and Immediate window.
 //----------------------------------------------------------------------------

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;

 namespace GetSetCompositeFrame_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         SelectionMgr selMgr;
         ModelDoc2 Part;
         Gtol gtol;

         public void Main()
         {
             Part = (ModelDoc2)swApp.ActiveDoc;
             selMgr = (SelectionMgr)Part.SelectionManager;
             gtol = (Gtol)selMgr.GetSelectedObject6(1, -1);

             gtol.SetCompositeFrame2(true, 1);
             Debug.Print("Frame 1 is part of a GTol composite frame? " + gtol.GetCompositeFrame2(1));

         }

         public SldWorks swApp;

     }

 }
```
