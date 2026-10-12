---
title: "ICreatePlanarTrimSurfaceDLL Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "ICreatePlanarTrimSurfaceDLL"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreatePlanarTrimSurfaceDLL.html"
---

# ICreatePlanarTrimSurfaceDLL Method (IBody2)

Creates a planar trim surface for this body.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ICreatePlanarTrimSurfaceDLL( _
   ByVal VertexCount As System.Integer, _
   ByRef Points As System.Double, _
   ByRef Normal As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim VertexCount As System.Integer
Dim Points As System.Double
Dim Normal As System.Double

instance.ICreatePlanarTrimSurfaceDLL(VertexCount, Points, Normal)
```

### C#

```csharp
void ICreatePlanarTrimSurfaceDLL(
   System.int VertexCount,
   ref System.double Points,
   ref System.double Normal
)
```

### C++/CLI

```cpp
void ICreatePlanarTrimSurfaceDLL(
   System.int VertexCount,
   System.double% Points,
   System.double% Normal
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VertexCount`: Number of vertices
- `Points`: Pointer to an array of doubles describing the points for the surface; trim curves are automatically created between each sequential vertex
- `Normal`: Pointer to an array of normal vectors for the surface

## VBA Syntax

See [Body2::ICreatePlanarTrimSurfaceDLL](ms-its:sldworksapivb6.chm::/sldworks~Body2~ICreatePlanarTrimSurfaceDLL.html).

## Remarks

You can use this method instead of [IBody2:CreateTrimmedSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreateTrimmedSurface.html), [IBody2::ICreatePlanarSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ICreatePlanarSurface.html), and [ISurface::IAddTrimmingLoop2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~IAddTrimmingLoop2.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::CreatePlanarTrimSurfaceDLL Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreatePlanarTrimSurfaceDLL.html)

## Availability

SOLIDWORKS 2004 SP1, Revision Number 12
