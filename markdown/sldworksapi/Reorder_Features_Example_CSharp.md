---
title: "Reorder Features Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Reorder_Features_Example_CSharp.htm"
---

# Reorder Features Example (C#)

This example shows how to move a feature to another location in the
FeatureManager design tree of a part.

```vb
 //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\api\clamp2.sldprt.
 // 2. Open an Immediate window.
 //
 // Postconditions:
 // 1. Fillet5 moves to the end of the FeatureManager design tree.
 // 2. Inspect the Immediate window.
 //
 // NOTE: Because the assembly document is used by elsewhere,
 // do not save any changes when closing the document.
 //---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace ReorderFeature_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 modelDoc2;
         ModelDocExtension modelDocExt;
         bool retVal;

         public void Main()
         {
             modelDoc2 = (ModelDoc2)swApp.ActiveDoc;
             modelDocExt = modelDoc2.Extension;

             retVal = modelDocExt.ReorderFeature2("Fillet5", "", (int)swMoveLocation_e.swMoveToEnd);
             Debug.Print("Fillet5 moved to the end of the FeatureManager design tree? " + retVal);

         }

         public SldWorks swApp;

     }
 }
```
