---
title: "Get and Set Pattern Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/Get_and_Set_Pattern_Example_VB.htm"
---

# Get and Set Pattern Example (VBA)

This example shows how to get and set DimXpert pattern features.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
' 1. Open public_documents\samples\tutorial\dimxpert\bracket_auto_manual.sldprt.
 ' 2. Select one of the CBORE hole faces in the SOLIDWORKS viewer.
 ' 3. Open an Immediate window .
 ' 4. Ensure that the latest SOLIDWORKS DimXpert type library is loaded:
 '    a. Select Tools > References.
 '    b. Click Browse.
 '    c. Find and select install_dir\swdimxpert.tlb.
 '
 ' Postconditions: Inspect the Immediate Window and the DimXpertManager tab.
 '
 ' NOTE: Because this part is used elsewhere, do not save changes.
 '---------------------------------------------------------------------------
Option Explicit
 Dim dimXpertPart As dimXpertPart
 Dim swApp As SldWorks.SldWorks

    Dim swModelDoc As SldWorks.ModelDoc2
     Dim swModelDocExt As SldWorks.ModelDocExtension
     Dim swSelMgr As SldWorks.SelectionMgr
     Dim swConfig As SldWorks.Configuration
     Dim swFeature As SldWorks.feature
     Dim swAnn As SldWorks.feature
     Dim swSchema As SldWorks.DimXpertManager
     Dim swDXPart As dimXpertPart
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
     Dim annoType As Long
     Dim retval As Boolean
Sub Main()

     Set swApp = Application.SldWorks
     Set swModelDoc = swApp.ActiveDoc
   If swModelDoc Is Nothing Then
      Exit Sub
    End If
    Dim dimXpertMgr As SldWorks.DimXpertManager
     Set dimXpertMgr = swApp.IActiveDoc2.Extension.DimXpertManager(swApp.IActiveDoc2.IGetActiveConfiguration().Name, True)
     Debug.Print "Model: " & swApp.IActiveDoc2.GetPathName
    Dim dimXpertPartObj As dimXpertPart
     Set dimXpertPartObj = dimXpertMgr.dimXpertPart
     Set dimXpertPart = dimXpertPartObj

    Dim selectMgr As SelectionMgr
     Set selectMgr = swApp.IActiveDoc2.SelectionManager

    Dim dimOption As DimXpertDimensionOption
     Set dimOption = dimXpertPart.GetDimOption

    Dim patternType As Long
     patternType = 2 ' collection pattern

    Dim findall As Boolean
     findall = True ' find all similar features on this face

    Dim dimarray(0) As Long
     dimarray(0) = -1  ' default
     Dim dimvar As Variant
     dimvar = dimarray
     dimOption.FeatureSelectorOptions = dimvar

    'Mark the current selection with an index value greater than 50
    retval = selectMgr.SetSelectedObjectMark(1, 51, swSelectionMarkSet)

    ' Insert the collection pattern feature
     retval = dimXpertPart.InsertPattern(dimOption, patternType, findall)

    Dim featCount As Long
     featCount = dimXpertPart.GetFeatureCount

   If Not (featCount = 0) Then
    Dim patternFeature As IDimXpertPatternFeature
     Set patternFeature = dimXpertPart.GetFeature("Collection1")
    msgStr = patternFeature.Name + " is a DimXpert collection pattern feature."
         Debug.Print ""
         Debug.Print msgStr
    featureType = patternFeature.patternType
    Call GetPatternType(featureType, msgStr2)
    Dim featureCount As Integer
    featureCount = patternFeature.GetSubFeatureCount()
     msgStr = "     Number of "
     msgStr3 = featureCount
     Debug.Print msgStr + msgStr2 + " sub-features in this pattern is " + msgStr3
    Dim subfeatures As Variant
     subfeatures = patternFeature.GetSubFeatures()
    Debug.Print "     Sub-features of Collection1:"
     Dim subFeature As DimXpertCompoundHoleFeature

    For n = 0 To UBound(subfeatures)
         Set subFeature = subfeatures(n)
         Debug.Print "        " + subFeature.Name
     Next
   Else
      Debug.Print "Please select a CBORE hole face in the viewer and run this macro again."

   End If

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
