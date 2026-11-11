---
title: "IsTemporaryEntity Method (IApplication)"
project: ""
interface: "IApplication"
member: "IsTemporaryEntity"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~IsTemporaryEntity.html"
---

# IsTemporaryEntity Method (IApplication)

Gets whether the specified entity is a temporary entity.

## Syntax

### Visual Basic

```vb
Function IsTemporaryEntity( _
   ByVal Obj As System.Object _
) As System.Boolean
```

### C#

```csharp
System.bool IsTemporaryEntity(
   System.object Obj
)
```

### JScript

```
function IsTemporaryEntity(
   Obj : System.Object
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool IsTemporaryEntity(
   System.Object* Obj
)
```

### C++/CLI

```cpp
System.bool IsTemporaryEntity(
   System.Object^ Obj
)
```

### Parameters

- `Obj`: Entity

### Return Value

True if the entity is a temporary entity, false if the entity is not a temporary entity

## Remarks

Temporary entities are not added to the drawing database.

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)
[IApplication::TemporaryEntityMode Property ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~TemporaryEntityMode.html)
[IBlockDefinition::AddTemporaryEntity Method ()](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition~AddTemporaryEntity.html)
[ISketchManager::AddTemporaryEntity Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~AddTemporaryEntity.html)
[ITracker::AddTemporaryEntity Method ()](Interop.dsAutomation~Interop.dsAutomation.ITracker~AddTemporaryEntity.html)

## Availability

DraftSight V1R4.0
