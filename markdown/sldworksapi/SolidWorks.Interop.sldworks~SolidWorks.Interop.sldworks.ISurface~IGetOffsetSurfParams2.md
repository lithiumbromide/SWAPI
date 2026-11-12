---
title: "IGetOffsetSurfParams2 Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "IGetOffsetSurfParams2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetOffsetSurfParams2.html"
---

# IGetOffsetSurfParams2 Method (ISurface)

Gets the overall offset distance of this offset surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetOffsetSurfParams2( _
   ByRef BaseSurf As Surface, _
   ByRef Sense As System.Boolean _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim BaseSurf As Surface
Dim Sense As System.Boolean
Dim value As System.Double

value = instance.IGetOffsetSurfParams2(BaseSurf, Sense)
```

### C#

```csharp
System.double IGetOffsetSurfParams2(
   out Surface BaseSurf,
   out System.bool Sense
)
```

### C++/CLI

```cpp
System.double IGetOffsetSurfParams2(
   [Out] Surface^ BaseSurf,
   [Out] System.bool Sense
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BaseSurf`: Base [surface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface.html) used to generate the offset surface
- `Sense`: If true, then the offset is in the direction of the original surface's normal; if false, then the offset is in the opposite direction of the original surface's normal

### Return Value

Offset for the surface

## VBA Syntax

See [Surface::IGetOffsetSurfParams2](ms-its:sldworksapivb6.chm::/sldworks~Surface~IGetOffsetSurfParams2.html).

## Remarks

This method can get a pointer to the base surface and its sense. Both BaseSurf and Sense parameters can be a NULL pointer.

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::GetOffsetSurfParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetOffsetSurfParams2.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
