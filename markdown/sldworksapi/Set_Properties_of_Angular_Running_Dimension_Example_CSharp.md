---
title: "Insert Angular Running Dimension Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Properties_of_Angular_Running_Dimension_Example_CSharp.htm"
---

# Insert Angular Running Dimension Example (C#)

This example shows how to insert an angular running dimension and get its properties.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\advdrawings\foodprocessor.slddrw.
 // 2. Open an Immediate window.
 //
 // Postconditions:
 // 1. The specified angular running dimension is inserted into the drawing.
 // 2. Inspect the Immediate window.
 //
 // NOTE: Because the model is used elsewhere, do not save changes to it.
 // ---------------------------------------------------------------------------

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;
 namespace AngularRunningDimensions_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 Part = default(ModelDoc2);
             SelectionMgr selmgr = default(SelectionMgr);
             DisplayDimension dispdim = default(DisplayDimension);
              object dispdimvar;
             bool boolstatus = false;
             int intstatus;

             Part = (ModelDoc2)swApp.ActiveDoc;

             boolstatus = Part.Extension.SelectByID2("", "EDGE", 0.163726736787323, 0.199115091463415, 0.00479999999993197,  true, 0, null, 0);
             boolstatus = Part.Extension.SelectByID2("", "EDGE", 0.220795425811714, 0.179644597560976, 0.00479999999998881,  true, 0, null, 0);

             dispdimvar = Part.Extension.AddAngularRunningDim(false, true, true, 0.154288188900673, 0.0794194886913027, 0,  out  intstatus);
             Part.Extension.ReJogRunningDimension();
             Part.Extension.AlignRunningDimension();

             Part.SetPickMode();

             boolstatus = Part.Extension.SelectByID2("D2@Sketch31@foodprocessor.SLDDRW", "DIMENSION", 0.0408612062995185, 0.166216670731707, 0,  false, 0, null, 0);
             selmgr = (SelectionMgr)Part.SelectionManager;
             dispdim = (DisplayDimension)selmgr.GetSelectedObject6(1, -1);

             Debug.Print("Display chained angular dimensions? " + dispdim.DisplayAsChain);
             Debug.Print("Run the angular dimensions bidirectionally? " + dispdim.RunBidirectionally);
             Debug.Print("Extend extension lines from center of angular running dimension? " + dispdim.ExtensionLineExtendsFromCenterOfSet);
             Debug.Print("Are extension lines jogged? " + dispdim.Jogged);
             Debug.Print("Extension line style same as leader line style? " + dispdim.ExtensionLineSameAsLeaderStyle);
             Debug.Print("Extension line uses document settings? " + dispdim.ExtensionLineUseDocumentDisplay);

         }

         public SldWorks swApp;

     }
 }
```
