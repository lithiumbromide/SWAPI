---
title: "CreatePlanarSurface Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "CreatePlanarSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreatePlanarSurface.html"
---

# CreatePlanarSurface Method (IBody2)

Creates a new infinite planar surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreatePlanarSurface( _
   ByVal VRootPoint As System.Object, _
   ByVal VNormal As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim VRootPoint As System.Object
Dim VNormal As System.Object
Dim value As System.Object

value = instance.CreatePlanarSurface(VRootPoint, VNormal)
```

### C#

```csharp
System.object CreatePlanarSurface(
   System.object VRootPoint,
   System.object VNormal
)
```

### C++/CLI

```cpp
System.Object^ CreatePlanarSurface(
   System.Object^ VRootPoint,
   System.Object^ VNormal
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VRootPoint`: Array of 3 doubles (x,y,z)
- `VNormal`: Array of 3 doubles (x,y,z)

### Return Value

New planar surface

## VBA Syntax

See [Body2::CreatePlanarSurface](ms-its:sldworksapivb6.chm::/sldworks~Body2~CreatePlanarSurface.html).

## Examples

[Create Body Using Trimmed Surfaces (VBA)](Create_Body_using_Trimmed_Surfaces_Example_VB.htm)

## Remarks

You can use this method with:

- A set of related functions that construct a body from trimmed surfaces.
- Trimming curve creation routines (for example, [ISurface::AddTrimmingLoop2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~AddTrimmingLoop2.html)) to construct a trimmed surface.

To create a planar trimmed surface directly from the vertex points, see [IBody2::CreatePlanarTrimSurfaceDLL](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreatePlanarTrimSurfaceDLL.html).

Any existing object created by this method is destroyed if you call this method again.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::ICreatePlanarSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreatePlanarSurface.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
