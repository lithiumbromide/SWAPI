---
title: "Get Weldment Cut List Feature and Annotations Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Weldment_Cut-list_Feature_and_Annotations_Example_VBNET.htm"
---

# Get Weldment Cut List Feature and Annotations Example (VB.NET)

This example shows how to get a weldment cut list feature and weldment cut list annotations.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a Drawing document that has a weldment cut list table.
 ' 2. Open an Immediate window.
 '
 ' Postconditions: Inspect the Immediate window.
  '----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim swFeature As Feature
     Dim swWeldmentCutListFeat As WeldmentCutListFeature
     Dim vWeldCutListAnnotations As Object
     Dim vCustProperties As Object
     Dim i As Integer
     Dim j As Integer

     Sub main()

         swModel = swApp.ActiveDoc

         ' Traverse FeatureManager design tree
         ' Get first feature in FeatureManager design tree
         swFeature = swModel.FirstFeature

         ' If the type of feature is "WeldmentTableFeat"
         ' then get the WeldmentCutListFeature object
         Do While Not swFeature Is Nothing

             If swFeature.GetTypeName = "WeldmentTableFeat" Then
                 Debug.Print(swFeature.Name)
                 swWeldmentCutListFeat = swFeature.GetSpecificFeature2
                 Debug.Print("   Name of configuration:    " & swWeldmentCutListFeat.Configuration)
                 Debug.Print("   Keep missing items:       " & swWeldmentCutListFeat.KeepCurrentItemNumbers)
                 Debug.Print("   Strikeout missing items:  " & swWeldmentCutListFeat.StrikeoutMissingItems)
                 Debug.Print("   Starting sequence number: " & swWeldmentCutListFeat.SequenceStartNumber)

                 ' Get the weldment cut list annotations
                 vWeldCutListAnnotations = swWeldmentCutListFeat.GetTableAnnotations
                 For i = LBound(vWeldCutListAnnotations) To UBound(vWeldCutListAnnotations)
                     ' Print the number custom properties and then the custom properties
                     Debug.Print("   Number of custom properties: " & vWeldCutListAnnotations(i).GetAllCustomPropertiesCount)
                     vCustProperties = vWeldCutListAnnotations(i).GetAllCustomProperties
                     For j = LBound(vCustProperties) To UBound(vCustProperties)
                         Debug.Print("        Custom property: " & vCustProperties(j))
                     Next j
                 Next i
             End If

             ' Get the next feature in the FeatureManager design tree
             swFeature = swFeature.GetNextFeature

         Loop

     End Sub

     Public swApp As SldWorks

 End Class
```
