---
title: "Get Build Numbers Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Build_Numbers_Example_CSharp.htm"
---

# Get Build Numbers Example (C#)

This example shows how to get the build, major revision, and hot fix numbers of the SOLIDWORKS Design application.

```vb
 //--------------------------------------------------------
 // Preconditions: Open SOLIDWORKS Design.
 //
 // Postconditions: Inspect the Immediate window for build,
 // major revision, and hot fix numbers.
 //--------------------------------------------------------
using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 namespace GetBuildNumbers2_CSharp.csproj
 {
     partial class SolidWorksMacro
     {
         string BaseVersion;
         string CurrentVersion;
         string HotFixes;

         public void Main()
         {
             swApp.GetBuildNumbers2(out BaseVersion, out CurrentVersion, out HotFixes);
             Debug.Print("SOLIDWORKS major revision number: " + BaseVersion);
             Debug.Print("SOLIDWORKS build number: " + CurrentVersion);
             Debug.Print("SOLIDWORKS hot fix numbers: " + HotFixes);

         }

         public SldWorks swApp;
     }
 }
```
