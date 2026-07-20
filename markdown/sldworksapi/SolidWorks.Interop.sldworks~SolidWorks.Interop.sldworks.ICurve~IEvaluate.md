---
title: "IEvaluate Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "IEvaluate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IEvaluate.html"
---

# IEvaluate Method (ICurve)

Obsolete. Superseded by

[ICurve::Evaluate2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~Evaluate2.html)

.

## Syntax

### Visual Basic (Declaration)

```vb
Function IEvaluate( _
   ByVal Parameter As System.Double _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim Parameter As System.Double
Dim value As System.Double

value = instance.IEvaluate(Parameter)
```

### C#

```csharp
System.double IEvaluate(
   System.double Parameter
)
```

### C++/CLI

```cpp
System.double IEvaluate(
   System.double Parameter
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `Parameter`: Curve parameter

### Return Value

Pointer to an array of doubles (see**Remarks**)

## VBA Syntax

See

[Curve::IEvaluate](ms-its:sldworksapivb6.chm::/sldworks~Curve~IEvaluate.html)

.

## Remarks

To determine a valid parameter range, use[ICurve::GetEndParams](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~GetEndParams.html)or[IEdge::GetCurveParams2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~GetCurveParams2.html)or[IEdge::IGetCurveParams2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~IGetCurveParams2.html).

The OLE Automation return value is an array of doubles with the following format:

[PointX, PointY, PointZ, TangentX, TangentY, TangentZ, Success]

where:

- PointX,PointY,andPointZrepresent the 3D point in space for the given parameter
- TangentX,TangentY,andTangentZrepresent the tangent vector at the point
- True if the operation is successful

The COM return value is an array of 6 doubles representing the point and tangent. The success value is determined from the HRESULT return.

This method returns values in meters.

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)

[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
