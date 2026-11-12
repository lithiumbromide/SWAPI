---
title: "_IDocumentEvents_ObjectEraseNotifyEventHandler Delegate"
project: ""
interface: "_IDocumentEvents_ObjectEraseNotifyEventHandler"
member: ""
kind: "delegate"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_ObjectEraseNotifyEventHandler.html"
---

# _IDocumentEvents_ObjectEraseNotifyEventHandler Delegate

Post-notifies an application when the specified entity is erased from or restored to a document.

## Syntax

### Visual Basic

```vb
Public Delegate Sub _IDocumentEvents_ObjectEraseNotifyEventHandler( _
   ByVal object As System.Object, _
   ByVal Erased As System.Boolean _
)
```

### C#

```csharp
public delegate void _IDocumentEvents_ObjectEraseNotifyEventHandler(
   System.object object,
   System.bool Erased
)
```

### JScript

```
public delegate _IDocumentEvents_ObjectEraseNotifyEventHandler(
   object : System.Object,
   Erased : System.boolean
)
```

### Managed Extensions for C++

```
public: __gc __delegate void _IDocumentEvents_ObjectEraseNotifyEventHandler(
   System.Object* object,
   System.bool Erased
)
```

### C++/CLI

```cpp
public delegate void _IDocumentEvents_ObjectEraseNotifyEventHandler(
   System.Object^ object,
   System.bool Erased
)
```

### Parameters

- `object`: Entity or [IUnknownEntity](Interop.dsAutomation~Interop.dsAutomation.IUnknownEntity.html)
- `Erased`: True if the entity is erased from the document, false if the entity is restored to the document

## Remarks

If developing a C++ application, use [dsDocument_ObjectEraseNotify_id](Interop.dsAutomation~Interop.dsAutomation.dsDocumentEvent_id_e.html) to register for this notification.

See [Getting Started](GettingStarted-draftsightapi.html) for more information about C++ interface add-in template callback functions.

## See Also

[_IDocumentEvents_ObjectEraseNotifyEventHandler Members](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_ObjectEraseNotifyEventHandler.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IDocument Event ObjectAppendNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_ObjectAppendNotifyEventHandler.html)
[IDocument Event ObjectModifyNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_ObjectModifyNotifyEventHandler.html)

## Availability

DraftSight V1R3.0
