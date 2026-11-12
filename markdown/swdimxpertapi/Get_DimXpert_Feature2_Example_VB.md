---
title: "Get More DimXpert Feature Examples (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/Get_DimXpert_Feature2_Example_VB.htm"
---

# Get More DimXpert Feature Examples (VBA)

This example shows how to build and get attributes for the following DimXpert features:

* Hole

* Notch

```vb
'---------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\cover_with_dimensions.sldprt.
' 2. Open the DimXpert toolbar from View > Toolbars.
' 3. Observe the following DimXpert features on the DimXpertManager tab:
'    Simple Hole and, Notch1.
' 4. Open the Immediate window.
' 5. Ensure that the latest SOLIDWORKS DimXpert type library is loaded
'    in Tools > References.
' 6. Step through this macro (F8).
'
' Postconditions: Compare the output in the Immediate window
' with the features displayed on the DimXpertManager tab of the Management Panel.
'
' NOTE: Because this part is used elsewhere, do not save changes.
'--------------------------------------------------------------------------
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
Dim holeType As swDimXpertCompoundHoleType_e
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
    msgStr = msgStr + msgStr2 + " features in " + (swSchema.SchemaName)
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

    ' Get IDimXpertCompoundHoleFeature for the Simple Hole2 feature

    Dim holeFeature As IDimXpertCompoundHoleFeature
    Set holeFeature = swDXPart.GetFeature("Simple Hole2")
    msgStr = holeFeature.Name + " is a DimXpert feature"
        Debug.Print ""
        Debug.Print msgStr
    Debug.Print ""

    ' Get the bottom feature if one exists
    Dim bottomFeature As IDimXpertFeature
    Set bottomFeature = holeFeature.GetBottomFeature
    If Not (bottomFeature Is Nothing) Then
        msgStr = "Bottom feature is "
        msgStr2 = bottomFeature.Name
        Debug.Print msgStr + msgStr2
    End If

    ' Get the reference feature
    Dim refFeature As IDimXpertFeature
    Set refFeature = holeFeature.GetReferenceFeature
    msgStr = "Reference feature for dimensioning is "
    msgStr2 = refFeature.Name
    Debug.Print msgStr + msgStr2

    ' Get the sub-feature count
    Dim count As Integer
    count = holeFeature.GetSubFeatureCount
    msgStr = "Number of subfeatures is "
    msgStr2 = count
    Debug.Print msgStr + msgStr2

' Get the sub-features
    Dim subfeatures As Variant
    subfeatures = holeFeature.GetSubFeatures
    For n = 0 To UBound(subfeatures)
        Set feature = subfeatures(n)
        Debug.Print "  " + "Sub-feature name: " + (feature.Name)
    Next

    ' Get whether the hole is blind
    msgStr = "Hole feature is blind and not through: "
    msgStr2 = holeFeature.Blind
    Debug.Print msgStr + msgStr2

    ' Get the type of the hole
    holeType = holeFeature.CompoundHoleType
    msgStr = "Hole feature is type: "
    Call GetHoleType(holeType, msgStr2)
    Debug.Print msgStr + msgStr2

    ' Get IDimXpertCompoundNotchFeature for the Notch1 feature

    Dim notchFeature As IDimXpertCompoundNotchFeature
    Set notchFeature = swDXPart.GetFeature("Notch1")
    msgStr = notchFeature.Name + " is a DimXpert feature"
        Debug.Print ""
        Debug.Print msgStr
    Debug.Print ""

    ' Get the nominal notch coordinates

    Dim width As Double
    Dim length As Double
    Dim x As Double
    Dim y As Double
    Dim z As Double
    Dim i As Double
    Dim j As Double
    Dim k As Double
    Dim longitudeI As Double
    Dim longitudeJ As Double
    Dim longitudeK As Double

    Debug.Print "Nominal notch of Notch1"
    Debug.Print ""
    boolstatus = notchFeature.GetNominalNotch(width, length, x, y, z, i, j, k, longitudeI, longitudeJ, longitudeK)
    msgStr = "Width is "
    msgStr2 = width
    Debug.Print msgStr + msgStr2
    msgStr = "Length is "
    msgStr2 = length
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
    msgStr = "I-component of longitudinal unit vector is "
    msgStr2 = longitudeI
    Debug.Print msgStr + msgStr2
    msgStr = "J-component of longitudinal unit vector is "
    msgStr2 = longitudeJ
    Debug.Print msgStr + msgStr2
    msgStr = "K-component of longitudinal unit vector is "
    msgStr2 = longitudeK
    Debug.Print msgStr + msgStr2
    Debug.Print ""

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
            msgStr2 = "Bestfit plane"
ElseIf (featureType = swDimXpertFeature_Surface) Then
            msgStr2 = "Surface"
    End If

End Sub
Public Sub GetHoleType(ByRef holeType, ByRef msgStr2)
    If (holeType = swDimXpertCompoundHoleType_Compound) Then
            msgStr2 = "Compound"
    ElseIf (holeType = swDimXpertCompoundHoleType_Counterbore) Then
            msgStr2 = "Counterbore"
    ElseIf (holeType = swDimXpertCompoundHoleType_Countersink) Then
            msgStr2 = "Countersink"
    ElseIf (holeType = swDimXpertCompoundHoleType_Simple) Then
            msgStr2 = "Simple"
    End If

End Sub
```
