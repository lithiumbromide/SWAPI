---
title: "Get Structural Member Body Sketch Segments Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Structural_Member_Body_Sketch_Segments_Example_CSharp.htm"
---

# Get Structural Member Body Sketch Segments Example (C#)

This example shows how to get the sketch segments that define the path of a body in a structural member.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\api\weldment_box3.sldprt.
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. Gets the feature definition of Structural Member1.
 // 2. Selects body, Structural Member1[1].
 // 3. Gets the number of sketch segments that define the path of the
 //    selected body.
 // 4. Examine the Immediate window.
 //
 // NOTE: Because the part is used elsewhere, do not save changes.
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
 namespace GetSketchSegments_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Part;

         bool boolstatus;
         Feature swFeat;
         StructuralMemberFeatureData featData;
         SelectionMgr selMan;
         Body2 swBody;
         object[] vSeg;

         public void Main()
         {
             Part = (ModelDoc2)swApp.ActiveDoc;
             boolstatus = Part.Extension.SelectByID2("Structural Member1",  "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
             selMan = (SelectionMgr)Part.SelectionManager;
             swFeat = (Feature)selMan.GetSelectedObject6(1, -1);
             featData = (StructuralMemberFeatureData)swFeat.GetDefinition();

             Part.ClearSelection2(true);

             // Select a body in Structural Member1
             boolstatus = Part.Extension.SelectByID2("Structural Member1[1]",  "SOLIDBODY", 0, 0, 0, false, 0, null, 0);
             swBody = (Body2)selMan.GetSelectedObject6(1, -1);

             // Get the sketch segments that define the path of the selected body
             vSeg = (object[])featData.GetSketchSegments(swBody);
             Debug.Print(" Number of sketch segments: " + vSeg.Length);

         }

         public SldWorks swApp;

     }
 }
```
