---
title: "Get Pattern Display Dimension Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Pattern_Display_Dimension_Example_CSharp.htm"
---

# Get Pattern Display Dimension Example (C#)

This example shows how to get the display dimensions for various pattern properties of a linear pattern.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a part with a linear pattern.
 // 2. Select the linear pattern feature.
 // 3. Open the Immediate window.
 //
 // Postconditions: Inspect the Immediate window.
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
 namespace GetDisplayDimension_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Part;
         SelectionMgr selMan;
         Feature feat;
         DisplayDimension dispDim;

         public void Main()
         {
             Part = (ModelDoc2)swApp.ActiveDoc;
             selMan = (SelectionMgr)Part.SelectionManager;
             feat = (Feature)selMan.GetSelectedObject6(1, -1);
             Debug.Print(" Feature = " + feat.Name);

             dispDim = (DisplayDimension)feat.GetDisplayDimension((int)swFeatureDimensionParameter_e.swPatternInstanceCount1);
             Debug.Print(" Instance count 1 display dimension = " + dispDim.GetNameForSelection());
             Debug.Print(" Type of dimension as defined in swDimensionType_e = " + dispDim.Type2);
             dispDim = (DisplayDimension)feat.GetDisplayDimension((int)swFeatureDimensionParameter_e.swPatternSpacing1);
             Debug.Print(" Spacing 1 display dimension = " + dispDim.GetNameForSelection());

         }

         public SldWorks swApp;

     }

 }
```
