---
title: "GetOffsetSurfParams2 Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "GetOffsetSurfParams2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetOffsetSurfParams2.html"
---

# GetOffsetSurfParams2 Method (ISurface)

Gets the overall offset distance of this offset surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetOffsetSurfParams2( _
   ByRef BaseSurf As System.Object, _
   ByRef Sense As System.Boolean _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim BaseSurf As System.Object
Dim Sense As System.Boolean
Dim value As System.Double

value = instance.GetOffsetSurfParams2(BaseSurf, Sense)
```

### C#

```csharp
System.double GetOffsetSurfParams2(
   out System.object BaseSurf,
   out System.bool Sense
)
```

### C++/CLI

```cpp
System.double GetOffsetSurfParams2(
   [Out] System.Object^ BaseSurf,
   [Out] System.bool Sense
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BaseSurf`: Base [surface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface.html) used to generate the offset surface
- `Sense`: If true, then the offset is in the direction of the original surface's normal, if fakse, then the offset is in the opposite direction of the original surface's normal

### Return Value

Offset for the surface

## VBA Syntax

See [Surface::GetOffsetSurfParams2](ms-its:sldworksapivb6.chm::/sldworks~Surface~GetOffsetSurfParams2.html).

## Remarks

This method can get a pointer to the base surface and its sense. Both BaseSurf and Sense parameters can be a NULL pointer.

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::IGetOffsetSurfParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetOffsetSurfParams2.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
