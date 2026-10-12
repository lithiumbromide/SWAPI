---
title: "Evaluate2 Method (ICoEdge)"
project: "SOLIDWORKS API Help"
interface: "ICoEdge"
member: "Evaluate2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~Evaluate2.html"
---

# Evaluate2 Method (ICoEdge)

Gets the (X,Y,Z) location and the tangency vector on the coedge at the specified position.

## Syntax

### Visual Basic (Declaration)

```vb
Function Evaluate2( _
   ByVal Param As System.Double, _
   ByVal NumberOfDerivatives As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICoEdge
Dim Param As System.Double
Dim NumberOfDerivatives As System.Integer
Dim value As System.Object

value = instance.Evaluate2(Param, NumberOfDerivatives)
```

### C#

```csharp
System.object Evaluate2(
   System.double Param,
   System.int NumberOfDerivatives
)
```

### C++/CLI

```cpp
System.Object^ Evaluate2(
   System.double Param,
   System.int NumberOfDerivatives
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Param`: Curve parameter desired (U value desired for evaluation)
- `NumberOfDerivatives`: Number of derivatives

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [CoEdge::Evaluate2](ms-its:sldworksapivb6.chm::/sldworks~CoEdge~Evaluate2.html).

## Remarks

The tangency vector is defined to be in the direction of the coedge.

The format of the return value is an array of (NumberOfDerivatives + 1) * 3 doubles:

[evaluated point], [evaluated derivative 1],...[evaluated derivative NumberOfDerivatives]

In pseudo mathematical notation, this can be written as:

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

[ICoEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge.html)
[ICoEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge_members.html)
[ICoEdge::IEvaluate2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IEvaluate2.html)
[ICoEdge::GetCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetCurveParams.html)
[ICoEdge::IGetCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IGetCurveParams.html)

## Availability

SOLIDWORKS 2007 SP5, Revision Number 15.5
