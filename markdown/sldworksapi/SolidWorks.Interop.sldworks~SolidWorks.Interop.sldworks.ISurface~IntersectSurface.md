---
title: "IntersectSurface Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "IntersectSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IntersectSurface.html"
---

# IntersectSurface Method (ISurface)

Gets a surface-surface intersection.

## Syntax

### Visual Basic (Declaration)

```vb
Function IntersectSurface( _
   ByVal OtherSurf As System.Object, _
   ByRef CurveArray As System.Object, _
   ByRef BoundsArray As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim OtherSurf As System.Object
Dim CurveArray As System.Object
Dim BoundsArray As System.Object
Dim value As System.Boolean

value = instance.IntersectSurface(OtherSurf, CurveArray, BoundsArray)
```

### C#

```csharp
System.bool IntersectSurface(
   System.object OtherSurf,
   out System.object CurveArray,
   out System.object BoundsArray
)
```

### C++/CLI

```cpp
System.bool IntersectSurface(
   System.Object^ OtherSurf,
   [Out] System.Object^ CurveArray,
   [Out] System.Object^ BoundsArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `OtherSurf`: Intersecting [surface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface.html)
- `CurveArray`: Array of [curves](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)
- `BoundsArray`: Array containing the curve bounds

### Return Value

True if successful, false if not

## VBA Syntax

See [Surface::IntersectSurface](ms-its:sldworksapivb6.chm::/sldworks~Surface~IntersectSurface.html).

## Examples

[Get Intersecting Faces (VBA)](Get_Intersecting_Faces_Example_VB.htm)

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::IIntersectSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IIntersectSurface.html)
[ISurface::GetIntersectSurfaceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetIntersectSurfaceCount.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
