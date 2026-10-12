---
title: "Get and Set Location Dimension Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/Get_and_Set_Location_Dimension_Example_VBNET.htm"
---

# Get and Set Location Dimension Example (VB.NET)

This example shows how to get and set DimXpert distance-between or angle-between dimensions.

```vb
 '-----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\dimxpert\bracket_ads_plusminus.sldprt.
 ' 2. Multi-select two faces that:
 '    a. share a common edge to get the angle-between dimension.
 '    b. do not share a common edge to get the distance-between dimension.
 ' 3. Open an Immediate window.
 ' 4. Ensure that the latest SOLIDWORKS DimXpert interop assembly is referenced:
 '    a. Right-click the project in Project Explorer.
 '    b. Select Add Reference.
 '    c. Click the Browse tab.
 '    d. Find and select install_dir\api\redist\swdimxpert.dll.
 '
 ' Postconditions:
 ' 1. Inspect the Immediate window.
 ' 2. Observe the DistanceBetween1 or AngleBetween1 annotation on the
 '    DimXpertManager tab.
 '
 ' NOTE: Because this part is used elsewhere, do not save changes.
 '---------------------------------------------------------------------------

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
         Dim annoType As Long

         If swModelDoc Is Nothing Then
             Exit Sub
         End If

         Dim dimXpertMgr As DimXpertManager
         dimXpertMgr = swapp.IActiveDoc2.Extension.DimXpertManager(swapp.IActiveDoc2.IGetActiveConfiguration().Name, True)
         Debug.Print("Model: " & swapp.IActiveDoc2.GetPathName)

         Dim dimXpertPartObj As dimXpertPart
         dimXpertPartObj = dimXpertMgr.dimXpertPart
         dimXpertPart = dimXpertPartObj

         Dim dimOption As DimXpertDimensionOption
         dimOption = dimXpertPart.GetDimOption

         ' DimensionPositionOption works only for linear location dimensions
         dimOption.DimensionPositionOption = 0 ' Specify a dimension along the normal to the face

         ' Insert the dimension
         dimXpertPart.InsertLocationDimension(dimOption)

         Dim vAnnotations As Object
         vAnnotations = dimXpertPart.GetAnnotations()

         Debug.Print("------------------------")
         Debug.Print("Annotations...")
         Debug.Print("------------------------")

         Dim annotationTemp As DimXpertAnnotation
         Dim annotationIndex As Long
         For annotationIndex = 0 To UBound(vAnnotations)
             annotationTemp = vAnnotations(annotationIndex)
             Call GeneralInfo(annotationTemp)
             annoType = annotationTemp.Type
             Call DimensionToleranceData(annotationTemp)
         Next

     End Sub

     Private Sub GeneralInfo(ByVal annotation As DimXpertAnnotation)

         Dim annoType As String
         Dim modelObj As Object
         Dim modelFeature As Feature

         Debug.Print("")
         Debug.Print("Name: " + annotation.Name)

         annoType = annotationTypeNameFromObject(annotation)

         Debug.Print("Type: " + annoType)
         Debug.Print("Display Entity: " + DisplayEntity(annotation))

         modelObj = annotation.GetModelFeature
         modelFeature = modelObj
         If Not (modelFeature Is  Nothing)  Then
             Debug.Print("ModelFeature: " + modelFeature.Name +  " (" + modelFeature.GetTypeName2() + ")")
         End If

     End Sub

     Private Sub DimensionToleranceData(ByVal annotation As DimXpertDimensionTolerance)

         Dim isAngleType As Boolean
         Dim annoType As Long
         Dim upper As Double, lower As Double
         Dim plus As Double, minus As Double
         Dim boolstatus As Boolean

         annoType = annotation.Type
         isAngleType = False

         Debug.Print("")
         Debug.Print("Dimension Tolerance Compartment")

         If annoType = swDimXpertAnnotationType_e.swDimXpertDimTol_DistanceBetween Then
             Dim distancebetween As DimXpertDistanceBetweenDimTol
             distancebetween = annotation
             Call DistanceBetweenData(distancebetween)

         ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertDimTol_AngleBetween  Then
             isAngleType =  True
             Dim angleBetween As IDimXpertAngleBetweenDimTol
             angleBetween = annotation

             ' the origin and tolerance feature
             Debug.Print("Origin Feature: " + angleBetween.OriginFeature.Name)

             ' is supplement angle
             Debug.Print("Supplement Angle: " + IIf(angleBetween.Supplement, "True", "False"))

         End If

         ' conversion for radians to degrees when dimension type is angle

         Dim dbl As Double
         If isAngleType Then
             dbl = 57.2957795130823
         Else
             dbl = 1.0#
         End If

         ' the nominal, and upper and lower limits of size of the dimension

         Debug.Print("")
         Debug.Print("Compute Nominal Dimension: " + FormatDouble(annotation.GetNominalValue * dbl))
         boolstatus = annotation.GetUpperAndLowerLimit(upper, lower)
         Debug.Print("Get Upper Limit: " + FormatDouble(upper * dbl))
         Debug.Print("Get Lower Limit: " + FormatDouble(lower * dbl))

         ' the upper and lower tolerance value by type
         Select Case annotation.DimensionType

             Case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_BlockTolerance
                 Debug.Print("Dimension Type: Block Tolerance")

                 ' block tolerance

             Case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_BlockToleranceNoNominal
                 Dim blockTols As DimXpertBlockTolerances
                 blockTols = dimXpertPart.GetBlockTolerances

                 Select Case blockTols.Type

                     Case swDimXpertBlockToleranceType_e.swDimXpertBlockToleranceType_ASMEInch
                         Debug.Print("Dimension Type: Block Tolerance No Nominal")
                         If isAngleType Then
                             Debug.Print("Angular Block Tolerance")
                         Else
                             Debug.Print("Block Tolerance Decimal Places: " + Format(annotation.BlockToleranceDecimalPlaces,  "##,##0"))
                         End If

                     Case swDimXpertBlockToleranceType_e.swDimXpertBlockToleranceType_ISO2768
                         Debug.Print("Dimension Type: General Tolerance")

                 End Select

             Case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_ISOLimitsAndFits
                 Debug.Print("Dimension Type: Limits and Fits")

                 ' limits and fits tolerance
             Case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_ISOLimitsAndFitsNoNominal

                 Debug.Print("Dimension Type: Limits and Fits No Nominal")
                 Debug.Print("Limits and Fits: " + annotation.LimitsAndFitsCode)

                 ' limit dimension
             Case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_LimitDimension

                 Debug.Print("Dimension Type: Limit Dimension")
                 boolstatus = annotation.GetUpperAndLowerLimit(upper, lower)
                 Debug.Print("Get Upper Limit: " + FormatDouble(upper * dbl))
                 Debug.Print("Get Lower Limit: " + FormatDouble(lower * dbl))

             Case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_MAXTolerance
                 Debug.Print("Dimension Type: MAXTolerance")

             Case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_MINTolerance
                 Debug.Print("Dimension Type: MINTolerance")

             Case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_NoTolerance
                 Debug.Print("Dimension Type: NoTolerance")

             Case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_PlusMinusDimension
                 Debug.Print("Dimension Type: Plus Minus Dimension")

                 ' plus and minus dimension

             Case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_PlusMinusNoNominal
                 Debug.Print("Dimension Type: Plus Minus No Nominal")
                 boolstatus = annotation.GetPlusAndMinusTolerance(plus, minus)
                 Debug.Print("Plus  Tolerance: " + FormatDouble(plus * dbl))
                 Debug.Print("Minus Tolerance: " + FormatDouble(minus * dbl))

         End Select

     End Sub

     Private Sub DistanceBetweenData(ByVal annotation As DimXpertDistanceBetweenDimTol)

         Dim feature As DimXpertFeature
         Dim featureFosUsage As Long
         Dim I As  Double, J  As  Double, K  As  Double
         Dim boolstatus As Boolean

         feature =  Nothing
         ' the origin and tolerance feature along with their feature of size usage (min, max, center)
         boolstatus = annotation.GetOriginFeature(feature, featureFosUsage)

         Debug.Print("")
         Debug.Print("Origin Feature: " + feature.Name + " @ " + FosUsage(featureFosUsage))
         boolstatus = annotation.GetFeature(feature, featureFosUsage)
         Debug.Print("Tolerance Feature: " + feature.Name + " @ " + FosUsage(featureFosUsage))

         ' The direction vector

         boolstatus = annotation.GetDirectionVector(I, J, K)
         Debug.Print("")
         Debug.Print("Direction Vector: " + FormatVector(I, J, K))

     End Sub

     Private Function annotationTypeNameFromObject(ByVal anno As DimXpertAnnotation) As String
         annotationTypeNameFromObject = annotationTypeNameFromTypeNumber(anno.Type)
     End Function

     Private Function annotationTypeNameFromTypeNumber(ByVal annoTypeIndex As Long) As  String

         Select Case annoTypeIndex

             Case swDimXpertAnnotationType_e.swDimXpertDimTol_DistanceBetween
                 annotationTypeNameFromTypeNumber =  "DistanceBetween Dim"
             Case swDimXpertAnnotationType_e.swDimXpertDimTol_AngleBetween
                 annotationTypeNameFromTypeNumber =  "AngleBetween Dim"
             Case Else
                 annotationTypeNameFromTypeNumber = "Unknown"

         End Select

     End Function

     Private Function DisplayEntity(ByVal annotation As DimXpertAnnotation) As String

         Dim str As String
         Dim dispEnt As Object
         Dim swAnnot As Annotation

         dispEnt = annotation.GetDisplayEntity

         str = Nothing
         If Not dispEnt Is  Nothing  Then
             If TypeOf dispEnt Is Annotation Then
                 swAnnot = dispEnt
                 str = swAnnot.GetName
             End If
         End If

         DisplayEntity = str

     End Function

     Private Function FosUsage(ByVal value As Long) As  String

         Dim str As String
         Select Case value

             Case swDimXpertDistanceFosUsage_e.swDimXpertDistanceFosUsage_Center
                 str = "Center"

             Case swDimXpertDistanceFosUsage_e.swDimXpertDistanceFosUsage_MaximumSide
                 str = "Max"

             Case swDimXpertDistanceFosUsage_e.swDimXpertDistanceFosUsage_MinimumSide
                 str = "Min"

             Case Else
                 str =  "N/A"

         End Select

         FosUsage = str

     End Function

     Private Function FormatVector(ByVal I As  Double,  ByVal J  As  Double,  ByVal K  As  Double)  As  String

         Dim str As String
         str = FormatDouble(I) +  ", " + FormatDouble(J) + ", " + FormatDouble(K)
         FormatVector = str

     End Function

     Private Function FormatDouble(ByVal value As Double) As  String

         Dim str As String
         str = Format(value,  "##,##0.0000")
         FormatDouble = str

     End Function

     Private Function RadiansToDegrees(ByVal value As Double) As  String

         Dim str As String
         str = Format((value * 57.2957795130823), "##,##0.00")
         RadiansToDegrees = str

     End Function

     Public swApp As SldWorks

 End  Class
```
