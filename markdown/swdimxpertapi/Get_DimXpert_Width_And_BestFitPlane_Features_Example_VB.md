---
title: "Get DimXpert Compound Width and Best Fit Plane Features Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/Get_DimXpert_Width_And_BestFitPlane_Features_Example_VB.htm"
---

# Get DimXpert Compound Width and Best Fit Plane Features Example (VBA)

This example shows how to build a part and get attributes for the following DimXpert features:

* Compound width

* Best fit plane

```vb
'---------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\block.sldprt.
' 2. Open the DimXpert toolbar from View > Toolbars.
' 3. Create the best fit plane feature:
'    a. Click the Location Dimension icon on the DimXpert toolbar.
'    b. Select the left front face of the block.
'    c. Click the Compound Plane icon on the DimXpert pop up toolbar.
'    d. Select the right front face of the block.
'    e. Click the green check mark on the DimXpert pop up toolbar.
'    f. Select the back face of the block.
'    g. Click to place the location dimension annotation.
' 4. Create the compound width feature:
'    a. Click the Size Dimension icon on the DimXpert toolbar.
'    b. Select a front face of the block.
'    c. Click the Width icon on the DimXpert pop up toolbar.
'    d. Select the back face of the block.
'    e. Click the green check mark on the DimXpert pop up toolbar.
'    f. Click to place the size dimension annotation.
' 5. Observe the following DimXpert features on the DimXpertManager tab:
'    Plane2, Plane3, Width1.
' 6. Open an Immediate window.
' 7. Ensure that the latest SOLIDWORKS DimXpert type library is loaded
'    in Tools > References.
'
' Postconditions: Compare the output in the Immediate Window
' with the features displayed on the DimXpertManager tab of the
' Management Panel.
'
' NOTE: Because this part is used elsewhere, o not save changes.
'------------------------------------------------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks
Dim swModel As ModelDoc2
Dim swModelDocExt As ModelDocExtension
Dim swSelMgr As SelectionMgr
Dim swConfig As Configuration
Dim swFeature As feature
Dim swAnn As feature
Dim swSchema As DimXpertManager
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

    ' Get IDimXpertCompoundWidthFeature for the Width1 feature

    Dim widthFeature As IDimXpertCompoundWidthFeature
    Set widthFeature = swDXPart.GetFeature("Width1")
    msgStr = widthFeature.Name + " is a DimXpert Width feature"
    Debug.Print ""
    Debug.Print msgStr
    Debug.Print ""

    ' Get the nominal width coordinates

    Dim width As Double
    Dim x As Double
    Dim y As Double
    Dim z As Double
    Dim i As Double
    Dim j As Double
    Dim k As Double

    Debug.Print "Nominal width of Width1"
    Debug.Print ""
     boolstatus = widthFeature.GetNominalCompoundWidth(width, x, y, z, i, j, k)
    msgStr = "Width is "
    msgStr2 = width
    Debug.Print msgStr + msgStr2
    msgStr = "X-coordinate is "
    msgStr2 = x
    Debug.Print msgStr + msgStr2
    msgStr = "Y-coordinate is "
    msgStr2 = y
    Debug.Print msgStr + msgStr2
    msgStr = "Z-coordinate is "
    msgStr2 = z
    Debug.Print msgStr + msgStr2
    msgStr = "I-component of pierce vector is "
    msgStr2 = i
    Debug.Print msgStr + msgStr2
    msgStr = "J-component of pierce vector is "
    msgStr2 = j
    Debug.Print msgStr + msgStr2
    msgStr = "K-component of pierce vector is "
    msgStr2 = k
    Debug.Print msgStr + msgStr2
    Debug.Print ""

    ' Get whether the width is a hole or a pin

    boolstatus = widthFeature.Inner
    msgStr = "The width is for a hole and not a pin: "
    msgStr2 = boolstatus
    Debug.Print msgStr + msgStr2

    ' Get IDimXpertBestfitPlaneFeature for the Plane2 feature

    Dim bestfitPlaneFeature As IDimXpertBestfitPlaneFeature
    Set bestfitPlaneFeature = swDXPart.GetFeature("Plane2")
    msgStr = bestfitPlaneFeature.Name + " is a DimXpert Bestfit Plane feature"
    Debug.Print ""
    Debug.Print msgStr
    Debug.Print ""

    Dim featureCount As Integer
    featureCount = bestfitPlaneFeature.GetSubFeatureCount
    msgStr = "The number of sub-features of the bestfit plane is "
    msgStr2 = featureCount
    Debug.Print msgStr + msgStr2

    features = bestfitPlaneFeature.GetSubFeatures
    For n = 0 To UBound(features)
        Set feature = features(n)
        Debug.Print "  " + "Feature name: " + (feature.Name)

        featureType = feature.Type
        Call GetPatternType(featureType, msgStr2)

        msgStr = "     Feature type is "

        Debug.Print msgStr + msgStr2
    Next

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
