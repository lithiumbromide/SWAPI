---
title: "IGetAllowedRelationsCount Method (ISketchRelationManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchRelationManager"
member: "IGetAllowedRelationsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~IGetAllowedRelationsCount.html"
---

# IGetAllowedRelationsCount Method (ISketchRelationManager)

Gets the number of sketch relations valid for the specified entities.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetAllowedRelationsCount( _
   ByVal NumEntities As System.Integer, _
   ByRef EntityArray As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchRelationManager
Dim NumEntities As System.Integer
Dim EntityArray As System.Object
Dim value As System.Integer

value = instance.IGetAllowedRelationsCount(NumEntities, EntityArray)
```

### C#

```csharp
System.int IGetAllowedRelationsCount(
   System.int NumEntities,
   ref System.object EntityArray
)
```

### C++/CLI

```cpp
System.int IGetAllowedRelationsCount(
   System.int NumEntities,
   System.Object^% EntityArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumEntities`: Number of entities
- `EntityArray`: Array of entities

### Return Value

Number of sketch relations valid for the specified entities

## VBA Syntax

See [SketchRelationManager::IGetAllowedRelationsCount](ms-its:sldworksapivb6.chm::/sldworks~SketchRelationManager~IGetAllowedRelationsCount.html).

## Remarks

Call this method before calling [ISketchRelationManager::IGetAllowedRelations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelationManager~IGetAllowedRelations.html) to get the size of the array for that method.

## See Also

[ISketchRelationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager.html)
[ISketchRelationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager_members.html)
[ISketchRelationManager::GetAllowedRelations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~GetAllowedRelations.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
