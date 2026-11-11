---
title: "_IDocumentEvents_DropNotifyEventHandler Delegate"
project: ""
interface: "_IDocumentEvents_DropNotifyEventHandler"
member: ""
kind: "delegate"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_DropNotifyEventHandler.html"
---

# _IDocumentEvents_DropNotifyEventHandler Delegate

Notifies an application with drop data when the specified drop action occurs in the current DraftSight session.

## Syntax

### Visual Basic

```vb
Public Delegate Sub _IDocumentEvents_DropNotifyEventHandler( _
   ByVal DropAction As dsDropAction_e, _
   ByVal DropData As System.Object _
)
```

### C#

```csharp
public delegate void _IDocumentEvents_DropNotifyEventHandler(
   dsDropAction_e DropAction,
   System.object DropData
)
```

### JScript

```
public delegate _IDocumentEvents_DropNotifyEventHandler(
   DropAction : dsDropAction_e,
   DropData : System.Object
)
```

### Managed Extensions for C++

```
public: __gc __delegate void _IDocumentEvents_DropNotifyEventHandler(
   dsDropAction_e DropAction,
   System.Object* DropData
)
```

### C++/CLI

```cpp
public delegate void _IDocumentEvents_DropNotifyEventHandler(
   dsDropAction_e DropAction,
   System.Object^ DropData
)
```

### Parameters

- `DropAction`: Drop action as defined by [dsDropAction_e](Interop.dsAutomation~Interop.dsAutomation.dsDropAction_e.html)
- `DropData`: [IDropData](Interop.dsAutomation~Interop.dsAutomation.IDropData.html)

## Remarks

If developing a C++ application, use [dsDocument_DropNotify_id](Interop.dsAutomation~Interop.dsAutomation.dsDocumentEvent_id_e.html) to register for this notification.

See [Getting Started](GettingStarted-draftsightapi.html) for more information about C++ interface add-in template callback functions.

## See Also

[_IDocumentEvents_DropNotifyEventHandler Members](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_DropNotifyEventHandler.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)

## Availability

DraftSight 2020 SP3
