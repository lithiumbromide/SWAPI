---
title: "_IDocumentEvents_FileSavePostNotify2EventHandler Delegate"
project: ""
interface: "_IDocumentEvents_FileSavePostNotify2EventHandler"
member: ""
kind: "delegate"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_FileSavePostNotify2EventHandler.html"
---

# _IDocumentEvents_FileSavePostNotify2EventHandler Delegate

Post-notifies an application that a document has been saved.

## Syntax

### Visual Basic

```vb
Public Delegate Sub _IDocumentEvents_FileSavePostNotify2EventHandler( _
   ByVal FileName As System.String _
)
```

### C#

```csharp
public delegate void _IDocumentEvents_FileSavePostNotify2EventHandler(
   System.string FileName
)
```

### JScript

```
public delegate _IDocumentEvents_FileSavePostNotify2EventHandler(
   FileName : System.String
)
```

### Managed Extensions for C++

```
public: __gc __delegate void _IDocumentEvents_FileSavePostNotify2EventHandler(
   System.string* FileName
)
```

### C++/CLI

```cpp
public delegate void _IDocumentEvents_FileSavePostNotify2EventHandler(
   System.String^ FileName
)
```

### Parameters

- `FileName`: Path and file name of the saved document

## Remarks

When this event is triggered, the IDocument object's path and file name correspond to the document being saved. This event's FileName parameter corresponds to the path and file name of the saved document.

If developing a C++ application, use [dsDocument_FileSavePostNotify2_id](Interop.dsAutomation~Interop.dsAutomation.dsDocumentEvent_id_e.html) to register for this notification.

See [Getting Started](GettingStarted-draftsightapi.html) for more information about C++ interface add-in template callback functions.

## See Also

[_IDocumentEvents_FileSavePostNotify2EventHandler Members](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_FileSavePostNotify2EventHandler.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IDocument Event FileSavePreNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_FileSavePreNotifyEventHandler.html)

## Availability

DraftSight V1R5.0
