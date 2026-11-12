---
title: "Get Weldment Trim Extend Corner Type Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Weldment_Trim_Extend_Corner_Type_Example_VB.htm"
---

# Get Weldment Trim Extend Corner Type Example (VBA)

This example shows how to get the type of corner used for a weldment trim extend feature.

```vb
 '---------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\api\weldment_box3.sldprt.
 ' 2. Open an Immediate window.
 '
 ' Postconditions: Inspect the Immediate window.
 '----------------------------------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swFeature As SldWorks.Feature
 Dim swWeldmentTrimExtend As SldWorks.WeldmentTrimExtendFeatureData
Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc

    'Traverse FeatureManager design tree
     'Get first feature in FeatureManager design tree
     Set swFeature = swModel.FirstFeature

    'If the type of feature is "WeldCornerFeat" then get the
     'WeldmentTrimExtendFeatureData object and then get the type of corner
    Do While Not swFeature Is Nothing
         If swFeature.GetTypeName = "WeldCornerFeat" Then
             Debug.Print swFeature.Name
             Set swWeldmentTrimExtend = swFeature.GetDefinition
             Debug.Print swWeldmentTrimExtend.CornerType
         End If

        'Get the next feature in the FeatureManager design tree
         Set swFeature = swFeature.GetNextFeature
     Loop
End Sub
```
