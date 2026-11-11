---
title: "_IApplicationEvents_ApplicationOptionBoolChangeNotifyEventHandler Delegate"
project: ""
interface: "_IApplicationEvents_ApplicationOptionBoolChangeNotifyEventHandler"
member: ""
kind: "delegate"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_ApplicationOptionBoolChangeNotifyEventHandler.html"
---

# _IApplicationEvents_ApplicationOptionBoolChangeNotifyEventHandler Delegate

Post-notifies the application when the specified Boolean application option changes.

## Syntax

### Visual Basic

```vb
Public Delegate Sub _IApplicationEvents_ApplicationOptionBoolChangeNotifyEventHandler( _
   ByVal Option As dsApplicationOptionBool_e _
)
```

### C#

```csharp
public delegate void _IApplicationEvents_ApplicationOptionBoolChangeNotifyEventHandler(
   dsApplicationOptionBool_e Option
)
```

### JScript

```
public delegate _IApplicationEvents_ApplicationOptionBoolChangeNotifyEventHandler(
   Option : dsApplicationOptionBool_e
)
```

### Managed Extensions for C++

```
public: __gc __delegate void _IApplicationEvents_ApplicationOptionBoolChangeNotifyEventHandler(
   dsApplicationOptionBool_e Option
)
```

### C++/CLI

```cpp
public delegate void _IApplicationEvents_ApplicationOptionBoolChangeNotifyEventHandler(
   dsApplicationOptionBool_e Option
)
```

### Parameters

- `Option`: Option as defined in [dsApplicationOptionBool_e](Interop.dsAutomation~Interop.dsAutomation.dsApplicationOptionBool_e.html)

## Remarks

If developing a C++ application, use [dsApplication_ApplicationOptionBoolChangeNotify_id](Interop.dsAutomation~Interop.dsAutomation.dsApplicationEvent_id_e.html) to register for this notification.

See [Getting Started](GettingStarted-draftsightapi.html) for more information about C++ interface add-in template callback functions.

## See Also

[_IApplicationEvents_ApplicationOptionBoolChangeNotifyEventHandler Members](Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_ApplicationOptionBoolChangeNotifyEventHandler.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)

## Availability

DraftSight V1R5.0
