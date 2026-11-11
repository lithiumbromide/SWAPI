---
title: "_IDocumentEvents_FileXRefNotificationEventHandler Delegate"
project: ""
interface: "_IDocumentEvents_FileXRefNotificationEventHandler"
member: ""
kind: "delegate"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_FileXRefNotificationEventHandler.html"
---

# _IDocumentEvents_FileXRefNotificationEventHandler Delegate

Notifies the application when an external reference is added or removed from the current document.

## Syntax

### Visual Basic

```vb
Public Delegate Sub _IDocumentEvents_FileXRefNotificationEventHandler( _
   ByVal FileName As System.String _
)
```

### C#

```csharp
public delegate void _IDocumentEvents_FileXRefNotificationEventHandler(
   System.string FileName
)
```

### JScript

```
public delegate _IDocumentEvents_FileXRefNotificationEventHandler(
   FileName : System.String
)
```

### Managed Extensions for C++

```
public: __gc __delegate void _IDocumentEvents_FileXRefNotificationEventHandler(
   System.string* FileName
)
```

### C++/CLI

```cpp
public delegate void _IDocumentEvents_FileXRefNotificationEventHandler(
   System.String^ FileName
)
```

### Parameters

- `FileName`: Full path name of the added or deleted external reference; null or Nothing if the external reference was loaded, unloaded, or detached from the external references dialog

## Remarks

If developing a C++ application, use [dsDocument_FileXRefNotification_id](Interop.dsAutomation~Interop.dsAutomation.dsDocumentEvent_id_e.html) to register for this notification.

See [Getting Started](GettingStarted-draftsightapi.html) for more information about C++ interface add-in template callback functions.

## See Also

[_IDocumentEvents_FileXRefNotificationEventHandler Members](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_FileXRefNotificationEventHandler.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)

## Availability

DraftSight 2020 SP1
