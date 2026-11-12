---
title: "DimXpert Annotation Data Module Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/DimXpert_AnnotationData_Module_CSharp.htm"
---

# DimXpert Annotation Data Module Example (C#)

```vb
// This module is a component of
// Get DimXpert Features and Annotations in a Model Example (C#).

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swdimxpert;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
using System.Collections.Generic;
using System.Collections.ObjectModel;
public class DimXpertAnnotationData
{
    // Returns a collection of Strings containing the annotations data
    private Collection<string> strs = new Collection<string>();
    public void Clear(Collection<string> strs)
    {
        strs.Remove(strs[strs.Count]);
        if (!(strs.Count == 0))
        {
            Clear(strs);
        }
    }
    public Collection<string> AnnotationData(DimXpertAnnotation annotation, SolidWorks.Interop.swdimxpert.DimXpertPart dimXpertPart)
    {
        swDimXpertAnnotationType_e annoType = default(swDimXpertAnnotationType_e);

        if ((!(strs.Count == 0)))
        {
            Clear(strs);
        }
        //General info
        GeneralInfo(annotation);
        annoType = annotation.Type;
        if (annoType == swDimXpertAnnotationType_e.swDimXpertDatum)
        {
            DatumData((DimXpertDatum)annotation);
        }
        else if (annoType == swDimXpertAnnotationType_e.swDimXpertGeoTol_Position)
        {
            PositionData((DimXpertPositionTolerance)annotation);
        }
        else if (annoType == swDimXpertAnnotationType_e.swDimXpertGeoTol_CompositePosition)
        {
            CompositePositionData((DimXpertCompositePositionTolerance)annotation);
        }
        else if (annoType == swDimXpertAnnotationType_e.swDimXpertGeoTol_Symmetry)
        {
            SymmetryData((DimXpertSymmetryTolerance)annotation);
        }
        else if (annoType == swDimXpertAnnotationType_e.swDimXpertGeoTol_Concentricity)
        {
            ConcentricityData((DimXpertConcentricityTolerance)annotation);
        }
        else if (annoType == swDimXpertAnnotationType_e.swDimXpertGeoTol_LineProfile)
        {
            LineProfileData((DimXpertLineProfileTolerance)annotation);
        }
        else if (annoType == swDimXpertAnnotationType_e.swDimXpertGeoTol_CompositeLineProfile)
        {
            CompositeLineProfileData((DimXpertCompositeLineProfileTolerance)annotation);
        }
        else if (annoType == swDimXpertAnnotationType_e.swDimXpertGeoTol_SurfaceProfile)
        {
            SurfaceProfileData((DimXpertSurfaceProfileTolerance)annotation);
        }
        else if (annoType == swDimXpertAnnotationType_e.swDimXpertGeoTol_CompositeSurfaceProfile)
        {
            CompositeSurfaceProfileData((DimXpertCompositeSurfaceProfileTolerance)annotation);
        }
        else if (annoType == swDimXpertAnnotationType_e.swDimXpertGeoTol_Angularity | annoType ==
swDimXpertAnnotationType_e.swDimXpertGeoTol_Parallelism | annoType ==
swDimXpertAnnotationType_e.swDimXpertGeoTol_Perpendicularity)
        {
            OrientationData((DimXpertOrientationTolerance)annotation);
        }
        else if (annoType == swDimXpertAnnotationType_e.swDimXpertGeoTol_TotalRunout)
        {
            TotalRunoutData((DimXpertTolerance)annotation);
        }
        else if (annoType == swDimXpertAnnotationType_e.swDimXpertGeoTol_CircularRunout)
        {
            CircularRunoutData((DimXpertTolerance)annotation);
        }
        else if (annoType == swDimXpertAnnotationType_e.swDimXpertGeoTol_Flatness)
        {
            FlatnessData((DimXpertFlatnessTolerance)annotation);
        }
        else if (annoType == swDimXpertAnnotationType_e.swDimXpertGeoTol_Circularity)
        {
            CircularityData((DimXpertTolerance)annotation);
        }
        else if (annoType == swDimXpertAnnotationType_e.swDimXpertGeoTol_Cylindricity)
        {
            CylindricityData((DimXpertTolerance)annotation);
        }
        else if (annoType == swDimXpertAnnotationType_e.swDimXpertGeoTol_Straightness)
        {
            StraightnessData((DimXpertStraightnessTolerance)annotation);
        }
        else if (annoType == swDimXpertAnnotationType_e.swDimXpertGeoTol_Tangency)
        {
            TangencyData((DimXpertTangencyTolerance)annotation);
        }
        // any of the dimension tolerance types
        else
        {
            DimensionToleranceData((DimXpertDimensionTolerance)annotation, (DimXpertPart) dimXpertPart);
        }
        return strs;
    }
    private void GeneralInfo(DimXpertAnnotation annotation)
    {
        string annoType = null;
        Feature modelObj = default(Feature);
        strs.Add("Name: " + annotation.Name);
        annoType = annotationTypeNameFromObject(annotation);
        strs.Add("Type: " + annoType);
        strs.Add("Display Entity: " + DisplayEntity(annotation));
        strs.Add("Is Suppressed: " + (annotation.IsSuppressed() ? "True" : "False"));
        strs.Add("Inspection Dimension: " + (annotation.IsToBeInspected() ? "True" : "False"));
        strs.Add("Is Statistical: " + (annotation.IsStatistical() ? "True" : "False"));
        strs.Add("Is FreeState: " + (annotation.IsFreeState() ? "True" : "False"));
        modelObj = (Feature)annotation.GetModelFeature();
        if ((modelObj != null))
        {
            strs.Add("ModelFeature: " + modelObj.Name + " (" + modelObj.GetTypeName2() + ")");
        }
    }
    private void DatumData(DimXpertDatum annotation)
    {
        // the datum letter
        strs.Add("");
        strs.Add("Datum Letter: " + annotation.Identifier);
    }
    private void PositionData(DimXpertPositionTolerance annotation)
    {
        double I = 0;
        double J = 0;
        double K = 0;
        bool enabled = false;
        double value = 0;
        bool boolstatus = false;
        strs.Add("");
        strs.Add("Tolerance Compartment:");
        // the shape of the tolerance zone
        strs.Add(" Zone Type: " + PositionZoneType((long)annotation.ZoneType));
        // the zone vector if the tolerance zone is planar
        if (annotation.ZoneType == swDimXpertPositionZoneType_e.swDimXpertPositionZoneType_PlanarPosition)
        {
            boolstatus = annotation.GetPlanarZoneVector(ref I, ref J, ref K);
            strs.Add(" Direction: " + FormatVector(I, J, K));
        }
        // the tolerance value
        DimXpertTolerance tol;
        tol = (DimXpertTolerance)annotation;
        strs.Add(" Max Tolerance: " + FormatDouble(tol.Tolerance));
        // the material condition modifer applied to feature
        strs.Add(" Modifier: " + mcmStr((long)annotation.Modifier));
        // the projected tolerance zone when specified
        boolstatus = annotation.GetProjectedZone(ref enabled, ref value);
        FormatProjectedZone(enabled, value);
        // the datum reference frame
        DatumsStr((DimXpertTolerance)annotation);
    }
    private void CompositePositionData(DimXpertCompositePositionTolerance annotation)
    {
        double I = 0;
        double J = 0;
        double K = 0;
        bool enabled = false;
        double value = 0;
        bool boolstatus = false;
        strs.Add("");
        strs.Add("Tolerance Compartment");
        // the shape of the tolerance zone
        strs.Add(" Zone Type: " + PositionZoneType((long)annotation.ZoneType));
        // the zone vector when the zone is planar
        if (annotation.ZoneType == swDimXpertPositionZoneType_e.swDimXpertPositionZoneType_PlanarPosition)
        {
            boolstatus = annotation.GetPlanarZoneVector(ref I, ref J, ref K);
            strs.Add(" Direction: " + FormatVector(I, J, K));
        }
        // the tolerance value
        DimXpertTolerance tol;
        tol = (DimXpertTolerance)annotation;
        strs.Add(" Tolerance: " + FormatDouble(tol.Tolerance));
        // the material condition modifer
        strs.Add(" Modifier: " + mcmStr((long)annotation.Modifier));
        // the projected tolerance zone when specified
        boolstatus = annotation.GetProjectedZone(ref enabled, ref value);
        FormatProjectedZone(enabled, value);
        // the datum reference frame for the pattern location
        DatumsStr((DimXpertTolerance)annotation);
        // the datum reference frame for the feature to feature location
        strs.Add("Composite datums:");
        strs.Add(" Repeat Primary: " + (annotation.PrimaryInLowerTier ? "True" : "False"));
        strs.Add(" Repeat Secondary: " + (annotation.SecondaryInLowerTier ? "True" : "False"));
        strs.Add(" Repeat Tertiary: " + (annotation.TertiaryInLowerTier ? "True" : "False"));
    }
    private void SymmetryData(DimXpertSymmetryTolerance annotation)
    {
        double I = 0;
        double J = 0;
        double K = 0;
        bool boolstatus = false;
        strs.Add("");
        strs.Add("Tolerance Compartment");
        // the tolerance value
        DimXpertTolerance tol;
        tol = (DimXpertTolerance)annotation;
        strs.Add(" Tolerance: " + FormatDouble(tol.Tolerance));
        // the material condition modifer applied to feature
        strs.Add(" Modifier: " + mcmStr((long)annotation.Modifier));
        // the datum reference frame
        strs.Add("");
        DatumsStr((DimXpertTolerance)annotation);
        // the direction of the planar zone
        strs.Add("");
        boolstatus = annotation.GetZoneDirection(ref I, ref J, ref K);
        strs.Add("Planar Zone Direction: " + FormatVector(I, J, K));
    }
    private void ConcentricityData(DimXpertConcentricityTolerance annotation)
    {
        strs.Add("");
        strs.Add("Tolerance Compartment");
        // the tolerance value
        DimXpertTolerance tol;
        tol = (DimXpertTolerance)annotation;
        strs.Add(" Tolerance: " + FormatDouble(tol.Tolerance));
        // the material condition modifer applied to feature
        strs.Add(" Modifier: " + mcmStr((long)annotation.Modifier));
        // the datum reference frame
        DatumsStr((DimXpertTolerance)annotation);
    }
    private void TotalRunoutData(DimXpertTolerance annotation)
    {
        strs.Add("");
        strs.Add("Tolerance Compartment");
        // the tolerance value
        DimXpertTolerance tol;
        tol = (DimXpertTolerance)annotation;
        strs.Add(" Tolerance: " + FormatDouble(tol.Tolerance));
        // the datum reference frame
        DatumsStr(annotation);
    }
    private void CircularRunoutData(DimXpertTolerance annotation)
    {
        strs.Add("");
        strs.Add("Tolerance Compartment");
        // the tolerance value
        DimXpertTolerance tol;
        tol = (DimXpertTolerance)annotation;
        strs.Add(" Tolerance: " + FormatDouble(tol.Tolerance));
        // the datum reference frame
        DatumsStr(annotation);
    }
    private void LineProfileData(DimXpertLineProfileTolerance annotation)
    {
        double I = 0;
        double J = 0;
        double K = 0;
        bool boolstatus = false;
        strs.Add("");
        strs.Add("Tolerance Compartment");
        // the tolerance value
        DimXpertTolerance tol;
        tol = (DimXpertTolerance)annotation;
        strs.Add(" Tolerance: " + FormatDouble(tol.Tolerance));
        // the outer (outside material) tolerance value
        strs.Add(" Outer Tolerance: " + FormatDouble(annotation.OuterToleranceValue));
        // the vector normal to the profile zones
        strs.Add("");
        boolstatus = annotation.GetPlanarZoneVector(ref I, ref J, ref K);
        strs.Add("Planar Zone Vector: " + FormatVector(I, J, K));
        // the datum reference frame
        DatumsStr((DimXpertTolerance)annotation);
    }
    private void CompositeLineProfileData(DimXpertCompositeLineProfileTolerance annotation)
    {
        bool boolstatus = false;
        double i = 0;
        double j = 0;
        double k = 0;
        strs.Add("");
        strs.Add("Tolerance Compartment");
        // the tolerance value
        DimXpertTolerance tol;
        tol = (DimXpertTolerance)annotation;
        strs.Add(" Tolerance: " + FormatDouble(tol.Tolerance));
        // the outer (outside material) tolerance value
        strs.Add(" Outer Tolerance: " + FormatDouble(annotation.OuterToleranceValue));
        // the vector normal to the profile zones
        strs.Add("");
        boolstatus = annotation.GetPlanarZoneVector(ref i, ref j, ref k);
        strs.Add("Planar Zone Vector: " + FormatVector(i, j, k));
        // the datum reference frame
        DatumsStr((DimXpertTolerance)annotation);
        // the datum reference frame for the orientation and form
        strs.Add("Composite Datums:");
        strs.Add(" Repeat Primary: " + (annotation.PrimaryInLowerTier ? "True" : "False"));
        strs.Add(" Repeat Secondary: " + (annotation.SecondaryInLowerTier ? "True" : "False"));
        strs.Add(" Repeat Tertiary: " + (annotation.TertiaryInLowerTier ? "True" : "False"));
    }
    private void SurfaceProfileData(DimXpertSurfaceProfileTolerance annotation)
    {
        strs.Add("");
        strs.Add("Tolerance Compartment");
        // the tolerance value
        DimXpertTolerance tol;
        tol = (DimXpertTolerance)annotation;
        strs.Add(" Tolerance: " + FormatDouble(tol.Tolerance));
        // the outer (outside material) tolerance value
        strs.Add(" Outer Tolerance: " + FormatDouble(annotation.OuterToleranceValue));
        // the datum reference frame
        DatumsStr((DimXpertTolerance)annotation);
    }
    private void CompositeSurfaceProfileData(DimXpertCompositeSurfaceProfileTolerance annotation)
    {
        strs.Add("");
        strs.Add("Tolerance Compartment");
        // the tolerance value
        DimXpertTolerance tol;
        tol = (DimXpertTolerance)annotation;
        strs.Add(" Tolerance Upper Tier: " + FormatDouble(tol.Tolerance));
        // the outer tolerance value
        strs.Add(" Outer Tolerance Upper Tier: " + FormatDouble(annotation.OuterToleranceValue));
        // the datum reference frame for the location
        DatumsStr((DimXpertTolerance)annotation);
        // the datum reference frame for the orientation and form
        strs.Add("Composite Datums:");
        strs.Add(" Repeat Primary: " + (annotation.PrimaryInLowerTier ? "True" : "False"));
        strs.Add(" Repeat Secondary: " + (annotation.SecondaryInLowerTier ? "True" : "False"));
        strs.Add(" Repeat Tertiary: " + (annotation.TertiaryInLowerTier ? "True" : "False"));
    }
    private void OrientationData(DimXpertOrientationTolerance annotation)
    {
        double I = 0;
        double J = 0;
        double K = 0;
        bool enabled = false;
        double value = 0;
        SolidWorks.Interop.swdimxpert.swDimXpertAnnotationType_e annoType = default(SolidWorks.Interop.swdimxpert.swDimXpertAnnotationType_e);
        bool boolstatus = false;
        DimXpertAnnotation anno;
        anno = (DimXpertAnnotation)annotation;
        annoType = (SolidWorks.Interop.swdimxpert.swDimXpertAnnotationType_e)anno.Type;
        // the type or orientation tolerance
        if (annoType == swDimXpertAnnotationType_e.swDimXpertGeoTol_Perpendicularity)
        {
            strs.Add("Orientation Type: Perpendicularity");
        }
        else if (annoType == swDimXpertAnnotationType_e.swDimXpertGeoTol_Parallelism)
        {
            strs.Add("Orientation Type: Parallelism");
        }
        else if (annoType == swDimXpertAnnotationType_e.swDimXpertGeoTol_Angularity)
        {
            strs.Add("Orientation Type: Angularity");
        }
        strs.Add("");
        strs.Add("Tolerance Compartment:");
        // the shape of the tolerance zone
        switch (annotation.ZoneType)
        {
            case swDimXpertOrientationZoneType_e.swDimXpertOrientationZoneType_Cylindrical:
                strs.Add(" Zone Type: Cylindrical");
                break;
            case swDimXpertOrientationZoneType_e.swDimXpertOrientationZoneType_Planar:
                strs.Add(" Zone Type: Planar");
                boolstatus = annotation.GetPlanarZoneVector(ref I, ref J, ref K);
                strs.Add("Planar Zone Vector: " + FormatVector(I, J, K));
                break;
        }
        // the tolerance value
        DimXpertTolerance tol;
        tol = (DimXpertTolerance)annotation;
        strs.Add(" Tolerance: " + FormatDouble(tol.Tolerance));
        //material condition modifer applied to feature
        strs.Add(" Modifier: " + mcmStr((long)annotation.Modifier));
        // the projected tolerance zone when specified
        boolstatus = annotation.GetProjectedZone(ref enabled, ref value);
        FormatProjectedZone(enabled, value);
        // is tangent plane
        strs.Add(" IsTangentPlane: " + (annotation.IsTangentPlane() ? "True" : "False"));
        // the datum reference frame
        DatumsStr((DimXpertTolerance)annotation);
    }
    private void FlatnessData(DimXpertFlatnessTolerance annotation)
    {
        bool enabled = false;
        double length = 0;
        double width = 0;
        double I = 0;
        double J = 0;
        double K = 0;
        bool boolstatus = false;
        strs.Add("");
        strs.Add("Tolerance Compartment:");
        // the tolerance value
        DimXpertTolerance tol;
        tol = (DimXpertTolerance)annotation;
        strs.Add(" Tolerance: " + FormatDouble(tol.Tolerance));
        // the per unit area data
        boolstatus = annotation.GetPerUnitArea(ref enabled, ref length, ref width, ref I, ref J, ref K);
        strs.Add(" Per Unit Area: " + (enabled ? "True" : "False"));
        if (enabled)
        {
            strs.Add(" Per Unit Length: " + FormatDouble(length));
            strs.Add(" Per Unit Width: " + FormatDouble(width));
            strs.Add(" Per Unit Direction: " + FormatVector(I, J, K));
        }
    }
    private void CircularityData(DimXpertTolerance annotation)
    {
        strs.Add("");
        strs.Add("Tolerance Compartment");
        // the tolerance value
        DimXpertTolerance tol;
        tol = (DimXpertTolerance)annotation;
        strs.Add(" Tolerance: " + FormatDouble(tol.Tolerance));
    }
    private void CylindricityData(DimXpertTolerance annotation)
    {
        strs.Add("");
        strs.Add("Tolerance Compartment");
        // the tolerance value
        DimXpertTolerance tol;
        tol = (DimXpertTolerance)annotation;
        strs.Add(" Tolerance: " + FormatDouble(tol.Tolerance));
    }
    private void StraightnessData(DimXpertStraightnessTolerance annotation)
    {
        double I = 0;
        double J = 0;
        double K = 0;
        bool enabled = false;
        double dist = 0;
        bool boolstatus = false;
        //tolerance compartment info
        strs.Add("");
        strs.Add("Tolerance Compartment");
        //type or shape of the tolerance zone
        switch (annotation.ZoneType)
        {
            case swDimXpertStraightnessZoneType_e.swDimXpertStraightnessZoneType_Cylindrical:
                strs.Add(" Zone Type: Cylindrical");
                break;
            case swDimXpertStraightnessZoneType_e.swDimXpertStraightnessZoneType_PlanarMedian:
                strs.Add(" Zone Type: Planar Median");
                break;
            case swDimXpertStraightnessZoneType_e.swDimXpertStraightnessZoneType_Surface:
                strs.Add(" Zone Type: Surface Straightness");
                boolstatus = annotation.GetPlanarZoneVector(ref I, ref J, ref K);
                strs.Add(" Zone Vector: " + FormatVector(I, J, K));
                break;
        }
        // the tolerance value
        DimXpertTolerance tol;
        tol = (DimXpertTolerance)annotation;
        strs.Add(" Tolerance: " + FormatDouble(tol.Tolerance));
        //per unit length
        boolstatus = annotation.GetPerUnitLength(ref enabled, ref dist);
        strs.Add(" Per Unit Length: " + (enabled ? "True" : "False"));
        if (enabled)
        {
            strs.Add(" Per Unit Length Distance: " + FormatDouble(dist));
        }
        // the material condition modifer
        strs.Add(" Modifier: " + mcmStr((long)annotation.Modifier));
    }
    private void ProfileData(DimXpertTolerance annotation)
    {
        strs.Add("");
        strs.Add("Tolerance Compartment");
        // the tolerance value
        DimXpertTolerance tol;
        tol = (DimXpertTolerance)annotation;
        strs.Add(" Tolerance: " + FormatDouble(tol.Tolerance));
        // the datum reference frame
        DatumsStr(annotation);
    }
    private void SurfaceFinishData(DimXpertTolerance annotation)
    {
        strs.Add("");
        strs.Add("Tolerance Compartment");
        // the tolerance value
        DimXpertTolerance tol;
        tol = (DimXpertTolerance)annotation;
        strs.Add(" Tolerance: " + FormatDouble(tol.Tolerance));
    }
    private void TangencyData(DimXpertTangencyTolerance annotation)
    {
        strs.Add("Origin Feature: " + annotation.OriginFeature.Name);
        strs.Add("");
        strs.Add("Tolerance Compartment");
        // the tolerance value
        DimXpertTolerance tol;
        tol = (DimXpertTolerance)annotation;
        strs.Add(" Tolerance: " + FormatDouble(tol.Tolerance));
    }
    private void DimensionToleranceData(DimXpertDimensionTolerance annotation, SolidWorks.Interop.swdimxpert.DimXpertPart dimXpertPart)
    {
        bool isAngleType = false;
        swDimXpertAnnotationType_e annoType = default(swDimXpertAnnotationType_e);
        swDimXpertPatternTreatmentType_e patternTreatment = default(swDimXpertPatternTreatmentType_e);
        double upper = 0;
        double lower = 0;
        double plus = 0;
        double minus = 0;
        bool boolstatus = false;
        DimXpertAnnotation anno;
        anno = (DimXpertAnnotation)annotation;
        annoType = anno.Type;
        isAngleType = false;
        if (annoType == swDimXpertAnnotationType_e.swDimXpertDimTol_DistanceBetween)
        {

            DistanceBetweenData((DimXpertDistanceBetweenDimTol)annotation);
        }
        else if (annoType == swDimXpertAnnotationType_e.swDimXpertDimTol_CompositeDistanceBetween)
        {
            CompositeDistanceBetweenData((DimXpertCompositeDistanceBetweenDimTol)annotation, (DimXpertPart) dimXpertPart);
        }
        else if (annoType == swDimXpertAnnotationType_e.swDimXpertDimTol_CounterBore)
        {
            DimXpertCounterBoreDimTol dimtol;
            dimtol = (DimXpertCounterBoreDimTol)annotation;
            if (dimtol.ReferenceFeature == null)
            {
                strs.Add("Reference Feature: NULL");
            }
            else
            {
                strs.Add("Reference Feature: " + dimtol.ReferenceFeature.Name);
            }
        }
        else if (annoType == swDimXpertAnnotationType_e.swDimXpertDimTol_Depth)
        {
            DimXpertDepthDimTol dimtol;
            dimtol = (DimXpertDepthDimTol)annotation;
            if (dimtol.ReferenceFeature == null)
            {
                strs.Add("Reference Feature: NULL");
            }
            else
            {
                strs.Add("Reference Feature: " + dimtol.ReferenceFeature.Name);
            }
        }
        else if (annoType == swDimXpertAnnotationType_e.swDimXpertDimTol_CounterSinkDiameter)
        {
            DimXpertCounterSinkDiameterDimTol dimtol;
            dimtol = (DimXpertCounterSinkDiameterDimTol)annotation;
            if (dimtol.ReferenceFeature == null)
            {
                strs.Add("Reference Feature: NULL");
            }
            else
            {
                strs.Add("Reference Feature: " + dimtol.ReferenceFeature.Name);
            }
        }
        else if (annoType == swDimXpertAnnotationType_e.swDimXpertDimTol_ChamferDimension)
        {
            DimXpertChamferDimTol chamferDimTol = default(DimXpertChamferDimTol);
            chamferDimTol = (DimXpertChamferDimTol)annotation;
            switch (chamferDimTol.ChamferType)
            {
                case swDimXpertChamferDimensionType_e.swDimXpertChamferDimensionType_Angle:
                    strs.Add("Chamfer Dimension Type: Angle");
                    isAngleType = true;
                    break;
                case swDimXpertChamferDimensionType_e.swDimXpertChamferDimensionType_LinearDistance1:
                    strs.Add("Chamfer Dimension Type: Distance 1");
                    break;
                case swDimXpertChamferDimensionType_e.swDimXpertChamferDimensionType_LinearDistance2:
                    strs.Add("Chamfer Dimension Type: Distance 2");
                    break;
            }
        }
        else if (annoType == swDimXpertAnnotationType_e.swDimXpertDimTol_AngleBetween)
        {
            isAngleType = true;
            DimXpertAngleBetweenDimTol dimtol;
            dimtol = (DimXpertAngleBetweenDimTol)annotation;
            // the origin and tolerance feature
            strs.Add("Origin Feature: " + dimtol.OriginFeature.Name);
            // is supplement angle
            strs.Add("Supplement Angle: " + (dimtol.Supplement ? "True" : "False"));
        }
        else if (annoType == swDimXpertAnnotationType_e.swDimXpertDimTol_CounterSinkAngle)
        {
            isAngleType = true;
            DimXpertCounterSinkAngleDimTol dimtol;
            dimtol = (DimXpertCounterSinkAngleDimTol)annotation;
            if (dimtol.ReferenceFeature == null)
            {
                strs.Add("Reference Feature: NULL");
            }
            else
            {
                strs.Add("Reference Feature: " + dimtol.ReferenceFeature.Name);
            }
        }
        else if (annoType == swDimXpertAnnotationType_e.swDimXpertDimTol_ConeAngle)
        {
            isAngleType = true;
        }
        else if (annoType == swDimXpertAnnotationType_e.swDimXpertDimTol_Radius)
        {
        IDimXpertRadiusDimTol radiusDim;
        radiusDim = (IDimXpertRadiusDimTol)annotation;
        patternTreatment = radiusDim.PatternTreatment;
         //If radiusDim.patternTreatment Is Nothing Then
             //strs.Add ("Pattern Treatment: NULL")
         if (patternTreatment == swDimXpertPatternTreatmentType_e.swDimXpertPatternTreatmentType_unknown)
            {strs.Add ("Pattern Treatment: unknown");}
         else if (patternTreatment == swDimXpertPatternTreatmentType_e.swDimXpertPatternTreatmentType_CircularPattern)
            {strs.Add ("Pattern Treatment: Circular pattern");}
         else if (patternTreatment == swDimXpertPatternTreatmentType_e.swDimXpertPatternTreatmentType_IndividualFeatures)
            {strs.Add ("Pattern Treatment: Individual features");}
        }
        else if (annoType == swDimXpertAnnotationType_e.swDimXpertDimTol_Diameter)
        {
            IDimXpertDiameterDimTol diaDim;
            diaDim = (IDimXpertDiameterDimTol)annotation;
            patternTreatment = diaDim.PatternTreatment;
            //If radiusDim.patternTreatment Is Nothing Then
            //strs.Add ("Pattern Treatment: NULL")
            if (patternTreatment == swDimXpertPatternTreatmentType_e.swDimXpertPatternTreatmentType_unknown)
            { strs.Add("Pattern Treatment: unknown"); }
            else if (patternTreatment == swDimXpertPatternTreatmentType_e.swDimXpertPatternTreatmentType_CircularPattern)
            { strs.Add("Pattern Treatment: Circular pattern"); }
            else if (patternTreatment == swDimXpertPatternTreatmentType_e.swDimXpertPatternTreatmentType_IndividualFeatures)
            { strs.Add("Pattern Treatment: Individual features"); }
```

