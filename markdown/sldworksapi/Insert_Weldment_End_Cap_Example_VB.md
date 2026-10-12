---
title: "Insert Weldment End Cap Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Weldment_End_Cap_Example_VB.htm"
---

# Insert Weldment End Cap Example (VBA)

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
Dim swApp As SldWorks.SldWorks
 Dim myFeature As SldWorks.Feature
 Dim Part As SldWorks.ModelDoc2
 Dim swEndCap As SldWorks.EndCapFeatureData
 Dim boolstatus As Boolean
Option Explicit
 Sub main()
    Set swApp = Application.SldWorks
     Set Part = swApp.ActiveDoc

    boolstatus = Part.Extension.SelectByID2("End cap1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
     Part.EditDelete

    Part.ViewZoomTo2 0.632542197290199, 0.972121141705638, 3.46184961022406E-02, 1.1852319686392, 0.619681287512073, 3.46184961022431E-02

    boolstatus = Part.Extension.SelectByID2("", "FACE", 0.58771345904097, 0.614999999999952, -1.01293869257864, True, 0, Nothing, 0)
     boolstatus = Part.Extension.SelectByID2("", "FACE", -1.24763445314215E-02, 0.614999999999839, -1.0014248149476, True, 0, Nothing, 0)

     Set myFeature = Part.FeatureManager.InsertEndCapFeature3(0.005, False, False, 0.003, 0.6, 0.003, True, 0.002, False, 2)
    Set swEndCap = myFeature.GetDefinition

    Debug.Print "File = " & Part.GetPathName
     Debug.Print "  " & myFeature.Name
     Debug.Print "    Chamfer distance or fillet radius                  = " & swEndCap.ChamferDistance * 1000# & " mm"
     Debug.Print "    Inset distance                                     = " & swEndCap.DepthDistance * 1000# & " mm"
     Debug.Print "    Thickness direction (0=outward, 1=inward, 2=inset) = " & swEndCap.IsEndCapInward
     Debug.Print "    Offset distance                                    = " & swEndCap.OffsetDistance * 1000# & " mm"
     Debug.Print "    Thickness of end cap                               = " & swEndCap.Thickness * 1000# & " mm"
     Debug.Print "    Thickness ratio for offset                         = " & swEndCap.ThicknessRatioForOffset
     Debug.Print "    Chamfer corners                                    = " & swEndCap.UseChamferCorners
     Debug.Print "    Apply corner treatment                             = " & swEndCap.UseCornerTreatment
     Debug.Print "    Reverse offset                                     = " & swEndCap.UseReverse
     Debug.Print "    Use thickness ratio for offset                     = " & swEndCap.UseThicknessRatioForOffset

End Sub
```
