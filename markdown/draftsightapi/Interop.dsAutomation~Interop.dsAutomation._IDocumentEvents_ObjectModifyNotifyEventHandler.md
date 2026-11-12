---
title: "_IDocumentEvents_ObjectModifyNotifyEventHandler Delegate"
project: ""
interface: "_IDocumentEvents_ObjectModifyNotifyEventHandler"
member: ""
kind: "delegate"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_ObjectModifyNotifyEventHandler.html"
---

# _IDocumentEvents_ObjectModifyNotifyEventHandler Delegate

Post-notifies an application when an entity is modified in a document.

## Syntax

### Visual Basic

```vb
Public Delegate Sub _IDocumentEvents_ObjectModifyNotifyEventHandler( _
   ByVal object As System.Object _
)
```

### C#

```csharp
public delegate void _IDocumentEvents_ObjectModifyNotifyEventHandler(
   System.object object
)
```

### JScript

```
public delegate _IDocumentEvents_ObjectModifyNotifyEventHandler(
   object : System.Object
)
```

### Managed Extensions for C++

```
public: __gc __delegate void _IDocumentEvents_ObjectModifyNotifyEventHandler(
   System.Object* object
)
```

### C++/CLI

```cpp
public delegate void _IDocumentEvents_ObjectModifyNotifyEventHandler(
   System.Object^ object
)
```

### Parameters

- `object`: Entity or [IUnknownEntity](Interop.dsAutomation~Interop.dsAutomation.IUnknownEntity.html)

## Remarks

If developing a C++ application, use [dsDocument_ObjectModifyNotify_id](Interop.dsAutomation~Interop.dsAutomation.dsDocumentEvent_id_e.html) to register for this notification.

See [Getting Started](GettingStarted-draftsightapi.html) for more information about C++ interface add-in template callback functions.

## See Also

[_IDocumentEvents_ObjectModifyNotifyEventHandler Members](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_ObjectModifyNotifyEventHandler.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IDocument Event ObjectAppendNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_ObjectAppendNotifyEventHandler.html)
[IDocument Event ObjectEraseNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_ObjectEraseNotifyEventHandler.html)

## Availability

V1R3.0
