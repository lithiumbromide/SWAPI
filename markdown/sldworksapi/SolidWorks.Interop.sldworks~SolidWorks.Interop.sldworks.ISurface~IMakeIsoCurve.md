---
title: "IMakeIsoCurve Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "IMakeIsoCurve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IMakeIsoCurve.html"
---

# IMakeIsoCurve Method (ISurface)

Creates a curve that represents the ISO line of a given surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function IMakeIsoCurve( _
   ByVal UorV As System.Boolean, _
   ByVal UvValue As System.Double _
) As Curve
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim UorV As System.Boolean
Dim UvValue As System.Double
Dim value As Curve

value = instance.IMakeIsoCurve(UorV, UvValue)
```

### C#

```csharp
Curve IMakeIsoCurve(
   System.bool UorV,
   System.double UvValue
)
```

### C++/CLI

```cpp
Curve^ IMakeIsoCurve(
   System.bool UorV,
   System.double UvValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UorV`: True to specify V, false to specify U
- `UvValue`: U or V vertex or point that specifies the intersection of two curves

### Return Value

[Curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)

## VBA Syntax

See [Surface::IMakeIsoCurve](ms-its:sldworksapivb6.chm::/sldworks~Surface~IMakeIsoCurve.html).

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::MakeIsoCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~MakeIsoCurve.html)
[ISurface::MakeIsoCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~MakeIsoCurves.html)
[ISurface::IMakeIsoCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IMakeIsoCurves.html)
[ISurface::IGetMakeIsoCurvesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetMakeIsoCurvesCount.html)

## Availability

SOLIDWORKS 2001Plus SP2, Revision Number 10.2
