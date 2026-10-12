---
title: "Get Weldment Trim Extend Corner Type Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Weldment_Trim_Extend_Corner_Type_Example_VBNET.htm"
---

# Get Weldment Trim Extend Corner Type Example (VB.NET)

This example shows how to get the type of corner used for a weldment trim extend feature.

```vb
  '---------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\api\weldment_box3.sldprt.
 ' 2. Open an Immediate window.
 '
 ' Postconditions: Inspect the Immediate window.
  '----------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim swFeature As Feature
     Dim swWeldmentTrimExtend As WeldmentTrimExtendFeatureData

     Sub main()

         swModel = swApp.ActiveDoc

         'Traverse FeatureManager design tree
         'Get first feature in FeatureManager design tree
         swFeature = swModel.FirstFeature

         'If the type of feature is "WeldCornerFeat" then get the
         'WeldmentTrimExtendFeatureData object and then get the type of corner
         Do While Not swFeature Is Nothing
             If swFeature.GetTypeName = "WeldCornerFeat" Then
                 Debug.Print(swFeature.Name)
                 swWeldmentTrimExtend = swFeature.GetDefinition
                 Debug.Print(swWeldmentTrimExtend.CornerType)
             End If

             'Get the next feature in the FeatureManager design tree
             swFeature = swFeature.GetNextFeature
         Loop

     End Sub

     Public swApp As SldWorks

 End Class
```
