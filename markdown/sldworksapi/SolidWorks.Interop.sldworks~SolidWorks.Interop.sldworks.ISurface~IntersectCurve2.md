---
title: "IntersectCurve2 Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "IntersectCurve2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IntersectCurve2.html"
---

# IntersectCurve2 Method (ISurface)

Gets a surface-curve intersection.

## Syntax

### Visual Basic (Declaration)

```vb
Function IntersectCurve2( _
   ByVal OtherCurve As System.Object, _
   ByVal CurveBound As System.Object, _
   ByRef PointArray As System.Object, _
   ByRef TArray As System.Object, _
   ByRef UvArray As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim OtherCurve As System.Object
Dim CurveBound As System.Object
Dim PointArray As System.Object
Dim TArray As System.Object
Dim UvArray As System.Object
Dim value As System.Boolean

value = instance.IntersectCurve2(OtherCurve, CurveBound, PointArray, TArray, UvArray)
```

### C#

```csharp
System.bool IntersectCurve2(
   System.object OtherCurve,
   System.object CurveBound,
   out System.object PointArray,
   out System.object TArray,
   out System.object UvArray
)
```

### C++/CLI

```cpp
System.bool IntersectCurve2(
   System.Object^ OtherCurve,
   System.Object^ CurveBound,
   [Out] System.Object^ PointArray,
   [Out] System.Object^ TArray,
   [Out] System.Object^ UvArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `OtherCurve`: [Curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)
- `CurveBound`: Array of 6 doubles representing the start and end points of the curve
- `PointArray`: Array of points
- `TArray`: Array of parameters on curve
- `UvArray`: Array of parameters on surface

### Return Value

True if getting the intersection succeeded, false if not

## VBA Syntax

See [Surface::IntersectCurve2](ms-its:sldworksapivb6.chm::/sldworks~Surface~IntersectCurve2.html).

## Remarks

The curves must be bounded.

Visual Basic and C++ Dispatch applications should use this method instead of using [ISurface::GetIntersectCurveCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~GetIntersectCurveCount2.html).

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::IIntersectCurve2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IIntersectCurve2.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
