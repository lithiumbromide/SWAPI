---
title: "IIntersectCurve Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "IIntersectCurve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IIntersectCurve.html"
---

# IIntersectCurve Method (ISurface)

Obsolete. Superseded by [ISurface::IIntersectCurve2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~IIntersectCurve2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IIntersectCurve( _
   ByVal OtherCurve As Curve, _
   ByRef CurveBound As System.Double, _
   ByVal PointCount As System.Integer, _
   ByRef PointArray As System.Double, _
   ByRef TArray As System.Double, _
   ByRef UvArray As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim OtherCurve As Curve
Dim CurveBound As System.Double
Dim PointCount As System.Integer
Dim PointArray As System.Double
Dim TArray As System.Double
Dim UvArray As System.Double
Dim value As System.Boolean

value = instance.IIntersectCurve(OtherCurve, CurveBound, PointCount, PointArray, TArray, UvArray)
```

### C#

```csharp
System.bool IIntersectCurve(
   Curve OtherCurve,
   ref System.double CurveBound,
   System.int PointCount,
   out System.double PointArray,
   out System.double TArray,
   out System.double UvArray
)
```

### C++/CLI

```cpp
System.bool IIntersectCurve(
   Curve^ OtherCurve,
   System.double% CurveBound,
   System.int PointCount,
   [Out] System.double PointArray,
   [Out] System.double TArray,
   [Out] System.double UvArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `OtherCurve`:
- `CurveBound`:
- `PointCount`:
- `PointArray`:
- `TArray`:
- `UvArray`:

## VBA Syntax

See [Surface::IIntersectCurve](ms-its:sldworksapivb6.chm::/sldworks~Surface~IIntersectCurve.html).

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
