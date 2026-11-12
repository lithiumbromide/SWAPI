---
title: "CreateCoordinateSystem Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "CreateCoordinateSystem"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateCoordinateSystem.html"
---

# CreateCoordinateSystem Method (IFeatureManager)

Creates a coordinate system feature using the specified entities.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateCoordinateSystem( _
   ByVal OriginPointEntity As System.Object, _
   ByVal XAxisEntities As System.Object, _
   ByVal YAxisEntities As System.Object, _
   ByVal ZAxisEntities As System.Object _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim OriginPointEntity As System.Object
Dim XAxisEntities As System.Object
Dim YAxisEntities As System.Object
Dim ZAxisEntities As System.Object
Dim value As Feature

value = instance.CreateCoordinateSystem(OriginPointEntity, XAxisEntities, YAxisEntities, ZAxisEntities)
```

### C#

```csharp
Feature CreateCoordinateSystem(
   System.object OriginPointEntity,
   System.object XAxisEntities,
   System.object YAxisEntities,
   System.object ZAxisEntities
)
```

### C++/CLI

```cpp
Feature^ CreateCoordinateSystem(
   System.Object^ OriginPointEntity,
   System.Object^ XAxisEntities,
   System.Object^ YAxisEntities,
   System.Object^ ZAxisEntities
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `OriginPointEntity`: Entity (vertex, point, midpoint, or the default point of origin on a part or assembly) for the coordinate system origin
- `XAxisEntities`: Array of entities (vertex, point, or midpoint; linear edge or sketch line; non-linear edge or sketch entity; or planar face) for the x axis
- `YAxisEntities`: Array of entities (vertex, point, or midpoint; linear edge or sketch line; non-linear edge or sketch entity; or planar face) for the y axis
- `ZAxisEntities`: Array of entities (vertex, point, or midpoint; linear edge or sketch line; non-linear edge or sketch entity; or planar face) for the z axis

### Return Value

[Feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::CreateCoordinateSystem](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~CreateCoordinateSystem.html).

## Examples

[Create Coordinate System Feature (VBA)](Create_Coordinate_System_Feature_Example_VB.htm)

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[ICoordinateSystemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData.html)
[IFeatureManager::InsertCoordinateSystem Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCoordinateSystem.html)
[IFeatureManager::CreateCoordinateSystemUsingNumericalValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateCoordinateSystemUsingNumericalValues.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
