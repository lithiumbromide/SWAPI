---
title: "IUnknownEntity Interface"
project: ""
interface: "IUnknownEntity"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IUnknownEntity.html"
---

# IUnknownEntity Interface

Allows access to an unknown entity.

## Syntax

### Visual Basic

```vb
Public Interface IUnknownEntity
```

### C#

```csharp
public interface IUnknownEntity
```

### JScript

```
public interface IUnknownEntity
```

### Managed Extensions for C++

```
public __gc __interface IUnknownEntity
```

### C++/CLI

```cpp
public interface class IUnknownEntity
```

## Remarks

An unknown entity:

- is an entity that is not officially supported by the DraftSight API.
- may be a custom entity.
- may be an unknown entity that has surfaced during the course of event handling.

During the course of application processing, unknown entities may surface that have no interface representation in the DraftSight API. If you capture unknown entities with the event handlers, _IDocumentEvents_ObjectAppendNotify, _IDocumentEvents_ObjectEraseNotify, or _IDocumentEvents_ObjectModifyNotify, then you can use this interface to recognize and process only ones with a specific [IUnknownEntity::ClassName](Interop.dsAutomation~Interop.dsAutomation.IUnknownEntity~ClassName.html).

## Accessors

Unknown entities may surface during these events:

[_IDocumentEvents_ObjectAppendNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_ObjectAppendNotifyEventHandler.html)

[_IDocumentEvents_ObjectEraseNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_ObjectEraseNotifyEventHandler.html)

[_IDocumentEvents_ObjectModifyNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_ObjectModifyNotifyEventHandler.html)

## See Also

[IUnknownEntity Members](Interop.dsAutomation~Interop.dsAutomation.IUnknownEntity_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
