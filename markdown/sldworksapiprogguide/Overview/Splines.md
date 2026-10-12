---
title: "Splines"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Splines.htm"
---

# Splines

Some common questions and answers about SOLIDWORKS Design and splines are presented in this help topic.

**What are the different types of splines used in SOLIDWORKS Design?**

Any curve in SOLIDWORKS Design that is not an analytic curve, such as a line, arc, conic, or a composite curve, is represented as a b-spline. SOLIDWORKS Design uses standard b-splines as defined in computer-aided design literature.

**What are the mathematical names for b-spline and p-spline? What is the difference between ICurve::GetPCurveParams2 and ICurve::GetBCurveParams5? Do these methods return parameters for two different kinds of splines, or do they return parameters formatted in two different ways for a single spline type?**

Names such as p-spline, or p-curve, are used for b-splines in a particular context. If you are unsure of the context, then you might find the names confusing. For example, p-curves, as in [IModeler::CreatePCurve](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IModeler~CreatePCurve.html), are b-splines that lie on a surface and are created from b-splines in the parameter space of the surface.

Any b-spline is a piecewise polynomial curve, and a p-spline is a b-spline represented as the polynomial coefficients that define the polynomials in each segment of the b-spline.

- [ICurve::GetBCurveParams5](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ICurve~GetBCurveParams5.html) gets the control point/knot standard b-spline representation for the input curve.
- [ICurve::GetPCurveParams](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ICurve~GetPCurveParams.html) gets the polynomial coefficients for the segments of a b-spline for the input curve.
- [ICurve::GetPCurveParams2](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ICurve~GetPCurveParams2.html) is a hybrid of ICurve::GetBCurveParams5 and ICurve::GetPCurveParms. You can use either the control point/knot representation, which it returns in the [SplineParamData object](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ISplineParamData.html), or the polynomial coefficient representation for the individual segments.

**When can you edit the control points of a b-spline?**

You can edit control points when creating a b-spline; however, you currently cannot replace control points of an existing b-spline.

**What kind of spline is returned by ISketchManager::CreateSpline2, IModelDoc2::SketchSpline, and IFeatureManager::MakeStyledCurves2?**

All three methods create b-splines.

- [ISketchManager::CreateSpline2](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ISketchManager~CreateSpline2.html) creates a b-spline using the input points as through points, or interpolation points, with some control over the curve’s end conditions.
- [IModelDoc2::SketchSpline](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IModelDoc2~SketchSpline.html) is an attempt to simulate the way you create a b-spline in the SOLIDWORKS Design user interface, one point at a time.
- [IFeatureManager::MakeStyledCurves2](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFeatureManager~MakeStyledCurves2.html) fits a b-spline that approximates a composite curve of sketch segments.

**What b-spline points for the curve does ICurve::GetSplinePts return?**

[ICurve::GetSplinePts](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ICurve~GetSplinePts.html) gets a spline's through/interpolation points, i.e., the end points of its individual spline segments, as opposed to its representation by knots and control points.
