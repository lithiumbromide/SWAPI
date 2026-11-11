---
title: "_IDocumentEvents_CommandOptionStringChangeNotifyEventHandler Delegate"
project: ""
interface: "_IDocumentEvents_CommandOptionStringChangeNotifyEventHandler"
member: ""
kind: "delegate"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_CommandOptionStringChangeNotifyEventHandler.html"
---

# _IDocumentEvents_CommandOptionStringChangeNotifyEventHandler Delegate

Post-notifies an application when the specified string command option changes.

## Syntax

### Visual Basic

```vb
Public Delegate Sub _IDocumentEvents_CommandOptionStringChangeNotifyEventHandler( _
   ByVal Option As dsCommandOptionString_e _
)
```

### C#

```csharp
public delegate void _IDocumentEvents_CommandOptionStringChangeNotifyEventHandler(
   dsCommandOptionString_e Option
)
```

### JScript

```
public delegate _IDocumentEvents_CommandOptionStringChangeNotifyEventHandler(
   Option : dsCommandOptionString_e
)
```

### Managed Extensions for C++

```
public: __gc __delegate void _IDocumentEvents_CommandOptionStringChangeNotifyEventHandler(
   dsCommandOptionString_e Option
)
```

### C++/CLI

```cpp
public delegate void _IDocumentEvents_CommandOptionStringChangeNotifyEventHandler(
   dsCommandOptionString_e Option
)
```

### Parameters

- `Option`: String command option as defined in [dsCommandOptionString_e](Interop.dsAutomation~Interop.dsAutomation.dsCommandOptionString_e.html)

## Remarks

If developing a C++ application, use [dsDocument_CommandOptionStringChangeNotify](Interop.dsAutomation~Interop.dsAutomation.dsDocumentEvent_id_e.html) to register for this notification.

See [Getting Started](GettingStarted-draftsightapi.html) for more information about C++ interface add-in template callback functions.

## See Also

[_IDocumentEvents_CommandOptionStringChangeNotifyEventHandler Members](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_CommandOptionStringChangeNotifyEventHandler.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IDocument Event CommandOptionBoolChangeNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_CommandOptionBoolChangeNotifyEventHandler.html)
[IDocument Event CommandOptionDoubleChangeNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_CommandOptionDoubleChangeNotifyEventHandler.html)
[IDocument Event CommandOptionInt16ChangeNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_CommandOptionInt16ChangeNotifyEventHandler.html)
[IDocument Event CommandOptionInt32ChangeNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_CommandOptionInt32ChangeNotifyEventHandler.html)
[IDocument Event CommandOptionInt8ChangeNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_CommandOptionInt8ChangeNotifyEventHandler.html)
[IDocument Event CommandOptionPoint2DChangeNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_CommandOptionPoint2DChangeNotifyEventHandler.html)
[IDocument Event CommandOptionPoint3DChangeNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_CommandOptionPoint3DChangeNotifyEventHandler.html)

## Availability

DraftSight V1R3.0
