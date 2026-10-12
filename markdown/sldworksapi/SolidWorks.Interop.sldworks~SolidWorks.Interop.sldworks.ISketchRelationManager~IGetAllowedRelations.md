---
title: "IGetAllowedRelations Method (ISketchRelationManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchRelationManager"
member: "IGetAllowedRelations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~IGetAllowedRelations.html"
---

# IGetAllowedRelations Method (ISketchRelationManager)

Gets the types of sketch relations valid for the specified entities.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetAllowedRelations( _
   ByVal NumEntities As System.Integer, _
   ByRef EntityArray As System.Object, _
   ByVal NumAllowedRelations As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchRelationManager
Dim NumEntities As System.Integer
Dim EntityArray As System.Object
Dim NumAllowedRelations As System.Integer
Dim value As System.Integer

value = instance.IGetAllowedRelations(NumEntities, EntityArray, NumAllowedRelations)
```

### C#

```csharp
System.int IGetAllowedRelations(
   System.int NumEntities,
   ref System.object EntityArray,
   System.int NumAllowedRelations
)
```

### C++/CLI

```cpp
System.int IGetAllowedRelations(
   System.int NumEntities,
   System.Object^% EntityArray,
   System.int NumAllowedRelations
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumEntities`: Number of entities
- `EntityArray`: Array of entities
- `NumAllowedRelations`: Number of relations valid for the specified entities

### Return Value

- in-process, unmanaged C++: Pointer to an array of sketch relation types valid for the specified entities as defined in [swConstraintType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConstraintType_e.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [ISketchRelationManager::IGetAllowedRelationsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelationManager~IGetAllowedRelationsCount.html) before calling this method to get the value for NumEntities.

## See Also

[ISketchRelationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager.html)
[ISketchRelationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager_members.html)
[ISketchRelationManager::GetAllowedRelations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~GetAllowedRelations.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
