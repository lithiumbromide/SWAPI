---
title: "ICreateOffsetSurface Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "ICreateOffsetSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~ICreateOffsetSurface.html"
---

# ICreateOffsetSurface Method (IBody)

Obsolete. Superseded by [IBody2::ICreateOffsetSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ICreateOffsetSurface.html).

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
Dim instance As IBody
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

- `SurfaceIn`:
- `Distance`:

## VBA Syntax

See [Body::ICreateOffsetSurface](ms-its:sldworksapivb6.chm::/sldworks~Body~ICreateOffsetSurface.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
