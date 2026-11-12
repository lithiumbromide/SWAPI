---
title: "_IDocumentEvents_FileSavePreNotifyEventHandler Delegate"
project: ""
interface: "_IDocumentEvents_FileSavePreNotifyEventHandler"
member: ""
kind: "delegate"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_FileSavePreNotifyEventHandler.html"
---

# _IDocumentEvents_FileSavePreNotifyEventHandler Delegate

Pre-notifies an application before a file is saved.

## Syntax

### Visual Basic

```vb
Public Delegate Sub _IDocumentEvents_FileSavePreNotifyEventHandler( _
   ByVal FileName As System.String, _
   ByVal SaveOption As dsDocumentSaveAsOption_e _
)
```

### C#

```csharp
public delegate void _IDocumentEvents_FileSavePreNotifyEventHandler(
   System.string FileName,
   dsDocumentSaveAsOption_e SaveOption
)
```

### JScript

```
public delegate _IDocumentEvents_FileSavePreNotifyEventHandler(
   FileName : System.String,
   SaveOption : dsDocumentSaveAsOption_e
)
```

### Managed Extensions for C++

```
public: __gc __delegate void _IDocumentEvents_FileSavePreNotifyEventHandler(
   System.string* FileName,
   dsDocumentSaveAsOption_e SaveOption
)
```

### C++/CLI

```cpp
public delegate void _IDocumentEvents_FileSavePreNotifyEventHandler(
   System.String^ FileName,
   dsDocumentSaveAsOption_e SaveOption
)
```

### Parameters

- `FileName`: Name of the file about to be saved
- `SaveOption`: Save option as defined in [dsDocumentSaveAsOption_e](Interop.dsAutomation~Interop.dsAutomation.dsDocumentSaveAsOption_e.html)

## Examples

## Examples

[Fire Application and Document Events (C#)](Fire_Application_and_Document_Events_Example_CSharp.htm)
[Fire Application and Document Events (VB.NET)](Fire_Application_and_Document_Events_Example_VBNET.htm)
[Fire Application and Document Events (VBA)](Fire_Application_and_Document_Events_Example_VBA.htm)

## Remarks

If developing a C++ application, use [dsDocument_FileSavePreNotify_id](Interop.dsAutomation~Interop.dsAutomation.dsDocumentEvent_id_e.html) to register for this notification.

See [Getting Started](GettingStarted-draftsightapi.html) for more information about C++ interface add-in template callback functions.

## See Also

[_IDocumentEvents_FileSavePreNotifyEventHandler Members](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_FileSavePreNotifyEventHandler.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IDocument Event FileSavePostNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_FileSavePostNotifyEventHandler.html)

## Availability

DraftSight V1R1
