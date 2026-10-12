---
title: "Get DimXpert Tolerance1 Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/Get_DimXpert_Tolerance1_Example_VBNET.htm"
---

# Get DimXpert Tolerance1 Example (VB.NET)

This example shows how to build a part and get attributes for the following DimXpert annotations:

* Circularity geometric tolerance

* Cylindricity geometric tolerance

* Countersink angle dimension tolerance

* Countersink diameter dimension tolerance

* Flatness geometric tolerance

* Surface profile geometric tolerance

```vb
'----------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\cover_with_geometric_tolerances.sldprt.
' 2. Click Geometric Tolerance the DimXpert toolbar.
'    In the Geometric Tolerance Properties dialog:
'    a. Select Cylindricity from the Symbol dropdown.
'    b. In the second row, select Profile of Surface from the Symbol dropdown
'       and type a tolerance of 0.5 next to it.
'    c. Click the outer base cylinder and click again outside the part
'       to place the annotation.
'    d. Click OK to close the Geometric Tolerance Properties dialog.
' 3. In the DimXpertManager tab of the Management Panel,
'    expand all of the nodes in the tree.
' 4. Observe the following Dimxpert annotations:
'    Flatness1, Circularity1, Diameter1, CounterSinkAngle1,
'    CounterSinkDiameter1, Cylindricity1, and Surface Profile1
' 5. Ensure that the SolidWorks.Interop.swdimxpert.dll interop assembly is loaded
'    (right-click the project in Project Explorer and click on Add Reference >
'     NET tab).
' 6. Ensure that the Microsoft Scripting Runtime library is loaded
'    (right-click the project in Project Explorer and click on Add Reference >
'    COM tab).
'
' Postconditions:
' 1. Writes the output to c:\temp\dimXpertInfo.txt.
' 2. Inspect the Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save changes.
 '--------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swdimxpert
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics
Imports Scripting
Partial Class SolidWorksMacro
    Dim strs As New Collection
    Dim boolstatus As Boolean
    Dim dimXpertPart As DimXpertPart
    Dim i As Double
    Dim j As Double
    Dim k As Double
    Sub Main()
        Dim swModelDoc As IModelDoc2
        swModelDoc = swApp.ActiveDoc
        If swModelDoc Is Nothing Then
            Exit Sub
        End If
        Dim fso As New Scripting.FileSystemObject()
        Dim f As Scripting.File
        Dim textStr As Scripting.TextStream
        textStr = fso.CreateTextFile("c:\temp\dimXpertInfo.txt")
        f = fso.GetFile("c:\temp\dimXpertInfo.txt")
        'textStr = f.OpenAsTextStream(2, -2)
        If textStr Is Nothing Then
            Debug.Print("Error creating temp file.")
            Exit Sub
        End If
        Call log("Starting DimXpert log...", textStr)
        Call retrieve_info_text(swApp, textStr)
        textStr.Close()
    End Sub
    Private Sub log(ByVal text As String, ByVal textStr As Scripting.TextStream)
        Debug.Print(text)
        textStr.WriteLine(text)
    End Sub
    Private Sub retrieve_info_text(ByVal swapp As SldWorks, ByVal textStr As TextStream)
        Dim dimXpertMgr As SolidWorks.Interop.sldworks.DimXpertManager
        dimXpertMgr = swapp.IActiveDoc2.Extension.DimXpertManager(swapp.IActiveDoc2.IGetActiveConfiguration().Name, True)
        Call log("Model: " & swapp.IActiveDoc2.GetPathName, textStr)
        Dim dimXpertPartObj As DimXpertPart
        dimXpertPartObj = dimXpertMgr.DimXpertPart
        dimXpertPart = dimXpertPartObj
        Dim vAnnotations As Object
        vAnnotations = dimXpertPart.GetAnnotations()
        Call log("------------------------", textStr)
        Call log("Annotations...", textStr)
        Call log("------------------------", textStr)
        Dim annotationTemp As DimXpertAnnotation
        Dim annotationIndex As Long
        For annotationIndex = 0 To UBound(vAnnotations)
            annotationTemp = vAnnotations(annotationIndex)
            Dim AnnotationDataText As Collection
            AnnotationDataText = AnnotationData(annotationTemp)
            Dim annotationTextIndex As Long
            For annotationTextIndex = 1 To AnnotationDataText.Count
                Call log(AnnotationDataText(annotationTextIndex), textStr)
            Next
        Next
    End Sub
    Public Function AnnotationData(ByVal annotation As DimXpertAnnotation) As Collection
        Dim annoType As Long
        'general info
        Call GeneralInfo(annotation)
        annoType = annotation.Type
        If annoType = swDimXpertAnnotationType_e.swDimXpertDatum Then
            Call DatumData(annotation)
        ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_Position Then
            Call PositionData(annotation)
        ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_CompositePosition Then
            Call CompositePositionData(annotation)
        ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_Symmetry Then
            Call SymmetryData(annotation)
        ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_Concentricity Then
            Call ConcentricityData(annotation)
        ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_LineProfile Then
            Call LineProfileData(annotation)
        ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_CompositeLineProfile Then
            Call CompositeLineProfileData(annotation)
        ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_SurfaceProfile Then
            Call SurfaceProfileData(annotation)
        ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_CompositeSurfaceProfile Then
            Call CompositeSurfaceProfileData(annotation)
        ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_Angularity Or annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_Parallelism Or annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_Perpendicularity Then
            Call OrientationData(annotation)
        ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_TotalRunout Then
            Call TotalRunoutData(annotation)
        ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_CircularRunout Then
            Call CircularRunoutData(annotation)
        ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_Flatness Then
            Call FlatnessData(annotation)
        ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_Circularity Then
            Call CircularityData(annotation)
        ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_Cylindricity Then
            Call CylindricityData(annotation)
        ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_Straightness Then
            Call StraightnessData(annotation)
        ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_Tangency Then
            Call TangencyData(annotation)
        Else    ' any of the dimension tolerance types
            Call DimensionToleranceData(annotation)
        End If
        AnnotationData = strs
    End Function
    Private Sub Clear(ByVal strs As Collection)
        strs.Remove(strs.Count)
        If Not strs.Count = 0 Then
            Call Clear(strs)
        End If
    End Sub
    Private Sub GeneralInfo(ByVal annotation As DimXpertAnnotation)
        Dim annoType As String
        Dim modelObj As Feature
        If Not strs.Count = 0 Then
            Call Clear(strs)
        End If
        strs.Add("")
        strs.Add("Name: " + annotation.Name)
        annoType = annotationTypeNameFromObject(annotation)
        strs.Add("Type: " + annoType)
        strs.Add("Display Entity: " + DisplayEntity(annotation))
        modelObj = annotation.GetModelFeature()
        If Not (modelObj Is Nothing) Then
            strs.Add("ModelFeature: " + modelObj.Name + " (" + modelObj.GetTypeName2() + ")")
        End If
    End Sub
    Private Sub DatumData(ByVal annotation As DimXpertDatum)
        ' the datum letter
        strs.Add("")
        strs.Add("Datum Letter:  " + annotation.Identifier)
    End Sub
    Private Sub PositionData(ByVal annotation As DimXpertPositionTolerance)
        Dim I As Double, J As Double, K As Double
        Dim enabled As Boolean, value As Double
        Dim boolstatus As Boolean
        strs.Add("")
        strs.Add("Position Tolerance Compartment:")
        ' the shape of the tolerance zone
        strs.Add("  Zone Type: " + PositionZoneType(annotation.ZoneType))
        ' the zone vector if the tolerance zone is planar
        If annotation.ZoneType = swDimXpertPositionZoneType_e.swDimXpertPositionZoneType_PlanarPosition Then
            boolstatus = annotation.GetPlanarZoneVector(I, J, K)
            strs.Add("  Direction: " + FormatVector(I, J, K))
        End If
        ' the tolerance value
        strs.Add("  Tolerance: " + FormatDouble(annotation.Tolerance))
        ' the material condition modifer applied to feature
        strs.Add("  Modifier: " + mcmStr(annotation.Modifier))
        ' the projected tolerance zone when specified
        boolstatus = annotation.GetProjectedZone(enabled, value)
        Call FormatProjectedZone(enabled, value)
        ' the datum reference frame
        Call DatumsStr(annotation)
    End Sub
    Private Sub CompositePositionData(ByVal annotation As DimXpertCompositePositionTolerance)
        Dim I As Double, J As Double, K As Double
        Dim enabled As Boolean, value As Double
        Dim boolstatus As Boolean
        strs.Add("")
        strs.Add("Composite Position Tolerance Compartment")
        ' the shape of the tolerance zone
        strs.Add("  Zone Type: " + PositionZoneType(annotation.ZoneType))
        ' the zone vector when the zone is planar
        If annotation.ZoneType = swDimXpertPositionZoneType_e.swDimXpertPositionZoneType_PlanarPosition Then
            boolstatus = annotation.GetPlanarZoneVector(I, J, K)
            strs.Add("  Direction: " + FormatVector(I, J, K))
        End If
        ' the tolerance value
        strs.Add("  Tolerance: " + FormatDouble(annotation.Tolerance))
        ' the material condition modifer
        strs.Add("  Modifier: " + mcmStr(annotation.Modifier))
        ' the projected tolerance zone when specified
        boolstatus = annotation.GetProjectedZone(enabled, value)
        Call FormatProjectedZone(enabled, value)
        ' the datum reference frame for the pattern location
        Call DatumsStr(annotation)
        ' the datum reference frame for the feature to feature location
        strs.Add("Composite datums:")
        strs.Add("  Repeat Primary: " + IIf(annotation.PrimaryInLowerTier, "True", "False"))
        strs.Add("  Repeat Secondary: " + IIf(annotation.SecondaryInLowerTier, "True", "False"))
        strs.Add("  Repeat Tertiary: " + IIf(annotation.TertiaryInLowerTier, "True", "False"))
    End Sub
    Private Sub SymmetryData(ByVal annotation As DimXpertSymmetryTolerance)
        Dim I As Double, J As Double, K As Double
        Dim boolstatus As Boolean
        strs.Add("")
        strs.Add("Symmetry Tolerance Compartment")
        ' the tolerance value
        strs.Add("  Tolerance: " + FormatDouble(annotation.Tolerance))
        ' the material condition modifer applied to feature
        strs.Add("  Modifier: " + mcmStr(annotation.Modifier))
        ' the datum reference frame
        strs.Add("")
        Call DatumsStr(annotation)
        ' the direction of the planar zone
        strs.Add("")
        boolstatus = annotation.GetZoneDirection(I, J, K)
        strs.Add("Planar Zone Direction: " + FormatVector(I, J, K))
    End Sub
    Private Sub ConcentricityData(ByVal annotation As DimXpertConcentricityTolerance)
        strs.Add("")
        strs.Add("Concentricity Tolerance Compartment")
        ' the tolerance value
        strs.Add("  Tolerance: " + FormatDouble(annotation.Tolerance))
        ' the material condition modifer applied to feature
        strs.Add("  Modifier: " + mcmStr(annotation.Modifier))
        ' the datum reference frame
        Call DatumsStr(annotation)
    End Sub
    Private Sub TotalRunoutData(ByVal annotation As DimXpertTolerance)
        strs.Add("")
        strs.Add("Total Runout Tolerance Compartment")
        ' the tolerance value
        strs.Add("  Tolerance: " + FormatDouble(annotation.Tolerance))
        ' the datum reference frame
        Call DatumsStr(annotation)
    End Sub
    Private Sub CircularRunoutData(ByVal annotation As DimXpertTolerance)
        strs.Add("")
        strs.Add("Ciircular Runout Tolerance Compartment")
        ' the tolerance value
        strs.Add("  Tolerance: " + FormatDouble(annotation.Tolerance))
        ' the datum reference frame
        Call DatumsStr(annotation)
    End Sub
    Private Sub LineProfileData(ByVal annotation As DimXpertLineProfileTolerance)
        Dim I As Double, J As Double, K As Double
        Dim boolstatus As Boolean
        strs.Add("")
        strs.Add("Line Profile Tolerance Compartment")
        ' the tolerance value
        strs.Add("  Tolerance: " + FormatDouble(annotation.Tolerance))
        ' the outer (outside material) tolerance value
        strs.Add("  Outer Tolerance: " + FormatDouble(annotation.OuterToleranceValue))
        ' the vector normal to the profile zones
        strs.Add("")
        boolstatus = annotation.GetPlanarZoneVector(I, J, K)
        strs.Add("Planar Zone Vector: " + FormatVector(I, J, K))
        ' the datum reference frame
        Call DatumsStr(annotation)
    End Sub
    Private Sub CompositeLineProfileData(ByVal annotation As DimXpertCompositeLineProfileTolerance)
        strs.Add("")
        strs.Add("Composite Line Profile Tolerance Compartment")
        ' the tolerance value
        strs.Add("  Tolerance: " + FormatDouble(annotation.Tolerance))
        ' the outer (outside material) tolerance value
        strs.Add("  Outer Tolerance: " + FormatDouble(annotation.OuterToleranceValue))
        ' the vector normal to the profile zones
        strs.Add("")
        boolstatus = annotation.GetPlanarZoneVector(i, j, k)
        strs.Add("Planar Zone Vector: " + FormatVector(i, j, k))
        ' the datum reference frame
        Call DatumsStr(annotation)
        ' the datum reference frame for the orientation and form
        strs.Add("Composite Datums:")
        strs.Add("  Repeat Primary: " + IIf(annotation.PrimaryInLowerTier, "True", "False"))
        strs.Add("  Repeat Secondary: " + IIf(annotation.SecondaryInLowerTier, "True", "False"))
        strs.Add("  Repeat Tertiary: " + IIf(annotation.TertiaryInLowerTier, "True", "False"))
    End Sub
    Private Sub SurfaceProfileData(ByVal annotation As DimXpertSurfaceProfileTolerance)
        strs.Add("")
        strs.Add("Surface Profile Tolerance Compartment")
        ' the tolerance value
        strs.Add("  Tolerance: " + FormatDouble(annotation.Tolerance))
        ' the outer (outside material) tolerance value
        strs.Add("  Outer Tolerance: " + FormatDouble(annotation.OuterToleranceValue))
        ' the datum reference frame
        Call DatumsStr(annotation)
    End Sub
    Private Sub CompositeSurfaceProfileData(ByVal annotation As DimXpertCompositeSurfaceProfileTolerance)
        strs.Add("")
        strs.Add("Composite Surface Profile Tolerance Compartment")
        ' the tolerance value
        strs.Add("  Tolerance Upper Tier: " + FormatDouble(annotation.Tolerance))
        ' the outer tolerance value
        strs.Add("  Outer Tolerance Upper Tier: " + FormatDouble(annotation.OuterToleranceValue))
        ' the datum reference frame for the location
        Call DatumsStr(annotation)
        ' the datum reference frame for the orientation and form
        strs.Add("Composite Datums:")
        strs.Add("  Repeat Primary: " + IIf(annotation.PrimaryInLowerTier, "True", "False"))
        strs.Add("  Repeat Secondary: " + IIf(annotation.SecondaryInLowerTier, "True", "False"))
        strs.Add("  Repeat Tertiary: " + IIf(annotation.TertiaryInLowerTier, "True", "False"))
    End Sub
    Private Sub OrientationData(ByVal annotation As DimXpertOrientationTolerance)
        Dim I As Double, J As Double, K As Double
        Dim enabled As Boolean, value As Double
        Dim annoType As Long
        annoType = annotation.Type
        ' the type or orientation tolerance
        If annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_Perpendicularity Then
            strs.Add("Orientation Type:  Perpendicularity")
        ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_Parallelism Then
            strs.Add("Orientation Type:  Parallelism")
        ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertGeoTol_Angularity Then
            strs.Add("Orientation Type:  Angularity")
        End If
        strs.Add("")
        strs.Add("Orientation Tolerance Compartment:")
        ' the shape of the tolerance zone
        Select Case annotation.ZoneType
            Case swDimXpertOrientationZoneType_e.swDimXpertOrientationZoneType_Cylindrical
                strs.Add("  Zone Type: Cylindrical")
            Case swDimXpertOrientationZoneType_e.swDimXpertOrientationZoneType_Planar
                strs.Add("  Zone Type: Planar")
                boolstatus = annotation.GetPlanarZoneVector(I, J, K)
                strs.Add("Planar Zone Vector: " + FormatVector(I, J, K))
        End Select
        ' the tolerance value
        strs.Add("  Tolerance: " + FormatDouble(annotation.Tolerance))
        'material condition modifer applied to feature
        strs.Add("  Modifier: " + mcmStr(annotation.Modifier))
        ' the projected tolerance zone when specified
        boolstatus = annotation.GetProjectedZone(enabled, value)
        Call FormatProjectedZone(enabled, value)
        ' is tangent plane
        strs.Add("  IsTangentPlane: " + IIf(annotation.IsTangentPlane, "True", "False"))
        ' the datum reference frame
        Call DatumsStr(annotation)
    End Sub
    Private Sub FlatnessData(ByVal annotation As DimXpertFlatnessTolerance)
        Dim enabled As Boolean
        Dim length As Double, width As Double
        Dim I As Double, J As Double, K As Double
        Dim boolstatus As Boolean
        strs.Add("")
        strs.Add("Flatness Tolerance Compartment:")
        ' the tolerance value
        strs.Add("  Tolerance: " + FormatDouble(annotation.Tolerance))
        ' the per unit area data
        boolstatus = annotation.GetPerUnitArea(enabled, length, width, I, J, K)
        strs.Add("  Per Unit Area: " + IIf(enabled, "True", "False"))
        If enabled Then
            strs.Add("  Per Unit Length: " + FormatDouble(length))
            strs.Add("  Per Unit Width: " + FormatDouble(width))
            strs.Add("  Per Unit Direction: " + FormatVector(I, J, K))
        End If
    End Sub
    Private Sub CircularityData(ByVal annotation As DimXpertTolerance)
        strs.Add("")
        strs.Add("Circularity Tolerance Compartment")
        ' the tolerance value
        strs.Add("  Tolerance: " + FormatDouble(annotation.Tolerance))
    End Sub
    Private Sub CylindricityData(ByVal annotation As DimXpertTolerance)
        strs.Add("")
        strs.Add("Cylindricity Tolerance Compartment")
        ' the tolerance value
        strs.Add("  Tolerance: " + FormatDouble(annotation.Tolerance))
    End Sub
    Private Sub StraightnessData(ByVal annotation As DimXpertStraightnessTolerance)
        Dim I As Double, J As Double, K As Double
        Dim enabled As Boolean
        Dim dist As Double
        Dim boolstatus As Boolean
        'tolerance compartment info
        strs.Add("")
        strs.Add("Straightness Tolerance Compartment")
        'type or shape of the tolerance zone
        Select Case annotation.ZoneType
            Case swDimXpertStraightnessZoneType_e.swDimXpertStraightnessZoneType_Cylindrical
                strs.Add("  Zone Type: Cylindrical")
            Case swDimXpertStraightnessZoneType_e.swDimXpertStraightnessZoneType_PlanarMedian
                strs.Add("  Zone Type: Planar Median")
            Case swDimXpertStraightnessZoneType_e.swDimXpertStraightnessZoneType_Surface
                strs.Add("  Zone Type: Surface Straightness")
                boolstatus = annotation.GetPlanarZoneVector(I, J, K)
                strs.Add("  Zone Vector: " + FormatVector(I, J, K))
        End Select
        ' the tolerance value
        strs.Add("  Tolerance: " + FormatDouble(annotation.Tolerance))
        'per unit length
        boolstatus = annotation.GetPerUnitLength(enabled, dist)
        strs.Add("  Per Unit Length: " + IIf(enabled, "True", "False"))
        If enabled Then
            strs.Add("  Per Unit Length Distance:  " + FormatDouble(dist))
        End If
        ' the material condition modifer
        strs.Add("  Modifier: " + mcmStr(annotation.Modifier))
    End Sub
    Private Sub ProfileData(ByVal annotation As DimXpertTolerance)
        strs.Add("")
        strs.Add("Profile Tolerance Compartment")
        ' the tolerance value
        strs.Add("  Tolerance: " + FormatDouble(annotation.Tolerance))
        ' the datum reference frame
        Call DatumsStr(annotation)
    End Sub
    Private Sub SurfaceFinishData(ByVal annotation As DimXpertTolerance)
        strs.Add("")
        strs.Add("Surface Finish Tolerance Compartment")
        ' the tolerance value
        strs.Add("  Tolerance: " + FormatDouble(annotation.Tolerance))
    End Sub
    Private Sub TangencyData(ByVal annotation As DimXpertTolerance)
        strs.Add("")
        strs.Add("Tangency Tolerance Compartment")
        ' the tolerance value
        strs.Add("  Tolerance: " + FormatDouble(annotation.Tolerance))
    End Sub
    Private Sub DimensionToleranceData(ByVal annotation As DimXpertDimensionTolerance)
        Dim isAngleType As Boolean
        Dim annoType As Long
        Dim upper As Double, lower As Double
        Dim plus As Double, minus As Double
        Dim boolstatus As Boolean
        annoType = annotation.Type
        isAngleType = False
        strs.Add("")
        strs.Add("Dimension Tolerance Compartment")
        If annoType = swDimXpertAnnotationType_e.swDimXpertDimTol_DistanceBetween Then
            Call DistanceBetweenData(annotation)
        ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertDimTol_CompositeDistanceBetween Then
            Call CompositeDistanceBetweenData(annotation)
        ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertDimTol_CounterBore Then
            If annotation.ReferenceFeature Is Nothing Then
                strs.Add("Reference Feature: NULL")
            Else
                strs.Add("Reference Feature: " + annotation.ReferenceFeature.Name)
            End If
        ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertDimTol_Depth Then
            If annotation.ReferenceFeature Is Nothing Then
                strs.Add("Reference Feature: NULL")
            Else
                strs.Add("Reference Feature: " + annotation.ReferenceFeature.Name)
            End If
        ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertDimTol_CounterSinkDiameter Then
            Dim csDiameter As IDimXpertCounterSinkDiameterDimTol
            csDiameter = annotation
            If csDiameter.ReferenceFeature Is Nothing Then
                strs.Add("Reference Feature: NULL")
            Else
                strs.Add("Reference Feature: " + csDiameter.ReferenceFeature.Name)
            End If
        ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertDimTol_ChamferDimension Then
            Dim chamferAnno As IDimXpertChamferDimTol
            chamferAnno = annotation
            Select Case chamferAnno.ChamferType
                Case swDimXpertChamferDimensionType_e.swDimXpertChamferDimensionType_Angle
                    strs.Add("Chamfer Dimension Type: Angle")
                    isAngleType = True
                Case swDimXpertChamferDimensionType_e.swDimXpertChamferDimensionType_LinearDistance1
                    strs.Add("Chamfer Dimension Type: Distance 1")
                Case swDimXpertChamferDimensionType_e.swDimXpertChamferDimensionType_LinearDistance2
                    strs.Add("Chamfer Dimension Type: Distance 2")
            End Select
        ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertDimTol_AngleBetween Then
            isAngleType = True
            ' the origin and tolerance feature
            strs.Add("Origin Feature: " + annotation.OriginFeature.Name)
            ' is supplement angle
            strs.Add("Supplement Angle: " + IIf(annotation.Supplement, "True", "False"))
        ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertDimTol_CounterSinkAngle Then
            Dim csAngle As IDimXpertCounterSinkAngleDimTol
            csAngle = annotation
            isAngleType = True
            If csAngle.ReferenceFeature Is Nothing Then
                strs.Add("Reference Feature: NULL")
            Else
                strs.Add("Reference Feature: " + csAngle.ReferenceFeature.Name)
            End If
        ElseIf annoType = swDimXpertAnnotationType_e.swDimXpertDimTol_ConeAngle Then
            isAngleType = True
        End If
        ' conversion for radians to degrees when dimension type is angle
        Dim dbl As Double
        If isAngleType Then
            dbl = 57.2957795130823
        Else
            dbl = 1.0#
        End If
        ' the nominal, and upper and lower limits of size of the dimension
        strs.Add("")
        strs.Add("Compute Nominal Dimension: " + FormatDouble(annotation.GetNominalValue * dbl))
        boolstatus = annotation.GetUpperAndLowerLimit(upper, lower)
        strs.Add("Get Upper Limit: " + FormatDouble(upper * dbl))
        strs.Add("Get Lower Limit: " + FormatDouble(lower * dbl))
        ' the upper and lower tolerance value by type
        Select Case annotation.DimensionType
            Case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_BlockTolerance
                strs.Add("Dimension Type: Block Tolerance")
                ' block tolerance
            Case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_BlockToleranceNoNominal
                Dim blockTols As DimXpertBlockTolerances
                blockTols = dimXpertPart.GetBlockTolerances
                Select Case blockTols.Type
                    Case swDimXpertBlockToleranceType_e.swDimXpertBlockToleranceType_ASMEInch
                        strs.Add("Dimension Type: Block Tolerance No Nominal")
                        If isAngleType Then
                            strs.Add("Angular Block Tolerance")
                        Else
                            strs.Add("Block Tolerance Decimal Places: " + Format(annotation.BlockToleranceDecimalPlaces, "##,##0"))
                        End If
                    Case swDimXpertBlockToleranceType_e.swDimXpertBlockToleranceType_ISO2768
                        strs.Add("Dimension Type: General Tolerance")
                End Select
            Case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_ISOLimitsAndFits
                strs.Add("Dimension Type: Limits and Fits")
                ' limits and fits tolerance
            Case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_ISOLimitsAndFitsNoNominal
                strs.Add("Dimension Type: Limits and Fits No Nominal")
                strs.Add("Limits and Fits: " + annotation.LimitsAndFitsCode)
                ' limit dimension
            Case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_LimitDimension
                strs.Add("Dimension Type: Limit Dimension")
                boolstatus = annotation.GetUpperAndLowerLimit(upper, lower)
                strs.Add("Get Upper Limit: " + FormatDouble(upper * dbl))
                strs.Add("Get Lower Limit: " + FormatDouble(lower * dbl))
            Case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_MAXTolerance
                strs.Add("Dimension Type: MAXTolerance")
            Case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_MINTolerance
                strs.Add("Dimension Type: MINTolerance")
            Case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_NoTolerance
                strs.Add("Dimension Type: NoTolerance")
            Case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_PlusMinusDimension
                strs.Add("Dimension Type: Plus Minus Dimension")
                ' plus and minus dimension
            Case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_PlusMinusNoNominal
                strs.Add("Dimension Type: Plus Minus No Nominal")
                boolstatus = annotation.GetPlusAndMinusTolerance(plus, minus)
                strs.Add("Plus  Tolerance: " + FormatDouble(plus * dbl))
                strs.Add("Minus Tolerance: " + FormatDouble(minus * dbl))
        End Select
    End Sub
    Private Sub DistanceBetweenData(ByVal annotation As DimXpertDistanceBetweenDimTol)
        Dim feature As DimXpertFeature
        Dim featureFosUsage As Long
        Dim I As Double, J As Double, K As Double
        Dim boolstatus As Boolean
        feature = Nothing
        ' the origin and tolerance feature along with their feature of size usage (min, max, center)
        boolstatus = annotation.GetOriginFeature(feature, featureFosUsage)
        strs.Add("")
        strs.Add("Origin Feature: " + feature.Name + " @ " + FosUsage(featureFosUsage))
        boolstatus = annotation.GetFeature(feature, featureFosUsage)
        strs.Add("Tolerance Feature: " + feature.Name + " @ " + FosUsage(featureFosUsage))
        ' The direction vector
        boolstatus = annotation.GetDirectionVector(I, J, K)
        strs.Add("")
        strs.Add("Direction Vector: " + FormatVector(I, J, K))
    End Sub
    Private Sub CompositeDistanceBetweenData(ByVal annotation As DimXpertCompositeDistanceBetweenDimTol)
        Dim feature As DimXpertFeature
        Dim featureFosUsage As Long
        Dim plus As Double, minus As Double
        Dim I As Double, J As Double, K As Double
        Dim boolstatus As Boolean
        feature = Nothing
        ' the origin and tolerance feature along with their feature of size usage (min, max, center)
        boolstatus = annotation.GetOriginFeature(feature, featureFosUsage)
        strs.Add("")
        strs.Add("Origin Feature: " + feature.Name + " @ " + FosUsage(featureFosUsage))
        boolstatus = annotation.GetFeature(feature, featureFosUsage)
        strs.Add("Tolerance Feature: " + feature.Name + " @ " + FosUsage(featureFosUsage))
        ' the pattern locating feature
        boolstatus = annotation.GetIntraFeature(feature, featureFosUsage)
        strs.Add("Pattern Locating Feature: " + feature.Name + " @ " + FosUsage(featureFosUsage))
        ' The direction vector
        boolstatus = annotation.GetDirectionVector(I, J, K)
        strs.Add("")
        strs.Add("Direction Vector: " + FormatVector(I, J, K))
        ' the upper and lower tolerance value for the pattern location by type
        Dim dimTol As IDimXpertDimensionTolerance
        dimTol = annotation
        Select Case dimTol.DimensionType
            ' plus and minus dimension
            Case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_PlusMinusNoNominal
                dimTol.GetPlusAndMinusTolerance(plus, minus)
                strs.Add("Pattern Locating Dimension Type:  Plus Minus No Nominal")
                strs.Add("  Plus  Tolerance: " + FormatDouble(plus))
                strs.Add("  Minus Tolerance: " + FormatDouble(minus))
                ' block tolerance
            Case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_BlockToleranceNoNominal
                Dim blockTols As DimXpertBlockTolerances
                blockTols = dimXpertPart.GetBlockTolerances
                Select Case blockTols.Type
                    Case swDimXpertBlockToleranceType_e.swDimXpertBlockToleranceType_ASMEInch
                        strs.Add("Pattern Locating Dimension Type: Block Tolerance No Nominal")
                        strs.Add("  Block Tolerance Decimal Places: " + Format(annotation.BlockToleranceDecimalPlaces, "##,##0"))
                    Case swDimXpertBlockToleranceType_e.swDimXpertBlockToleranceType_ISO2768
                        strs.Add("Pattern Locating Dimension Type: General Tolerance")
                End Select
        End Select
        ' the upper and lower tolerance value for the feature to feature location by type
        Select Case annotation.DimensionTypeIntraFeature
            ' plus and minus dimension
            Case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_PlusMinusNoNominal
                strs.Add("Feature Locating Dimension Type: Plus Minus No Nominal")
                boolstatus = annotation.GetPlusAndMinusToleranceIntraFeature(plus, minus)
                strs.Add("  Plus  Tolerance: " + FormatDouble(plus))
                strs.Add("  Minus Tolerance: " + FormatDouble(minus))
                ' block tolerance
            Case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_BlockToleranceNoNominal
                Dim blockTols As DimXpertBlockTolerances
                blockTols = dimXpertPart.GetBlockTolerances
                Select Case blockTols.Type
                    Case swDimXpertBlockToleranceType_e.swDimXpertBlockToleranceType_ASMEInch
                        strs.Add("Feature locating Dimension Type: Block Tolerance No Nominal")
                        strs.Add("  Block Tolerance Decimal Places: " + Format(annotation.BlockToleranceDecimalPlacesIntraFeature, "##,##0"))
                    Case swDimXpertBlockToleranceType_e.swDimXpertBlockToleranceType_ISO2768
                        strs.Add("Feature locating Dimension Type: General Tolerance")
                End Select
        End Select
    End Sub
    Private Sub DatumsStr(ByVal annotation As DimXpertTolerance)
        strs.Add("")
        strs.Add("Datums:")
        Call datumStr(annotation.GetPrimaryDatums(), annotation.GetPrimaryDatumModifiers(), "  Primary:")
        Call datumStr(annotation.GetSecondaryDatums(), annotation.GetSecondaryDatumModifiers(), "  Secondary:")
        Call datumStr(annotation.GetTertiaryDatums(), annotation.GetTertiaryDatumModifiers(), "  Tertiary:")
    End Sub
    Private Sub datumStr(ByVal dats As Object, ByVal mods As Object, ByVal datumOrder As String)
        Dim I As Long
        Dim str As String
        Dim mcm As Long
        If IsNothing(dats) Then
            Exit Sub
        End If
        str = ""
        For I = LBound(dats) To UBound(dats)
            mcm = mods(I)
            str = str + "  " + dats(I).Identifier + " @ " + mcmStr(mcm)
        Next I
        If StrComp(str, "") > 0 Then
            strs.Add(datumOrder + str)
        Else
            strs.Add(datumOrder + " <none>")
        End If
    End Sub
    ' returns a string containing the heith of the projected tolerance zone
    Private Sub FormatProjectedZone(ByVal enabled As Boolean, ByVal height As Double)
        If enabled = True Then
            strs.Add("  Projected Zone:  True")
            strs.Add("  Zone Height: " + FormatDouble(height))
        Else
            strs.Add("  Projected Zone:  False")
        End If
    End Sub
    Private Function mcmStr(ByVal mcm As Long) As String
        Dim str As String
        str = ""
        Select Case mcm
            Case swDimXpertMaterialConditionModifier_e.swDimXpertMCM_LMC
                str = "LMC"
            Case swDimXpertMaterialConditionModifier_e.swDimXpertMCM_MMC
                str = "MMC"
            Case swDimXpertMaterialConditionModifier_e.swDimXpertMCM_NoMCM
                str = "NoMCM"
            Case swDimXpertMaterialConditionModifier_e.swDimXpertMCM_RFS
                str = "RFS"
        End Select
        mcmStr = str
    End Function
    ' returns a string containing the type of position tolerance zone used
    Private Function PositionZoneType(ByVal typ As Long) As String
        Dim str As String
        Select Case typ
            Case swDimXpertPositionZoneType_e.swDimXpertPositionZoneType_CylindricalPosition
                str = "Cylindrical"
            Case swDimXpertPositionZoneType_e.swDimXpertPositionZoneType_PlanarPosition
                str = "Planar"
            Case swDimXpertPositionZoneType_e.swDimXpertPositionZoneType_SphericalPosition
                str = "Spherical"
            Case swDimXpertPositionZoneType_e.swDimXpertPositionZoneType_Boundary
                str = "Boundary"
            Case swDimXpertPositionZoneType_e.swDimXpertPositionZoneType_RadialPositionArc
                str = "RadialPositionArc"
            Case swDimXpertPositionZoneType_e.swDimXpertPositionZoneType_RadialPositionPlanar
                str = "RadialPositionPlanar"
            Case Else
                str = "N/A"
        End Select
        PositionZoneType = str
    End Function
    ' returns a string containing the names of the SW display entities
    Private Function DisplayEntity(ByVal annotation As DimXpertAnnotation) As String
        Dim str As String
        Dim dispEnt As Object
        Dim swAnnot As SolidWorks.Interop.sldworks.Annotation
        str = ""
        'Set dispEnt = swDimXpert.GetDisplayEntity(annot)
        dispEnt = annotation.GetDisplayEntity()
        If Not dispEnt Is Nothing Then
            If TypeOf dispEnt Is SolidWorks.Interop.sldworks.Annotation Then
                swAnnot = dispEnt
                str = swAnnot.GetName
            End If
        End If
        DisplayEntity = str
    End Function
    ' returns a string containing the feature of size usage (min, max, center)
    Private Function FosUsage(ByVal value As Long) As String
        Dim str As String
        Select Case value
            Case swDimXpertDistanceFosUsage_e.swDimXpertDistanceFosUsage_Center
                str = "Center"
            Case swDimXpertDistanceFosUsage_e.swDimXpertDistanceFosUsage_MaximumSide
                str = "Max"
            Case swDimXpertDistanceFosUsage_e.swDimXpertDistanceFosUsage_MinimumSide
                str = "Min"
            Case Else
                str = "N/A"
        End Select
        FosUsage = str
    End Function
    Private Function FormatVector(ByVal I As Double, ByVal J As Double, ByVal K As Double) As String
        Dim str As String
        str = FormatDouble(I) + ", " + FormatDouble(J) + ", " + FormatDouble(K)
        FormatVector = str
    End Function
    Private Function FormatDouble(ByVal value As Double) As String
        Dim str As String
        str = Format(value, "##,##0.0000")
        FormatDouble = str
    End Function
    Private Function RadiansToDegrees(ByVal value As Double) As String
        Dim str As String
        str = Format((value * 57.2957795130823), "##,##0.00")
        RadiansToDegrees = str
    End Function
    Private Function annotationTypeNameFromObject(ByVal anno As DimXpertAnnotation) As String
        annotationTypeNameFromObject = annotationTypeNameFromTypeNumber(anno.Type)
    End Function
    Private Function annotationTypeNameFromTypeNumber(ByVal annoTypeIndex As Long) As String
        Select Case annoTypeIndex
            Case swDimXpertAnnotationType_e.swDimXpertDimTol_DistanceBetween
                annotationTypeNameFromTypeNumber = "DistanceBetween Dim"
            Case swDimXpertAnnotationType_e.swDimXpertDimTol_CounterBore
                annotationTypeNameFromTypeNumber = "CounterBore Dim"
            Case swDimXpertAnnotationType_e.swDimXpertDimTol_Depth
                annotationTypeNameFromTypeNumber = "Depth Dim"
            Case swDimXpertAnnotationType_e.swDimXpertDimTol_CounterSinkDiameter
                annotationTypeNameFromTypeNumber = "CounterSinkDiameter Dim"
            Case swDimXpertAnnotationType_e.swDimXpertDimTol_ChamferDimension
                annotationTypeNameFromTypeNumber = "ChamferDimension Dim"
            Case swDimXpertAnnotationType_e.swDimXpertDimTol_AngleBetween
                annotationTypeNameFromTypeNumber = "AngleBetween Dim"
            Case swDimXpertAnnotationType_e.swDimXpertDimTol_CounterSinkAngle
                annotationTypeNameFromTypeNumber = "CounterSinkAngle Dim"
            Case swDimXpertAnnotationType_e.swDimXpertDimTol_ConeAngle
                annotationTypeNameFromTypeNumber = "ConeAngle Dim"
            Case swDimXpertAnnotationType_e.swDimXpertDimTol_Diameter
                annotationTypeNameFromTypeNumber = "Diameter Dim"
            Case swDimXpertAnnotationType_e.swDimXpertDimTol_Length
                annotationTypeNameFromTypeNumber = "Length Dim"
            Case swDimXpertAnnotationType_e.swDimXpertDimTol_Radius
                annotationTypeNameFromTypeNumber = "Radius Dim"
            Case swDimXpertAnnotationType_e.swDimXpertDimTol_Width
                annotationTypeNameFromTypeNumber = "Width Dim"
            Case swDimXpertAnnotationType_e.swDimXpertDimTol_CompositeDistanceBetween
                annotationTypeNameFromTypeNumber = "CompositeDistanceBetween Dim"
            Case swDimXpertAnnotationType_e.swDimXpertDatum
                annotationTypeNameFromTypeNumber = "Datum"
            Case swDimXpertAnnotationType_e.swDimXpertGeoTol_Position
                annotationTypeNameFromTypeNumber = "Position Tol"
            Case swDimXpertAnnotationType_e.swDimXpertGeoTol_CompositePosition
                annotationTypeNameFromTypeNumber = "CompositePosition Tol"
            Case swDimXpertAnnotationType_e.swDimXpertGeoTol_Symmetry
                annotationTypeNameFromTypeNumber = "Symmetry Tol"
            Case swDimXpertAnnotationType_e.swDimXpertGeoTol_Concentricity
                annotationTypeNameFromTypeNumber = "Concentricity Tol"
            Case swDimXpertAnnotationType_e.swDimXpertGeoTol_LineProfile
                annotationTypeNameFromTypeNumber = "LineProfile Tol"
            Case swDimXpertAnnotationType_e.swDimXpertGeoTol_CompositeLineProfile
                annotationTypeNameFromTypeNumber = "CompositeLineProfile Tol"
            Case swDimXpertAnnotationType_e.swDimXpertGeoTol_SurfaceProfile
                annotationTypeNameFromTypeNumber = "SurfaceProfile Tol"
            Case swDimXpertAnnotationType_e.swDimXpertGeoTol_CompositeSurfaceProfile
                annotationTypeNameFromTypeNumber = "CompositeSurfaceProfile Tol"
            Case swDimXpertAnnotationType_e.swDimXpertGeoTol_Angularity
                annotationTypeNameFromTypeNumber = "Angularity Tol"
            Case swDimXpertAnnotationType_e.swDimXpertGeoTol_Parallelism
                annotationTypeNameFromTypeNumber = "Parallelism Tol"
            Case swDimXpertAnnotationType_e.swDimXpertGeoTol_Perpendicularity
                annotationTypeNameFromTypeNumber = "Perpendicularity Tol"
            Case swDimXpertAnnotationType_e.swDimXpertGeoTol_TotalRunout
                annotationTypeNameFromTypeNumber = "TotalRunout Tol"
            Case swDimXpertAnnotationType_e.swDimXpertGeoTol_CircularRunout
                annotationTypeNameFromTypeNumber = "CircularRunout Tol"
            Case swDimXpertAnnotationType_e.swDimXpertGeoTol_Flatness
                annotationTypeNameFromTypeNumber = "Flatness Tol"
            Case swDimXpertAnnotationType_e.swDimXpertGeoTol_Circularity
                annotationTypeNameFromTypeNumber = "Circularity Tol"
            Case swDimXpertAnnotationType_e.swDimXpertGeoTol_Cylindricity
                annotationTypeNameFromTypeNumber = "Cylindricity Tol"
            Case swDimXpertAnnotationType_e.swDimXpertGeoTol_Straightness
                annotationTypeNameFromTypeNumber = "Straightness Tol"
            Case swDimXpertAnnotationType_e.swDimXpertGeoTol_Tangency
                annotationTypeNameFromTypeNumber = "Tangency Tol"
            Case Else
                annotationTypeNameFromTypeNumber = "<unknown> " & CStr(annoTypeIndex)
        End Select
    End Function
    Public swApp As SldWorks
End Class
```
