---
title: "IntersectCurve Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "IntersectCurve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IntersectCurve.html"
---

# IntersectCurve Method (ISurface)

Obsolete. Superseded by [ISurface::IntersectCurve2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IIntersectCurve2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IntersectCurve( _
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

value = instance.IntersectCurve(OtherCurve, CurveBound, PointArray, TArray, UvArray)
```

### C#

```csharp
System.bool IntersectCurve(
   System.object OtherCurve,
   System.object CurveBound,
   out System.object PointArray,
   out System.object TArray,
   out System.object UvArray
)
```

### C++/CLI

```cpp
System.bool IntersectCurve(
   System.Object^ OtherCurve,
   System.Object^ CurveBound,
   [Out] System.Object^ PointArray,
   [Out] System.Object^ TArray,
   [Out] System.Object^ UvArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `OtherCurve`:
- `CurveBound`:
- `PointArray`:
- `TArray`:
- `UvArray`:

## VBA Syntax

See [Surface::IntersectCurve](ms-its:sldworksapivb6.chm::/sldworks~Surface~IntersectCurve.html).

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
