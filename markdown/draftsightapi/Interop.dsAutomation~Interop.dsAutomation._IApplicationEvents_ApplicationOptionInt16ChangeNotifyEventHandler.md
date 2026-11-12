---
title: "_IApplicationEvents_ApplicationOptionInt16ChangeNotifyEventHandler Delegate"
project: ""
interface: "_IApplicationEvents_ApplicationOptionInt16ChangeNotifyEventHandler"
member: ""
kind: "delegate"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_ApplicationOptionInt16ChangeNotifyEventHandler.html"
---

# _IApplicationEvents_ApplicationOptionInt16ChangeNotifyEventHandler Delegate

Post-notifies the application when the specified Int16 application option changes.

## Syntax

### Visual Basic

```vb
Public Delegate Sub _IApplicationEvents_ApplicationOptionInt16ChangeNotifyEventHandler( _
   ByVal Option As dsApplicationOptionInt16_e _
)
```

### C#

```csharp
public delegate void _IApplicationEvents_ApplicationOptionInt16ChangeNotifyEventHandler(
   dsApplicationOptionInt16_e Option
)
```

### JScript

```
public delegate _IApplicationEvents_ApplicationOptionInt16ChangeNotifyEventHandler(
   Option : dsApplicationOptionInt16_e
)
```

### Managed Extensions for C++

```
public: __gc __delegate void _IApplicationEvents_ApplicationOptionInt16ChangeNotifyEventHandler(
   dsApplicationOptionInt16_e Option
)
```

### C++/CLI

```cpp
public delegate void _IApplicationEvents_ApplicationOptionInt16ChangeNotifyEventHandler(
   dsApplicationOptionInt16_e Option
)
```

### Parameters

- `Option`: Option as defined in [dsApplicationOptionInt16_e](Interop.dsAutomation~Interop.dsAutomation.dsApplicationOptionInt16_e.html)

## Remarks

If developing a C++ application, use [dsApplication_ApplicationOptionInt16ChangeNotify_id](Interop.dsAutomation~Interop.dsAutomation.dsApplicationEvent_id_e.html) to register for this notification.

See [Getting Started](GettingStarted-draftsightapi.html) for more information about C++ interface add-in template callback functions.

## See Also

[_IApplicationEvents_ApplicationOptionInt16ChangeNotifyEventHandler Members](Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_ApplicationOptionInt16ChangeNotifyEventHandler.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)

## Availability

DraftSight V1R5.0
