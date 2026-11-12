---
title: "GetEntities Method (IBlockDefinition)"
project: ""
interface: "IBlockDefinition"
member: "GetEntities"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition~GetEntities.html"
---

# GetEntities Method (IBlockDefinition)

Gets the entities that form the Block definition.

## Syntax

### Visual Basic

```vb
Sub GetEntities( _
   ByRef EntityTypeLongArray As System.Object, _
   ByRef EntitiesArray As System.Object _
)
```

### C#

```csharp
void GetEntities(
   out System.object EntityTypeLongArray,
   out System.object EntitiesArray
)
```

### JScript

```
function GetEntities(
   EntityTypeLongArray : System.Object,
   EntitiesArray : System.Object
);
```

### Managed Extensions for C++

```
void GetEntities(
   [PARAMFLAG::Out] System.Object* EntityTypeLongArray,
   [PARAMFLAG::Out] System.Object* EntitiesArray
)
```

### C++/CLI

```cpp
void GetEntities(
   [Out] System.Object^ EntityTypeLongArray,
   [Out] System.Object^ EntitiesArray
)
```

### Parameters

- `EntityTypeLongArray`: Array of longs indicating the types of entities returned as defined in [dsObjectType_e](Interop.dsAutomation~Interop.dsAutomation.dsObjectType_e.html)
- `EntitiesArray`: Array of objects of the entities that form the Block definition

## See Also

[IBlockDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition.html)
[IBlockDefinition Members](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition_members.html)
[IEntityHelper Interface](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper.html)

## Availability

DraftSight V1R1.4
