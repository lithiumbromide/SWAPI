---
title: "InsertEntitiesAt Method (IGroup)"
project: ""
interface: "IGroup"
member: "InsertEntitiesAt"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IGroup~InsertEntitiesAt.html"
---

# InsertEntitiesAt Method (IGroup)

Inserts the specified entities at the specified index in the EntityGroup.

## Syntax

### Visual Basic

```vb
Sub InsertEntitiesAt( _
   ByVal Index As System.Integer, _
   ByVal EntitiesArray As System.Object _
)
```

### C#

```csharp
void InsertEntitiesAt(
   System.int Index,
   System.object EntitiesArray
)
```

### JScript

```
function InsertEntitiesAt(
   Index : System.int,
   EntitiesArray : System.Object
);
```

### Managed Extensions for C++

```
void InsertEntitiesAt(
   System.int Index,
   System.Object* EntitiesArray
)
```

### C++/CLI

```cpp
void InsertEntitiesAt(
   System.int Index,
   System.Object^ EntitiesArray
)
```

### Parameters

- `Index`: 0-based index where to insert the entity
- `EntitiesArray`: Array of entities to insert at Index

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
[IGroup::AddEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.IGroup~AddEntities.html)
[IGroup::RemoveEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.IGroup~RemoveEntities.html)
[IGroup::RemoveEntityAt Method ()](Interop.dsAutomation~Interop.dsAutomation.IGroup~RemoveEntityAt.html)
[IGroup::Reorder Method ()](Interop.dsAutomation~Interop.dsAutomation.IGroup~Reorder.html)
[IGroup::ReverseOrder Method ()](Interop.dsAutomation~Interop.dsAutomation.IGroup~ReverseOrder.html)

## Availability

DraftSight V1R4.0
