---
title: "_IApplicationEvents_CurrentProfileResetPreNotifyEventHandler Delegate"
project: ""
interface: "_IApplicationEvents_CurrentProfileResetPreNotifyEventHandler"
member: ""
kind: "delegate"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_CurrentProfileResetPreNotifyEventHandler.html"
---

# _IApplicationEvents_CurrentProfileResetPreNotifyEventHandler Delegate

Pre-notifies an application before the current profile is reset.

## Syntax

### Visual Basic

```vb
Public Delegate Sub _IApplicationEvents_CurrentProfileResetPreNotifyEventHandler( _
   ByVal CurrentProfileName As System.String _
)
```

### C#

```csharp
public delegate void _IApplicationEvents_CurrentProfileResetPreNotifyEventHandler(
   System.string CurrentProfileName
)
```

### JScript

```
public delegate _IApplicationEvents_CurrentProfileResetPreNotifyEventHandler(
   CurrentProfileName : System.String
)
```

### Managed Extensions for C++

```
public: __gc __delegate void _IApplicationEvents_CurrentProfileResetPreNotifyEventHandler(
   System.string* CurrentProfileName
)
```

### C++/CLI

```cpp
public delegate void _IApplicationEvents_CurrentProfileResetPreNotifyEventHandler(
   System.String^ CurrentProfileName
)
```

### Parameters

- `CurrentProfileName`: Current profile name

## Remarks

If developing a C++ application, then use [dsApplication_CurrentProfileResetPreNotify_id](Interop.dsAutomation~Interop.dsAutomation.dsApplicationEvent_id_e.html) to register for this notification. See [Getting Started](GettingStarted-draftsightapi.html) for more information about C++ interface add-in template callback functions.

## See Also

[_IApplicationEvents_CurrentProfileResetPreNotifyEventHandler Members](Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_CurrentProfileResetPreNotifyEventHandler.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)

## Availability

DraftSight 2021 SP0
