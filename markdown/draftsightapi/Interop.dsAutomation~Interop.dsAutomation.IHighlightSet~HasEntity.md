---
title: "HasEntity Method (IHighlightSet)"
project: ""
interface: "IHighlightSet"
member: "HasEntity"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IHighlightSet~HasEntity.html"
---

# HasEntity Method (IHighlightSet)

Gets whether this highlight selection set contains the specified entity.

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

True if the highlight selection set contains the specified entity, false if not

## See Also

[IHighlightSet Interface](Interop.dsAutomation~Interop.dsAutomation.IHighlightSet.html)
[IHighlightSet Members](Interop.dsAutomation~Interop.dsAutomation.IHighlightSet_members.html)
[IHighlightSet::AddEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.IHighlightSet~AddEntities.html)
[IHighlightSet::GetEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.IHighlightSet~GetEntities.html)
[IHighlightSet::RemoveEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.IHighlightSet~RemoveEntities.html)

## Availability

DraftSight V1R5.0
