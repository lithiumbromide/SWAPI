---
title: "ConeParams Property (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "ConeParams"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ConeParams.html"
---

# ConeParams Property (ISurface)

Obsolete. Superseded by [ISurface::ConeParams2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ConeParams2.html).

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ConeParams As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim value As System.Object

value = instance.ConeParams
```

### C#

```csharp
System.object ConeParams {get;}
```

### C++/CLI

```cpp
property System.Object^ ConeParams {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of doubles describing the parameters of a conical surface

## VBA Syntax

See [Surface::ConeParams](ms-its:sldworksapivb6.chm::/sldworks~Surface~ConeParams.html).

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
[ISurface::IConeParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IConeParams.html)
[ISurface::IsCone Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IsCone.html)
