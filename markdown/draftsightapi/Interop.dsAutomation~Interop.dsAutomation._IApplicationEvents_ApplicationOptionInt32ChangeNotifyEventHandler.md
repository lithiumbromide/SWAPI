---
title: "_IApplicationEvents_ApplicationOptionInt32ChangeNotifyEventHandler Delegate"
project: ""
interface: "_IApplicationEvents_ApplicationOptionInt32ChangeNotifyEventHandler"
member: ""
kind: "delegate"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_ApplicationOptionInt32ChangeNotifyEventHandler.html"
---

# _IApplicationEvents_ApplicationOptionInt32ChangeNotifyEventHandler Delegate

Post-notifies the application when the specified Int32 application option changes.

## Syntax

### Visual Basic

```vb
Public Delegate Sub _IApplicationEvents_ApplicationOptionInt32ChangeNotifyEventHandler( _
   ByVal Option As dsApplicationOptionInt32_e _
)
```

### C#

```csharp
public delegate void _IApplicationEvents_ApplicationOptionInt32ChangeNotifyEventHandler(
   dsApplicationOptionInt32_e Option
)
```

### JScript

```
public delegate _IApplicationEvents_ApplicationOptionInt32ChangeNotifyEventHandler(
   Option : dsApplicationOptionInt32_e
)
```

### Managed Extensions for C++

```
public: __gc __delegate void _IApplicationEvents_ApplicationOptionInt32ChangeNotifyEventHandler(
   dsApplicationOptionInt32_e Option
)
```

### C++/CLI

```cpp
public delegate void _IApplicationEvents_ApplicationOptionInt32ChangeNotifyEventHandler(
   dsApplicationOptionInt32_e Option
)
```

### Parameters

- `Option`: Option as defined in [dsApplicationOptionInt32_e](Interop.dsAutomation~Interop.dsAutomation.dsApplicationOptionInt32_e.html)

## Remarks

If developing a C++ application, use [dsApplication_ApplicationOptionInt32ChangeNotify_id](Interop.dsAutomation~Interop.dsAutomation.dsApplicationEvent_id_e.html) to register for this notification.

See [Getting Started](GettingStarted-draftsightapi.html) for more information about C++ interface add-in template callback functions.

## See Also

[_IApplicationEvents_ApplicationOptionInt32ChangeNotifyEventHandler Members](Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_ApplicationOptionInt32ChangeNotifyEventHandler.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)

## Availability

DraftSight V1R5.0
