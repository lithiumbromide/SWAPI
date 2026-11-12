---
title: "IConeParams Property (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "IConeParams"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IConeParams.html"
---

# IConeParams Property (ISurface)

Gets the parameters of a conical surface.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IConeParams As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim value As System.Double

value = instance.IConeParams
```

### C#

```csharp
System.double IConeParams {get;}
```

### C++/CLI

```cpp
property System.double IConeParams {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of doubles describing the parameters of a conical surface

## VBA Syntax

See [Surface::IConeParams](ms-its:sldworksapivb6.chm::/sldworks~Surface~IConeParams.html).

## Remarks

Returns an array of 8 doubles:

- origin.x
- origin.y
- origin.z
- axis.x
- axis.y
- axis.z
- radius
- half angle

The half angle, origin, and radius parameters are in meters.

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::ConeParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ConeParams.html)
[ISurface::IsCone Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IsCone.html)
