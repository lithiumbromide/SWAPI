---
title: "_IApplicationEvents_PrintPreNotifyEventHandler Delegate"
project: ""
interface: "_IApplicationEvents_PrintPreNotifyEventHandler"
member: ""
kind: "delegate"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_PrintPreNotifyEventHandler.html"
---

# _IApplicationEvents_PrintPreNotifyEventHandler Delegate

Pre-notifies an application before the specified document is printed.

## Syntax

### Visual Basic

```vb
Public Delegate Sub _IApplicationEvents_PrintPreNotifyEventHandler( _
   ByVal Document As Document, _
   ByVal PrintSpecification As PrintSpecification _
)
```

### C#

```csharp
public delegate void _IApplicationEvents_PrintPreNotifyEventHandler(
   Document Document,
   PrintSpecification PrintSpecification
)
```

### JScript

```
public delegate _IApplicationEvents_PrintPreNotifyEventHandler(
   Document : Document,
   PrintSpecification : PrintSpecification
)
```

### Managed Extensions for C++

```
public: __gc __delegate void _IApplicationEvents_PrintPreNotifyEventHandler(
   Document* Document,
   PrintSpecification* PrintSpecification
)
```

### C++/CLI

```cpp
public delegate void _IApplicationEvents_PrintPreNotifyEventHandler(
   Document^ Document,
   PrintSpecification^ PrintSpecification
)
```

### Parameters

- `Document`: [IDocument](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
- `PrintSpecification`: [IPrintSpecification](Interop.dsAutomation~Interop.dsAutomation.IPrintSpecification.html)

## Remarks

If developing a C++ application, use [dsApplication_PrintPreNotify_id](Interop.dsAutomation~Interop.dsAutomation.dsApplicationEvent_id_e.html) to register for this notification.

See [Getting Started](GettingStarted-draftsightapi.html) for more information about C++ interface add-in template callback functions.

## See Also

[_IApplicationEvents_PrintPreNotifyEventHandler Members](Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_PrintPreNotifyEventHandler.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IApplication Event PrintPostNotify](Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_PrintPostNotifyEventHandler.html)

## Availability

DraftSight 2017 SP0
