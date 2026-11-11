---
title: "Reorder Method (IGroup)"
project: ""
interface: "IGroup"
member: "Reorder"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IGroup~Reorder.html"
---

# Reorder Method (IGroup)

Reorders the entities within the EntityGroup.

## Syntax

### Visual Basic

```vb
Sub Reorder( _
   ByVal CurrentIndex As System.Integer, _
   ByVal NewIndex As System.Integer, _
   ByVal EntityCount As System.Integer _
)
```

### C#

```csharp
void Reorder(
   System.int CurrentIndex,
   System.int NewIndex,
   System.int EntityCount
)
```

### JScript

```
function Reorder(
   CurrentIndex : System.int,
   NewIndex : System.int,
   EntityCount : System.int
);
```

### Managed Extensions for C++

```
void Reorder(
   System.int CurrentIndex,
   System.int NewIndex,
   System.int EntityCount
)
```

### C++/CLI

```cpp
void Reorder(
   System.int CurrentIndex,
   System.int NewIndex,
   System.int EntityCount
)
```

### Parameters

- `CurrentIndex`: Current starting 0-based index of the entities that you want to reorder
- `NewIndex`: New starting 0-based index of the entities that you wanted reordered, after the entities are reordered
- `EntityCount`: Number of entities to reorder (see **Remarks**)

## Remarks

EntityCount must be <= [IGroup::GetEntitiesCount](Interop.dsAutomation~Interop.dsAutomation.IGroup~GetEntitiesCount.html) - NewIndex.

For example, if you have a group of five lines (line1, line2, line3, line4, and line5) and call IGroup::Reorder:

| Passing these parameters... | Then the lines are reordered as... |
| --- | --- |
| (0, 3, 1) | (line2, line3, line4, line1, line5) |
| (0, 3, 2) | (line3, line4, line5, line1, line2) |

## See Also

[IGroup Interface](Interop.dsAutomation~Interop.dsAutomation.IGroup.html)
[IGroup Members](Interop.dsAutomation~Interop.dsAutomation.IGroup_members.html)
[IGroup::ReverseOrder Method ()](Interop.dsAutomation~Interop.dsAutomation.IGroup~ReverseOrder.html)

## Availability

DraftSight V1R4.0
