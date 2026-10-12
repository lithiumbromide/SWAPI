---
title: "SphereParams Property (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "SphereParams"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~SphereParams.html"
---

# SphereParams Property (ISurface)

Gets the parameters of a spherical surface.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property SphereParams As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim value As System.Object

value = instance.SphereParams
```

### C#

```csharp
System.object SphereParams {get;}
```

### C++/CLI

```cpp
property System.Object^ SphereParams {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of doubles describing the parameters of a spherical surface

## VBA Syntax

See [Surface::SphereParams](ms-its:sldworksapivb6.chm::/sldworks~Surface~SphereParams.html).

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
[ISurface::IsSphere Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IsSphere.html)
[ISurface::ISphereParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ISphereParams.html)
