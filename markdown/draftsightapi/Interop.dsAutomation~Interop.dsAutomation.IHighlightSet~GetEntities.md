---
title: "GetEntities Method (IHighlightSet)"
project: ""
interface: "IHighlightSet"
member: "GetEntities"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IHighlightSet~GetEntities.html"
---

# GetEntities Method (IHighlightSet)

Gets the entities and their types in this highlight selection set.

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

- `EntityTypeLongArray`: Types of entities in this highlight selection set as defined in [dsObjectType_e](Interop.dsAutomation~Interop.dsAutomation.dsObjectType_e.html)

### Return Value

Array of entities in this highlight selection set

## See Also

[IHighlightSet Interface](Interop.dsAutomation~Interop.dsAutomation.IHighlightSet.html)
[IHighlightSet Members](Interop.dsAutomation~Interop.dsAutomation.IHighlightSet_members.html)
[IHighlightSet::AddEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.IHighlightSet~AddEntities.html)
[IHighlightSet::HasEntity Method ()](Interop.dsAutomation~Interop.dsAutomation.IHighlightSet~HasEntity.html)
[IHighlightSet::RemoveEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.IHighlightSet~RemoveEntities.html)

## Availability

DraftSight V1R5.0
