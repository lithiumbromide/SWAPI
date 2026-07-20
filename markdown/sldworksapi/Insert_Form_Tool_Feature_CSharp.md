---
title: "Insert Forming Tool Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Form_Tool_Feature_CSharp.htm"
---

# Insert Forming Tool Feature Example (C#)

This example shows how to insert a forming tool feature into a sheet metal
part.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a sheet metal part.
 // 2. Verify that the specified forming tool part exists.
 // 3. Select a face on which to apply the counter sink emboss forming tool from
 //    the Design Library.
 //
 // Postconditions:
 // 1. Inserts the counter sink emboss1 feature.
 // 2. Examine the FeatureManager design tree and graphics area.
  // ---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;

 namespace Macro1CSharp.csproj
 {
     partial class SolidWorksMacro
     {
         ModelDoc2 Part;
         Feature myFeature;
         string formingTool;

         public void Main()
         {
             Part = (ModelDoc2)swApp.ActiveDoc;

             // Insert a counter sink emboss forming tool feature
             formingTool = "C:\\ProgramData\\SolidWorks\\SOLIDWORKS 2025\\design library\\forming tools\\embosses\\counter sink emboss.sldprt";
             myFeature = Part.FeatureManager.InsertFormToolFeature(formingTool, false, 0.0, "", true, true, true, true, false);
         }

         public SldWorks swApp;
     }
 }
```
