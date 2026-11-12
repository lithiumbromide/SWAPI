---
title: "IGetSegments Method (ISplineParamData)"
project: "SOLIDWORKS API Help"
interface: "ISplineParamData"
member: "IGetSegments"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~IGetSegments.html"
---

# IGetSegments Method (ISplineParamData)

Gets the coefficients of all of the piecewise polynomials of a spline.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSegments( _
   ByVal Count As System.Integer, _
   ByRef Segments As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISplineParamData
Dim Count As System.Integer
Dim Segments As System.Double
Dim value As System.Boolean

value = instance.IGetSegments(Count, Segments)
```

### C#

```csharp
System.bool IGetSegments(
   System.int Count,
   out System.double Segments
)
```

### C++/CLI

```cpp
System.bool IGetSegments(
   System.int Count,
   [Out] System.double Segments
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Size of Segments array
- `Segments`: - in-process, unmanaged C++: Pointer to an array of doubles

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

True if successful, false if not

## Remarks

This method works only with P-spline parameterization data. Before calling this method, call [ICurve::GetPCurveParams2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~GetPCurveParams2.html) to obtain the P-spline parameterization data object for the curve.

Before calling this method, call [ISplineParamData::SegmentCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineParamData~SegmentCount.html) to populate the Count parameter.

Each pair of spline control points defines one segment of a curve. Each segment is typically represented by a cubic polynomial. This method returns a one-dimensional array containing doubles that are the coefficients of all of the piecewise cubic polynomials of the spline.

The segment coefficients are stored in the Segments array in order of increasing variable exponent:

(constants)(first degree coefficients)(second degree coefficients)(third degree coefficients) etc.

For example, if the spline segments are represented by cubic rational (dim=4) polynomials in parametric form,

(w0*a0 + w1*a1*t + w2*a2*t**2 + w3*a3*t**3)

p(t) = --------------------------------------------

(w0 + w1*t + w2*t**2 + w3*t**3)

where w0, w1, w2, w3 are weighting coefficients and a0, a1, a2, a3 are vector coefficients, then the Segments array stores (dimension(4) X order(4)) = 16 coefficients:

(a0x,a0y,a0z,w0)(a1x,a1y,a1z,w1)(a2x,a2y,a2z,w2)(a3x,a3y,a3z,w3).

If the spline segments are represented by cubic non-rational (dim=3) polynomials, then the Segments array stores (dimension(3) X order(4)) = 12 coefficients:

(a0x,a0y,a0z)(a1x,a1y,a1z)(a2x,a2y,a2z)(a3x,a3y,a3z0).

The total number of coefficients returned by this method is:

([segment count](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineParamData~SegmentCount.html)) x ([order](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineParamData~Order.html)) x ([dimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineParamData~Dimension.html))

## See Also

[ISplineParamData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData.html)
[ISplineParamData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData_members.html)
[ISplineParamData::GetSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~GetSegments.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
