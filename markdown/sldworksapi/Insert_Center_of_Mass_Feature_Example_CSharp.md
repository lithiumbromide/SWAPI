---
title: "Insert Center of Mass Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Center_of_Mass_Feature_Example_CSharp.htm"
---

# Insert Center of Mass Feature Example (C#)

This example shows how to insert Center of Mass and Center of Mass Reference Point features.

```vb
 //----------------------------------------------------------------------------
 // Preconditions: Open a part.
 //
 // Postconditions: The FeatureManager design tree contains:
 // * Center of Mass
 // * Center of Mass Reference Point1
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
 namespace InsertCenterOfMass_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Part;
         Feature COM;
         Feature COMRP;

         public void Main()
         {
             Part = (ModelDoc2)swApp.ActiveDoc;

             COM = Part.FeatureManager.InsertCenterOfMass();
             COMRP = Part.FeatureManager.InsertCenterOfMassReferencePoint();
         }

         public SldWorks swApp;

     }
 }
```
