---
title: "HasEntity Method (IGroup)"
project: ""
interface: "IGroup"
member: "HasEntity"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IGroup~HasEntity.html"
---

# HasEntity Method (IGroup)

Gets whether the EntityGroup contains the specified entity.

## Syntax

### Visual Basic

```vb
Function HasEntity( _
   ByVal Entity As System.Object _
) As System.Boolean
```

### C#

```csharp
System.bool HasEntity(
   System.object Entity
)
```

### JScript

```
function HasEntity(
   Entity : System.Object
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool HasEntity(
   System.Object* Entity
)
```

### C++/CLI

```cpp
System.bool HasEntity(
   System.Object^ Entity
)
```

### Parameters

- `Entity`: Entity

### Return Value

True if the EntityGroup contains the specified entity, false if not

## Examples

[Create and Change EntityGroups (C#)](Create_and_Change_EntityGroups_Example_CSharp.htm)
[Create and Change EntityGroups (VB.NET)](Create_and_Change_EntityGroups_Example_VBNET.htm)
[Create and Change EntityGroups (VBA)](Create_and_Change_EntityGroups_Example_VBA.htm)
[Create and Change EntityGroups (JavaScript)](Create_and_Change_EntityGroups_Example_JS.htm)

## See Also

[IGroup Interface](Interop.dsAutomation~Interop.dsAutomation.IGroup.html)
[IGroup Members](Interop.dsAutomation~Interop.dsAutomation.IGroup_members.html)
[IGroup::AddEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.IGroup~AddEntities.html)
[IGroup::GetEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.IGroup~GetEntities.html)
[IGroup::InsertEntitiesAt Method ()](Interop.dsAutomation~Interop.dsAutomation.IGroup~InsertEntitiesAt.html)
[IGroup::RemoveEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.IGroup~RemoveEntities.html)
[IGroup::RemoveEntityAt Method ()](Interop.dsAutomation~Interop.dsAutomation.IGroup~RemoveEntityAt.html)

## Availability

DraftSight V1R4.0
