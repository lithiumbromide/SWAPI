---
title: "_IApplicationEvents_ApplicationOptionStringChangeNotifyEventHandler Delegate"
project: ""
interface: "_IApplicationEvents_ApplicationOptionStringChangeNotifyEventHandler"
member: ""
kind: "delegate"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_ApplicationOptionStringChangeNotifyEventHandler.html"
---

# _IApplicationEvents_ApplicationOptionStringChangeNotifyEventHandler Delegate

Post-notifies the application when the specified string application option changes.

## Syntax

### Visual Basic

```vb
Public Delegate Sub _IApplicationEvents_ApplicationOptionStringChangeNotifyEventHandler( _
   ByVal Option As dsApplicationOptionString_e _
)
```

### C#

```csharp
public delegate void _IApplicationEvents_ApplicationOptionStringChangeNotifyEventHandler(
   dsApplicationOptionString_e Option
)
```

### JScript

```
public delegate _IApplicationEvents_ApplicationOptionStringChangeNotifyEventHandler(
   Option : dsApplicationOptionString_e
)
```

### Managed Extensions for C++

```
public: __gc __delegate void _IApplicationEvents_ApplicationOptionStringChangeNotifyEventHandler(
   dsApplicationOptionString_e Option
)
```

### C++/CLI

```cpp
public delegate void _IApplicationEvents_ApplicationOptionStringChangeNotifyEventHandler(
   dsApplicationOptionString_e Option
)
```

### Parameters

- `Option`: Option as defined in [dsApplicationOptionString_e](Interop.dsAutomation~Interop.dsAutomation.dsApplicationOptionString_e.html)

## Remarks

If developing a C++ application, use [dsApplication_ApplicationOptionStringChangeNotify_id](Interop.dsAutomation~Interop.dsAutomation.dsApplicationEvent_id_e.html) to register for this notification. See [Getting Started](GettingStarted-draftsightapi.html) for more information about C++ interface add-in template callback functions.

## See Also

[_IApplicationEvents_ApplicationOptionStringChangeNotifyEventHandler Members](Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_ApplicationOptionStringChangeNotifyEventHandler.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)

## Availability

DraftSight V1R5.0
