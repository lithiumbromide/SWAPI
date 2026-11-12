---
title: "Auto Dimension Scheme Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/Auto_Dimension_Scheme_Example_VB.htm"
---

# Auto Dimension Scheme Example (VBA)

This example shows how to create a DimXpert Auto Dimension Scheme, turn tolerance status on and off, and delete tolerances.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
'  1. Open public_documents\samples\tutorial\dimxpert\bracket_auto_plusminus.sldprt.
 '  2. (Optional) Multi-select three faces to specify primary, secondary,
 '     and tertiary datum.
 '  3. Open an Immediate window.
 '  4. Ensure that the latest SOLIDWORKS DimXpert type library is loaded:
 '     a. Click Tools > References.
 '     b. Click Browse.
 '     c. Find and select install_dir\swdimxpert.tlb.
 '  5. Set two breakpoints on these lines:
 '     * swDXPart.ShowToleranceStatus = False
 '     * retval = swDXPart.DeleteAllTolerances
 '  6. Press F5.
 '  7. Observe on the DimXpertManager tab: Hole Pattern1, Hole Pattern2,
 '     Fillet1, Fillet Pattern1. Also observe that tolerance status is turned
 '     on in the SOLIDWORKS viewer.
 '  8. Press F5 and observe that tolerance status is turned off.
 '  9. Compare the output in the Immediate window with the features
 '     displayed on the DimXpertManager tab.
 ' 10. Press F5 and observe that all tolerance annotations have been
 '     removed from the model.
 '
 ' Postconditions: None
 '
 ' NOTE: Because this part is used elsewhere, do not save changes.
 '---------------------------------------------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swModelDocExt As SldWorks.ModelDocExtension
 Dim swSelMgr As SldWorks.SelectionMgr
 Dim swConfig As SldWorks.Configuration
 Dim swFeature As SldWorks.feature
 Dim swAnn As SldWorks.feature
 Dim swSchema As SldWorks.DimXpertManager
 Dim swDXPart As DimXpertPart
 Dim schemeOption As DimXpertAutoDimSchemeOption
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
    ' Set Auto Dimension Scheme using default options
     Set schemeOption = swDXPart.GetAutoDimSchemeOption
     Debug.Print "Default for ScopeAllFeature is: "
     Debug.Print (schemeOption.ScopeAllFeature)
     Debug.Print "Default for FeatureFilters is: "
     Debug.Print (schemeOption.FeatureFilters)
     Debug.Print "Default for PartType is: "
     Debug.Print (schemeOption.PartType)
     Debug.Print "Default for PatternType is: "
     Debug.Print (schemeOption.PatternType)
     Debug.Print "Default for PolarPatternHoleCount is: "
     Debug.Print (schemeOption.PolarPatternHoleCount)
     Debug.Print "Default for ToleranceType is: "
     Debug.Print (schemeOption.ToleranceType)

    Dim retval As Boolean
     retval = swDXPart.AutoDimensionScheme(schemeOption)

    ' Turn tolerance status off
     swDXPart.ShowToleranceStatus = False

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
        'Use IDimXpertFeature to get feature data
         Set feature = features(n)
        Debug.Print "  " + "Feature name: " + (feature.Name)

        featureType = feature.Type
         Call GetPatternType(featureType, msgStr2)

         msgStr = "     Feature type "
         msgStr3 = " is suppressed on the DimXpertManager tab? "
         msgStr4 = feature.IsSuppressed()
        Debug.Print msgStr + msgStr2 + msgStr3 + msgStr4
        msgStr = "     " + "Swift model: "
        'Use IFeature to get the Swift model corresponding to this geometric dimensioning and tolerancing data
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
     ' Delete all tolerances
       retval = swDXPart.DeleteAllTolerances

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
```
