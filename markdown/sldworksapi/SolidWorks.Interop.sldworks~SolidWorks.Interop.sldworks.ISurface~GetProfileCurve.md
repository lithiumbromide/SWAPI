---
title: "GetProfileCurve Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "GetProfileCurve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetProfileCurve.html"
---

# GetProfileCurve Method (ISurface)

Gets the curve used to create the surface of revolution or extrusion surface and applies to only surface of revolution or extrusion surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetProfileCurve() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim value As System.Object

value = instance.GetProfileCurve()
```

### C#

```csharp
System.object GetProfileCurve()
```

### C++/CLI

```cpp
System.Object^ GetProfileCurve();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Profile [curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html) used to create the surface of revolution or extrusion surface

## VBA Syntax

See [Surface::GetProfileCurve](ms-its:sldworksapivb6.chm::/sldworks~Surface~GetProfileCurve.html).

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::IGetProfileCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetProfileCurve.html)
