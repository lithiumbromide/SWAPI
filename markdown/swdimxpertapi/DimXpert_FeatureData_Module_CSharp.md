---
title: "DimXpert Feature Data Module Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/DimXpert_FeatureData_Module_CSharp.htm"
---

# DimXpert Feature Data Module Example (C#)

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
public class DimXpertFeatureData
{
    // Returns a collection of Strings containing the features data
    private Collection<string> strs = new Collection<string>();
    public void Clear(Collection<string> strs)
    {
        strs.Remove(strs[strs.Count]);
        if (!(strs.Count == 0))
        {
            Clear(strs);
        }
    }
    public Collection<string> FeatureData(DimXpertFeature feature)
    {
        SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e featureType = default(SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e);
        if ((!(strs.Count == 0)))
        {
            Clear(strs);
        }
        // General info, including the feature name, face id, and suppressed status
        FeatInfo(feature);

        featureType = feature.Type;
        // DimXpert plane
        if (featureType == SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_Plane)
        {
            PlaneData((DimXpertPlaneFeature)feature);
        }
        // DimXpert cylinder or boss. Also used for the sub-feature of a
        // compound hole (simple hole, counterbore, countersink...)
        else if (featureType == SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_Cylinder)
        {
            CylinderData((DimXpertCylinderFeature)feature);
        }
        // DimXpert cone
        else if (featureType == SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_Cone)
        {
            ConeData((DimXpertConeFeature)feature);
        }
        // DimXpert pocket or extrude
        else if (featureType == SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_Extrude)
        {
            ExtrudeData((DimXpertExtrudeFeature)feature);
        }
        // DimXpert fillet
        else if (featureType == SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_Fillet)
        {
            FilletData((DimXpertFilletFeature)feature);
        }
        // DimXpert chamfer
        else if (featureType == SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_Chamfer)
        {
            ChamferData((DimXpertChamferFeature)feature);
        }
        // DimXpert hole type (Simple, counterbore, countersink...)
        else if (featureType == SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_CompoundHole)
        {
            CompoundHoleData((DimXpertCompoundHoleFeature)feature);
        }
        // DimXpert width
        else if (featureType == SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_CompoundWidth)
        {
            CompoundWidthData((DimXpertCompoundWidthFeature)feature);
        }
        // DimXpert notch
        else if (featureType == SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_CompoundNotch)
        {
            CompoundNotchData((DimXpertCompoundNotchFeature)feature);
        }
        // DimXpert slot
        else if (featureType == SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_CompoundClosedSlot3D)
        {
            CompoundSlot3dData((DimXpertCompoundClosedSlot3DFeature)feature);
        }
        // DimXpert intersect point
        else if (featureType == SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_IntersectPoint)
        {
            IntersectPointData((DimXpertIntersectPointFeature)feature);
        }
        // DimXpert intersect line
        else if (featureType == SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_IntersectLine)
        {
            IntersectLineData((DimXpertIntersectLineFeature)feature);
        }
        // DimXpert intersect circle
        else if (featureType == SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_IntersectCircle)
        {
            IntersectCircleData((DimXpertIntersectCircleFeature)feature);
        }
        // DimXpert intersect plane
        else if (featureType == SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_IntersectPlane)
        {
            IntersectPlaneData((DimXpertIntersectPlaneFeature)feature);
        }
        // DimXpert pattern (hole, slot, notch...)
        else if (featureType == SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_Pattern)
        {
            PatternData((DimXpertPatternFeature)feature);
        }
        // DimXpert sphere
        else if (featureType == SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_Sphere)
        {
            SphereData((DimXpertSphereFeature)feature);
        }
        // DimXpert best fit plane
        else if (featureType == SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_BestfitPlane)
        {
            BestfitPlaneData((DimXpertBestfitPlaneFeature)feature);
        }
        // DimXpert surface
        else if (featureType == SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_Surface)
        {
            SurfaceData((DimXpertFeature)feature);
        }
        return strs;
    }
    private void FeatInfo(DimXpertFeature feature)
    {
        string featureType = null;
        Feature modelObj = default(Feature);
        strs.Add("Name: " + feature.Name);
        featureType = featureTypeNameFromObject(feature);
        strs.Add("Type: " + featureType);
        strs.Add(GetFaceId(feature));
        strs.Add("IsSuppressed: " + (feature.IsSuppressed() ? "True" : "False"));
        modelObj = (Feature)feature.GetModelFeature();
        if ((modelObj != null))
        {
            strs.Add("ModelFeature: " + modelObj.Name + " (" + modelObj.GetTypeName2() + ")");
        }
    }
    private void PlaneData(DimXpertPlaneFeature feature)
    {
        bool boolstatus = false;
        double X = 0;
        double Y = 0;
        double Z = 0;
        double I = 0;
        double J = 0;
        double K = 0;
        // list the plane's nominal point and vector
        strs.Add("");
        strs.Add("Nominal Plane:");
        boolstatus = feature.GetNominalPlane(ref X, ref Y, ref Z, ref I, ref J, ref K);
        strs.Add(" Point: " + FormatABC(X, Y, Z));
        strs.Add(" Vector: " + FormatABC(I, J, K));
    }
    private void CylinderData(DimXpertCylinderFeature feature)
    {
        bool boolstatus = false;
        bool isThreaded = false;
        string threadDesignation = null;
        double threadDepth = 0;
        double X = 0;
        double Y = 0;
        double Z = 0;
        double I = 0;
        double J = 0;
        double K = 0;
        double R = 0;
        // isInner status, is the feature a hole or boss?
        strs.Add("");
        strs.Add("IsInner: " + (feature.Inner ? "True" : "False"));
        threadDesignation = "";
        // isThreaded status
        boolstatus = feature.GetThread(ref isThreaded, ref threadDesignation, ref threadDepth);
        strs.Add("IsThreaded: " + (isThreaded ? "True" : "False"));
        // thread designation and depth
        if (isThreaded)
        {
            strs.Add("Thread Designation: " + threadDesignation);
            strs.Add("Thread Depth: " + FormatDouble(threadDepth));
        }
        // the cylinder's diameter, axis point, and vector
        strs.Add("");
        strs.Add("Nominal Cylinder:");
        boolstatus = feature.GetNominalCylinder(ref R, ref X, ref Y, ref Z, ref I, ref J, ref K);
        strs.Add(" Diameter: " + FormatDouble(R * 2));
        strs.Add(" Point: " + FormatABC(X, Y, Z));
        strs.Add(" Vector: " + FormatABC(I, J, K));
        // the nominal top plane of the cylinder, which is the highest point
        // of the cylinder's boundary projected onto its axis
        strs.Add("");
        strs.Add("Nominal Top Plane:");
        boolstatus = feature.GetNominalTopPlane(ref X, ref Y, ref Z, ref I, ref J, ref K);
        strs.Add(" Point: " + FormatABC(X, Y, Z));
        strs.Add(" Vector: " + FormatABC(I, J, K));
        // the nominal bottom plane of the cylinder, which is the lowest point
        // of the cylinder's boundary projected onto its axis
        strs.Add("");
        strs.Add("Nominal Bottom Plane:");
        boolstatus = feature.GetNominalBottomPlane(ref X, ref Y, ref Z, ref I, ref J, ref K);
        strs.Add(" Point: " + FormatABC(X, Y, Z));
        strs.Add(" Vector: " + FormatABC(I, J, K));
    }
    private void ConeData(DimXpertConeFeature feature)
    {
        bool boolstatus = false;
        double X = 0;
        double Y = 0;
        double Z = 0;
        double I = 0;
        double J = 0;
        double K = 0;
        double Angle = 0;
        //isInner status
        strs.Add("");
        strs.Add("IsInner: " + (feature.Inner ? "True" : "False"));
        //the nominal cone's angle, axis point, and vector
        strs.Add("");
        strs.Add("Nominal Cone:");
        boolstatus = feature.GetNominalCone(ref Angle, ref X, ref Y, ref Z, ref I, ref J, ref K);
        strs.Add(" Cone Angle: " + RadiansToDegrees(Angle));
        strs.Add(" Point: " + FormatABC(X, Y, Z));
        strs.Add(" Vector: " + FormatABC(I, J, K));
        // the nominal top plane of the cone, which is the highest point
        // of the cone's boundary projected onto its axis
        strs.Add("");
        strs.Add("Nominal Top Plane:");
        boolstatus = feature.GetNominalTopPlane(ref X, ref Y, ref Z, ref I, ref J, ref K);
        strs.Add(" Point: " + FormatABC(X, Y, Z));
        strs.Add(" Vector: " + FormatABC(I, J, K));
        // the nominal bottom plane of the cone, which is the lowest point
        // of the cone's boundary projected onto its axis
        strs.Add("");
        strs.Add("Nominal Bottom Plane:");
        boolstatus = feature.GetNominalBottomPlane(ref X, ref Y, ref Z, ref I, ref J, ref K);
        strs.Add(" Point: " + FormatABC(X, Y, Z));
        strs.Add(" Vector: " + FormatABC(I, J, K));
    }
    private void FilletData(DimXpertFilletFeature feature)
    {
        //isInner status
        strs.Add("");
        strs.Add("IsInner: " + (feature.Inner ? "True" : "False"));
        //the fillet radius
        strs.Add("Radius: " + FormatDouble(feature.Radius));
    }
    private void ChamferData(DimXpertChamferFeature feature)
    {
        strs.Add("");
        // chamfer dimension scheme, which can be a distance and an angle, or 2 distances
        switch (feature.ChamferType)
        {
            case SolidWorks.Interop.swdimxpert.swDimXpertChamferType_e.swDimXpertChamferType_DistanceAngle:
                strs.Add("Chamfer Dimension: Distance and Angle");
                strs.Add(" Distance: " + FormatDouble(feature.Distance1));
                strs.Add(" Angle: " + RadiansToDegrees(feature.Angle));
                break;
            case SolidWorks.Interop.swdimxpert.swDimXpertChamferType_e.swDimXpertChamferType_DistanceDistance:
                strs.Add("Chamfer Dimension: 2 Distances");
                strs.Add(" Distance1: " + FormatDouble(feature.Distance1));
                strs.Add(" Distance2: " + FormatDouble(feature.Distance2));
                break;
            case SolidWorks.Interop.swdimxpert.swDimXpertChamferType_e.swDimXpertChamferType_Vertex:
                strs.Add("Chamfer Type: Vertex");
                break;
        }
    }
    private void CompoundHoleData(DimXpertCompoundHoleFeature feature)
    {
        double X = 0;
        double Y = 0;
        double Z = 0;
        double I = 0;
        double J = 0;
        double K = 0;
        double R = 0;
        long index = 0;
        DimXpertFeature featObj = default(DimXpertFeature);
        bool boolstatus = false;
        strs.Add("");
        // the type of compound hole
        string typ = null;
        typ = "";
        switch (feature.CompoundHoleType)
        {
            case SolidWorks.Interop.swdimxpert.swDimXpertCompoundHoleType_e.swDimXpertCompoundHoleType_Counterbore:
                typ = "Counterbore";
                break;
            case SolidWorks.Interop.swdimxpert.swDimXpertCompoundHoleType_e.swDimXpertCompoundHoleType_Countersink:
                typ = "Countersink";
                break;
            case SolidWorks.Interop.swdimxpert.swDimXpertCompoundHoleType_e.swDimXpertCompoundHoleType_Compound:
                typ = "Compound";
                break;
            case SolidWorks.Interop.swdimxpert.swDimXpertCompoundHoleType_e.swDimXpertCompoundHoleType_Simple:
                typ = "Simple";
                break;
        }
        strs.Add("Hole Type: " + typ);
        // is blind status
        strs.Add("IsBlind: " + (feature.Blind ? "True" : "False"));
        // reference plane, which is the basis for all depth tolerances
        if ((feature.GetReferenceFeature() != null))
        {
            strs.Add("Reference Feature: " + feature.GetReferenceFeature().Name);
        }
        else
        {
            strs.Add("Reference Feature: isNothing");
        }
        // bottom feature, used for the depth of blind holes
        if ((feature.GetBottomFeature() != null))
        {
            strs.Add("Bottom Feature: " + feature.GetBottomFeature().Name);
        }
        else
        {
            strs.Add("Bottom Feature: isNothing");
        }
        //get the collection of sub-features
        object[] subFeats = null;
        subFeats = (object[])feature.GetSubFeatures();
        // the collection of sub-features that make up the hole
        strs.Add("" + "Sub-Features:");
        if (!((subFeats == null)))
        {
            for (index = subFeats.GetLowerBound(0); index <= subFeats.GetUpperBound(0); index++)
            {
                featObj = (DimXpertFeature)subFeats[index];
                strs.Add(" " + featObj.Name + "");
            }
            // the location of the hole based on the first cylinder in the list of sub-feaures
            for (index = subFeats.GetLowerBound(0); index <= subFeats.GetUpperBound(0); index++)
            {
                featObj = (DimXpertFeature)subFeats[index];
                if (featObj.Type == SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_Cylinder)
                {
                    strs.Add("");
                    DimXpertCylinderFeature cylFeat = default(DimXpertCylinderFeature);
                    cylFeat = (DimXpertCylinderFeature)featObj;
                    boolstatus = cylFeat.GetNominalCylinder(ref R, ref X, ref Y, ref Z, ref I, ref J, ref K);
                    // the diameter of the hole for type simple
                    switch (feature.CompoundHoleType)
                    {
                        case SolidWorks.Interop.swdimxpert.swDimXpertCompoundHoleType_e.swDimXpertCompoundHoleType_Simple:
                            strs.Add("Diameter: " + FormatDouble(R * 2));
                            break;
                    }
                    strs.Add("Nominal Axis:");
                    strs.Add(" Point: " + FormatABC(X, Y, Z));
                    strs.Add(" Vector: " + FormatABC(I, J, K));
                    index = subFeats.GetUpperBound(0);
                }
            }
        }
    }
    private void CompoundWidthData(DimXpertCompoundWidthFeature feature)
    {
        DimXpertPlaneFeature plane1 = default(DimXpertPlaneFeature);
        DimXpertPlaneFeature plane2 = default(DimXpertPlaneFeature);
        bool boolstatus = false;
        double X = 0;
        double Y = 0;
        double Z = 0;
        double I = 0;
        double J = 0;
        double K = 0;
        double width = 0;
        // the two side features
        strs.Add("");
        strs.Add("Features:");
        plane1 = null;
        plane2 = null;
        boolstatus = feature.GetPlaneFeatures(ref plane1, ref plane2);
        if ((plane1 != null) & (plane2 != null))
        {
            DimXpertFeature feat1 = (DimXpertFeature)plane1;
            DimXpertFeature feat2 = (DimXpertFeature)plane2;
            strs.Add(" Plane1: " + feat1.Name);
            strs.Add(" Plane2: " + feat2.Name);
        }
        // isInner status
        strs.Add("IsInner: " + (feature.Inner ? "True" : "False"));
        // the nominal width and mid-plane
        strs.Add("");
        strs.Add("Nominal Width:");
        boolstatus = feature.GetNominalCompoundWidth(ref width, ref X, ref Y, ref Z, ref I, ref J, ref K);
        strs.Add(" Width: " + FormatDouble(width));
        strs.Add(" Point: " + FormatABC(X, Y, Z));
        strs.Add(" Vector: " + FormatABC(I, J, K));
        // the width's longitudinal direction
        boolstatus = feature.GetNominalLongitude(ref I, ref J, ref K );
        strs.Add("Longitudinal Direction: " + FormatABC(I, J, K));
    }
    private void CompoundSlot3dData(DimXpertCompoundClosedSlot3DFeature feature)
    {
        DimXpertPlaneFeature plane1 = default(DimXpertPlaneFeature);
        DimXpertPlaneFeature plane2 = default(DimXpertPlaneFeature);
        DimXpertFeature end1 = default(DimXpertFeature);
        DimXpertFeature end2 = default(DimXpertFeature);
        bool boolstatus = false;
        double X = 0;
        double Y = 0;
        double Z = 0;
        double I = 0;
        double J = 0;
        double K = 0;
        double longitudeI = 0;
        double longitudeJ = 0;
        double longitudeK = 0;
        double width = 0;
        double length = 0;
        //isInner status
        strs.Add("");

        //isBlind status
        strs.Add("IsBlind: " + (feature.Blind ? "True" : "False"));
        // the two side features
        strs.Add("Features:");
        plane1 = null;
        plane2 = null;
        boolstatus = feature.GetPlaneFeatures(ref plane1, ref plane2);
        DimXpertFeature feat1 = (DimXpertFeature)plane1;
        DimXpertFeature feat2 = (DimXpertFeature)plane2;
        strs.Add(" Side1: " + feat1.Name);
        strs.Add(" Side2: " + feat2.Name);
        //the two end features, which can be cylinders or planes
        end1 = null;
        end2 = null;
        boolstatus = feature.GetEndFeatures(ref end1, ref end2);
        strs.Add(" End1: " + end1.Name);
        strs.Add(" End2: " + end2.Name);
        // bottom feature, used for the depth of blind holes
        if ((feature.GetBottomFeature() != null))
        {
            strs.Add("Bottom Feature: " + feature.GetBottomFeature().Name);
        }
        else
        {
            strs.Add("Bottom Feature: isNothing");
        }
        // the size and location of the nominal slot
        boolstatus = feature.GetNominalClosedSlot(ref width, ref length, ref X, ref Y, ref Z, ref I, ref J, ref K, ref longitudeI, ref longitudeJ,
        ref longitudeK);
        strs.Add("");
        strs.Add("Nominal Slot:");
        strs.Add(" Width: " + FormatDouble(width));
        strs.Add(" Length: " + FormatDouble(length));
        strs.Add(" Axis Point: " + FormatABC(X, Y, Z));
        strs.Add(" Axis Vector: " + FormatABC(I, J, K));
        strs.Add(" Longitudinal Vector: " + FormatABC(longitudeI, longitudeJ, longitudeK));
        // the nominal top plane of the slot
        strs.Add("");
        strs.Add("Nominal Top Plane:");
        boolstatus = feature.GetNominalTopPlane(ref X, ref Y, ref Z, ref I, ref J, ref K);
        strs.Add(" Point: " + FormatABC(X, Y, Z));
        strs.Add(" Vector: " + FormatABC(I, J, K));
        // the nominal bottom plane of the slot
        strs.Add("");
        strs.Add("Nominal Bottom Plane:");
        boolstatus = feature.GetNominalBottomPlane(ref X, ref Y, ref Z, ref I, ref J, ref K);
        strs.Add(" Point: " + FormatABC(X, Y, Z));
        strs.Add(" Vector: " + FormatABC(I, J, K));
    }
    private void CompoundNotchData(DimXpertCompoundNotchFeature feature)
    {
        DimXpertPlaneFeature plane1 = default(DimXpertPlaneFeature);
        DimXpertPlaneFeature plane2 = default(DimXpertPlaneFeature);
        bool boolstatus = false;
        double X = 0;
        double Y = 0;
        double Z = 0;
        double I = 0;
        double J = 0;
        double K = 0;
        double longitudeI = 0;
        double longitudeJ = 0;
        double longitudeK = 0;
        double width = 0;
        double length = 0;
        // isInner status
        strs.Add("");

        // isBlind status
        strs.Add("IsBlind: " + (feature.Blind ? "True" : "False"));
        // the reference feature or top of the notch
        strs.Add("Top Reference Feature: " + feature.GetTopReferenceFeature().Name);
        // the open side reference feature, which bounds the notch
        strs.Add("Open Side Reference Feature: " + feature.GetOpenSideReferenceFeature().Name);
        // the two side features
        plane1 = null;
        plane2 = null;
        boolstatus = feature.GetPlaneFeatures(ref plane1, ref plane2);
        strs.Add("Features:" + "");
        DimXpertFeature feat1 = (DimXpertFeature)plane1;
        DimXpertFeature feat2 = (DimXpertFeature)plane2;
        strs.Add(" Side1: " + feat1.Name);
        strs.Add(" Side2: " + feat2.Name);
        // the end features, which can be a cylinder or a plane
        if ((feature.GetEndFeature() != null))
        {
            strs.Add(" End Feature: " + feature.GetEndFeature().Name);
        }
        else
        {
            strs.Add(" End Feature: isNothing");
        }
        // bottom feature, used for the depth of blind holes
        if ((feature.GetBottomFeature() != null))
        {
            strs.Add(" Bottom Feature: " + feature.GetBottomFeature().Name);
        }
        else
        {
            strs.Add(" Bottom Feature: isNothing");
        }
        // the nominal size and location of the notch
        boolstatus = feature.GetNominalNotch(ref width, ref length, ref X, ref Y, ref Z, ref I, ref J, ref K, ref longitudeI, ref longitudeJ,
        ref longitudeK);
        strs.Add("");
        strs.Add("Nominal Notch:");
        strs.Add(" Width: " + FormatDouble(width));
        strs.Add(" Length: " + FormatDouble(length));
        strs.Add(" Point: " + FormatABC(X, Y, Z));
        strs.Add(" Plane Vector: " + FormatABC(I, J, K));
        strs.Add(" Longitudinal Vector: " + FormatABC(longitudeI, longitudeJ, longitudeK));
        // the nominal bottom plane of the notch
        strs.Add("");
        strs.Add("Nominal Bottom Plane:");
        boolstatus = feature.GetNominalBottomPlane(ref X, ref Y, ref Z, ref I, ref J, ref K);
        strs.Add(" Point: " + FormatABC(X, Y, Z));
        strs.Add(" Vector: " + FormatABC(I, J, K));
    }
    private void ExtrudeData(DimXpertExtrudeFeature feature)
    {
        long index = 0;
        object[] wallFeats = null;
        DimXpertFeature featObj = default(DimXpertFeature);
        // isBlind status
        strs.Add("");
        strs.Add("IsBlind: " + (feature.Blind ? "True" : "False"));
        // the reference feature or top plane
        strs.Add("Reference Feature: " + feature.GetReferenceFeature().Name);
        // the bottom feature
        strs.Add("Bottom Feature: " + feature.GetBottomFeature().Name);
        // the top blends (fillets or chamfers)
        if ((feature.GetTopBlends() != null))
        {
            strs.Add("Top Blends: " + feature.GetTopBlends().Name);
        }
        else
        {
            strs.Add("Top Blends: Is_Nothing");
        }
        // the bottom blends
        if ((feature.GetBottomBlends() != null))
        {
            strs.Add("Bottom Blends: " + feature.GetBottomBlends().Name);
        }
        else
        {
            strs.Add("Bottom Blends: Is_Nothing");
        }
        // the wall features of the pocket or extrude
        strs.Add("Wall Features:");
        wallFeats = (object[])feature.GetSubFeatures();
        if ((wallFeats != null))
        {
            for (index = wallFeats.GetLowerBound(0); index <= wallFeats.GetUpperBound(0); index++)
            {
                featObj = (DimXpertFeature)wallFeats[index];
                strs.Add(" " + featObj.Name);
            }
        }
    }
    private void IntersectPointData(DimXpertIntersectPointFeature feature)
    {
        DimXpertFeature feature1 = default(DimXpertFeature);
        DimXpertFeature feature2 = default(DimXpertFeature);
        bool boolstatus = false;
        double X = 0;
        double Y = 0;
        double Z = 0;
        double I = 0;
        double J = 0;
        double K = 0;
        // the two features that make up the intersect point
        feature1 = null;
        feature2 = null;
        boolstatus = feature.GetFeatures(ref feature1, ref feature2);
        if ((feature1 != null) & (feature2 != null))
        {
            strs.Add("");
            strs.Add("Sub-Features:" + "");

            strs.Add(" " + feature1.Name);
            strs.Add(" " + feature2.Name);
        }
        // the nominal point
        boolstatus = feature.GetNominalPoint(ref X, ref Y, ref Z);
        strs.Add("Intersect Point: " + FormatABC(X, Y, Z));
        // the nominal vector
        boolstatus = feature.GetNominalVector(ref I, ref J, ref K);
        strs.Add("Point Vector: " + FormatABC(I, J, K));
    }
    private void IntersectLineData(DimXpertIntersectLineFeature feature)
    {
        DimXpertPlaneFeature plane1 = default(DimXpertPlaneFeature);
        DimXpertPlaneFeature plane2 = default(DimXpertPlaneFeature);
        bool boolstatus = false;
        double X = 0;
        double Y = 0;
        double Z = 0;
        double I = 0;
        double J = 0;
        double K = 0;
        // the two features that make up the intersect line
        plane1 = null;
        plane2 = null;
        boolstatus = feature.GetPlaneFeatures(ref plane1, ref plane2);
        if ((plane1 != null) & (plane2 != null))
        {
            strs.Add("");
            strs.Add("Sub-Features:" + "");
            DimXpertFeature feat1 = (DimXpertFeature)plane1;
            DimXpertFeature feat2 = (DimXpertFeature)plane2;
            strs.Add(" " + feat1.Name);
            strs.Add(" " + feat2.Name);
        }
        // the nominal line
        boolstatus = feature.GetNominalLine(ref X, ref Y, ref Z, ref I, ref J, ref K);
        strs.Add("Nominal Line:");
        strs.Add(" Point: " + FormatABC(X, Y, Z));
        strs.Add(" Vector: " + FormatABC(I, J, K));

    }
    private void IntersectCircleData(DimXpertIntersectCircleFeature feature)
    {
        DimXpertPlaneFeature plane1 = default(DimXpertPlaneFeature);
        bool boolstatus = false;
        double X = 0;
        double Y = 0;
        double Z = 0;
        double I = 0;
        double J = 0;
        double K = 0;
        double R = 0;
        plane1 = null;
        boolstatus = feature.GetPlaneFeature(ref plane1);
        if ((plane1 != null))
        {
            DimXpertFeature feat = (DimXpertFeature)plane1;
            strs.Add("Plane Feature: " + feat.Name);
        }
        boolstatus = feature.GetNominalCircle(ref R, ref X, ref Y, ref Z, ref I, ref J, ref K);
        strs.Add("Nominal Circle:");
        strs.Add(" Diameter: " + FormatDouble(R * 2));
        strs.Add(" Point: " + FormatABC(X, Y, Z));
        strs.Add(" Vector: " + FormatABC(I, J, K));
    }
    private void IntersectPlaneData(DimXpertIntersectPlaneFeature feature)
    {
        DimXpertFeature feature1 = default(DimXpertFeature);
        DimXpertFeature feature2 = default(DimXpertFeature);
        bool boolstatus = false;
        double X = 0;
        double Y = 0;
        double Z = 0;
        double I = 0;
        double J = 0;
        double K = 0;
        // the two features that make up the intersect plane
        feature1 = null;
        feature2 = null;
        boolstatus = feature.GetFeatures(ref feature1, ref feature2);
        if ((feature1 != null) & (feature2 != null))
        {
            strs.Add("");
            strs.Add("Sub-Features:");
            strs.Add(" " + feature1.Name);
            strs.Add(" " + feature2.Name);
        }
        // the nominal plane
        strs.Add("Nominal Plane");
        boolstatus = feature.GetNominalPlane(ref X, ref Y, ref Z, ref I, ref J, ref K);
        strs.Add(" Point: " + FormatABC(X, Y, Z));
        strs.Add(" Vector: " + FormatABC(I, J, K));
    }
    private void PatternData(DimXpertPatternFeature feature)
    {
        object[] afeats = null;
        DimXpertFeature featObj = default(DimXpertFeature);
        long index = 0;
        strs.Add("");
        strs.Add("Pattern Type: " + featureTypeNameFromTypeNumber(feature.PatternType));
        // list the collection of features
        afeats = (object[])feature.GetSubFeatures();
        strs.Add("Sub-Features:");
        if ((afeats != null))
        {
            for (index = afeats.GetLowerBound(0); index <= afeats.GetUpperBound(0); index++)
            {
                featObj = (DimXpertFeature)afeats[index];
                strs.Add(" " + featObj.Name);
            }
        }
    }
    private void SphereData(DimXpertSphereFeature feature)
    {
        strs.Add("");
        bool boolstatus = false;
        double R = 0;
        double X = 0;
        double Y = 0;
        double Z = 0;
        //isInner status
        strs.Add("");
        strs.Add("IsInner: " + (feature.Inner ? "True" : "False"));
        //the nominal sphere's radius and x, y, and z
        strs.Add("");
        strs.Add("Nominal Sphere:");
        boolstatus = feature.GetNominalSphere(ref R, ref X, ref Y, ref Z);
        strs.Add(" Radius: " + R);
        strs.Add(" Point: " + FormatABC(X, Y, Z));
    }
    private void BestfitPlaneData(DimXpertBestfitPlaneFeature feature)
    {
        strs.Add("");
        object[] afeats = null;
        DimXpertFeature featObj = default(DimXpertFeature);
        long index = 0;
        // list the collection of features
        afeats = (object[])feature.GetSubFeatures();
        strs.Add("Sub-Features:");
        if ((afeats != null))
        {
            for (index = afeats.GetLowerBound(0); index <= afeats.GetUpperBound(0); index++)
            {
                featObj = (DimXpertFeature)afeats[index];
                strs.Add(" " + featObj.Name);
            }
        }
    }
    private void SurfaceData(DimXpertFeature feature)
    {
        strs.Add("");
        strs.Add("Surface Feature...");
    }
    private string FormatABC(double a, double b, double c)
    {
        string str = null;
        str = FormatDouble(a) + ", " + FormatDouble(b) + ", " + FormatDouble(c);
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
    private string GetFaceId(DimXpertFeature feature)
    {
        string str = null;
        object[] vFaceArr = null;
        Face2 swFace2 = null;
        long lFeatId = 0;
        long I = 0;
        str = "Face ID:";
        vFaceArr = (Object[])feature.GetFaces();
        if ((vFaceArr != null))
        {
            for (I = vFaceArr.GetUpperBound(0); I <= vFaceArr.GetUpperBound(0); I++)
            {
                swFace2 = (Face2)vFaceArr[I];
                lFeatId = swFace2.GetFeatureId();
                str = str + " " + System.String.Format("{0:N}", lFeatId.ToString());
            }
        }
        else
        {
            str = str + " <Nothing>";
        }
        return str;
    }
    private string featureTypeNameFromObject(DimXpertFeature feature)
    {
        return featureTypeNameFromTypeNumber(feature.Type);
    }
    private string featureTypeNameFromTypeNumber(SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e featureTypeIndex)
    {
        string functionReturnValue = null;
        switch (featureTypeIndex)
        {
            case SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_Plane:
                functionReturnValue = "Plane";
                break;
            case SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_Cylinder:
                functionReturnValue = "Cylinder";
                break;
            case SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_Cone:
                functionReturnValue = "Cone";
                break;
            case SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_Extrude:
                functionReturnValue = "Extrude";
                break;
            case SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_Fillet:
                functionReturnValue = "Fillet";
                break;
            case SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_Chamfer:
                functionReturnValue = "Chamfer";
                break;
            case SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_CompoundHole:
                functionReturnValue = "Compound Hole";
                break;
            case SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_CompoundWidth:
                functionReturnValue = "Compound Width";
                break;
            case SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_CompoundNotch:
                functionReturnValue = "Compound Notch";
                break;
            case SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_CompoundClosedSlot3D:
                functionReturnValue = "Compound Closed Slot";
                break;
            case SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_IntersectPoint:
                functionReturnValue = "IntersectPoint";
                break;
            case SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_IntersectLine:
                functionReturnValue = "IntersectLine";
                break;
            case SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_IntersectCircle:
                functionReturnValue = "IntersectCircle";
                break;
            case SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_IntersectPlane:
                functionReturnValue = "IntersectPlane";
                break;
            case SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_Pattern:
                functionReturnValue = "Pattern";
                break;
            case SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_Sphere:
                functionReturnValue = "Sphere";
                break;
            case SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_BestfitPlane:
                functionReturnValue = "Best Fit Plane";
                break;
            case SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_Surface:
                functionReturnValue = "Surface";
                break;
            default:
                functionReturnValue = "<unknown> " + featureTypeIndex;
                break;
        }
        return functionReturnValue;
    }
}
```
