---
title: "ISurface Interface Members"
project: "SOLIDWORKS API Help"
interface: "ISurface_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html"
---

# ISurface Interface Members

The following tables list the members exposed by [ISurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | ConeParams | Obsolete. Superseded by ISurface::ConeParams2 . |
| Property | ConeParams2 | Gets the parameters of a conical surface. |
| Property | CylinderParams | Gets the parameters of a cylindrical surface. |
| Property | IConeParams | Gets the parameters of a conical surface. |
| Property | ICylinderParams | Gets the parameters of a cylindrical surface. |
| Property | IPlaneParams | Gets the parameters of a planar surface. |
| Property | ISphereParams | Gets the parameters of a spherical surface. |
| Property | ITorusParams | Gets the parameters of a toroidal surface. |
| Property | PlaneParams | Gets the parameters of a planar surface. |
| Property | SphereParams | Gets the parameters of a spherical surface. |
| Property | TorusParams | Gets the parameters of a toroidal surface. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddTrimmingLoop | Obsolete. Superseded by ISurface::AddTrimmingLoop2 . |
| Method | AddTrimmingLoop2 | Creates a trimming loop out of specified surface parametric UV-curves and adds it to a list of such loops. |
| Method | Copy | Gets a copy of this surface. |
| Method | CreateNewCurve | Creates a new empty curve for the part. |
| Method | CreateTrimmedSheet | Obsolete. Superseded by ISurface::CreateTrimmedSheet4 . |
| Method | CreateTrimmedSheet4 | Obsolete. Superseded by ISurface::CreateTrimmedSheet5 . |
| Method | CreateTrimmedSheet5 | Creates a trimmed sheet body from this surface. |
| Method | Evaluate | Evaluates the surface, given the u and v parameters of the surface. |
| Method | EvaluateAtPoint | Evaluates a surface at the specified XYZ point. |
| Method | FindMinimumRadius | Gets the minimum radius of curvature for the selected surface. |
| Method | GetBSurfParams | Obsolete. Superseded by ISurface::GetBSurfParams2 . |
| Method | GetBSurfParams2 | Obsolete. Superseded by ISurface::GetBSurfParams3 . |
| Method | GetBSurfParams3 | Gets the parameterization data for a B-spline surface. |
| Method | GetClosestPointOn | Uses the X,Y,Z input point to determine the closest point on the surface. |
| Method | GetExtrusionsurfParams | Gets the parameters for the extrusion surface. |
| Method | GetIntersectCurveCount | Obsolete. Superseded by ISurface::GetIntersectCurveCount2 . |
| Method | GetIntersectCurveCount2 | Gets the number of points for a surface-curve intersection. |
| Method | GetIntersectSurfaceCount | Gets the number of curves for a surface-surface intersection. |
| Method | GetOffsetSurfParams | Obsolete. Superseded by ISurface::GetOffsetSurfParams2 . |
| Method | GetOffsetSurfParams2 | Gets the overall offset distance of this offset surface. |
| Method | GetProfileCurve | Gets the curve used to create the surface of revolution or extrusion surface and applies to only surface of revolution or extrusion surface. |
| Method | GetProjectedPointOn | Gets the point where the input point is projected on to this surface. |
| Method | GetRevsurfParams | Gets the parameters for the surface. |
| Method | IAddTrimmingLoop | Obsolete. Superseded by ISurface::IAddTrimmingLoop2 . |
| Method | IAddTrimmingLoop2 | Creates a trimming loop out of specified surface parametric (UV-curves) and adds it to a list of such loops. |
| Method | ICopy | Gets a copy of this surface. |
| Method | ICreateNewCurve | Creates a new empty curve for the part. |
| Method | ICreateTrimmedSheet | Obsolete. Superseded by ISurface::ICreateTrimmedSheet4 . |
| Method | ICreateTrimmedSheet2 | Obsolete. Superseded by ISurface::ICreateTrimmedSheet4 . |
| Method | ICreateTrimmedSheet4 | Obsolete. Superseded by ISurface::CreateTrimmedSheet5 . |
| Method | Identity | Gets the type of surface. |
| Method | IEvaluate | Evaluates the surface, given the u and v parameters of the surface. |
| Method | IEvaluateAtPoint | Evaluates a surface at the specified XYZ point. |
| Method | IFindMinimumRadius | Gets the minimum radius of curvature for the selected surface. |
| Method | IGetBSurfParams | Gets the b-spline surface parameters for the surface. |
| Method | IGetBSurfParamsSize | Obsolete. Superseded by ISurface::IGetBSurfParamsSize3 . |
| Method | IGetBSurfParamsSize2 | Obsolete. Superseded by ISurface::IGetBSurfParamsSize3 . |
| Method | IGetBSurfParamsSize3 | Gets the allocation size necessary for Bsurface parameter data retrieval in a subsequent call to ISurface::IGetBSurfParams . |
| Method | IGetClosestPointOn | Uses the X,Y,Z input point to determine the closest point on the surface. |
| Method | IGetExtrusionsurfParams | Gets the parameters for the extrusion surface. |
| Method | IGetMakeIsoCurvesCount | Gets the number of curves that represent the ISO line of a given direction. |
| Method | IGetOffsetSurfParams2 | Gets the overall offset distance of this offset surface. |
| Method | IGetProfileCurve | Gets the curve used to create the surface of revolution or extrusion surface and applies to only surface of revolution or extrusion surface. |
| Method | IGetRevsurfParams | Gets the parameters for the surface. |
| Method | IIntersectCurve | Obsolete. Superseded by ISurface::IIntersectCurve2 . |
| Method | IIntersectCurve2 | Gets a surface-curve intersection. |
| Method | IIntersectSurface | Gets a surface-surface intersection. |
| Method | IMakeIsoCurve | Creates a curve that represents the ISO line of a given surface. |
| Method | IMakeIsoCurves | Creates curves on a surface. |
| Method | IntersectCurve | Obsolete. Superseded by ISurface::IntersectCurve2 . |
| Method | IntersectCurve2 | Gets a surface-curve intersection. |
| Method | IntersectSurface | Gets a surface-surface intersection. |
| Method | IParameterization | Gets the parameterization of the surface. |
| Method | IReverseEvaluate | Gets the UV parameters at the specified location, which must be on the surface. |
| Method | IsBlending | Gets whether the surface is a blending surface. |
| Method | IsCone | Gets whether the surface is a cone. |
| Method | IsCylinder | Gets whether the surface is a cylinder. |
| Method | IsForeign | Gets whether the surface is a foreign surface. |
| Method | IsOffset | Gets whether the surface is an offset surface. |
| Method | IsParametric | Gets whether the surface is a parametric (spline type) surface. |
| Method | IsPlane | Gets whether the surface is a planar surface. |
| Method | IsRevolved | Gets whether the surface is a revolved surface. |
| Method | IsSphere | Gets whether the surface is a sphere. |
| Method | IsSwept | Gets whether the surface is swept. |
| Method | IsTorus | Gets whether the surface is a torus. |
| Method | MakeIsoCurve | Creates an untrimmed curve using the specified surface parameter. |
| Method | MakeIsoCurve2 | Creates an untrimmed curve on a surface using the specified u or v surface function parameter. |
| Method | MakeIsoCurves | Creates curves on a surface. |
| Method | Parameterization | Obsolete. Superseded by ISurface::Parameterization2 . |
| Method | Parameterization2 | Gets the parameterization of the surface. |
| Method | ReverseEvaluate | Gets the UV parameters at the specified location, which must be on the surface. |

[Top](#topBookmark)

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
