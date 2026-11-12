---
title: "_IApplicationEvents_OnIdleNotifyEventHandler Delegate"
project: ""
interface: "_IApplicationEvents_OnIdleNotifyEventHandler"
member: ""
kind: "delegate"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_OnIdleNotifyEventHandler.html"
---

# _IApplicationEvents_OnIdleNotifyEventHandler Delegate

Fired when there are no more events in the event queue; i.e., the event queue is idle.

## Syntax

### Visual Basic

```vb
Public Delegate Sub _IApplicationEvents_OnIdleNotifyEventHandler()
```

### C#

```csharp
public delegate void _IApplicationEvents_OnIdleNotifyEventHandler()
```

### JScript

```
public delegate _IApplicationEvents_OnIdleNotifyEventHandler()
```

### Managed Extensions for C++

```
public: __gc __delegate void _IApplicationEvents_OnIdleNotifyEventHandler();
```

### C++/CLI

```cpp
public delegate void _IApplicationEvents_OnIdleNotifyEventHandler();
```

## Remarks

If developing a C++ application, use [OnIdleNotify](Interop.dsAutomation~Interop.dsAutomation.dsApplicationEvent_id_e.html) to register for this event.

## See Also

[_IApplicationEvents_OnIdleNotifyEventHandler Members](Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_OnIdleNotifyEventHandler.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IApplication::RegisterOnIdleNotify Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~RegisterOnIdleNotify.html)

## Availability

DraftSight V1R5.0
