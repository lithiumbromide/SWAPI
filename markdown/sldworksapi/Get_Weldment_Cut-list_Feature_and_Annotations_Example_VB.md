---
title: "Get Weldment Cut List Feature and Annotations Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Weldment_Cut-list_Feature_and_Annotations_Example_VB.htm"
---

# Get Weldment Cut List Feature and Annotations Example (VBA)

This example shows how to get a weldment cut list feature and weldment cut list annotations.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a drawing document that has a weldment cut list table.
 ' 2. Open an Immediate window.
 '
 ' Postconditions: Inspect the Immediate window.
 '----------------------------------------------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swFeature As SldWorks.Feature
 Dim swWeldmentCutListFeat As SldWorks.WeldmentCutListFeature
 Dim vWeldCutListAnnotations As Variant
 Dim vCustProperties As Variant
 Dim i As Long
 Dim j As Long

Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc

    ' Traverse FeatureManager design tree
     ' Get first feature in FeatureManager design tree
     Set swFeature = swModel.FirstFeature

    ' If the type of feature is "WeldmentTableFeat"
     ' then get the WeldmentCutListFeature object
     Do While Not swFeature Is Nothing

        If swFeature.GetTypeName = "WeldmentTableFeat" Then
            Debug.Print swFeature.Name
             Set swWeldmentCutListFeat = swFeature.GetSpecificFeature2
             Debug.Print "   Name of configuration:    " & swWeldmentCutListFeat.Configuration
             Debug.Print "   Keep missing items:       " & swWeldmentCutListFeat.KeepCurrentItemNumbers
             Debug.Print "   Strike out missing items:  " & swWeldmentCutListFeat.StrikeoutMissingItems
             Debug.Print "   Starting sequence number: " & swWeldmentCutListFeat.SequenceStartNumber
            ' Get the weldment cut list annotations
             vWeldCutListAnnotations = swWeldmentCutListFeat.GetTableAnnotations
             For i = LBound(vWeldCutListAnnotations) To UBound(vWeldCutListAnnotations)
                 ' Print the number custom properties and then the custom properties
                 Debug.Print "   Number of custom properties: " & vWeldCutListAnnotations(i).GetAllCustomPropertiesCount
                 vCustProperties = vWeldCutListAnnotations(i).GetAllCustomProperties
                 For j = LBound(vCustProperties) To UBound(vCustProperties)
                     Debug.Print "        Custom property: " & vCustProperties(j)
                 Next j
             Next i
         End If

        ' Get the next feature in the FeatureManager design tree
         Set swFeature = swFeature.GetNextFeature

    Loop
End Sub
```
