---
title: "Get Weldment Trim Extend Corner Type Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Weldment_Trim_Extend_Corner_Type_Example_CSharp.htm"
---

# Get Weldment Trim Extend Corner Type Example (C#)

This example shows how to get the type of corner used for a weldment trim extend feature.

```vb
  //---------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\api\weldment_box3.sldprt.
 // 2. Open an Immediate window.
 //
 // Postconditions: Inspect the Immediate window.
  //----------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace GetWeldmentTrimExtendCornerType_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModel;
         Feature swFeature;
         WeldmentTrimExtendFeatureData swWeldmentTrimExtend;

         public void Main()
         {
             swModel = (ModelDoc2)swApp.ActiveDoc;

             //Traverse FeatureManager design tree
             //Get first feature in FeatureManager design tree
             swFeature = (Feature)swModel.FirstFeature();

             //If the type of feature is "WeldCornerFeat" then get the
             //WeldmentTrimExtendFeatureData object and then get the type of corner
             while ((swFeature != null))
             {
                 if (swFeature.GetTypeName() == "WeldCornerFeat")
                 {
                     Debug.Print(swFeature.Name);
                     swWeldmentTrimExtend = (WeldmentTrimExtendFeatureData)swFeature.GetDefinition();
                     Debug.Print(swWeldmentTrimExtend.CornerType.ToString());
                 }

                 //Get the next feature in the FeatureManager design tree
                 swFeature = (Feature)swFeature.GetNextFeature();
             }

         }

         public SldWorks swApp;
     }
 }
```
