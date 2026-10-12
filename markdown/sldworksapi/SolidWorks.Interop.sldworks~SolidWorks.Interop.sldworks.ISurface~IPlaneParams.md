---
title: "IPlaneParams Property (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "IPlaneParams"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IPlaneParams.html"
---

# IPlaneParams Property (ISurface)

Gets the parameters of a planar surface.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IPlaneParams As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim value As System.Double

value = instance.IPlaneParams
```

### C#

```csharp
System.double IPlaneParams {get;}
```

### C++/CLI

```cpp
property System.double IPlaneParams {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of doubles describing the parameters of a planar surface

## VBA Syntax

See [Surface::IPlaneParams](ms-its:sldworksapivb6.chm::/sldworks~Surface~IPlaneParams.html).

## Remarks

Returns an array of 6 double values:

normal.x

normal.y

normal.z

rootPoint.x

rootPoint.y

rootPoint.z

The rootPoint values are in meters.

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::PlaneParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~PlaneParams.html)
[ISurface::IsPlane Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IsPlane.html)
