---
title: "MakeIsoCurve Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "MakeIsoCurve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~MakeIsoCurve.html"
---

# MakeIsoCurve Method (ISurface)

Creates an untrimmed curve using the specified surface parameter.

## Syntax

### Visual Basic (Declaration)

```vb
Function MakeIsoCurve( _
   ByVal UorV As System.Boolean, _
   ByVal UvValue As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim UorV As System.Boolean
Dim UvValue As System.Double
Dim value As System.Object

value = instance.MakeIsoCurve(UorV, UvValue)
```

### C#

```csharp
System.object MakeIsoCurve(
   System.bool UorV,
   System.double UvValue
)
```

### C++/CLI

```cpp
System.Object^ MakeIsoCurve(
   System.bool UorV,
   System.double UvValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UorV`: True to specify v, false to specify u
- `UvValue`: U or v value

### Return Value

[Curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)

## VBA Syntax

See [Surface::MakeIsoCurve](ms-its:sldworksapivb6.chm::/sldworks~Surface~MakeIsoCurve.html).

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::IMakeIsoCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IMakeIsoCurve.html)
[ISurface::IMakeIsoCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IMakeIsoCurves.html)
[ISurface::MakeIsoCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~MakeIsoCurves.html)
[ISurface::IGetMakeIsoCurvesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetMakeIsoCurvesCount.html)

## Availability

SOLIDWORKS 2001Plus SP2, Revision Number 10.2
