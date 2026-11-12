---
title: "ISetCurrentSurface Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "ISetCurrentSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~ISetCurrentSurface.html"
---

# ISetCurrentSurface Method (IBody)

Obsolete. Superseded by [IBody2::ISetCurrentSurface.](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ISetCurrentSurface.html)

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetCurrentSurface( _
   ByVal SurfaceIn As Surface _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim SurfaceIn As Surface

instance.ISetCurrentSurface(SurfaceIn)
```

### C#

```csharp
void ISetCurrentSurface(
   Surface SurfaceIn
)
```

### C++/CLI

```cpp
void ISetCurrentSurface(
   Surface^ SurfaceIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SurfaceIn`:

## VBA Syntax

See [Body::ISetCurrentSurface](ms-its:sldworksapivb6.chm::/sldworks~Body~ISetCurrentSurface.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
