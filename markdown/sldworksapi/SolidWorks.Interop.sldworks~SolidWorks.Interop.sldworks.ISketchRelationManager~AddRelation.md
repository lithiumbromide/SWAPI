---
title: "AddRelation Method (ISketchRelationManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchRelationManager"
member: "AddRelation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~AddRelation.html"
---

# AddRelation Method (ISketchRelationManager)

Adds a relation to the specified entities in the active sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddRelation( _
   ByVal Entities As System.Object, _
   ByVal RelationType As System.Integer _
) As SketchRelation
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchRelationManager
Dim Entities As System.Object
Dim RelationType As System.Integer
Dim value As SketchRelation

value = instance.AddRelation(Entities, RelationType)
```

### C#

```csharp
SketchRelation AddRelation(
   System.object Entities,
   System.int RelationType
)
```

### C++/CLI

```cpp
SketchRelation^ AddRelation(
   System.Object^ Entities,
   System.int RelationType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Entities`: Array of entities to which add the relation
- `RelationType`: Type of relation as defined by [swConstraintType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConstraintType_e.html)

### Return Value

[Sketch relation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelation.html)

## VBA Syntax

See [SketchRelationManager::AddRelation](ms-its:sldworksapivb6.chm::/sldworks~SketchRelationManager~AddRelation.html).

## Remarks

A sketch must be active for this method to have any effect. Use [IModelDoc2::GetActiveSketch2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetActiveSketch2.html) or [IModelDoc2::IGetActiveSketch2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGetActiveSketch2.html) to determine if a sketch is active.

## See Also

[ISketchRelationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager.html)
[ISketchRelationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager_members.html)
[ISketchRelationManager::IAddRelation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~IAddRelation.html)
[ISketchRelationManager::GetRelationsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~GetRelationsCount.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
