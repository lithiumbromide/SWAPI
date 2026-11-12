---
title: "ITorusParams Property (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "ITorusParams"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ITorusParams.html"
---

# ITorusParams Property (ISurface)

Gets the parameters of a toroidal surface.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ITorusParams As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim value As System.Double

value = instance.ITorusParams
```

### C#

```csharp
System.double ITorusParams {get;}
```

### C++/CLI

```cpp
property System.double ITorusParams {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of doubles describing the parameters of a toroidal surface

## VBA Syntax

See [Surface::ITorusParams](ms-its:sldworksapivb6.chm::/sldworks~Surface~ITorusParams.html).

## Remarks

Returns an array of 8 double values:

center.x

center.y

center.z

axis.x

axis.y

axis.z

major radius - the distance between the center of torus and the center of revolved circle

minor radius - the radius of the revolved circle

NOTES:

- The real major radius (the outer radius) of the torus is major radius + minor radius.
- The center, major radius, and minor radius are in meters.
- Possible values that indicate a type of self-intersecting torus:

  - Apple - when the major radius is positive and less than or equal to the minor radius.
  - Lemon - when the major radius is negative and the sum of the radii is positive.

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::TorusParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~TorusParams.html)
[ISurface::IsTorus Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IsTorus.html)
