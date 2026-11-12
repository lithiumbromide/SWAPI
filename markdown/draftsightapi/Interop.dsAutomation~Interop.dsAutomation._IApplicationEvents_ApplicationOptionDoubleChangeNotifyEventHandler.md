---
title: "_IApplicationEvents_ApplicationOptionDoubleChangeNotifyEventHandler Delegate"
project: ""
interface: "_IApplicationEvents_ApplicationOptionDoubleChangeNotifyEventHandler"
member: ""
kind: "delegate"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_ApplicationOptionDoubleChangeNotifyEventHandler.html"
---

# _IApplicationEvents_ApplicationOptionDoubleChangeNotifyEventHandler Delegate

Post-notifies the application when the specified double value application option changes.

## Syntax

### Visual Basic

```vb
Public Delegate Sub _IApplicationEvents_ApplicationOptionDoubleChangeNotifyEventHandler( _
   ByVal Option As dsApplicationOptionDouble_e _
)
```

### C#

```csharp
public delegate void _IApplicationEvents_ApplicationOptionDoubleChangeNotifyEventHandler(
   dsApplicationOptionDouble_e Option
)
```

### JScript

```
public delegate _IApplicationEvents_ApplicationOptionDoubleChangeNotifyEventHandler(
   Option : dsApplicationOptionDouble_e
)
```

### Managed Extensions for C++

```
public: __gc __delegate void _IApplicationEvents_ApplicationOptionDoubleChangeNotifyEventHandler(
   dsApplicationOptionDouble_e Option
)
```

### C++/CLI

```cpp
public delegate void _IApplicationEvents_ApplicationOptionDoubleChangeNotifyEventHandler(
   dsApplicationOptionDouble_e Option
)
```

### Parameters

- `Option`: Option as defined in [dsApplicationOptionString_e](Interop.dsAutomation~Interop.dsAutomation.dsApplicationOptionString_e.html)

## Remarks

If developing a C++ applicatio0n, use [dsApplication_ApplicationOptionDoubleChangeNotify_id](Interop.dsAutomation~Interop.dsAutomation.dsApplicationEvent_id_e.html) to register for this notification. See [Getting Started](GettingStarted-draftsightapi.html) for more information about C++ interface add-in template callback functions.

## See Also

[_IApplicationEvents_ApplicationOptionDoubleChangeNotifyEventHandler Members](Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_ApplicationOptionDoubleChangeNotifyEventHandler.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)

## Availability

DraftSight V1R5.0
