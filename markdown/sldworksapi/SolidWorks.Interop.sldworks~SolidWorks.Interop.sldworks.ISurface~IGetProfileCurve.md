---
title: "IGetProfileCurve Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "IGetProfileCurve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetProfileCurve.html"
---

# IGetProfileCurve Method (ISurface)

Gets the curve used to create the surface of revolution or extrusion surface and applies to only surface of revolution or extrusion surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetProfileCurve() As Curve
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim value As Curve

value = instance.IGetProfileCurve()
```

### C#

```csharp
Curve IGetProfileCurve()
```

### C++/CLI

```cpp
Curve^ IGetProfileCurve();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Profile [curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html) used to create the surface of revolution or extrusion surface

## VBA Syntax

See [Surface::IGetProfileCurve](ms-its:sldworksapivb6.chm::/sldworks~Surface~IGetProfileCurve.html).

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::GetProfileCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetProfileCurve.html)
