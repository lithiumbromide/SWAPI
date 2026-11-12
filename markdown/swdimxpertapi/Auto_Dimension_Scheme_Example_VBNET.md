---
title: "Auto Dimension Scheme Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/Auto_Dimension_Scheme_Example_VBNET.htm"
---

# Auto Dimension Scheme Example (VB.NET)

This example shows how to create a DimXpert Auto Dimension Scheme, turn tolerance status on and off, and delete tolerances.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 '  1. Open public_documents\samples\tutorial\dimxpert\bracket_auto_plusminus.sldprt.
 '  2. (Optional) Multi-select three faces to specify primary, secondary,
 '      and tertiary datum.
 '  3. Open the Immediate window.
 '  4. Ensure that the latest SOLIDWORKS DimXpert interop assembly is referenced:
 '     a. Right-click the project in Project Explorer.
 '     b. Select Add Reference.
 '     c. Click the Browse tab.
 '     d. Find and select install_dir\api\redist\swdimxpert.dll.
 '  5. Set two breakpoints on these lines:
 '     * swDXPart.ShowToleranceStatus = False
 '     * retval = swDXPart.DeleteAllTolerances
 '  6. Press F5.
 '  7. Observe on the DimXpertManager tab: Hole Pattern1, Hole Pattern2,
 '      Fillet1, Fillet Pattern1. Also observe that tolerance status is
 '     turned on in the SOLIDWORKS viewer.
 '  8.  Press   F5 and observe that tolerance status is turned off.
 '  9. Compare the output in the Immediate window with the features displayed
 '       on the DimXpertManager tab.
 ' 10.  Press   F5 and observe that all tolerance annotations have been
 '     removed from the part.
 '
 ' Postconditions: None
 '
 ' NOTE: Because this part is used elsewhere, do not save changes.
 '---------------------------------------------------------------------------
