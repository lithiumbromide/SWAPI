---
title: "_IDocumentEvents_CommandOptionPoint3DChangeNotifyEventHandler Delegate"
project: ""
interface: "_IDocumentEvents_CommandOptionPoint3DChangeNotifyEventHandler"
member: ""
kind: "delegate"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_CommandOptionPoint3DChangeNotifyEventHandler.html"
---

# _IDocumentEvents_CommandOptionPoint3DChangeNotifyEventHandler Delegate

Post-notifies an application when the specified 3D point command option changes.

## Syntax

### Visual Basic

```vb
Public Delegate Sub _IDocumentEvents_CommandOptionPoint3DChangeNotifyEventHandler( _
   ByVal Option As dsCommandOptionPoint3d_e _
)
```

### C#

```csharp
public delegate void _IDocumentEvents_CommandOptionPoint3DChangeNotifyEventHandler(
   dsCommandOptionPoint3d_e Option
)
```

### JScript

```
public delegate _IDocumentEvents_CommandOptionPoint3DChangeNotifyEventHandler(
   Option : dsCommandOptionPoint3d_e
)
```

### Managed Extensions for C++

```
public: __gc __delegate void _IDocumentEvents_CommandOptionPoint3DChangeNotifyEventHandler(
   dsCommandOptionPoint3d_e Option
)
```

### C++/CLI

```cpp
public delegate void _IDocumentEvents_CommandOptionPoint3DChangeNotifyEventHandler(
   dsCommandOptionPoint3d_e Option
)
```

### Parameters

- `Option`: 3D command option as defined in [dsCommandOptionPoint3d_e](Interop.dsAutomation~Interop.dsAutomation.dsCommandOptionPoint3d_e.html)

## Remarks

If developing a C++ application, use [dsDocument_CommandOptionPoint3DChangeNotify](Interop.dsAutomation~Interop.dsAutomation.dsDocumentEvent_id_e.html) to register for this notification.

See [Getting Started](GettingStarted-draftsightapi.html) for more information about C++ interface add-in template callback functions.

## See Also

[_IDocumentEvents_CommandOptionPoint3DChangeNotifyEventHandler Members](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_CommandOptionPoint3DChangeNotifyEventHandler.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IDocument Event CommandOptionBoolChangeNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_CommandOptionBoolChangeNotifyEventHandler.html)
[IDocument Event CommandOptionDoubleChangeNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_CommandOptionDoubleChangeNotifyEventHandler.html)
[IDocument Event CommandOptionInt16ChangeNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_CommandOptionInt16ChangeNotifyEventHandler.html)
[IDocument Event CommandOptionInt32ChangeNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_CommandOptionInt32ChangeNotifyEventHandler.html)
[IDocument Event CommandOptionInt8ChangeNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_CommandOptionInt8ChangeNotifyEventHandler.html)
[IDocument Event CommandOptionPoint2DChangeNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_CommandOptionPoint2DChangeNotifyEventHandler.html)
[IDocument Event CommandOptionStringChangeNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_CommandOptionStringChangeNotifyEventHandler.html)

## Availability

DraftSight V1R3.0
