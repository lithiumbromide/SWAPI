---
title: "_IDocumentEvents_ObjectAppendNotifyEventHandler Delegate"
project: ""
interface: "_IDocumentEvents_ObjectAppendNotifyEventHandler"
member: ""
kind: "delegate"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_ObjectAppendNotifyEventHandler.html"
---

# _IDocumentEvents_ObjectAppendNotifyEventHandler Delegate

Post-notifies an application when an entity is appended to or detached from a document.

## Syntax

### Visual Basic

```vb
Public Delegate Sub _IDocumentEvents_ObjectAppendNotifyEventHandler( _
   ByVal object As System.Object, _
   ByVal Appended As System.Boolean _
)
```

### C#

```csharp
public delegate void _IDocumentEvents_ObjectAppendNotifyEventHandler(
   System.object object,
   System.bool Appended
)
```

### JScript

```
public delegate _IDocumentEvents_ObjectAppendNotifyEventHandler(
   object : System.Object,
   Appended : System.boolean
)
```

### Managed Extensions for C++

```
public: __gc __delegate void _IDocumentEvents_ObjectAppendNotifyEventHandler(
   System.Object* object,
   System.bool Appended
)
```

### C++/CLI

```cpp
public delegate void _IDocumentEvents_ObjectAppendNotifyEventHandler(
   System.Object^ object,
   System.bool Appended
)
```

### Parameters

- `object`: Entity or [IUnknownEntity](Interop.dsAutomation~Interop.dsAutomation.IUnknownEntity.html)
- `Appended`: True if the entity is appended to the document, false if the entity is detached from the document

## Remarks

If developing a C++ application, use [dsDocument_ObjectAppendNotify_id](Interop.dsAutomation~Interop.dsAutomation.dsDocumentEvent_id_e.html) to register for this notification.

See [Getting Started](GettingStarted-draftsightapi.html) for more information about C++ interface add-in template callback functions.

## See Also

[_IDocumentEvents_ObjectAppendNotifyEventHandler Members](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_ObjectAppendNotifyEventHandler.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IDocument Event ObjectEraseNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_ObjectEraseNotifyEventHandler.html)
[IDocument Event ObjectModifyNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_ObjectModifyNotifyEventHandler.html)

## Availability

DraftSight V1R3.0
