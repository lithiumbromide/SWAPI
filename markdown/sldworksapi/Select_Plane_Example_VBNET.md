---
title: "Select Plane Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Plane_Example_VBNET.htm"
---

# Select Plane Example (VB.NET)

This example shows how to select the default Right Plane.

```vb
 '---------------------------------------------------------
 ' Preconditions: Open a new part document.
 '
 ' Postconditions:
 ' 1. Selects the Right Plane.
 ' 2. Examine the graphics area.
 '---------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Sub main()

         ' Select Right Plane (1-based index)
         Const ReqPlane As Long = 3

         Dim swModel As ModelDoc2
         Dim swFeat As Feature
         Dim PlaneCount As Long
         Dim bRet As Boolean

         swModel = swApp.ActiveDoc
         swFeat = swModel.FirstFeature

         Do While Not swFeat Is  Nothing
             If "RefPlane" = swFeat.GetTypeName Then
                 PlaneCount = PlaneCount + 1

                 If ReqPlane = PlaneCount Then
                     bRet = swFeat.Select2(False, 0)
                     Exit Do
                 End If
             End If

             swFeat = swFeat.GetNextFeature
         Loop

     End Sub

     Public swApp As SldWorks

 End  Class
```
