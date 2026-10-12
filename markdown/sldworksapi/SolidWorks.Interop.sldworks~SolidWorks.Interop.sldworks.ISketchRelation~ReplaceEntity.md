---
title: "ReplaceEntity Method (ISketchRelation)"
project: "SOLIDWORKS API Help"
interface: "ISketchRelation"
member: "ReplaceEntity"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~ReplaceEntity.html"
---

# ReplaceEntity Method (ISketchRelation)

Replaces an entity in this sketch relation.

## Syntax

### Visual Basic (Declaration)

```vb
Function ReplaceEntity( _
   ByVal OldEntity As System.Object, _
   ByVal NewEntity As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchRelation
Dim OldEntity As System.Object
Dim NewEntity As System.Object
Dim value As System.Boolean

value = instance.ReplaceEntity(OldEntity, NewEntity)
```

### C#

```csharp
System.bool ReplaceEntity(
   System.object OldEntity,
   System.object NewEntity
)
```

### C++/CLI

```cpp
System.bool ReplaceEntity(
   System.Object^ OldEntity,
   System.Object^ NewEntity
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `OldEntity`: Entity to replace
- `NewEntity`: Replacement entity

### Return Value

True if OldEntity is replaced by NewEntity, false if not

## VBA Syntax

See [SketchRelation::ReplaceEntity](ms-its:sldworksapivb6.chm::/sldworks~SketchRelation~ReplaceEntity.html).

## Examples

[Replace Sketch Relation (VBA)](Replace_Sketch_Relation_Example_VB.htm)

## Remarks

This method requires that the sketch be in edit mode.

## See Also

[ISketchRelation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation.html)
[ISketchRelation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
