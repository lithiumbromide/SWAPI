---
title: "RemoveEntityAt Method (IGroup)"
project: ""
interface: "IGroup"
member: "RemoveEntityAt"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IGroup~RemoveEntityAt.html"
---

# RemoveEntityAt Method (IGroup)

Removes the entity at the specified index from the EntityGroup.

## Syntax

### Visual Basic

```vb
Sub RemoveEntityAt( _
   ByVal Index As System.Integer _
)
```

### C#

```csharp
void RemoveEntityAt(
   System.int Index
)
```

### JScript

```
function RemoveEntityAt(
   Index : System.int
);
```

### Managed Extensions for C++

```
void RemoveEntityAt(
   System.int Index
)
```

### C++/CLI

```cpp
void RemoveEntityAt(
   System.int Index
)
```

### Parameters

- `Index`: 0-based index of entity to remove from the EntityGroup

## Examples

[Create and Change EntityGroups (C#)](Create_and_Change_EntityGroups_Example_CSharp.htm)
[Create and Change EntityGroups (VB.NET)](Create_and_Change_EntityGroups_Example_VBNET.htm)
[Create and Change EntityGroups (VBA)](Create_and_Change_EntityGroups_Example_VBA.htm)
[Create and Change EntityGroups (JavaScript)](Create_and_Change_EntityGroups_Example_JS.htm)

## Remarks

Before calling this method, call [IGroup::GetEntitiesCount](Interop.dsAutomation~Interop.dsAutomation.IGroup~GetEntitiesCount.html) to determine a valid value for Index.

## See Also

[IGroup Interface](Interop.dsAutomation~Interop.dsAutomation.IGroup.html)
[IGroup Members](Interop.dsAutomation~Interop.dsAutomation.IGroup_members.html)
[IGroup::RemoveEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.IGroup~RemoveEntities.html)
[IGroup::AddEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.IGroup~AddEntities.html)
[IGroup::GetEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.IGroup~GetEntities.html)
[IGroup::InsertEntitiesAt Method ()](Interop.dsAutomation~Interop.dsAutomation.IGroup~InsertEntitiesAt.html)
[IGroup::Reorder Method ()](Interop.dsAutomation~Interop.dsAutomation.IGroup~Reorder.html)

## Availability

DraftSight V1R4.0
