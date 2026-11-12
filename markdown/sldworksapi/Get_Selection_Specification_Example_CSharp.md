---
title: "Get Selection Specification Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Selection_Specification_Example_CSharp.htm"
---

# Get Selection Specification Example (C#)

This example shows how to get the selection specification of a selected object.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
  // 1. Open a model document that contains at least two features.
 // 2. Select two features in the FeatureManager design tree.
 // 3. Open an Immediate window.
 //
 // Postconditions:
  // 1. Gets the selection specifications of the first and second selections.
 // 2. Inspect the Immediate window.
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
 namespace GetSelectionSpecification_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Part;
         SelectionMgr SelMgr;
         Feature selObject;
         string selectByString;
         string objectTypeStr;
         int objectTypeInt;
         double X;
         double Y;
         double Z;

         public void Main()
         {
             Part = (ModelDoc2)swApp.ActiveDoc;
             SelMgr = (SelectionMgr)Part.SelectionManager;

             // Get the selection specification of the first selected object
             selObject = (Feature)SelMgr.GetSelectedObject6(1, -1);
             SelMgr.GetSelectByIdSpecification(selObject, out selectByString, out objectTypeStr, out objectTypeInt);
             Debug.Print("Name of selected feature: " + selectByString);
             Debug.Print("Type of object: " + objectTypeStr);
             Debug.Print("Type of object as defined in swSelectType_e: " + objectTypeInt);

             Debug.Print("");

             // Get the selection specification of the selected object in position 2 of the selection list
             SelMgr.GetSelectionSpecification(2, out selectByString, out objectTypeStr, out objectTypeInt, out X, out Y, out Z);
             Debug.Print("Name of selected feature: " + selectByString);
             Debug.Print("Type of object: " + objectTypeStr);
             Debug.Print("Type of object as defined in swSelectType_e: " + objectTypeInt);
             Debug.Print("X Coordinate: " + X);
             Debug.Print("Y Coordinate: " + Y);
             Debug.Print("Z Coordinate: " + Z);

         }

         public SldWorks swApp;

     }
 }
```
