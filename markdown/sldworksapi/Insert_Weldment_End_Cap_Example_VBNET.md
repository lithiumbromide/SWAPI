---
title: "Insert Weldment End Cap Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Weldment_End_Cap_Example_VBNET.htm"
---

# Insert Weldment End Cap Example (VB.NET)

This example shows how to create an end cap on the open face of a structural member.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\api\weldment_box3.sldprt.
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Deletes End cap1.
 ' 2. Inserts End cap3 in the FeatureManager design tree.
 ' 3. Inspect the Immediate window.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 ' ---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim myFeature As Feature
     Dim Part As ModelDoc2
     Dim swEndCap As EndCapFeatureData
     Dim boolstatus As Boolean

     Sub main()

         Part = swApp.ActiveDoc

         boolstatus = Part.Extension.SelectByID2("End cap1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
         Part.EditDelete()

         Part.ViewZoomTo2(0.632542197290199, 0.972121141705638, 0.0346184961022406, 1.1852319686392, 0.619681287512073, 0.0346184961022431)

         boolstatus = Part.Extension.SelectByID2("", "FACE", 0.58771345904097, 0.614999999999952, -1.01293869257864,  True, 0,  Nothing, 0)
         boolstatus = Part.Extension.SelectByID2("", "FACE", -0.0124763445314215, 0.614999999999839, -1.0014248149476,  True, 0,  Nothing, 0)

         myFeature = Part.FeatureManager.InsertEndCapFeature3(0.005, False, False, 0.003, 0.6, 0.003, True, 0.002, False, 2)

         swEndCap = myFeature.GetDefinition

         Debug.Print("File = " & Part.GetPathName)
         Debug.Print("  " & myFeature.Name)
         Debug.Print("    Chamfer distance or fillet radius                      = " & swEndCap.ChamferDistance * 1000.0#   " mm")
         Debug.Print("    Inset distance                                         = " & swEndCap.DepthDistance * 1000.0#   " mm")
         Debug.Print("    Thickness direction (0=outward, 1=inward, 2=inset)     = " & swEndCap.IsEndCapInward)
         Debug.Print("    Offset distance                                        = " & swEndCap.OffsetDistance * 1000.0#   " mm")
         Debug.Print("    Thickness of end cap                                   = " & swEndCap.Thickness * 1000.0# & " mm")
         Debug.Print("    Thickness ratio for offset                             = " & swEndCap.ThicknessRatioForOffset)
         Debug.Print("    Chamfer corners                                        = " & swEndCap.UseChamferCorners)
         Debug.Print("    Apply corner treatment                                 = " & swEndCap.UseCornerTreatment)
         Debug.Print("    Reverse offset                                         = " & swEndCap.UseReverse)
         Debug.Print("    Use thickness ratio for offset                         = " & swEndCap.UseThicknessRatioForOffset)

     End Sub

     Public swApp As SldWorks

 End  Class
```
