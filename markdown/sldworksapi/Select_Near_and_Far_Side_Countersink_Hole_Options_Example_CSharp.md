---
title: "Select Near and Far Side Hole Wizard Countersink Features Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Near_and_Far_Side_Countersink_Hole_Options_Example_CSharp.htm"
---

# Select Near and Far Side Hole Wizard Countersink Features Example (C#)

This example shows how to select near and far side Hole Wizard countersink features.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a part that contains a Hole Wizard hole named, Hole1.
 // 2. Modify the countersink diameter and angle values as required by Hole1.
 // 3. Open an Immediate window.
 //
 // Postconditions:
 // 1. Inspect the Immediate window.
 // 2. The current near side countersink option is displayed.
 // 3. The current far side countersink option is displayed.
 // 4. The near side countersink option is toggled.
 //    If the near side countersink option is selected,
 //    the proper angle and diameter are set.
 // 5. The far side countersink option is toggled.
 //    If the far side countersink option is selected,
 //    the proper angle and diameter are set.
 // 6. The new near side countersink option is displayed.
 // 7. The new far side countersink option is displayed.
 // ---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 namespace NearFarCounterSink_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModel;
         WizardHoleFeatureData2 FeatureData;
         Feature Feature;
         ModelDocExtension swModelDocExt;
         SelectionMgr swSelMgr;

         bool boolstatus;

         public void Main()
         {
             swModel = (ModelDoc2)swApp.ActiveDoc;
             swModelDocExt = swModel.Extension;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;

             swModel.ClearSelection2(true);

             boolstatus = swModelDocExt.SelectByID2("Hole1", "BODYFEATURE", 0, 0, 0, false, 0, null, (int)swSelectOption_e.swSelectOptionDefault);
             Feature = (Feature)swSelMgr.GetSelectedObject6(1, -1);
             FeatureData = (WizardHoleFeatureData2)Feature.GetDefinition();

             Debug.Print("Near side countersink option is selected: " + FeatureData.NearSideCounterSink);

             if ((FeatureData.NearSideCounterSink))
             {
                 FeatureData.NearSideCounterSink =  false;
             }
             else
             {
                 FeatureData.NearSideCounterSink =  true;
                 // near side countersink option is selected
                 FeatureData.NearCounterSinkDiameter = 0.0061;
                 // meters
                 FeatureData.NearCounterSinkAngle = 1.57;
                 // radians
             }

             Debug.Print("Far side countersink option is selected: " + FeatureData.FarSideCounterSink);

             if ((FeatureData.FarSideCounterSink))
             {
                 FeatureData.FarSideCounterSink =  false;
             }
             else
             {
                 FeatureData.FarSideCounterSink =  true;
                 // far side countersink option is selected
                 FeatureData.FarCounterSinkDiameter = 0.0061;
                 // meters
                 FeatureData.FarCounterSinkAngle = 1.57;
                 // radians
             }

             boolstatus = Feature.ModifyDefinition(FeatureData, swModel, null);
             FeatureData = (WizardHoleFeatureData2)Feature.GetDefinition();

             Debug.Print("Near side countersink option is selected: " + FeatureData.NearSideCounterSink);
             Debug.Print("Far side countersink option is selected: " + FeatureData.FarSideCounterSink);

         }

         public SldWorks swApp;

     }
 }
```
