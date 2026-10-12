---
title: "Get DimXpertManager Info Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_DimXpertManager_Info_Example_VB.htm"
---

# Get DimXpertManager Info Example (VBA)

This example shows the usage of several interfaces that provide access to information on the DimXpertManager tab of the Management Panel in SOLIDWORKS Design.

The IDimXpertManager interface exposes schema information on the DimXpertManager tab.

This macro demonstrates several ways of acquiring IDimXpertManager on an open document:

- ISelectionManager.GetSelectedObject6()
- IModelDocExtension.DimXpertManager
- IConfiguration.DimXpertManager

This macro also demonstrates how to get the features and annotations displayed on the DimXpertManager tab using:

- ISelectionManager.GetSelectedObject6()
- IDimXpertManager.DimXpertPart

'----------------------------------------------------------------------------
' Preconditions:
' 1. Open `public_documents`**\samples\tutorial\api\cover_with_geometric_tolerances.sldprt**.
' 2. Select the DimXpertManager tab in the Management Panel.
' 3. Open the Immediate window.
' 4. Add a reference to **SOLIDWORKS** `version` **DimXpert type library**.
'
' Postconditions: Inspect the Immediate Window.
'
' NOTE: Because this part is used elsewhere, do not save changes.
'----------------------------------------------------------------------------

```vb
Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swModel As IModelDoc2
 Dim swModelDocExt As IModelDocExtension
 Dim swSelMgr As ISelectionMgr
 Dim swConfig As IConfiguration
 Dim swFeature As IFeature
 Dim swAnn As IFeature
 Dim swSchema As IDimXpertManager
 Dim swDXPart As IDimXpertPart
 Dim msgStr As String
 Dim msgStr2 As String
 Dim displaytype As swDimXpertTreeDisplay_e
 Dim boolstatus As Boolean
 Dim n as Long

 Sub main()

     Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swModelDocExt = swModel.Extension
     Set swSelMgr = swModel.SelectionManager

     ' Select a DimXpert schema using swSelectType_e.swSelSWIFTSCHEMA type
     'boolstatus = swModelDocExt.SelectByID2("Scheme15", "SWIFTSCHEMA", 0, 0, 0, False, 0, Nothing, 0)
     ' Get IDimXpertManager (swSchema) for the DimXpert schema using ISelectionManager.GetSelectedObject6()
     'Set swSchema = swSelMgr.GetSelectedObject6(1, -1)
     'Debug.Print (swSchema.SchemaName) + " acquired through ISelectionManager"

     ' Get IDimXpertManager (swSchema) for a DimXpert schema using IModelDocExtension.DimXpertManager()
     Set swSchema = swModelDocExt.DimXpertManager("Default", True)
     Debug.Print (swSchema.SchemaName) + " acquired through IModelDocExtension"

     ' Get IDimXpertManager (swSchema) for a DimXpert schema using IConfiguration.DimXpertManager()
     Set swConfig = swModel.GetConfigurationByName("Default")
     Set swSchema = swConfig.DimXpertManager(True)
     Debug.Print (swSchema.SchemaName) + " acquired through IConfiguration"

     msgStr = (swSchema.SchemaName) + " shows a "
     displaytype = swSchema.TreeDisplay
     Debug.Print ""

         If (displaytype = swDimXpertTreeDisplay_Flat) Then
             Debug.Print msgStr + "flat display of information on DimXpert tab"

         ElseIf (displaytype = swDimXpertTreeDisplay_Annotation) Then
             Debug.Print msgStr + "annotation-based display of information on DimXpert tab"

         ElseIf (displaytype = swDimXpertTreeDisplay_Feature) Then
             Debug.Print msgStr + "feature-based display of information on DimXpert tab"

         End If

     ' Select a DimXpert annotation using swSelectType_e.swSelSWIFTANNOTATIONS type
     boolstatus = swModelDocExt.SelectByID2("Flatness1", "SWIFTANN", 0, 0, 0, False, 0, Nothing, 0)
     ' All DimXpert features and annotations returned by GetSelectedObject6 are instances of IFeature
     Set swAnn = swSelMgr.GetSelectedObject6(1, -1)

     ' Is Flatness1 an annotation or a feature?
     If (swAnn.IsDimXpertAnnotation()) Then
         msgStr = "Flatness1 is an annotation"
         Debug.Print ""
         Debug.Print msgStr
     ElseIf (swAnn.IsDimXpertFeature()) Then
         msgStr = "Flatness1 is a feature"
         Debug.Print ""
         Debug.Print msgStr
     End If

     ' Get all DimXpert features and annotations using DimXpertPart
     Set swDXPart = swSchema.DimXpertPart

     ' Display all DimXpert annotations using IDimXpertManager.DimXpertPart

     Dim annCount As Long
     annCount = swDXPart.GetAnnotationCount
     msgStr = "Total of "
     msgStr2 = annCount
     msgStr = msgStr + msgStr2 + " annotations in " + (swSchema.SchemaName)
     Debug.Print ""
     Debug.Print msgStr

     Dim annotations As Variant
     Dim annotation As IDimXpertAnnotation
     annotations = swDXPart.GetAnnotations

     msgStr = (swSchema.SchemaName) + " has the following annotations: "
     Debug.Print ""
     Debug.Print msgStr
     For n = 0 To UBound(annotations)
         Set annotation = annotations(n)
         Debug.Print "  " + (annotation.Name)
     Next

     ' Select another DimXpert feature using swSelectType_e.swSelSWIFTFEATURES type
     boolstatus = swModelDocExt.SelectByID2("Plane1", "SWIFTFEATURE", 0, 0, 0, False, 0, Nothing, 0)
     Set swFeature = swSelMgr.GetSelectedObject6(1, -1)

     ' Is Plane1 an annotation or a feature?
     If (swFeature.IsDimXpertFeature()) Then
         msgStr = "Plane1 is a feature"
         Debug.Print ""
         Debug.Print msgStr
     ElseIf (swFeature.IsDimXpertAnnotation()) Then
         msgStr = "Flatness1 is an annotation"
         Debug.Print msgStr
     End If

     ' Display all DimXpert features using IDimXpertManager.DimXpertPart

     Dim featCount As Long
     featCount = swDXPart.GetFeatureCount
     msgStr = "Total of "
     msgStr2 = featCount
     msgStr = msgStr + msgStr2 + " features in " + (swSchema.SchemaName)
     Debug.Print ""
     Debug.Print msgStr

     Dim features As Variant
     Dim feature As IDimXpertFeature
     features =  swDXPart.GetFeatures

     msgStr = (swSchema.SchemaName) + " has the following features: "
     Debug.Print ""
     Debug.Print msgStr
     For n = 0 To UBound(features)
         Set feature = features(n)
         Debug.Print "  " + (feature.Name)
     Next
End Sub
```
