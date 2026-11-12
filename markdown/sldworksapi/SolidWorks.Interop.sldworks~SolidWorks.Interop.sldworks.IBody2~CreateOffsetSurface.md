---
title: "CreateOffsetSurface Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "CreateOffsetSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateOffsetSurface.html"
---

# CreateOffsetSurface Method (IBody2)

Creates a new surface offset from an existing surface.

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
Dim instance As IBody2
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

- `SurfaceIn`: Surface from which to offset the new surface
- `Distance`: Offset distance

### Return Value

Newly created offset surface

## VBA Syntax

See [Body2::CreateOffsetSurface](ms-its:sldworksapivb6.chm::/sldworks~Body2~CreateOffsetSurface.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::ICreateOffsetSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateOffsetSurface.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
