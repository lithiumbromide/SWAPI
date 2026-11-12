---
title: "Create Derived or Underived Sketch Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Derived_or_Underived_Sketch_Example_CSharp.htm"
---

# Create Derived or Underived Sketch Example (C#)

This example shows how to create a derived or underived sketch.

```vb
 //--------------------------------------------------------------
 // Preconditions:
 // 1. Open a part that contains at least one sketch.
 // 2. Select a sketch.
 // 3. Open the Immediate window.
 //
 // Postconditions:
 // 1. If the selected sketch is not derived, then a
 //    derived sketch is created.
 //    - or -
 //    If the selected sketch is derived, then the
 //    sketch is changed to underived.
 // 2. Examine the FeatureManager design tree and Immediate
 //    window.
 //--------------------------------------------------------------
using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;
 namespace DeriveSketch_CSharp.csproj
 {
     partial class SolidWorksMacro
     {
         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             SelectionMgr swSelMgr = default(SelectionMgr);
             Feature swFeat = default(Feature);
             Sketch swSketch = default(Sketch);

             swModel = (ModelDoc2)swApp.ActiveDoc;

             // Interactively select a sketch
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
             swSketch = (Sketch)swFeat.GetSpecificFeature2();

             // Is the selected sketch derived?
             Debug.Print("Is the selected sketch derived? " + swSketch.IsDerived());
             // If the selected sketch is a derived sketch,
             // then create a derived sketch; else, underive the
             // selected sketch
             if (swSketch.IsDerived())
             {
                 swModel.UnderiveSketch();
                 Debug.Print(" Selected sketch was derived; sketch is now underived.");
             }
             else
             {
                 swModel.DeriveSketch();
                 Debug.Print(" Selected sketch was not derived; a derived sketch has been created.");
             }
             swModel.ForceRebuild3(false);
         }
         public SldWorks swApp;
     }
 }
```
