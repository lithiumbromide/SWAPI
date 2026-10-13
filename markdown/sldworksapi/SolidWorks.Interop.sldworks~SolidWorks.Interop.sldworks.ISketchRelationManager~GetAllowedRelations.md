---
title: "GetAllowedRelations Method (ISketchRelationManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchRelationManager"
member: "GetAllowedRelations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~GetAllowedRelations.html"
---

# GetAllowedRelations Method (ISketchRelationManager)

Gets the types of sketch relations valid for the specified entities.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAllowedRelations( _
   ByVal Entities As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchRelationManager
Dim Entities As System.Object
Dim value As System.Object

value = instance.GetAllowedRelations(Entities)
```

### C#

```csharp
System.object GetAllowedRelations(
   System.object Entities
)
```

### C++/CLI

```cpp
System.Object^ GetAllowedRelations(
   System.Object^ Entities
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Entities`: Array of entities

### Return Value

Array of sketch relation types valid for the specified entities as defined in [swConstraintType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConstraintType_e.html)

## VBA Syntax

See [SketchRelationManager::GetAllowedRelations](ms-its:sldworksapivb6.chm::/sldworks~SketchRelationManager~GetAllowedRelations.html).

## See Also

[ISketchRelationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager.html)
[ISketchRelationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager_members.html)
[ISketchManagerRelation::IGetAllowedRelations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~IGetAllowedRelations.html)
[ISketchManagerRelation::IGetAllowedRelationsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~IGetAllowedRelationsCount.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
