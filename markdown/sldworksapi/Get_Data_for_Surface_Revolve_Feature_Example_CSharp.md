---
title: "Get Data for Surface Revolve Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Data_for_Surface_Revolve_Feature_Example_CSharp.htm"
---

# Get Data for Surface Revolve Feature Example (C#)

This example shows how to get the data for the selected surface revolve feature.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a model document with a surface revolve feature.
 // 2. Select the surface revolve feature.
 //
 // Postconditions: Inspect the Immediate window.
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
 namespace SurfaceRevolveFEatureData_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             SelectionMgr swSelMgr = default(SelectionMgr);
             Feature swFeat = default(Feature);
             SurfRevolveFeatureData swSurfRevolve = default(SurfRevolveFeatureData);

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
             swSurfRevolve = (SurfRevolveFeatureData)swFeat.GetDefinition();

             Debug.Print("File = " + swModel.GetPathName());
             Debug.Print("Feature = " + swFeat.Name);
             Debug.Print("   Reverse direction?  " + swSurfRevolve.ReverseDirection);
             Debug.Print("   Type of surface revolve =  " + swSurfRevolve.Type);

         }

         public SldWorks swApp;

     }
 }
```
