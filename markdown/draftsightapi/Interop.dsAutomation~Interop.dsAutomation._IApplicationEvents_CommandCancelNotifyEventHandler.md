---
title: "_IApplicationEvents_CommandCancelNotifyEventHandler Delegate"
project: ""
interface: "_IApplicationEvents_CommandCancelNotifyEventHandler"
member: ""
kind: "delegate"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_CommandCancelNotifyEventHandler.html"
---

# _IApplicationEvents_CommandCancelNotifyEventHandler Delegate

Notifies an application when a command is canceled.

## Syntax

### Visual Basic

```vb
Public Delegate Sub _IApplicationEvents_CommandCancelNotifyEventHandler( _
   ByVal CommandName As System.String, _
   ByVal Document As Document _
)
```

### C#

```csharp
public delegate void _IApplicationEvents_CommandCancelNotifyEventHandler(
   System.string CommandName,
   Document Document
)
```

### JScript

```
public delegate _IApplicationEvents_CommandCancelNotifyEventHandler(
   CommandName : System.String,
   Document : Document
)
```

### Managed Extensions for C++

```
public: __gc __delegate void _IApplicationEvents_CommandCancelNotifyEventHandler(
   System.string* CommandName,
   Document* Document
)
```

### C++/CLI

```cpp
public delegate void _IApplicationEvents_CommandCancelNotifyEventHandler(
   System.String^ CommandName,
   Document^ Document
)
```

### Parameters

- `CommandName`: Name of command that was canceled
- `Document`: [Document](Interop.dsAutomation~Interop.dsAutomation.IDocument.html) in which command was canceled

## Remarks

If developing a C++ application, then use [dsApplication_CommandCancelNotify_id](Interop.dsAutomation~Interop.dsAutomation.dsApplicationEvent_id_e.html) to register for this notification. See [Getting Started](GettingStarted-draftsightapi.html) for more information about C++ interface add-in template callback functions.

## See Also

[_IApplicationEvents_CommandCancelNotifyEventHandler Members](Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_CommandCancelNotifyEventHandler.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IApplication Event CommandPostNotify](Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_CommandPostNotifyEventHandler.html)
[IApplication Event CommandPreNotify](Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_CommandPreNotifyEventHandler.html)

## Availability

DraftSight V1R3.0
