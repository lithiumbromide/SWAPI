---
title: "GetEntities Method (IGroup)"
project: ""
interface: "IGroup"
member: "GetEntities"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IGroup~GetEntities.html"
---

# GetEntities Method (IGroup)

Gets all of the entities and their entity types in this EntityGroup.

## Syntax

### Visual Basic

```vb
Function GetEntities( _
   ByRef EntityTypeLongArray As System.Object _
) As System.Object
```

### C#

```csharp
System.object GetEntities(
   out System.object EntityTypeLongArray
)
```

### JScript

```
function GetEntities(
   EntityTypeLongArray : System.Object
) : System.Object;
```

### Managed Extensions for C++

```
System.Object* GetEntities(
   [PARAMFLAG::Out] System.Object* EntityTypeLongArray
)
```

### C++/CLI

```cpp
System.Object^ GetEntities(
   [Out] System.Object^ EntityTypeLongArray
)
```

### Parameters

- `EntityTypeLongArray`: Types of entities as defined in [dsObjectType_e](Interop.dsAutomation~Interop.dsAutomation.dsObjectType_e.html)

### Return Value

Array of entities

## Examples

[Create and Change EntityGroups (C#)](Create_and_Change_EntityGroups_Example_CSharp.htm)
[Create and Change EntityGroups (VB.NET)](Create_and_Change_EntityGroups_Example_VBNET.htm)
[Create and Change EntityGroups (VBA)](Create_and_Change_EntityGroups_Example_VBA.htm)
[Create and Change EntityGroups (JavaScript)](Create_and_Change_EntityGroups_Example_JS.htm)

## See Also

[IGroup Interface](Interop.dsAutomation~Interop.dsAutomation.IGroup.html)
[IGroup Members](Interop.dsAutomation~Interop.dsAutomation.IGroup_members.html)
[IGroup::AddEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.IGroup~AddEntities.html)
[IGroup::RemoveEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.IGroup~RemoveEntities.html)

## Availability

DraftSight V1R4.0
