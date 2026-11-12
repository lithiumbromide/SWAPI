---
title: "Traverse All Cosmetic Threads Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Traverse_All_Cosmetic_Threads_Example_CSharp.htm"
---

# Traverse All Cosmetic Threads Example (C#)

This example shows how to traverse all cosmetic threads in a part and extract their data.

**NOTE**: In a part or assembly, a cosmetic thread is a subfeature of a hole or cut extrusion. Thus, you can traverse all of the cosmetic threads in a model using the IFeature traversal methods.

```vb
 //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\api\holecube.sldprt.
 // 2. Open an Immediate window.
 //
 // Postconditions:
 // 1. Creates a Helicoil Metric standard cosmetic thread.
 // 2. Examine the Immediate window.
 //
 // NOTE: Because the part is used elsewhere, do not save changes.
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

 namespace InsertCosmeticThread3_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             Feature swFeat = default(Feature);
             Feature swSubFeat = default(Feature);
             string sFeatType = null;
             CosmeticThreadFeatureData swCosThread = default(CosmeticThreadFeatureData);
             bool bRet = false;

             swModel = (ModelDoc2)swApp.ActiveDoc;

             bRet = swModel.Extension.SelectByID2("", "EDGE", -0.000802489357837999, -0.0246888176810671, 6.00726028778809E-05,  true, 0,  null, 0);
             swFeat = swModel.FeatureManager.InsertCosmeticThread3((int)swCosmeticStandardType_e.swStandardType_StandardHelicoilMetric, "Helicoil threads", "M33x2.0", 0.033, (int)swCosmeticEndConditions_e.swEndConditionBlind2Dia, 0.025, "M33x2.0 Helicoil Threads");

             Debug.Print("File = " + swModel.GetPathName());

             swFeat = (Feature)swModel.FirstFeature();

             while ((swFeat != null))
             {
                 swSubFeat = (Feature)swFeat.GetFirstSubFeature();
                 while ((swSubFeat != null))
                 {
                     sFeatType = swSubFeat.GetTypeName();

                     switch (sFeatType)
                     {

                         case "CosmeticThread":
                             Debug.Print("    " + swSubFeat.Name + " [" + sFeatType + "]");

                             swCosThread = (CosmeticThreadFeatureData)swSubFeat.GetDefinition();

                             Debug.Print("      ApplyThread      = " + swCosThread.ApplyThread);
                             Debug.Print("      BlindDepth       = " + swCosThread.BlindDepth * 1000.0 + " mm");
                             Debug.Print("      Diameter         = " + swCosThread.Diameter * 1000.0 + " mm");
                             Debug.Print("      DiameterType     = " + swCosThread.DiameterType);
                             Debug.Print("      ThreadCallout    = " + swCosThread.ThreadCallout);
                             Debug.Print("      ConfigurationOption as defined in swCosmeticConfigOptions_e = " + swCosThread.ConfigurationOption);
                             Debug.Print("      EndCondition as defined in swCosmeticEndConditions_e = " + swCosThread.EndCondition);
                             Debug.Print("      Size = " + swCosThread.Size);
                             Debug.Print("      Standard as defined in swCosmeticStandardType_e = " + swCosThread.Standard);
                             Debug.Print("      StandardType = " + swCosThread.StandardType);

                             Debug.Print("");

                             break;
                     }

                     swSubFeat = (Feature)swSubFeat.GetNextSubFeature();

                 }

                 swFeat = (Feature)swFeat.GetNextFeature();

             }

         }

         public SldWorks swApp;
     }
 }
```
