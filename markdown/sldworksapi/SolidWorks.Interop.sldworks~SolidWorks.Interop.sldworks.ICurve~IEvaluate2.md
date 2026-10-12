---
title: "IEvaluate2 Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "IEvaluate2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IEvaluate2.html"
---

# IEvaluate2 Method (ICurve)

Evaluates the curve at the specified parameter of the curve.

## Syntax

### Visual Basic (Declaration)

```vb
Function IEvaluate2( _
   ByVal Parameter As System.Double, _
   ByVal NumberOfDerivatives As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim Parameter As System.Double
Dim NumberOfDerivatives As System.Integer
Dim value As System.Double

value = instance.IEvaluate2(Parameter, NumberOfDerivatives)
```

### C#

```csharp
System.double IEvaluate2(
   System.double Parameter,
   System.int NumberOfDerivatives
)
```

### C++/CLI

```cpp
System.double IEvaluate2(
   System.double Parameter,
   System.int NumberOfDerivatives
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Parameter`: Curve parameter
- `NumberOfDerivatives`: Number of derivatives

### Return Value

Array of doubles (see Remarks)

## VBA Syntax

See [Curve::IEvaluate2](ms-its:sldworksapivb6.chm::/sldworks~Curve~IEvaluate2.html).

## Remarks

To determine a valid parameter range, use [ICurve::GetEndParams](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~GetEndParams.html) or [IEdge::GetCurveParams2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~GetCurveParams2.html).

The format of the return value is an array of (NumberOfDerivatives + 1) * 3 doubles:

[evaluated point], [evaluated derivative 1],...[evaluated derivative NumberOfDerivatives]

In pseudo mathematical notation, this could be written as:

```vb
    P(t)  P(t)/dt  P(t)/dtdt ..........
```

In terms of the number of derivatives that can be returned for a curve type, you could write:

| Curve type | Maximum number of derivatives |
| --- | --- |
| Line/circle/ellipse | 2 |
| Intersection curve | 2 |
| Constant parameter line | Determined by underlying surface |
| SP-curve | 2 |
| B-curve | Any number |

where the curve type is from [ICurve::Identity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~Identity.html).

For a curve of type swCurveTypes_e::TRIMMED_TYPE, the number of derivatives is determined by the base curve as obtained from [ICurve::GetBaseCurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~GetBaseCurve.html).

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[ICurve::Evaluate2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~Evaluate2.html)

## Availability

SOLIDWORKS 2007 SP5, Revision Number 15.5
