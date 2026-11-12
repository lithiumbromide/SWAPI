---
title: "CreateOffsetSurface Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "CreateOffsetSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~CreateOffsetSurface.html"
---

# CreateOffsetSurface Method (IBody)

Obsolete. Superseded by [IBody2::CreateOffsetSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreateOffsetSurface.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateOffsetSurface( _
   ByVal SurfaceIn As System.Object, _
   ByVal Distance As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim SurfaceIn As System.Object
Dim Distance As System.Double
Dim value As System.Object

value = instance.CreateOffsetSurface(SurfaceIn, Distance)
```

### C#

```csharp
System.object CreateOffsetSurface(
   System.object SurfaceIn,
   System.double Distance
)
```

### C++/CLI

```cpp
System.Object^ CreateOffsetSurface(
   System.Object^ SurfaceIn,
   System.double Distance
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SurfaceIn`:
- `Distance`:

## VBA Syntax

See [Body::CreateOffsetSurface](ms-its:sldworksapivb6.chm::/sldworks~Body~CreateOffsetSurface.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
