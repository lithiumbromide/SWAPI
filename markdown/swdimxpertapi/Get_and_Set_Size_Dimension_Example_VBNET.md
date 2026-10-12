---
title: "Get and Set Size Dimension Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/Get_and_Set_Size_Dimension_Example_VBNET.htm"
---

# Get and Set Size Dimension Example (VB.NET)

This example shows how to get and set DimXpert compound width features.

```vb
 '------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\dimxpert\bracket_ads_plusminus.sldprt.
 ' 2. Select an edge.
 ' 3. Open the Immediate window.
 ' 4. Ensure that the latest SOLIDWORKS DimXpert interop assembly is referenced:
 '    a. Right-click the project in Project Explorer.
 '    b. Select Add Reference.
 '    c. Click the Browse tab.
 '    d. Find and select install_dir\api\redist\swdimxpert.dll.
 '
 ' Postconditions:
 ' 1. Inspect the Immediate Window.
 ' 2. Observe the Width1 feature and the Width2 size dimension on the
 '    DimXpertManager tab.
 '
 ' NOTE: Because this part is used elsewhere, do not save changes.
 '----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.swdimxpert
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim dimXpertPart As dimXpertPart

     Sub Main()

         Dim swModelDoc As ModelDoc2
         swModelDoc = swapp.ActiveDoc
         Dim swFeature As feature
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

         If swModelDoc Is Nothing Then
             Exit Sub
         End If

         Dim dimXpertMgr As DimXpertManager
         dimXpertMgr = swApp.IActiveDoc2.Extension.DimXpertManager(swApp.IActiveDoc2.IGetActiveConfiguration().Name, True)
         Debug.Print("Model: " & swapp.IActiveDoc2.GetPathName)

         Dim dimXpertPartObj As dimXpertPart
         dimXpertPartObj = dimXpertMgr.dimXpertPart
         dimXpertPart = dimXpertPartObj

         Dim dimOption As DimXpertDimensionOption
         dimOption = dimXpertPart.GetDimOption

         ' Specify the position of the dimension annotation
         Dim textPos(2) As Double
         textPos(0) = 0.05
         textPos(1) = -0.03
         textPos(2) = -0.03
         Dim posvar As Object
         posvar = textPos
         dimOption.TextPosition = posvar

         Dim dimarray(0) As Long
         dimarray(0) = -1  ' default feature
         Dim dimvar As Object
         dimvar = dimarray
         dimOption.FeatureSelectorOptions = dimvar

         ' Insert the size dimension
         dimXpertPart.InsertSizeDimension(dimOption)

         Dim featCount As Long
         featCount = dimXpertPart.GetFeatureCount

         msgStr = "Total of "
         msgStr2 = featCount
         msgStr = msgStr + msgStr2 + " DimXpert features"
         Debug.Print("")
         Debug.Print(msgStr)

         ' Get IDimXpert features through IDimXpertPart

         features = dimXpertPart.GetFeatures
         If Not IsNothing(features) Then
             msgStr =  "  Features: "
             Debug.Print("")
             Debug.Print(msgStr)

             For n = 0 To UBound(features)
                 feature = features(n)
                 Debug.Print("  " + "Feature name: " + (feature.Name))
                 featureType = feature.Type
                 Call GetPatternType(featureType, msgStr2)

                 msgStr = "     Feature type "
                 msgStr3 =  " is suppressed on the DimXpertManager tab? "
                 msgStr4 = feature.IsSuppressed()
                 Debug.Print(msgStr + msgStr2 + msgStr3 + msgStr4)

                 msgStr = "     " + "Model feature: "

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

                 If Not IsNothing(appliedFeatures) Then
                     For o = 0 To UBound(appliedFeatures)
                         appliedFeature = appliedFeatures(o)
                         Debug.Print("        " + "Applied feature name: " + (appliedFeature.Name))
                     Next
                 End If

                 msgStr =  "     " + "Number of applied annotations: "
                 msgStr2 = feature.GetAppliedAnnotationCount()
                 Debug.Print(msgStr + msgStr2)

                 appliedAnnotations = feature.GetAppliedAnnotations()

                 If Not IsNothing(appliedAnnotations) Then
                     For p = 0 To UBound(appliedAnnotations)
                         appliedAnnotation = appliedAnnotations(p)
                         Debug.Print("        " + "Applied annotation name: " + (appliedAnnotation.Name))
                     Next
                 End If
                 Debug.Print("     ")
             Next

             ' Get specific information about the Width1 feature

             Dim widthFeature As IDimXpertCompoundWidthFeature
             widthFeature = dimXpertPart.GetFeature("Width1")
             msgStr = widthFeature.Name +  " is a DimXpert compound width feature."
             Debug.Print("")
             Debug.Print(msgStr)
             Debug.Print("")

             ' Get the nominal width coordinates

             Dim width As Double
             Dim x As  Double
             Dim y As  Double
             Dim z As  Double
             Dim i As  Double
             Dim j As  Double
             Dim k As  Double

             Debug.Print("Nominal width of Width1")
             Debug.Print("")
             boolstatus = widthFeature.GetNominalCompoundWidth(width, x, y, z, i, j, k)

             msgStr = "Width is "
             msgStr2 = width
             Debug.Print(msgStr + msgStr2)

             msgStr = "X-coordinate is "
             msgStr2 = x
             Debug.Print(msgStr + msgStr2)

             msgStr = "Y-coordinate is "
             msgStr2 = y
             Debug.Print(msgStr + msgStr2)

             msgStr = "Z-coordinate is "
             msgStr2 = z
             Debug.Print(msgStr + msgStr2)

             msgStr = "I-component of pierce vector is "
             msgStr2 = i
             Debug.Print(msgStr + msgStr2)

             msgStr = "J-component of pierce vector is "
             msgStr2 = j
             Debug.Print(msgStr + msgStr2)

             msgStr = "K-component of pierce vector is "
             msgStr2 = k
             Debug.Print(msgStr + msgStr2)
             Debug.Print("")

             ' Get whether the width is a hole or a pin

             boolstatus = widthFeature.Inner
             msgStr = "This width is for a hole: "
             msgStr2 = boolstatus
             Debug.Print(msgStr + msgStr2)
         End If
     End Sub

     Public Sub GetPatternType(ByRef featureType As swDimXpertFeatureType_e, ByRef msgStr2 As String)

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
             msgStr2 =  "Bestfit Plane"
         ElseIf (featureType = swDimXpertFeatureType_e.swDimXpertFeature_Surface)  Then
             msgStr2 =  "Surface"
         End If

     End Sub

     Public swApp As SldWorks

 End  Class
```