```vb
Boolean indReq;
 Boolean envReq;
 indReq = diaDim.IndependencyRequirement;
 envReq = diaDim.EnvelopeRequirement;
 strs.Add("Independency is required: " + indReq.ToString());
 strs.Add("Envelope is required: " + envReq.ToString());
```

```vb
        }
        // conversion for radians to degrees when dimension type is angle
        double dbl = 0;
        if (isAngleType)
        {
            dbl = 57.2957795130823;
        }
        else
        {
            dbl = 1.0;
        }
        // the nominal, and upper and lower limits of size of the dimension
        strs.Add("");
        strs.Add("Compute Nominal Dimension: " + FormatDouble(annotation.GetNominalValue() * dbl));
        boolstatus = annotation.GetUpperAndLowerLimit(ref upper, ref lower);
        strs.Add("Get Upper Limit: " + FormatDouble(upper * dbl));
        strs.Add("Get Lower Limit: " + FormatDouble(lower * dbl));
        // the upper and lower tolerance value by type
        switch (annotation.DimensionType)
        {
            case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_BlockTolerance:
                strs.Add("Dimension Type: Block Tolerance");
                break;
            // block tolerance
            case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_BlockToleranceNoNominal:
                DimXpertBlockTolerances blockTols = default(DimXpertBlockTolerances);
                blockTols = dimXpertPart.GetBlockTolerances();
                switch (blockTols.Type)
                {
                    case swDimXpertBlockToleranceType_e.swDimXpertBlockToleranceType_ASMEInch:
                        strs.Add("Dimension Type: Block Tolerance No Nominal");
                        if (isAngleType)
                        {
                            strs.Add("Angular Block Tolerance");
                        }
                        else
                        {
                            strs.Add("Block Tolerance Decimal Places: " +
System.String.Format("{0:N}", annotation.BlockToleranceDecimalPlaces.ToString()));
                        }
                        break;
                    case swDimXpertBlockToleranceType_e.swDimXpertBlockToleranceType_ISO2768:
                        strs.Add("Dimension Type: General Tolerance");
                        break;
                }
                break;
            case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_ISOLimitsAndFits:
                strs.Add("Dimension Type: Limits and Fits");
                break;
            // limits and fits tolerance
            case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_ISOLimitsAndFitsNoNominal:
                strs.Add("Dimension Type: Limits and Fits No Nominal");
                strs.Add("Limits and Fits: " + annotation.LimitsAndFitsCode);
                break;
            // limit dimension
            case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_LimitDimension:
                strs.Add("Dimension Type: Limit Dimension");
                boolstatus = annotation.GetUpperAndLowerLimit(ref upper, ref lower);
                strs.Add("Get Upper Limit: " + FormatDouble(upper * dbl));
                strs.Add("Get Lower Limit: " + FormatDouble(lower * dbl));
                break;
            case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_MAXTolerance:
                strs.Add("Dimension Type: MAXTolerance");
                break;
            case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_MINTolerance:
                strs.Add("Dimension Type: MINTolerance");
                break;
            case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_NoTolerance:
                strs.Add("Dimension Type: NoTolerance");
                break;
            case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_PlusMinusDimension:
                strs.Add("Dimension Type: Plus Minus Dimension");
                break;
            // plus and minus dimension
            case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_PlusMinusNoNominal:
                strs.Add("Dimension Type: Plus Minus No Nominal");
                boolstatus = annotation.GetPlusAndMinusTolerance(ref plus, ref minus);
                strs.Add("Plus Tolerance: " + FormatDouble(plus * dbl));
                strs.Add("Minus Tolerance: " + FormatDouble(minus * dbl));
                break;
        }
    }
    private void DistanceBetweenData(DimXpertDistanceBetweenDimTol annotation)
    {
        DimXpertFeature feature = default(DimXpertFeature);
        swDimXpertDistanceFosUsage_e featureFosUsage = default(swDimXpertDistanceFosUsage_e);
        double I = 0;
        double J = 0;
        double K = 0;
        bool boolstatus = false;
        feature = null;
        // the origin and tolerance feature along with their feature of size usage (min, max, center)
        boolstatus = annotation.GetOriginFeature(ref feature, ref featureFosUsage);
        strs.Add("");
        strs.Add("Origin Feature: " + feature.Name + " @ " + FosUsage(featureFosUsage));
        boolstatus = annotation.GetFeature(ref feature, ref featureFosUsage);
        strs.Add("Tolerance Feature: " + feature.Name + " @ " + FosUsage(featureFosUsage));
        // The direction vector
        boolstatus = annotation.GetDirectionVector(ref I, ref J, ref K);
        strs.Add("");
        strs.Add("Direction Vector: " + FormatVector(I, J, K));

    }
    private void CompositeDistanceBetweenData(DimXpertCompositeDistanceBetweenDimTol annotation, SolidWorks.Interop.swdimxpert.DimXpertPart dimXpertPart)
    {
        DimXpertFeature feature = default(DimXpertFeature);
        swDimXpertDistanceFosUsage_e featureFosUsage = default(swDimXpertDistanceFosUsage_e);
        double plus = 0;
        double minus = 0;
        double I = 0;
        double J = 0;
        double K = 0;
        bool boolstatus = false;
        bool isAngleType = false;
        DimXpertBlockTolerances blockTols = default(DimXpertBlockTolerances);
        isAngleType = false;
        // conversion for radians to degrees when dimension type is angle
        double dbl = 0;
        if (isAngleType)
        {
            dbl = 57.2957795130823;
        }
        else
        {
            dbl = 1.0;
        }
        feature = null;
        // the origin and tolerance feature along with their feature of size usage (min, max, center)
        boolstatus = annotation.GetOriginFeature(ref feature, ref featureFosUsage);
        strs.Add("");
        strs.Add("Origin Feature: " + feature.Name + " @ " + FosUsage(featureFosUsage));
        boolstatus = annotation.GetFeature(ref feature, ref featureFosUsage);
        strs.Add("Tolerance Feature: " + feature.Name + " @ " + FosUsage(featureFosUsage));
        // the pattern locating feature
        boolstatus = annotation.GetIntraFeature(ref feature, ref featureFosUsage);
        strs.Add("Pattern Locating Feature: " + feature.Name + " @ " + FosUsage(featureFosUsage));
        // The direction vector
        boolstatus = annotation.GetDirectionVector(ref I, ref J, ref K);
        strs.Add("");
        strs.Add("Direction Vector: " + FormatVector(I, J, K));

        // the upper and lower tolerance value for the pattern location by type
        DimXpertDimensionTolerance dimTol = default(DimXpertDimensionTolerance);
        dimTol = null;
        dimTol = (DimXpertDimensionTolerance)annotation;
        switch (dimTol.DimensionType)
        {
            // plus and minus dimension
            case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_PlusMinusNoNominal:
                strs.Add("Pattern Locating Dimension Type: Plus Minus No Nominal");
                boolstatus = dimTol.GetPlusAndMinusTolerance(ref plus, ref minus);
                strs.Add(" Plus Tolerance: " + FormatDouble(plus));
                strs.Add(" Minus Tolerance: " + FormatDouble(minus));
                break;
            // block tolerance
            case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_BlockToleranceNoNominal:
                blockTols = dimXpertPart.GetBlockTolerances();
                switch (blockTols.Type)
                {
                    case swDimXpertBlockToleranceType_e.swDimXpertBlockToleranceType_ASMEInch:
                        strs.Add("Pattern Locating Dimension Type: Block Tolerance No Nominal");
                        strs.Add(" Block Tolerance Decimal Places: " +
System.String.Format("{0:N}", dimTol.BlockToleranceDecimalPlaces.ToString()));
                        break;
                    case swDimXpertBlockToleranceType_e.swDimXpertBlockToleranceType_ISO2768:
                        strs.Add("Pattern Locating Dimension Type: General Tolerance");
                        break;
                }
                break;
        }
        // the upper and lower tolerance value for the feature to feature location by type
        switch (annotation.DimensionTypeIntraFeature)
        {
            // plus and minus dimension
            case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_PlusMinusNoNominal:
                strs.Add("Feature Locating Dimension Type: Plus Minus No Nominal");
                boolstatus = annotation.GetPlusAndMinusToleranceIntraFeature(ref plus, ref minus);
                strs.Add(" Plus Tolerance: " + FormatDouble(plus * dbl));
                strs.Add(" Minus Tolerance: " + FormatDouble(minus * dbl));
                break;
            // block tolerance
            case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_BlockToleranceNoNominal:
                blockTols = dimXpertPart.GetBlockTolerances();
                switch (blockTols.Type)
                {

                    case swDimXpertBlockToleranceType_e.swDimXpertBlockToleranceType_ASMEInch:
                        strs.Add("Feature locating Dimension Type: Block Tolerance No Nominal");
                        strs.Add(" Block Tolerance Decimal Places: " +
System.String.Format("{0:N}", annotation.BlockToleranceDecimalPlacesIntraFeature.ToString()));
                        break;
                    case swDimXpertBlockToleranceType_e.swDimXpertBlockToleranceType_ISO2768:
                        strs.Add("Feature locating Dimension Type: General Tolerance");
                        break;
                }
                break;
        }
    }
    private void DatumsStr(DimXpertTolerance annotation)
    {
        strs.Add("");
        strs.Add("Datums:");
        datumStr((object[])annotation.GetPrimaryDatums(), (int[])annotation.GetPrimaryDatumModifiers(), " Primary:");
        datumStr((object[])annotation.GetSecondaryDatums(), (int[])annotation.GetSecondaryDatumModifiers(), " Secondary:");
        datumStr((object[])annotation.GetTertiaryDatums(), (int[])annotation.GetTertiaryDatumModifiers(), " Tertiary:");
    }
    private void datumStr(object[] dats, int[] mods, string datumOrder)
    {
        long I = 0;
        string str = null;
        long mcm = 0;

        if ((dats == null))
        {
            return;
        }
        str = "";
        for (I = dats.GetLowerBound(0); I <= dats.GetUpperBound(0); I++)
        {
            mcm = (long)mods[I];
            DimXpertDatum datum;
            datum = (DimXpertDatum)dats[I];
            str = str + " " + datum.Identifier + " @ " + mcmStr(mcm);
        }
        if (System.String.Compare(str, "") > 0)
        {
            strs.Add(datumOrder + str);
        }
        else
        {
            strs.Add(datumOrder + " <none>");
        }
    }
    // returns a string containing the height of the projected tolerance zone
    private void FormatProjectedZone(bool enabled, double height)
    {
        if (enabled == true)
        {
            strs.Add(" Projected Zone: True");
            strs.Add(" Zone Height: " + FormatDouble(height));
        }
        else
        {
            strs.Add(" Projected Zone: False");
        }
    }
    private string mcmStr(long mcm)
    {
        string str = null;
        str = "";
        switch ((swDimXpertMaterialConditionModifier_e)mcm)
        {
            case swDimXpertMaterialConditionModifier_e.swDimXpertMCM_LMC:
                str = "LMC";
                break;
            case swDimXpertMaterialConditionModifier_e.swDimXpertMCM_MMC:
                str = "MMC";
                break;
            case swDimXpertMaterialConditionModifier_e.swDimXpertMCM_NoMCM:
                str = "NoMCM";
                break;
            case swDimXpertMaterialConditionModifier_e.swDimXpertMCM_RFS:
                str = "RFS";
                break;
        }
        return str;
    }
    // returns a string containing the type of position tolerance zone used
    private string PositionZoneType(long typ)
    {
        string str = null;
        str = "";
        switch ((swDimXpertPositionZoneType_e)typ)
        {
            case swDimXpertPositionZoneType_e.swDimXpertPositionZoneType_CylindricalPosition:
                str = "Cylindrical";
                break;
            case swDimXpertPositionZoneType_e.swDimXpertPositionZoneType_PlanarPosition:
                str = "Planar";
                break;
            case swDimXpertPositionZoneType_e.swDimXpertPositionZoneType_SphericalPosition:
                str = "Spherical";
                break;
            case swDimXpertPositionZoneType_e.swDimXpertPositionZoneType_Boundary:
                str = "Boundary";
                break;
            case swDimXpertPositionZoneType_e.swDimXpertPositionZoneType_RadialPositionArc:
                str = "RadialPositionArc";
                break;
            case swDimXpertPositionZoneType_e.swDimXpertPositionZoneType_RadialPositionPlanar:
                str = "RadialPositionPlanar";
                break;
            default:
                str = "N/A";
                break;
        }
        return str;
    }
    // returns a string containing the names of the SW display entities
    private string DisplayEntity(DimXpertAnnotation annotation)
    {
        string str = null;
        object dispEnt = null;
        Annotation swAnnot = default(Annotation);
        str = "";
        dispEnt = annotation.GetDisplayEntity();
        if ((dispEnt != null))
        {
            if (dispEnt is Annotation)
            {
                swAnnot = (Annotation)dispEnt;
                str = (String)swAnnot.GetName();
            }
        }
        return str;
    }
    // returns a string containing the feature of size usage (min, max, center)
    private string FosUsage(swDimXpertDistanceFosUsage_e value)
    {
        string str = null;
        str = "";
        switch (value)
        {
            case swDimXpertDistanceFosUsage_e.swDimXpertDistanceFosUsage_Center:
                str = "Center";
                break;
            case swDimXpertDistanceFosUsage_e.swDimXpertDistanceFosUsage_MaximumSide:
                str = "Max";
                break;
            case swDimXpertDistanceFosUsage_e.swDimXpertDistanceFosUsage_MinimumSide:
                str = "Min";
                break;
            default:
                str = "N/A";
                break;
        }
        return str;
    }
    private string FormatVector(double I, double J, double K)
    {
        string str = null;
        str = FormatDouble(I) + ", " + FormatDouble(J) + ", " + FormatDouble(K);
        return str;
    }
    private string FormatDouble(double value)
    {
        string str = null;
        str = System.String.Format("{0:D}", value.ToString());
        return str;
    }
    private string RadiansToDegrees(double value)
    {
        string str = null;
        str = System.String.Format("{0:D}", (value * 57.2957795130823).ToString());
        return str;
    }
    private string annotationTypeNameFromObject(DimXpertAnnotation anno)
    {
        return annotationTypeNameFromTypeNumber(anno.Type);
    }
    private string annotationTypeNameFromTypeNumber(swDimXpertAnnotationType_e annoTypeIndex)
    {
        string functionReturnValue = null;
        switch (annoTypeIndex)
        {
            case swDimXpertAnnotationType_e.swDimXpertDimTol_DistanceBetween:
                functionReturnValue = "DistanceBetween Dim";
                break;
            case swDimXpertAnnotationType_e.swDimXpertDimTol_CounterBore:
                functionReturnValue = "CounterBore Dim";
                break;
            case swDimXpertAnnotationType_e.swDimXpertDimTol_Depth:
                functionReturnValue = "Depth Dim";
                break;
            case swDimXpertAnnotationType_e.swDimXpertDimTol_CounterSinkDiameter:
                functionReturnValue = "CounterSinkDiameter Dim";
                break;
            case swDimXpertAnnotationType_e.swDimXpertDimTol_ChamferDimension:
                functionReturnValue = "ChamferDimension Dim";
                break;
            case swDimXpertAnnotationType_e.swDimXpertDimTol_AngleBetween:
                functionReturnValue = "AngleBetween Dim";
                break;
            case swDimXpertAnnotationType_e.swDimXpertDimTol_CounterSinkAngle:
                functionReturnValue = "CounterSinkAngle Dim";
                break;
            case swDimXpertAnnotationType_e.swDimXpertDimTol_ConeAngle:
                functionReturnValue = "ConeAngle Dim";
                break;
            case swDimXpertAnnotationType_e.swDimXpertDimTol_Diameter:
                functionReturnValue = "Diameter Dim";
                break;
            case swDimXpertAnnotationType_e.swDimXpertDimTol_Length:
                functionReturnValue = "Length Dim";
                break;
            case swDimXpertAnnotationType_e.swDimXpertDimTol_Radius:
                functionReturnValue = "Radius Dim";
                break;
            case swDimXpertAnnotationType_e.swDimXpertDimTol_Width:
                functionReturnValue = "Width Dim";
                break;
            case swDimXpertAnnotationType_e.swDimXpertDimTol_CompositeDistanceBetween:
                functionReturnValue = "CompositeDistanceBetween Dim";
                break;
            case swDimXpertAnnotationType_e.swDimXpertDatum:
                functionReturnValue = "Datum";
                break;
            case swDimXpertAnnotationType_e.swDimXpertGeoTol_Position:
                functionReturnValue = "Position Tol";
                break;
            case swDimXpertAnnotationType_e.swDimXpertGeoTol_CompositePosition:
                functionReturnValue = "CompositePosition Tol";
                break;
            case swDimXpertAnnotationType_e.swDimXpertGeoTol_Symmetry:
                functionReturnValue = "Symmetry Tol";
                break;
            case swDimXpertAnnotationType_e.swDimXpertGeoTol_Concentricity:
                functionReturnValue = "Concentricity Tol";
                break;
            case swDimXpertAnnotationType_e.swDimXpertGeoTol_LineProfile:
                functionReturnValue = "LineProfile Tol";
                break;
            case swDimXpertAnnotationType_e.swDimXpertGeoTol_CompositeLineProfile:
                functionReturnValue = "CompositeLineProfile Tol";
                break;
            case swDimXpertAnnotationType_e.swDimXpertGeoTol_SurfaceProfile:
                functionReturnValue = "SurfaceProfile Tol";
                break;
            case swDimXpertAnnotationType_e.swDimXpertGeoTol_CompositeSurfaceProfile:
                functionReturnValue = "CompositeSurfaceProfile Tol";
                break;
            case swDimXpertAnnotationType_e.swDimXpertGeoTol_Angularity:
                functionReturnValue = "Angularity Tol";
                break;
            case swDimXpertAnnotationType_e.swDimXpertGeoTol_Parallelism:
                functionReturnValue = "Parallelism Tol";
                break;
            case swDimXpertAnnotationType_e.swDimXpertGeoTol_Perpendicularity:
                functionReturnValue = "Perpendicularity Tol";
                break;
            case swDimXpertAnnotationType_e.swDimXpertGeoTol_TotalRunout:
                functionReturnValue = "TotalRunout Tol";
                break;
            case swDimXpertAnnotationType_e.swDimXpertGeoTol_CircularRunout:
                functionReturnValue = "CircularRunout Tol";
                break;
            case swDimXpertAnnotationType_e.swDimXpertGeoTol_Flatness:
                functionReturnValue = "Flatness Tol";
                break;
            case swDimXpertAnnotationType_e.swDimXpertGeoTol_Circularity:
                functionReturnValue = "Circularity Tol";
                break;
            case swDimXpertAnnotationType_e.swDimXpertGeoTol_Cylindricity:
                functionReturnValue = "Cylindricity Tol";
                break;
            case swDimXpertAnnotationType_e.swDimXpertGeoTol_Straightness:
                functionReturnValue = "Straightness Tol";
                break;
            case swDimXpertAnnotationType_e.swDimXpertGeoTol_Tangency:
                functionReturnValue = "Tangency Tol";
                break;
            default:
                functionReturnValue = "<unknown> " + annoTypeIndex;
                break;
        }
        return functionReturnValue;
    }
}
```
