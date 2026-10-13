---
title: "IAddRelation Method (ISketchRelationManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchRelationManager"
member: "IAddRelation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~IAddRelation.html"
---

# IAddRelation Method (ISketchRelationManager)

Adds a relation to the specified entities in the active sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function IAddRelation( _
   ByVal NumEntities As System.Integer, _
   ByRef EntityArray As System.Object, _
   ByVal RelationType As System.Integer _
) As SketchRelation
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchRelationManager
Dim NumEntities As System.Integer
Dim EntityArray As System.Object
Dim RelationType As System.Integer
Dim value As SketchRelation

value = instance.IAddRelation(NumEntities, EntityArray, RelationType)
```

### C#

```csharp
SketchRelation IAddRelation(
   System.int NumEntities,
   ref System.object EntityArray,
   System.int RelationType
)
```

### C++/CLI

```cpp
SketchRelation^ IAddRelation(
   System.int NumEntities,
   System.Object^% EntityArray,
   System.int RelationType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumEntities`: Number of entities to which to add the relation
- `EntityArray`: Array of entities to which to add the relation
- `RelationType`: Type of relation as defined by [swConstraintType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConstraintType_e.html)

### Return Value

[Sketch relation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelation.html)

## VBA Syntax

See [SketchRelationManager::IAddRelation](ms-its:sldworksapivb6.chm::/sldworks~SketchRelationManager~IAddRelation.html).

## Remarks

A sketch must be active for this method to have any effect. Use [IModelDoc2::GetActiveSketch2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetActiveSketch2.html) or [IModelDoc2::IGetActiveSketch2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGetActiveSketch2.html) to determine if a sketch is active.

Call [ISketchRelationManager::GetRelationsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelationManager~GetRelationsCount.html) before calling this method to get the value for NumEntities.

## See Also

[ISketchRelationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager.html)
[ISketchRelationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager_members.html)
[ISketchRelationManager::AddRelation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~AddRelation.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