```

```vb
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.swdimxpert
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim swModelDocExt As ModelDocExtension
     Dim swSelMgr As SelectionMgr
     Dim swConfig As Configuration
     Dim swFeature As Feature
     Dim swAnn As Feature
     Dim swSchema As DimXpertManager
     Dim swDXPart As DimXpertPart
     Dim schemeOption As DimXpertAutoDimSchemeOption
     Dim featureType As swDimXpertFeatureType_e
     Dim features As Object
     Dim appliedFeatures As Object
     Dim appliedAnnotations As Object
     Dim appliedAnnotation As DimXpertAnnotation
     Dim feature As DimXpertFeature
     Dim appliedFeature As DimXpertFeature
     Dim msgStr As String
     Dim msgStr2 As String
     Dim msgStr3 As String
     Dim msgStr4 As String
     Dim n As  Long
     Dim o As  Long
     Dim p As  Long

     Dim boolstatus As Boolean

     Sub main()

         swModel = swApp.ActiveDoc
         swModelDocExt = swModel.Extension
         swSelMgr = swModel.SelectionManager

         ' Get the default DimXpert schema using IModelDocExtension.DimXpertManager()
         swSchema = swModelDocExt.DimXpertManager("Default", True)

         ' Get IDimXpertPart from the IDimXpertManager
         swDXPart = swSchema.DimXpertPart

         ' Set Auto Dimension Scheme using default options
         schemeOption = swDXPart.GetAutoDimSchemeOption
         Debug.Print("Default for ScopeAllFeature is: ")
         Debug.Print(schemeOption.ScopeAllFeature)
         Debug.Print("Default for FeatureFilters is: ")
         Debug.Print(schemeOption.FeatureFilters)
         Debug.Print("Default for PartType is: ")
         Debug.Print(schemeOption.PartType)
         Debug.Print("Default for PatternType is: ")
         Debug.Print(schemeOption.PatternType)
         Debug.Print("Default for PolarPatternHoleCount is: ")
         Debug.Print(schemeOption.PolarPatternHoleCount)
         Debug.Print("Default for ToleranceType is: ")
         Debug.Print(schemeOption.ToleranceType)

         Dim retval As Boolean
         retval = swDXPart.AutoDimensionScheme(schemeOption)

         ' Turn tolerance status off
         swDXPart.ShowToleranceStatus = False

         Dim featCount As Long
         featCount = swDXPart.GetFeatureCount

         msgStr = "Total of "
         msgStr2 = featCount
         msgStr = msgStr + msgStr2 + " features in " + (swSchema.SchemaName)

         Debug.Print("")
         Debug.Print(msgStr)

         ' Get IDimXpert features through IDimXpertPart
         features = swDXPart.GetFeatures
         msgStr = (swSchema.SchemaName) +  " has the following features: "

         Debug.Print("")
         Debug.Print(msgStr)

         For n = 0 To UBound(features)

             'Use IDimXpertFeature to get feature data
             feature = features(n)

             Debug.Print("  " + "Feature name: " + (feature.Name))

             featureType = feature.Type
             Call GetPatternType(featureType, msgStr2)

             msgStr = "     Feature type "
             msgStr3 =  " is suppressed on the DimXpertManager tab? "
             msgStr4 = feature.IsSuppressed()

             Debug.Print(msgStr + msgStr2 + msgStr3 + msgStr4)

             msgStr = "     " + "Swift model: "

             'Use IFeature to get the Swift model corresponding to this geometric dimensioning and tolerancing data
             swFeature = feature.GetModelFeature()

             If Not (swFeature Is  Nothing)  Then
                 msgStr2 = swFeature.GetTypeName2()
                 Debug.Print(msgStr + msgStr2)

             End If

             msgStr =  "     " + "Number of SOLIDWORKS face entities in this feature: "
             msgStr2 = feature.GetFaceCount

             Debug.Print(msgStr + msgStr2)

             msgStr = "     " + "Number of applied features: "
             msgStr2 = feature.GetAppliedFeatureCount()

             Debug.Print(msgStr + msgStr2)

             appliedFeatures = feature.GetAppliedFeatures()

             If Not (IsNothing(appliedFeatures)) Then
                 For o = 0 To UBound(appliedFeatures)

                     appliedFeature = appliedFeatures(o)
                     Debug.Print("        " + "Applied feature name: " + (appliedFeature.Name))

                 Next
             End If

             msgStr =  "     " + "Number of applied annotations: "
             msgStr2 = feature.GetAppliedAnnotationCount()
             Debug.Print(msgStr + msgStr2)

             appliedAnnotations = feature.GetAppliedAnnotations()

             If Not (IsNothing(appliedAnnotations)) Then
                 For p = 0 To UBound(appliedAnnotations)

                     appliedAnnotation = appliedAnnotations(p)
                     Debug.Print("        " + "Applied annotation name: " + (appliedAnnotation.Name))

                 Next

             End If

             Debug.Print("     ")

         Next

         ' Delete all tolerances
         retval = swDXPart.DeleteAllTolerances

     End Sub

     Public Sub GetPatternType(ByRef featureType, ByRef msgStr2)

         If (featureType = swDimXpertFeatureType_e.swDimXpertFeature_Plane)  Then
             msgStr2 =  "Plane"

         ElseIf (featureType = swDimXpertFeatureType_e.swDimXpertFeature_Cylinder)  Then
             msgStr2 =  "Cylinder"

         ElseIf (featureType = swDimXpertFeatureType_e.swDimXpertFeature_Cone)  Then
             msgStr2 =  "Cone"

         ElseIf (featureType = swDimXpertFeatureType_e.swDimXpertFeature_Extrude)  Then
             msgStr2 =  "Extrude"

         ElseIf (featureType = swDimXpertFeatureType_e.swDimXpertFeature_Fillet)  Then
             msgStr2 =  "Fillet"

         ElseIf (featureType = swDimXpertFeatureType_e.swDimXpertFeature_Chamfer)  Then
             msgStr2 =  "Chamfer"

         ElseIf (featureType = swDimXpertFeatureType_e.swDimXpertFeature_CompoundHole) Then
             msgStr2 =  "CompoundHole"

         ElseIf (featureType = swDimXpertFeatureType_e.swDimXpertFeature_CompoundWidth) Then
             msgStr2 =  "CompoundWidth"

         ElseIf (featureType = swDimXpertFeatureType_e.swDimXpertFeature_CompoundNotch) Then
             msgStr2 =  "CompoundNotch"

         ElseIf (featureType = swDimXpertFeatureType_e.swDimXpertFeature_CompoundClosedSlot3D)  Then
             msgStr2 =  "CompoundClosedSlot3D"

         ElseIf (featureType = swDimXpertFeatureType_e.swDimXpertFeature_IntersectPoint) Then
             msgStr2 =  "IntersectPoint"

         ElseIf (featureType = swDimXpertFeatureType_e.swDimXpertFeature_IntersectLine) Then
             msgStr2 =  "IntersectLine"

         ElseIf (featureType = swDimXpertFeatureType_e.swDimXpertFeature_IntersectCircle) Then
             msgStr2 =  "IntersectCircle"

         ElseIf (featureType = swDimXpertFeatureType_e.swDimXpertFeature_IntersectPlane) Then
             msgStr2 =  "IntersectPlane"

         ElseIf (featureType = swDimXpertFeatureType_e.swDimXpertFeature_Pattern)  Then
             msgStr2 =  "Pattern"

         ElseIf (featureType = swDimXpertFeatureType_e.swDimXpertFeature_Sphere)  Then
             msgStr2 =  "Sphere"

         ElseIf (featureType = swDimXpertFeatureType_e.swDimXpertFeature_BestfitPlane) Then
             msgStr2 =  "Bestfit plane"

         ElseIf (featureType = swDimXpertFeatureType_e.swDimXpertFeature_Surface)  Then
             msgStr2 =  "Surface"

         End If

     End Sub

     Public swApp As SldWorks

 End  Class
```
