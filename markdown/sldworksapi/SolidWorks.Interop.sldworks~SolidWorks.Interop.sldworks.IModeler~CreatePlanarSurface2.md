---
title: "CreatePlanarSurface2 Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "CreatePlanarSurface2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreatePlanarSurface2.html"
---

# CreatePlanarSurface2 Method (IModeler)

Creates a new infinite planar surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreatePlanarSurface2( _
   ByVal VRootPoint As System.Object, _
   ByVal VNormal As System.Object, _
   ByVal VRef As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim VRootPoint As System.Object
Dim VNormal As System.Object
Dim VRef As System.Object
Dim value As System.Object

value = instance.CreatePlanarSurface2(VRootPoint, VNormal, VRef)
```

### C#

```csharp
System.object CreatePlanarSurface2(
   System.object VRootPoint,
   System.object VNormal,
   System.object VRef
)
```

### C++/CLI

```cpp
System.Object^ CreatePlanarSurface2(
   System.Object^ VRootPoint,
   System.Object^ VNormal,
   System.Object^ VRef
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VRootPoint`: Array of 3 doubles (x,y,z) representing the root point of the VNormal and VRef vectors
- `VNormal`: Array of 3 doubles (x,y,z) defining a vector with root point, VRootPoint; this vector must be perpendicular to VRef
- `VRef`: Array of 3 doubles (x,y,z) defining the x-axis on the planar surface with root point, VRootPoint; this vector must be perpendicular to VNormal

### Return Value

Newly created planar [surface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface.html)

## VBA Syntax

See [Modeler::CreatePlanarSurface2](ms-its:sldworksapivb6.chm::/sldworks~Modeler~CreatePlanarSurface2.html).

## Examples

[Create Infinite Plane (VBA)](Create_Infinite_Plane_Example_VB.htm)
[Cut Body in Half Using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)
[Create Temporary Extruded Body (C#)](Create_Temporary_Extruded_Body_Example_CSharp.htm)
[Create Temporary Extruded Body (VB.NET)](Create_Temporary_Extruded_Body_Example_VBNET.htm)
[Create Temporary Extruded Body (VBA)](Create_Temporary_Extruded_Body_Example_VB.htm)

## Remarks

You can use this method with:

- A set of related functions designed to construct a body from trimmed surfaces. It can also be used with trimming curve creation routines to construct a trimmed planar surface.
- Trimming curve creation routines such as [ISurface::AddTrimmingLoop2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~AddTrimmingLoop2.html) or [ISurface::IAddTrimmingLoop2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~IAddTrimmingLoop2.html) to construct a trimmed surface.

See [IBody2::CreatePlanarTrimSurfaceDLL](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreatePlanarTrimSurfaceDLL.html) or [IBody2::ICreatePlanarTrimSurfaceDLL](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ICreatePlanarTrimSurfaceDLL.html), which allows you to create a planar trimmed surface directly from the vertex points.

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::CreateBsplineSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBsplineSurface.html)
[IModeler::CreateConicalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateConicalSurface2.html)
[IModeler::CreateCoonsBSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateCoonsBSurface.html)
[IModeler::CreateCylindricalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateCylindricalSurface2.html)
[IModeler::CreateExtrusionSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateExtrusionSurface.html)
[IModeler::CreateLoftSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateLoftSurface.html)
[IModeler::CreateOffsetSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateOffsetSurface.html)
[IModeler::CreateRuledSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateRuledSurface.html)
[IModeler::CreateSphericalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSphericalSurface2.html)
[IModeler::CreateSweptSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSweptSurface.html)
[IModeler::CreateToroidalSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateToroidalSurface.html)
[IModeler::ICreateBsplineSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBsplineSurface.html)
[IModeler::ICreateConicalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateConicalSurface2.html)
[IModeler::ICreateCylindricalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateCylindricalSurface2.html)
[IModeler::ICreateExtrusionSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateExtrusionSurface.html)
[IModeler::ICreateLoftSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateLoftSurface.html)
[IModeler::ICreateOffsetSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateOffsetSurface.html)
[IModeler::ICreatePlanarSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreatePlanarSurface2.html)
[IModeler::ICreateRuledSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateRuledSurface.html)
[IModeler::ICreateSphericalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSphericalSurface2.html)
[IModeler::ICreateSweptSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSweptSurface.html)
[IModeler::ICreateToroidalSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateToroidalSurface.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
