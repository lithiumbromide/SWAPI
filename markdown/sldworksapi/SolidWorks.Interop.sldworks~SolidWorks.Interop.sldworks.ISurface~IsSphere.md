---
title: "IsSphere Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "IsSphere"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IsSphere.html"
---

# IsSphere Method (ISurface)

Gets whether the surface is a sphere.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsSphere() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim value As System.Boolean

value = instance.IsSphere()
```

### C#

```csharp
System.bool IsSphere()
```

### C++/CLI

```cpp
System.bool IsSphere();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if surface is spherical, false if not

## VBA Syntax

See [Surface::IsSphere](ms-its:sldworksapivb6.chm::/sldworks~Surface~IsSphere.html).

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[IModeler::CreateSphericalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSphericalSurface2.html)
[IModeler::ICreateSphericalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSphericalSurface2.html)
[ISurface::ISphereParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ISphereParams.html)
[ISurface::SphereParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~SphereParams.html)
