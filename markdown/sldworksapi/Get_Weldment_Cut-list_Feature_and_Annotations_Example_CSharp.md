---
title: "Get Weldment Cut List Feature and Annotations Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Weldment_Cut-list_Feature_and_Annotations_Example_CSharp.htm"
---

# Get Weldment Cut List Feature and Annotations Example (C#)

This example shows how to get a weldment cut list feature and weldment cut list annotations.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a Drawing document that has a weldment cut list table.
 // 2. Open an Immediate window.
 //
 // Postconditions: Inspect the Immediate window.
  //----------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace GetWeldmentCutListFeature_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModel;
         Feature swFeature;
         WeldmentCutListFeature swWeldmentCutListFeat;
         object[] vWeldCutListAnnotations;
         object[] vCustProperties;
         int i;
         int j;

         public void Main()
         {
             swModel = (ModelDoc2)swApp.ActiveDoc;

             // Traverse FeatureManager design tree
             // Get first feature in FeatureManager design tree
             swFeature = (Feature)swModel.FirstFeature();

             // If the type of feature is "WeldmentTableFeat"
             // then get the WeldmentCutListFeature object
             while ((swFeature != null))
             {

                 if (swFeature.GetTypeName() == "WeldmentTableFeat")
                 {
                     Debug.Print(swFeature.Name);
                     swWeldmentCutListFeat = (WeldmentCutListFeature)swFeature.GetSpecificFeature2();
                     Debug.Print("   Name of configuration:    " + swWeldmentCutListFeat.Configuration);
                     Debug.Print("   Keep missing items:       " + swWeldmentCutListFeat.KeepCurrentItemNumbers);
                     Debug.Print("   Strikeout missing items:  " + swWeldmentCutListFeat.StrikeoutMissingItems);
                     Debug.Print("   Starting sequence number: " + swWeldmentCutListFeat.SequenceStartNumber);

                     // Get the weldment cut list annotations
                     vWeldCutListAnnotations = (object[])swWeldmentCutListFeat.GetTableAnnotations();
                     for (i = vWeldCutListAnnotations.GetLowerBound(0); i <= vWeldCutListAnnotations.GetUpperBound(0); i++)
                     {
                         // Print the number custom properties and then the custom properties
                         Debug.Print("   Number of custom properties: " + ((WeldmentCutListAnnotation)vWeldCutListAnnotations[i]).GetAllCustomPropertiesCount());
                         vCustProperties = (object[])((WeldmentCutListAnnotation)vWeldCutListAnnotations[i]).GetAllCustomProperties();
                         for (j = vCustProperties.GetLowerBound(0); j <= vCustProperties.GetUpperBound(0); j++)
                         {
                             Debug.Print("        Custom property: " + vCustProperties[j]);
                         }
                     }
                 }

                 // Get the next feature in the FeatureManager design tree
                 swFeature = (Feature)swFeature.GetNextFeature();

             }

         }

         public SldWorks swApp;

     }
 }
```
