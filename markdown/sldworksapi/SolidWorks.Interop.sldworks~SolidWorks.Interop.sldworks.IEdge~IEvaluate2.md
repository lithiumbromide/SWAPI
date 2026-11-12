---
title: "IEvaluate2 Method (IEdge)"
project: "SOLIDWORKS API Help"
interface: "IEdge"
member: "IEvaluate2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IEvaluate2.html"
---

# IEvaluate2 Method (IEdge)

Evaluates the edge for the specified U parameter.

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
Dim instance As IEdge
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

- `Parameter`: Curve parameter U value (see **Remarks**)
- `NumberOfDerivatives`: Number of derivatives (see **Remarks**)

### Return Value

Array of doubles (see Remarks)

## VBA Syntax

See [Edge::IEvaluate2](ms-its:sldworksapivb6.chm::/sldworks~Edge~IEvaluate2.html).

## Remarks

Use [IEdge::IGetCurveParams2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetCurveParams2.html) to determine the valid range of U parameter values for Parameter.

The returned array contains ((NumberOfDerivatives + 1) * 3) + 1 doubles:

[evaluated_point], [evaluated_derivative_1],...[evaluated_derivative_NumberOfDerivatives, **[**`status_code`**]**

where `status_code` is a packed double. After unpacking `status_code` into two longs, the lower long value is 1 for success or 0 for error. See the Example in [IEdge::Evaluate2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~Evaluate2.html).

| If curve type ICurve::Identity is... | Then the maximum number of derivatives is... |
| --- | --- |
| Line/circle/ellipse | 2 |
| Intersection curve | 2 |
| Constant parameter line | Determined by underlying surface |
| SP-curve | 2 |
| B-curve | Any number |

For a curve of type swCurveTypes_e::TRIMMED_TYPE, the number of derivatives is determined by the base curve as obtained from [ICurve::GetBaseCurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~GetBaseCurve.html).

## See Also

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.html)
[IEdge::GetCurveParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCurveParams2.html)

## Availability

SOLIDWORKS 2007 SP5, Revision Number 15.5
