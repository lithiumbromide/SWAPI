---
title: "CreateSphericalSurface2 Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "CreateSphericalSurface2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSphericalSurface2.html"
---

# CreateSphericalSurface2 Method (IModeler)

Creates an untrimmed spherical surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateSphericalSurface2( _
   ByVal Center As System.Object, _
   ByVal Axis As System.Object, _
   ByVal RefDir As System.Object, _
   ByVal Radius As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim Center As System.Object
Dim Axis As System.Object
Dim RefDir As System.Object
Dim Radius As System.Double
Dim value As System.Object

value = instance.CreateSphericalSurface2(Center, Axis, RefDir, Radius)
```

### C#

```csharp
System.object CreateSphericalSurface2(
   System.object Center,
   System.object Axis,
   System.object RefDir,
   System.double Radius
)
```

### C++/CLI

```cpp
System.Object^ CreateSphericalSurface2(
   System.Object^ Center,
   System.Object^ Axis,
   System.Object^ RefDir,
   System.double Radius
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Center`: Array containing 3 doubles for XYZ location of the center of the spherical surface
- `Axis`: Array containing 3 doubles
- `RefDir`: rray containing 3 doubles
- `Radius`: Radius at the center

### Return Value

Untrimmed spherical [surface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface.html)

## VBA Syntax

See [Modeler::CreateSphericalSurface2](ms-its:sldworksapivb6.chm::/sldworks~Modeler~CreateSphericalSurface2.html).

## Remarks

The axis argument is the axis of the sphere; the refDir argument is perpendicular to the axis and through the center of the sphere and defines the origin of the UV space.

You can trim the resulting surface to generate a sheet body, for example, using [ISurface::CreateTrimmedSheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~CreateTrimmedSheet.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::CreateBsplineSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBsplineSurface.html)
[IModeler::CreateConicalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateConicalSurface2.html)
[IModeler::CreateCoonsBSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateCoonsBSurface.html)
[IModeler::CreateCylindricalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateCylindricalSurface2.html)
[IModeler::CreateExtrusionSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateExtrusionSurface.html)
[IModeler::CreateOffsetSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateOffsetSurface.html)
[IModeler::CreatePlanarSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreatePlanarSurface2.html)
[IModeler::CreateRuledSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateRuledSurface.html)
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
[IModeler::ICreateSweptSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSweptSurface.html)
[IModeler::ICreateToroidalSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateToroidalSurface.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
