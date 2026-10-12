---
title: "Get DimXpert Extrude Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/Get_DimXpert_Extrude_Feature_Example_VB.htm"
---

# Get DimXpert Extrude Feature Example (VBA)

This example shows how to build a part and get attributes for the DimXpert Extrude feature.

```vb
'----------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\plate_ads_plusminus.sldprt.
' 2. Open the DimXpert toolbar from View > Toolbars.
' 3. Create the Extrude Feature:
'    a. Click Auto Dimension Scheme btton on the DimXpert toolbar.
'    b. Ensure that all feature filters are selected.
'    c. Click the green check mark to accept the settings.
' 4. Observe the following DimXpert features on the DimXpertManager tab:
'    Hole Pattern1 and Pocket1.
' 5. Open the Immediate window.
' 6. Ensure that the latest SOLIDWORKS DimXpert type library is loaded
'    in Tools > References.
'
' Postconditions: Compare the output in the Immediate window with
' the features displayed on the DimXpertManager tab of the Management Panel.
'
' NOTE: Because this part is used elsewhere, do not save changes.
'---------------------------------------------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelMgr As SldWorks.SelectionMgr
Dim swConfig As SldWorks.ConfigurationManager
Dim swFeature As SldWorks.feature
Dim swAnn As SldWorks.feature
Dim swSchema As SldWorks.DimXpertManager
Dim swDXPart As DimXpertPart
Dim featureType As swDimXpertFeatureType_e
Dim features As Variant
Dim appliedFeatures As Variant
Dim appliedAnnotations As Variant
Dim appliedAnnotation As DimXpertAnnotation
Dim feature As DimXpertFeature
Dim appliedFeature As DimXpertFeature
Dim msgStr As String
Dim msgStr2 As String
Dim msgStr3 As String
Dim msgStr4 As String
Dim n As Long
Dim o As Long
Dim p As Long
Dim boolstatus As Boolean
Sub main()
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc

    Set swModelDocExt = swModel.Extension
    Set swSelMgr = swModel.SelectionManager

    ' Get the default DimXpert schema using IModelDocExtension.DimXpertManager()

    Set swSchema = swModelDocExt.DimXpertManager("Default", True)

    ' Get IDimXpertPart from the IDimXpertManager
    Set swDXPart = swSchema.DimXpertPart

    Dim featCount As Long
    featCount = swDXPart.GetFeatureCount
    msgStr = "Total of "
    msgStr2 = featCount
    msgStr = msgStr + msgStr2 + " DimXpert features in " + (swSchema.SchemaName)
    Debug.Print ""
    Debug.Print msgStr

    ' Get IDimXpert features through IDimXpertPart

    features = swDXPart.GetFeatures

    msgStr = (swSchema.SchemaName) + " has the following features: "
    Debug.Print ""
    Debug.Print msgStr
    For n = 0 To UBound(features)
        Set feature = features(n)
        Debug.Print "  " + "Feature name: " + (feature.Name)

        featureType = feature.Type
        Call GetPatternType(featureType, msgStr2)

        msgStr = "     Feature type "
        msgStr3 = " is suppressed on the DimXpertManager tab? "
        msgStr4 = feature.IsSuppressed()
        Debug.Print msgStr + msgStr2 + msgStr3 + msgStr4

        msgStr = "     " + "Model feature: "
        Set swFeature = feature.GetModelFeature()
        If Not (swFeature Is Nothing) Then
            msgStr2 = swFeature.GetTypeName2()
            Debug.Print msgStr + msgStr2
        End If

        msgStr = "     " + "Number of SOLIDWORKS face entities in this feature: "
        msgStr2 = feature.GetFaceCount
        Debug.Print msgStr + msgStr2

        msgStr = "     " + "Number of applied features: "
        msgStr2 = feature.GetAppliedFeatureCount()
        Debug.Print msgStr + msgStr2

        appliedFeatures = feature.GetAppliedFeatures()
        If Not (IsEmpty(appliedFeatures)) Then
            For o = 0 To UBound(appliedFeatures)
                Set appliedFeature = appliedFeatures(o)
                Debug.Print "        " + "Applied feature name: " + (appliedFeature.Name)
            Next
        End If

        msgStr = "     " + "Number of applied annotations: "
        msgStr2 = feature.GetAppliedAnnotationCount()
        Debug.Print msgStr + msgStr2

        appliedAnnotations = feature.GetAppliedAnnotations()
        If Not (IsEmpty(appliedAnnotations)) Then
            For p = 0 To UBound(appliedAnnotations)
                Set appliedAnnotation = appliedAnnotations(p)
                Debug.Print "        " + "Applied annotation name: " + (appliedAnnotation.Name)
            Next
        End If

        Debug.Print "     "
    Next

    ' If you know the name of a DimXpert feature, you can get it directly using IDimXpertPart.GetFeature("name"),
    ' which can return a general IDimXpertFeature or a more specific interface on the feature

    ' Get IDimXpertExtrudeFeature for the Pocket1 feature

    Dim extrudeFeature As IDimXpertExtrudeFeature
    Set extrudeFeature = swDXPart.GetFeature("Pocket1")
    msgStr = extrudeFeature.Name + " is a DimXpert extrude feature"
    Debug.Print ""
    Debug.Print msgStr
    Debug.Print ""

    ' Get the bottom blends
    Set feature = extrudeFeature.GetBottomBlends
    If Not feature Is Nothing Then
        msgStr = "The bottom blends for the extrude is "
        msgStr2 = feature.Name
        Debug.Print msgStr + msgStr2
    Else: Debug.Print "There are no bottom blends for this extrude."
    End If

    ' Get the bottom feature
    Set feature = extrudeFeature.GetBottomFeature
    If Not feature Is Nothing Then
        msgStr = "The bottom feature for the extrude is "
        msgStr2 = feature.Name
        Debug.Print msgStr + msgStr2
    End If

    ' Get the reference feature
    Set feature = extrudeFeature.GetReferenceFeature
    If Not feature Is Nothing Then
        msgStr = "The reference feature for the extrude is "
        msgStr2 = feature.Name
        Debug.Print msgStr + msgStr2
    End If

    ' Get the sub-features
    Dim featureCount As Integer
    featureCount = extrudeFeature.GetSubFeatureCount
    msgStr = "The number of sub-features of the extrude is "
    msgStr2 = featureCount
    Debug.Print msgStr + msgStr2

     features = extrudeFeature.GetSubFeatures
     For n = 0 To UBound(features)
        Set feature = features(n)
        Debug.Print "  " + "Feature name: " + (feature.Name)

        featureType = feature.Type
        Call GetPatternType(featureType, msgStr2)

        msgStr = "     Feature type is "

        Debug.Print msgStr + msgStr2
    Next

    ' Get whether the extrude is blind
    boolstatus = extrudeFeature.Blind
    msgStr = "The extrude is blind: "
    msgStr2 = boolstatus
    Debug.Print msgStr + msgStr2

End Sub
Public Sub GetPatternType(ByRef featureType, ByRef msgStr2)
    If (featureType = swDimXpertFeature_Plane) Then
            msgStr2 = "Plane"
    ElseIf (featureType = swDimXpertFeature_Cylinder) Then
            msgStr2 = "Cylinder"
    ElseIf (featureType = swDimXpertFeature_Cone) Then
            msgStr2 = "Cone"
    ElseIf (featureType = swDimXpertFeature_Extrude) Then
            msgStr2 = "Extrude"
    ElseIf (featureType = swDimXpertFeature_Fillet) Then
            msgStr2 = "Fillet"
    ElseIf (featureType = swDimXpertFeature_Chamfer) Then
            msgStr2 = "Chamfer"
    ElseIf (featureType = swDimXpertFeature_CompoundHole) Then
            msgStr2 = "CompoundHole"
    ElseIf (featureType = swDimXpertFeature_CompoundWidth) Then
            msgStr2 = "CompoundWidth"
    ElseIf (featureType = swDimXpertFeature_CompoundNotch) Then
            msgStr2 = "CompoundNotch"
    ElseIf (featureType = swDimXpertFeature_CompoundClosedSlot3D) Then
            msgStr2 = "CompoundClosedSlot3D"
    ElseIf (featureType = swDimXpertFeature_IntersectPoint) Then
            msgStr2 = "IntersectPoint"
    ElseIf (featureType = swDimXpertFeature_IntersectLine) Then
            msgStr2 = "IntersectLine"
    ElseIf (featureType = swDimXpertFeature_IntersectCircle) Then
            msgStr2 = "IntersectCircle"
    ElseIf (featureType = swDimXpertFeature_IntersectPlane) Then
            msgStr2 = "IntersectPlane"
    ElseIf (featureType = swDimXpertFeature_Pattern) Then
            msgStr2 = "Pattern"
    ElseIf (featureType = swDimXpertFeature_Sphere) Then
            msgStr2 = "Sphere"
    ElseIf (featureType = swDimXpertFeature_BestfitPlane) Then
            msgStr2 = "Bestfit Plane"
    ElseIf (featureType = swDimXpertFeature_Surface) Then
            msgStr2 = "Surface"
    End If

End Sub
```
