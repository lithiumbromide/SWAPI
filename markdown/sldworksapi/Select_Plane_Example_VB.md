---
title: "Select Plane Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Plane_Example_VB.htm"
---

# Select Plane Example (VBA)

This example shows how to select the default Right Plane.

```vb
 '---------------------------------------------------------
 ' Preconditions: Open a new part document.
 '
 ' Postconditions:
 ' 1. Selects the Right Plane.
 ' 2. Examine the graphics area.
 '---------------------------------------------------------
Option Explicit
Sub main()
    ' Select Right Plane (1-based index)
     Const ReqPlane              As Long = 3

     Dim swApp                   As SldWorks.SldWorks
     Dim swModel                 As SldWorks.ModelDoc2
     Dim swFeat                  As SldWorks.Feature
     Dim PlaneCount              As Long
     Dim bRet                    As Boolean
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swFeat = swModel.FirstFeature
    Do While Not swFeat Is Nothing
         If "RefPlane" = swFeat.GetTypeName Then
             PlaneCount = PlaneCount + 1
            If ReqPlane = PlaneCount Then
                 bRet = swFeat.Select2(False, 0)
                 Exit Do
             End If
         End If
        Set swFeat = swFeat.GetNextFeature
     Loop
End Sub
```
