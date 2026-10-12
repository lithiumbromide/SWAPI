---
title: "Create Forming Tool Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Forming_Tool_Example_CSharp.htm"
---

# Create Forming Tool Example (C#)

This example shows how to create a forming tool for a sheet metal part.

```vb
 //----------------------------------------------------------------------------
 // Preconditions: Open public_documents\samples\tutorial\api\formingTool.sldprt
 //
 // Postconditions:
 // 1. Creates FormTool1 with the specified stopping face, face to remove,
 //    and insertion point.
 // 2. Examine the FeatureManager design tree and graphics area.
 //
 // NOTE: Because the model is used elsewhere, do not save changes.
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
 namespace CreateFormTool_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Part;
         Feature myFeature;

         bool boolstatus;
         public void Main()
         {
             Part = (ModelDoc2)swApp.ActiveDoc;
             //Select the stopping face: Mark = 1
             boolstatus = Part.Extension.SelectByID2("", "FACE", 0.0283459459495816, 0.0187563215566229, 0,  true, 1,  null, 0);
             //Select the face to remove: Mark = 2
             boolstatus = Part.Extension.SelectByID2("", "FACE", 0.0358143533097106, 0.0308169322714775, 0.0066335048657038,  true, 2,  null, 0);
             //Create a forming tool with insertion point x=0, y=0
             myFeature = Part.FeatureManager.CreateFormTool2(0, 0);
         }

         public SldWorks swApp;

     }
 }
```
