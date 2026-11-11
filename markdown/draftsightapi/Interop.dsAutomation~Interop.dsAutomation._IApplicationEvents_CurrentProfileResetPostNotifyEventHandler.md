---
title: "_IApplicationEvents_CurrentProfileResetPostNotifyEventHandler Delegate"
project: ""
interface: "_IApplicationEvents_CurrentProfileResetPostNotifyEventHandler"
member: ""
kind: "delegate"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_CurrentProfileResetPostNotifyEventHandler.html"
---

# _IApplicationEvents_CurrentProfileResetPostNotifyEventHandler Delegate

Post-notifies an application when the current profile is reset.

## Syntax

### Visual Basic

```vb
Public Delegate Sub _IApplicationEvents_CurrentProfileResetPostNotifyEventHandler( _
   ByVal CurrentProfileName As System.String _
)
```

### C#

```csharp
public delegate void _IApplicationEvents_CurrentProfileResetPostNotifyEventHandler(
   System.string CurrentProfileName
)
```

### JScript

```
public delegate _IApplicationEvents_CurrentProfileResetPostNotifyEventHandler(
   CurrentProfileName : System.String
)
```

### Managed Extensions for C++

```
public: __gc __delegate void _IApplicationEvents_CurrentProfileResetPostNotifyEventHandler(
   System.string* CurrentProfileName
)
```

### C++/CLI

```cpp
public delegate void _IApplicationEvents_CurrentProfileResetPostNotifyEventHandler(
   System.String^ CurrentProfileName
)
```

### Parameters

- `CurrentProfileName`: Current profile name

## Remarks

If developing a C++ application, then use [dsApplication_CurrentProfileResetPostNotify_id](Interop.dsAutomation~Interop.dsAutomation.dsApplicationEvent_id_e.html) to register for this notification. See [Getting Started](GettingStarted-draftsightapi.html) for more information about C++ interface add-in template callback functions.

## See Also

[_IApplicationEvents_CurrentProfileResetPostNotifyEventHandler Members](Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_CurrentProfileResetPostNotifyEventHandler.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)

## Availability

DraftSight 2021 SP0
