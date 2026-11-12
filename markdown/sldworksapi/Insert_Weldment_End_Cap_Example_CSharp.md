---
title: "Insert Weldment End Cap Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Weldment_End_Cap_Example_CSharp.htm"
---

# Insert Weldment End Cap Example (C#)

This example shows how to create an end cap on the open face of a structural member.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\api\weldment_box3.sldprt.
 // 2. Open an Immediate window.
 //
 // Postconditions:
 // 1. Deletes End cap1.
 // 2. Inserts End cap3 in the FeatureManager design tree.
 // 3. Inspect the Immediate window.
 //
 // NOTE: Because the model is used elsewhere, do not save changes.
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
 namespace InsertEndCap_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         Feature myFeature;
         ModelDoc2 Part;
         EndCapFeatureData swEndCap;
         bool boolstatus;

         public void Main()
         {
             Part = (ModelDoc2)swApp.ActiveDoc;

             boolstatus = Part.Extension.SelectByID2("End cap1", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
             Part.EditDelete();

             Part.ViewZoomTo2(0.632542197290199, 0.972121141705638, 0.0346184961022406, 1.1852319686392, 0.619681287512073, 0.0346184961022431);

             boolstatus = Part.Extension.SelectByID2("", "FACE", 0.58771345904097, 0.614999999999952, -1.01293869257864,  true, 0,  null, 0);
             boolstatus = Part.Extension.SelectByID2("", "FACE", -0.0124763445314215, 0.614999999999839, -1.0014248149476,  true, 0,  null, 0);

             myFeature = Part.FeatureManager.InsertEndCapFeature3(0.005, false, false, 0.003, 0.6, 0.003, true, 0.002, false, 2);

             swEndCap = (EndCapFeatureData)myFeature.GetDefinition();

             Debug.Print("File = " + Part.GetPathName());
             Debug.Print("  " + myFeature.Name);
             Debug.Print("    Chamfer distance or fillet radius                      = " + swEndCap.ChamferDistance * 1000.0 +  " mm");
             Debug.Print("    Inset distance                                         = " + swEndCap.DepthDistance * 1000.0 +  " mm");
             Debug.Print("    Thickness direction (0=outward, 1=inward, 2=inset)     = " + swEndCap.IsEndCapInward);
             Debug.Print("    Offset distance                                        = " + swEndCap.OffsetDistance * 1000.0 +  " mm");
             Debug.Print("    Thickness of end cap                                   = " + swEndCap.Thickness * 1000.0 + " mm");
             Debug.Print("    Thickness ratio for offset                             = " + swEndCap.ThicknessRatioForOffset);
             Debug.Print("    Chamfer corners                                        = " + swEndCap.UseChamferCorners);
             Debug.Print("    Apply corner treatment                                 = " + swEndCap.UseCornerTreatment);
             Debug.Print("    Reverse offset                                         = " + swEndCap.UseReverse);
             Debug.Print("    Use thickness ratio for offset                         = " + swEndCap.UseThicknessRatioForOffset);

         }

         public SldWorks swApp;

     }

 }
```
