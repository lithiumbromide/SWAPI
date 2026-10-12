---
title: "Get and Set Model Break View Display Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Model_Break_View_Display_Example_CSharp.htm"
---

# Get and Set Model Break View Display Example (C#)

This example shows how to get and set whether to display an assembly's Model Break View in a drawing.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a drawing that has:
 //    * assembly with Model Break View1.
 //    * Drawing View1.
 // 2. Open an Immediate window.
 //
 // Postconditions:
 // 1. Displays Model Break View1.
 // 2. Inspect the Immediate window and graphics area.
 // ---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;

 namespace ModelBreakView_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Part;
         View swView;
         SelectionMgr swSelMgr;

         bool boolstatus;

         public void Main()
         {
             Part = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr = (SelectionMgr)Part.SelectionManager;

             boolstatus = ((DrawingDoc)Part).ActivateView("Drawing View1");
             boolstatus = Part.Extension.SelectByID2("Drawing View1",  "DRAWINGVIEW", 0.395146689428525, 0.746414551874767, 0, false, 0, null, 0);

             swView = (View)swSelMgr.GetSelectedObject6(1, -1);
             boolstatus = swView.ShowModelBreakState(true, "Model Break View1");

             Debug.Print("Displaying model break view? " + swView.IsModelBreakState());

             Part.ForceRebuild3(true);

         }

         public SldWorks swApp;

     }
 }
```
