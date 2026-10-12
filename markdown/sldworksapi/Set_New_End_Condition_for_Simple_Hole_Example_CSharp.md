---
title: "Set New End Condition for Simple Hole Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_New_End_Condition_for_Simple_Hole_Example_CSharp.htm"
---

# Set New End Condition for Simple Hole Feature Example (C#)

This example shows how to set a new end condition for a simple hole feature.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a part document containing a block with a simple hole feature named
 /     Hole1.
 // 2. Select the bottom face of the block.
 // 3. Open the Immediate window.
 //
 // Postconditions:
 // 1. Sets the bottom face of the block as the new end condition
 //    of the simple hole feature.
 // 2. Examine the Immediate window.
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
 namespace SimpleHoleFeatureData_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Model;
         SelectionMgr SelMgr;
         Feature SimpleHoleFeature;
         SimpleHoleFeatureData2 SimpleHoleFeature_DEF;
         Face2 bottomFace;
         Face2 SimpleHoleEndCondition;

         bool boolstatus;

         public void Main()
         {
             Model = (ModelDoc2)swApp.ActiveDoc;
             SelMgr = (SelectionMgr)Model.SelectionManager;

             bottomFace = (Face2)SelMgr.GetSelectedObject6(1, -1);

             boolstatus = Model.Extension.SelectByID2("Hole1", "BODYFEATURE", 0, 0, 0, false, 0, null, (int)swSelectOption_e.swSelectOptionDefault);
             SimpleHoleFeature = (Feature)SelMgr.GetSelectedObject6(1, -1);

             SimpleHoleFeature_DEF = (SimpleHoleFeatureData2)SimpleHoleFeature.GetDefinition();
             SimpleHoleFeature_DEF.AccessSelections(Model,  null);

             int SimpleHoleType = 0;

             // Print the type of hole
             SimpleHoleType = SimpleHoleFeature_DEF.Type;
             Debug.Print("Hole type: " + SimpleHoleType);

             // If the end condition is blind, no reference is returned
             SimpleHoleEndCondition = (Face2)SimpleHoleFeature_DEF.GetEndConditionReference(out SimpleHoleType);

             SimpleHoleFeature_DEF.Type = (int)swEndConditions_e.swEndCondUpToSurface;
             SimpleHoleFeature_DEF.SetEndConditionReference(bottomFace);
             SimpleHoleFeature.ModifyDefinition(SimpleHoleFeature_DEF, Model, null);
             SimpleHoleFeature_DEF.AccessSelections(Model,  null);

             // Print the type of hole
             SimpleHoleType = SimpleHoleFeature_DEF.Type;
             Debug.Print("Hole type after setting end condition: " + SimpleHoleType);

             // The end condition is not blind, so a reference is returned
             SimpleHoleEndCondition = (Face2)SimpleHoleFeature_DEF.GetEndConditionReference(out SimpleHoleType);
             Debug.Print("End condition face ID: " + SimpleHoleEndCondition.GetFaceId());

             SimpleHoleFeature_DEF.ReleaseSelectionAccess();

         }

         public SldWorks swApp;

     }
 }
```
