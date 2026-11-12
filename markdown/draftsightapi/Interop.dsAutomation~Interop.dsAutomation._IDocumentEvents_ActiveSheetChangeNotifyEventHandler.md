---
title: "_IDocumentEvents_ActiveSheetChangeNotifyEventHandler Delegate"
project: ""
interface: "_IDocumentEvents_ActiveSheetChangeNotifyEventHandler"
member: ""
kind: "delegate"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_ActiveSheetChangeNotifyEventHandler.html"
---

# _IDocumentEvents_ActiveSheetChangeNotifyEventHandler Delegate

Post-notifies an application when the active sheet has changed.

## Syntax

### Visual Basic

```vb
Public Delegate Sub _IDocumentEvents_ActiveSheetChangeNotifyEventHandler( _
   ByVal SheetName As System.String _
)
```

### C#

```csharp
public delegate void _IDocumentEvents_ActiveSheetChangeNotifyEventHandler(
   System.string SheetName
)
```

### JScript

```
public delegate _IDocumentEvents_ActiveSheetChangeNotifyEventHandler(
   SheetName : System.String
)
```

### Managed Extensions for C++

```
public: __gc __delegate void _IDocumentEvents_ActiveSheetChangeNotifyEventHandler(
   System.string* SheetName
)
```

### C++/CLI

```cpp
public delegate void _IDocumentEvents_ActiveSheetChangeNotifyEventHandler(
   System.String^ SheetName
)
```

### Parameters

- `SheetName`: Name of the new active sheet

## Remarks

If developing a c++ application, use [dsDocument_ActiveSheetChangeNotify](Interop.dsAutomation~Interop.dsAutomation.dsDocumentEvent_id_e.html) to register for this notification.

See [Getting Started](GettingStarted-draftsightapi.html) for more information about C++ interface add-in template callback functions.

## See Also

[_IDocumentEvents_ActiveSheetChangeNotifyEventHandler Members](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_ActiveSheetChangeNotifyEventHandler.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)

## Availability

DraftSight V1R3.0
