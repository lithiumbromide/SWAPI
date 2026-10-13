---
title: "ICreateOffsetSurface Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "ICreateOffsetSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateOffsetSurface.html"
---

# ICreateOffsetSurface Method (IBody2)

Creates a new surface offset from an existing surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateOffsetSurface( _
   ByVal SurfaceIn As Surface, _
   ByVal Distance As System.Double _
) As Surface
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim SurfaceIn As Surface
Dim Distance As System.Double
Dim value As Surface

value = instance.ICreateOffsetSurface(SurfaceIn, Distance)
```

### C#

```csharp
Surface ICreateOffsetSurface(
   Surface SurfaceIn,
   System.double Distance
)
```

### C++/CLI

```cpp
Surface^ ICreateOffsetSurface(
   Surface^ SurfaceIn,
   System.double Distance
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SurfaceIn`: [Surface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface.html) from which to offset the new surface
- `Distance`: Offset distance

### Return Value

Newly created offset [surface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface.html)

## VBA Syntax

See [Body2::ICreateOffsetSurface](ms-its:sldworksapivb6.chm::/sldworks~Body2~ICreateOffsetSurface.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::CreateOffsetSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateOffsetSurface.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
