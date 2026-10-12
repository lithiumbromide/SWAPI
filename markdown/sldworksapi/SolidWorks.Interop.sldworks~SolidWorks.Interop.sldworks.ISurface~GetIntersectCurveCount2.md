---
title: "GetIntersectCurveCount2 Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "GetIntersectCurveCount2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetIntersectCurveCount2.html"
---

# GetIntersectCurveCount2 Method (ISurface)

Gets the number of points for a surface-curve intersection.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetIntersectCurveCount2( _
   ByVal OtherCurve As Curve, _
   ByRef CurveBound As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim OtherCurve As Curve
Dim CurveBound As System.Double
Dim value As System.Integer

value = instance.GetIntersectCurveCount2(OtherCurve, CurveBound)
```

### C#

```csharp
System.int GetIntersectCurveCount2(
   Curve OtherCurve,
   ref System.double CurveBound
)
```

### C++/CLI

```cpp
System.int GetIntersectCurveCount2(
   Curve^ OtherCurve,
   System.double% CurveBound
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `OtherCurve`: [Curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)
- `CurveBound`: Array of 6 doubles representing the start and end points of the curve

### Return Value

Number of points

## VBA Syntax

See [Surface::GetIntersectCurveCount2](ms-its:sldworksapivb6.chm::/sldworks~Surface~GetIntersectCurveCount2.html).

## Remarks

Visual Basic and C++ Dispatch applications should use [ISurface::IntersectCurve2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~IIntersectCurve2.html) instead of this method.

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::IIntersectCurve2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IIntersectCurve2.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
