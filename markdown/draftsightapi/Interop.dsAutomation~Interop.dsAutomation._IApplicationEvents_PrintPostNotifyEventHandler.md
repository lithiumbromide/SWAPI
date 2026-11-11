---
title: "_IApplicationEvents_PrintPostNotifyEventHandler Delegate"
project: ""
interface: "_IApplicationEvents_PrintPostNotifyEventHandler"
member: ""
kind: "delegate"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_PrintPostNotifyEventHandler.html"
---

# _IApplicationEvents_PrintPostNotifyEventHandler Delegate

Post-notifies an application when the current document has been printed.

## Syntax

### Visual Basic

```vb
Public Delegate Sub _IApplicationEvents_PrintPostNotifyEventHandler()
```

### C#

```csharp
public delegate void _IApplicationEvents_PrintPostNotifyEventHandler()
```

### JScript

```
public delegate _IApplicationEvents_PrintPostNotifyEventHandler()
```

### Managed Extensions for C++

```
public: __gc __delegate void _IApplicationEvents_PrintPostNotifyEventHandler();
```

### C++/CLI

```cpp
public delegate void _IApplicationEvents_PrintPostNotifyEventHandler();
```

## Remarks

If developing a C++ application, use [dsApplication_PrintPostNotify_id](Interop.dsAutomation~Interop.dsAutomation.dsApplicationEvent_id_e.html) to register for this notification.

See [Getting Started](GettingStarted-draftsightapi.html) for more information about C++ interface add-in template callback functions.

## See Also

[_IApplicationEvents_PrintPostNotifyEventHandler Members](Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_PrintPostNotifyEventHandler.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IApplication Event PrintPreNotify](Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_PrintPreNotifyEventHandler.html)

## Availability

DraftSight 2017 SP0
