---
title: "Evaluate Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "Evaluate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~Evaluate.html"
---

# Evaluate Method (ICurve)

Obsolete. Superseded by [ICurve::Evaluate2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~Evaluate2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function Evaluate( _
   ByVal Parameter As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim Parameter As System.Double
Dim value As System.Object

value = instance.Evaluate(Parameter)
```

### C#

```csharp
System.object Evaluate(
   System.double Parameter
)
```

### C++/CLI

```cpp
System.Object^ Evaluate(
   System.double Parameter
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Parameter`: Curve parameter

### Return Value

Array containing an array of doubles (see **Remarks**)

## VBA Syntax

See [Curve::Evaluate](ms-its:sldworksapivb6.chm::/sldworks~Curve~Evaluate.html).

## Remarks

To determine a valid parameter range, use [ICurve::GetEndParams](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~GetEndParams.html) or [IEdge::GetCurveParams2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~GetCurveParams2.html) or [IEdge::IGetCurveParams2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~IGetCurveParams2.html).

The OLE Automation return value is an array of doubles with the following format:

[ PointX, PointY, PointZ, TangentX, TangentY, TangentZ, Success ]

where:

- PointX, PointY, and PointZ represent the 3D point in space for the given parameter
- TangentX, TangentY, and TangentZ represent the tangent vector at the point
- True if the operation is successful

This method returns values in meters.

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[ICurve::IEvaluate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IEvaluate.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
