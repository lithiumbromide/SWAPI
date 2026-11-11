---
title: "AddEntities Method (IHighlightSet)"
project: ""
interface: "IHighlightSet"
member: "AddEntities"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IHighlightSet~AddEntities.html"
---

# AddEntities Method (IHighlightSet)

Adds the specified entities to the highlight selection set.

## Syntax

### Visual Basic

```vb
Sub AddEntities( _
   ByVal EntitiesArray As System.Object _
)
```

### C#

```csharp
void AddEntities(
   System.object EntitiesArray
)
```

### JScript

```
function AddEntities(
   EntitiesArray : System.Object
);
```

### Managed Extensions for C++

```
void AddEntities(
   System.Object* EntitiesArray
)
```

### C++/CLI

```cpp
void AddEntities(
   System.Object^ EntitiesArray
)
```

### Parameters

- `EntitiesArray`: Array of entities to add to the highlight selection set

## Examples

See the [IHighlightSet](Interop.dsAutomation~Interop.dsAutomation.IHighlightSet.html) examples.

## Remarks

After calling this method, call [IHighlightSet::Highlight](Interop.dsAutomation~Interop.dsAutomation.IHighlightSet~Highlight.html) to highlight the entities in the highlight selection set.

## See Also

[IHighlightSet Interface](Interop.dsAutomation~Interop.dsAutomation.IHighlightSet.html)
[IHighlightSet Members](Interop.dsAutomation~Interop.dsAutomation.IHighlightSet_members.html)
[IHighlightSet::GetEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.IHighlightSet~GetEntities.html)
[IHighlightSet::HasEntity Method ()](Interop.dsAutomation~Interop.dsAutomation.IHighlightSet~HasEntity.html)
[IHighlightSet::RemoveEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.IHighlightSet~RemoveEntities.html)

## Availability

DraftSight V1R5.0
