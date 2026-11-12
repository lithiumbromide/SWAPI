---
title: "CreateRuledSurface Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "CreateRuledSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateRuledSurface.html"
---

# CreateRuledSurface Method (IModeler)

Creates a ruled surface from the curves.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateRuledSurface( _
   ByVal Curve1In As System.Object, _
   ByVal Curve2In As System.Object, _
   ByVal Apex As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim Curve1In As System.Object
Dim Curve2In As System.Object
Dim Apex As System.Object
Dim value As System.Object

value = instance.CreateRuledSurface(Curve1In, Curve2In, Apex)
```

### C#

```csharp
System.object CreateRuledSurface(
   System.object Curve1In,
   System.object Curve2In,
   System.object Apex
)
```

### C++/CLI

```cpp
System.Object^ CreateRuledSurface(
   System.Object^ Curve1In,
   System.Object^ Curve2In,
   System.Object^ Apex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Curve1In`: First [curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)
- `Curve2In`: Second [curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)
- `Apex`: Array of 3 doubles, (x, y, z), the apex point

### Return Value

Newly created ruled [surface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface.html)

## VBA Syntax

See [Modeler::CreateRuledSurface](ms-its:sldworksapivb6.chm::/sldworks~Modeler~CreateRuledSurface.html).

## Examples

[Create Ruled Surface (VBA)](Create_Ruled_Surface_Example_VB.htm)

## Remarks

Valid input curves are b-curves.

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::CreateBsplineSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBsplineSurface.html)
[IModeler::CreateConicalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateConicalSurface2.html)
[IModeler::CreateCoonsBSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateCoonsBSurface.html)
[IModeler::CreateCylindricalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateCylindricalSurface2.html)
[IModeler::CreateExtrudedBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateExtrudedBody.html)
[IModeler::CreateExtrusionSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateExtrusionSurface.html)
[IModeler::CreateLoftSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateLoftSurface.html)
[IModeler::CreateOffsetSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateOffsetSurface.html)
[IModeler::CreatePlanarSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreatePlanarSurface2.html)
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
[IModeler::ICreateSheetFromSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSheetFromSurface2.html)
[IModeler::ICreateSphericalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSphericalSurface2.html)
[IModeler::ICreateSweptSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSweptSurface.html)
[IModeler::ICreateToroidalSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateToroidalSurface.html)
[IModeler::CreateRuledSurfaceFromEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateRuledSurfaceFromEdge.html)
[IModeler::ICreateRuledSurfaceFromEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateRuledSurfaceFromEdge.html)
[IFeatureManager::InsertRuledSurfaceFromEdge2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertRuledSurfaceFromEdge2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
