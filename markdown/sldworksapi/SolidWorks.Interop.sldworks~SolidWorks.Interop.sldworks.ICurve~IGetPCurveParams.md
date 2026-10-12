---
title: "IGetPCurveParams Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "IGetPCurveParams"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetPCurveParams.html"
---

# IGetPCurveParams Method (ICurve)

Converts a curve to a piecewise rational cubic polynomial form.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetPCurveParams() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim value As System.Double

value = instance.IGetPCurveParams()
```

### C#

```csharp
System.double IGetPCurveParams()
```

### C++/CLI

```cpp
System.double IGetPCurveParams();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles describing the parameters of the curve (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

The curve is output as a series of segments.

This method returns the curve as a series of segments, each of which has this form:

(w0*a0 + w1*a1*t + w2*a2*t**2 + w3*a3*t**3)

p(t) = --------------------------------------------

(w0 + w1*t + w2*t**2 + w3*t**3)

Where w is the weight coefficient and a is the polynomial coefficient.

The coefficients returned are vectors of dimensions "dim". For example, if the curve is rational, then dimension = 4, and the coefficients returned for each segment are as follows:

(a0x,a0y,a0z,w0),(a1x,a1y,a1z,w1)...

However, if the curve is returned as non-rational, then dimension = 3, and its coefficients are:

(a0x,a0y,a0z),(a1x,a1y,a1z),...

Use [ICurve::IGetPCurveParamsSize](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~IGetPCurveParamsSize.html) to determine the size of the array returned.

The size of the return value array is (3 + NumberKnots + NumberSegments x Order x Dimension).

The array is as follows:

[ packedDouble1, packedDouble2, packedDouble3, knot1, knot2,..., CoefficientsSegment1[Dimension], CoefficientsSegment2[Dimension],... ]

where:

packedDouble1: Integer pair containing Reserved and Order

packedDouble2: Integer pair containing NumberSegments and Periodicity

packedDouble3: Integer pair containing NumberKnots and Dimension

knot1

knot2

...

CoefficientsSegment1[Dimension]

CoefficientsSegment2[Dimension]

...

The coefficients for each segment start with the constant term and end with the term of highest degree (for example, ConstantX, ConstantY, ConstantZ, AX, AY, AZ, BX, BY, BZ). The total number of coefficients is:

(NumberSegments) x (Order) x (Dimension).

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[ICurve::Identity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~Identity.html)
[ICurve::GetPCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetPCurveParams.html)
[ICurve::IGetPCurveParamsSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetPCurveParamsSize.html)
