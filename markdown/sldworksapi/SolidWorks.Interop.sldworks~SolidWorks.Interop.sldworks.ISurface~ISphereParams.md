---
title: "ISphereParams Property (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "ISphereParams"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ISphereParams.html"
---

# ISphereParams Property (ISurface)

Gets the parameters of a spherical surface.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ISphereParams As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim value As System.Double

value = instance.ISphereParams
```

### C#

```csharp
System.double ISphereParams {get;}
```

### C++/CLI

```cpp
property System.double ISphereParams {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of doubles describing the parameters of a spherical surface

## VBA Syntax

See [Surface::ISphereParams](ms-its:sldworksapivb6.chm::/sldworks~Surface~ISphereParams.html).

## Remarks

Returns an array of 4 doubles:

center.x

center.y

center.z

radius

The center and radius values are in meters.

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::SphereParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~SphereParams.html)
[ISurface::IsSphere Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IsSphere.html)
