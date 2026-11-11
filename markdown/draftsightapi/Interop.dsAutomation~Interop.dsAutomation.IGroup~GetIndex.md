---
title: "GetIndex Method (IGroup)"
project: ""
interface: "IGroup"
member: "GetIndex"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IGroup~GetIndex.html"
---

# GetIndex Method (IGroup)

Gets the index of the specified entity within the EntityGroup.

## Syntax

### Visual Basic

```vb
Function GetIndex( _
   ByVal Entity As System.Object _
) As System.Integer
```

### C#

```csharp
System.int GetIndex(
   System.object Entity
)
```

### JScript

```
function GetIndex(
   Entity : System.Object
) : System.int;
```

### Managed Extensions for C++

```
System.int GetIndex(
   System.Object* Entity
)
```

### C++/CLI

```cpp
System.int GetIndex(
   System.Object^ Entity
)
```

### Parameters

- `Entity`: Entity whose index to get within the EntityGroup

### Return Value

0-based index of the entity within the EntityGroup

## Examples

[Create and Change EntityGroups (C#)](Create_and_Change_EntityGroups_Example_CSharp.htm)
[Create and Change EntityGroups (VB.NET)](Create_and_Change_EntityGroups_Example_VBNET.htm)
[Create and Change EntityGroups (VBA)](Create_and_Change_EntityGroups_Example_VBA.htm)
[Create and Change EntityGroups (JavaScript)](Create_and_Change_EntityGroups_Example_JS.htm)

## See Also

[IGroup Interface](Interop.dsAutomation~Interop.dsAutomation.IGroup.html)
[IGroup Members](Interop.dsAutomation~Interop.dsAutomation.IGroup_members.html)
[IGroup::GetEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.IGroup~GetEntities.html)
[IGroup::InsertEntitiesAt Method ()](Interop.dsAutomation~Interop.dsAutomation.IGroup~InsertEntitiesAt.html)
[IGroup::RemoveEntityAt Method ()](Interop.dsAutomation~Interop.dsAutomation.IGroup~RemoveEntityAt.html)
[IGroup::Reorder Method ()](Interop.dsAutomation~Interop.dsAutomation.IGroup~Reorder.html)
[IGroup::ReverseOrder Method ()](Interop.dsAutomation~Interop.dsAutomation.IGroup~ReverseOrder.html)

## Availability

DraftSight V1R4.0
