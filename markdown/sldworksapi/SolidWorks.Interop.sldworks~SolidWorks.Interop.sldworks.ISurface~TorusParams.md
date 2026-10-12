---
title: "TorusParams Property (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "TorusParams"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~TorusParams.html"
---

# TorusParams Property (ISurface)

Gets the parameters of a toroidal surface.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property TorusParams As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim value As System.Object

value = instance.TorusParams
```

### C#

```csharp
System.object TorusParams {get;}
```

### C++/CLI

```cpp
property System.Object^ TorusParams {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [Surface::TorusParams](ms-its:sldworksapivb6.chm::/sldworks~Surface~TorusParams.html).

## Examples

[Get Parameters of Toroidal Surface (VBA)](Get_Parameters_of_Toroidal_Surface_Example_VB.htm)

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
[ISurface::ITorusParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ITorusParams.html)
[ISurface::IsTorus Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IsTorus.html)
