---
title: "ICylinderParams Property (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "ICylinderParams"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ICylinderParams.html"
---

# ICylinderParams Property (ISurface)

Gets the parameters of a cylindrical surface.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ICylinderParams As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim value As System.Double

value = instance.ICylinderParams
```

### C#

```csharp
System.double ICylinderParams {get;}
```

### C++/CLI

```cpp
property System.double ICylinderParams {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of doubles describing the parameters of a cylindrical surface

## VBA Syntax

See [Surface::ICylinderParams](ms-its:sldworksapivb6.chm::/sldworks~Surface~ICylinderParams.html).

## Remarks

Returns an array of 7 doubles:

- origin.x
- origin.y
- origin.z
- axis.x
- axis.y
- axis.z
- radius

The origin and radius parameters are in meters.

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::CylinderParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~CylinderParams.html)
[ISurface::IsCylinder Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IsCylinder.html)
