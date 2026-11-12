---
title: "GetDistance Method (IEntity)"
project: "SOLIDWORKS API Help"
interface: "IEntity"
member: "GetDistance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~GetDistance.html"
---

# GetDistance Method (IEntity)

Gets the minimum or maximum distance between this entity and the given face or edge entity (see **Remarks**).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDistance( _
   ByVal BaseEntity As System.Object, _
   ByVal MinDistance As System.Boolean, _
   ByVal Parameter As System.Object, _
   ByRef Position1 As System.Object, _
   ByRef Position2 As System.Object, _
   ByRef Distance As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEntity
Dim BaseEntity As System.Object
Dim MinDistance As System.Boolean
Dim Parameter As System.Object
Dim Position1 As System.Object
Dim Position2 As System.Object
Dim Distance As System.Double
Dim value As System.Integer

value = instance.GetDistance(BaseEntity, MinDistance, Parameter, Position1, Position2, Distance)
```

### C#

```csharp
System.int GetDistance(
   System.object BaseEntity,
   System.bool MinDistance,
   System.object Parameter,
   out System.object Position1,
   out System.object Position2,
   out System.double Distance
)
```

### C++/CLI

```cpp
System.int GetDistance(
   System.Object^ BaseEntity,
   System.bool MinDistance,
   System.Object^ Parameter,
   [Out] System.Object^ Position1,
   [Out] System.Object^ Position2,
   [Out] System.double Distance
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BaseEntity`: [IEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity.html) of another edge or face to get distance from this entity (see **Remarks**)
- `MinDistance`: True to return minimum distance between entities; false to return maximum distance between entities
- `Parameter`: If MinDistance = False,

  - and BaseEntity is an edge or curve, specify an array of two doubles (Min, Max), where Min and Max make up the U-parameter range of BaseEntity
  - and BaseEntity is a face, specify an array of four doubles (UMin, VMin, UMax, VMax), where UMin, VMin, UMax, and VMax make up the UV-parameter range of the surface of BaseEntity

  If MinDistance = True,

  - and BaseEntity is an edge or curve, optionally specify an array of two doubles (Min, Max), where Min and Max make up the U-parameter range of BaseEntity
  - and BaseEntity is a face, optionally specify an array of four doubles (UMin, VMin, UMax, VMax), where UMin, VMin, UMax, and VMax make up the UV-parameter range of the surface of BaseEntity
- `Position1`: Array of doubles; coordinates of this entity that were used to measure the distance
- `Position2`: Array of doubles; coordinates of BaseEntity that were used to measure the distance
- `Distance`: Minimum or maximum distance between entities; if Parameter is not specified, minimum distance

### Return Value

0 if success; -1 if failure

## VBA Syntax

See [Entity::GetDistance](ms-its:sldworksapivb6.chm::/sldworks~Entity~GetDistance.html).

## Examples

[Get Distance Between Entities (VBA)](Get_Distance_Between_Entities_Example_VB.htm)
[Get Distance Between Entities (VB.NET)](Get_Distance_Between_Entities_Example_VBNET.htm)
[Get Distance Between Entities (C#)](Get_Distance_Between_Entities_Example_CSharp.htm)

## Remarks

Only face and edge entities are supported.

To populate Parameter you can find the UV parameter ranges as follows:

- For edges and curves, use [IEdge::GetCurveParams2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~GetCurveParams2.html)
- For faces, use [IFace2::GetUVBounds](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetUVBounds.html)

## See Also

[IEntity Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.html)
[IEntity Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity_members.html)
[IEntity::IGetDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~IGetDistance.html)

## Availability

SOLIDWORKS 2009 SP5, Revision Number 17.5
