---
title: "_IDocumentEvents_DragNotifyEventHandler Delegate"
project: ""
interface: "_IDocumentEvents_DragNotifyEventHandler"
member: ""
kind: "delegate"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_DragNotifyEventHandler.html"
---

# _IDocumentEvents_DragNotifyEventHandler Delegate

Notifies an application when the specified drag event occurs in the current DraftSight session.

## Syntax

### Visual Basic

```vb
Public Delegate Sub _IDocumentEvents_DragNotifyEventHandler( _
   ByVal DragEvent As dsDragEvent_e _
)
```

### C#

```csharp
public delegate void _IDocumentEvents_DragNotifyEventHandler(
   dsDragEvent_e DragEvent
)
```

### JScript

```
public delegate _IDocumentEvents_DragNotifyEventHandler(
   DragEvent : dsDragEvent_e
)
```

### Managed Extensions for C++

```
public: __gc __delegate void _IDocumentEvents_DragNotifyEventHandler(
   dsDragEvent_e DragEvent
)
```

### C++/CLI

```cpp
public delegate void _IDocumentEvents_DragNotifyEventHandler(
   dsDragEvent_e DragEvent
)
```

### Parameters

- `DragEvent`: Drag event as defined by [dsDragEvent_e](Interop.dsAutomation~Interop.dsAutomation.dsDragEvent_e.html)

## Remarks

If developing a C++ application, use [dsDocument_DragNotify_id](Interop.dsAutomation~Interop.dsAutomation.dsDocumentEvent_id_e.html) to register for this notification.

See [Getting Started](GettingStarted-draftsightapi.html) for more information about C++ interface add-in template callback functions.

## See Also

[_IDocumentEvents_DragNotifyEventHandler Members](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_DragNotifyEventHandler.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)

## Availability

DraftSight 2020 SP3
