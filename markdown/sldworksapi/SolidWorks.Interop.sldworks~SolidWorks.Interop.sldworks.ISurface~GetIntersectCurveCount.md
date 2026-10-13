---
title: "GetIntersectCurveCount Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "GetIntersectCurveCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetIntersectCurveCount.html"
---

# GetIntersectCurveCount Method (ISurface)

Obsolete. Superseded by [ISurface::GetIntersectCurveCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~GetIntersectCurveCount2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetIntersectCurveCount( _
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

value = instance.GetIntersectCurveCount(OtherCurve, CurveBound)
```

### C#

```csharp
System.int GetIntersectCurveCount(
   Curve OtherCurve,
   ref System.double CurveBound
)
```

### C++/CLI

```cpp
System.int GetIntersectCurveCount(
   Curve^ OtherCurve,
   System.double% CurveBound
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `OtherCurve`:
- `CurveBound`:

## VBA Syntax

See [Surface::GetIntersectCurveCount](ms-its:sldworksapivb6.chm::/sldworks~Surface~GetIntersectCurveCount.html).

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
