---
title: "_IDocumentEvents_CommandOptionInt16ChangeNotifyEventHandler Delegate"
project: ""
interface: "_IDocumentEvents_CommandOptionInt16ChangeNotifyEventHandler"
member: ""
kind: "delegate"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_CommandOptionInt16ChangeNotifyEventHandler.html"
---

# _IDocumentEvents_CommandOptionInt16ChangeNotifyEventHandler Delegate

Post-notifies an application when the specified Int16 command option changes.

## Syntax

### Visual Basic

```vb
Public Delegate Sub _IDocumentEvents_CommandOptionInt16ChangeNotifyEventHandler( _
   ByVal Option As dsCommandOptionInt16_e _
)
```

### C#

```csharp
public delegate void _IDocumentEvents_CommandOptionInt16ChangeNotifyEventHandler(
   dsCommandOptionInt16_e Option
)
```

### JScript

```
public delegate _IDocumentEvents_CommandOptionInt16ChangeNotifyEventHandler(
   Option : dsCommandOptionInt16_e
)
```

### Managed Extensions for C++

```
public: __gc __delegate void _IDocumentEvents_CommandOptionInt16ChangeNotifyEventHandler(
   dsCommandOptionInt16_e Option
)
```

### C++/CLI

```cpp
public delegate void _IDocumentEvents_CommandOptionInt16ChangeNotifyEventHandler(
   dsCommandOptionInt16_e Option
)
```

### Parameters

- `Option`: Int16 command option as defined in [dsCommandOptionInt16_e](Interop.dsAutomation~Interop.dsAutomation.dsCommandOptionInt16_e.html)

## Remarks

If developing a C++ application, use [dsDocument_CommandOptionInt16ChangeNotify](Interop.dsAutomation~Interop.dsAutomation.dsDocumentEvent_id_e.html) to register for this notification.

See [Getting Started](GettingStarted-draftsightapi.html) for more information about C++ interface add-in template callback functions.

## See Also

[_IDocumentEvents_CommandOptionInt16ChangeNotifyEventHandler Members](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_CommandOptionInt16ChangeNotifyEventHandler.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IDocument Event CommandOptionBoolChangeNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_CommandOptionBoolChangeNotifyEventHandler.html)
[IDocument Event CommandOptionDoubleChangeNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_CommandOptionDoubleChangeNotifyEventHandler.html)
[IDocument Event CommandOptionInt32ChangeNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_CommandOptionInt32ChangeNotifyEventHandler.html)
[IDocument Event CommandOptionInt8ChangeNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_CommandOptionInt8ChangeNotifyEventHandler.html)
[IDocument Event CommandOptionPoint2DChangeNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_CommandOptionPoint2DChangeNotifyEventHandler.html)
[IDocument Event CommandOptionPoint3DChangeNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_CommandOptionPoint3DChangeNotifyEventHandler.html)
[IDocument Event CommandOptionStringChangeNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_CommandOptionStringChangeNotifyEventHandler.html)

## Availability

DraftSight V1R3.0
