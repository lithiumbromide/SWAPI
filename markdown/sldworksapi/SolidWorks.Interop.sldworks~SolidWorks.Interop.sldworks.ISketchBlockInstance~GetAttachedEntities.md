---
title: "GetAttachedEntities Method (ISketchBlockInstance)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockInstance"
member: "GetAttachedEntities"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetAttachedEntities.html"
---

# GetAttachedEntities Method (ISketchBlockInstance)

Gets the entities to which this block instance is attached.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAttachedEntities( _
   ByRef Entities As System.Object, _
   ByRef EntityTypes As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockInstance
Dim Entities As System.Object
Dim EntityTypes As System.Object
Dim value As System.Boolean

value = instance.GetAttachedEntities(Entities, EntityTypes)
```

### C#

```csharp
System.bool GetAttachedEntities(
   out System.object Entities,
   out System.object EntityTypes
)
```

### C++/CLI

```cpp
System.bool GetAttachedEntities(
   [Out] System.Object^ Entities,
   [Out] System.Object^ EntityTypes
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Entities`: Array of attached entities
- `EntityTypes`: Array of longs or integers (see [Long vs. Integer](sldworksapiprogguide.chm::/overview/Long_vs_Integer.htm)) of the types of attached entities (see **Remarks**)

### Return Value

True if the entities are retrieved, false if not

## VBA Syntax

See [SketchBlockInstance::GetAttachedEntities](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockInstance~GetAttachedEntities.html).

## Remarks

The arrays returned by this method can contain one or more different object and type.

| Possible returned Entities | Possible returned EntityTypes |
| --- | --- |
| IFace2 | swSelFACES |
| IEdge | swSelEDGES |
| IVertex | swSelVERTICES |
| ISketchSegment | swSelSKETCHSEGS |
| ISketchPoint | swSelSKETCHPOINTS |

A block instance that was inserted with a leader attached to an entity remains attached to that entity even if the leader is hidden. If the leader is shown again later on, the leader still points to the entity and the block instance is still properly associated with the entity.

## See Also

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.html)
[ISketchBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.html)

## Availability

SOLIDWORKS 2007 SP2, Revision Number 15.2
