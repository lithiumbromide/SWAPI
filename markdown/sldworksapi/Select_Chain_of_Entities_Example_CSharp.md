---
title: "Select Chains of Entities Attached to a Sketch Segment Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Chain_of_Entities_Example_CSharp.htm"
---

# Select Chains of Entities Attached to a Sketch Segment Example (C#)

This example shows how to select chains of entities attached to a sketch segment.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a part that contains a sketch of a rectangle.
 // 2. Select one sketch segment of the rectangle.
 //
 // Postconditions:
 // 1. Selects all of the sketch segments of the rectangle.
 // 2. Examine the graphics area.
 // ---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 namespace SelectChain_CSharp.csproj
 {
     partial class SolidWorksMacro
     {
         ModelDoc2 Part;
         SelectionMgr SelMgr;
         SketchSegment sketchSegment;
         SelectData SelData;

         bool boolstatus;

         public void Main()
         {
             Part = (ModelDoc2)swApp.ActiveDoc;
             SelMgr = (SelectionMgr)Part.SelectionManager;
             SelData = (SelectData)SelMgr.CreateSelectData();
             boolstatus = Part.Extension.SelectByID2("Line3@Sketch2", "EXTSKETCHSEGMENT", -0.01022262320328, 0.01646364019604, 0,  false, 0,  null, 0);
             sketchSegment = (SketchSegment)SelMgr.GetSelectedObject6(1, -1);
             boolstatus = sketchSegment.SelectChain(true, SelData);

         }

         public SldWorks swApp;

     }
 }
```
