---
title: "_IApplicationEvents_DestroyNotifyEventHandler Delegate"
project: ""
interface: "_IApplicationEvents_DestroyNotifyEventHandler"
member: ""
kind: "delegate"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_DestroyNotifyEventHandler.html"
---

# _IApplicationEvents_DestroyNotifyEventHandler Delegate

Pre-notifies an application when DraftSight is about to be destroyed.

## Syntax

### Visual Basic

```vb
Public Delegate Sub _IApplicationEvents_DestroyNotifyEventHandler()
```

### C#

```csharp
public delegate void _IApplicationEvents_DestroyNotifyEventHandler()
```

### JScript

```
public delegate _IApplicationEvents_DestroyNotifyEventHandler()
```

### Managed Extensions for C++

```
public: __gc __delegate void _IApplicationEvents_DestroyNotifyEventHandler();
```

### C++/CLI

```cpp
public delegate void _IApplicationEvents_DestroyNotifyEventHandler();
```

## Examples

##### COM native C++

**Header file:**

//Register the events for the IApplication class
BEGIN_SINK_MAP(CDsAddinConnection)
SINK_ENTRY_EX(IDC_DSAPPLICATIONEVENT, DIID__IApplicationEvents, dsApplication_ActiveDocumetnChangedNotify_id, OnActiveDocumentChangedNotify)
SINK_ENTRY_EX(IDC_DSAPPLICATIONEVENT, DIID__IApplicationEvents, dsApplication_DestroyNotify_id, OnDestroyNotifyHandler)
SINK_ENTRY_EX(IDC_DSAPPLICATIONEVENT, DIID__IApplicationEvents, dsApplication_FileNewNotify_id, OnFileNewNotify)
SINK_ENTRY_EX(IDC_DSAPPLICATIONEVENT, DIID__IApplicationEvents, dsApplication_FileOpenPostNotify_id, OnFileOpenPostNotify)
SINK_ENTRY_EX(IDC_DSAPPLICATIONEVENT, DIID__IApplicationEvents, dsApplication_FileOpenPreNotify_id, OnFileOpenPreNotify)
END_SINK_MAP()

//Declare the callbacks for IApplication class
void __stdcall OnActiveDocumentChangedNotify();
void __stdcall OnDestroyNotify();
void __stdcall OnFileNewNotify(IDocument* Doc);
void __stdcall OnFileOpenPostNotify(IDocument* Doc);
void __stdcall OnFileOpenPreNotify(BSTR FileName, dsDocumentOpenOption_e Option);

**Source file:**

void __stdcall CDsAddinConnection::DestroyNotify()
{

// TODO: Add your code here

}

## Examples

[Fire Application and Document Events (C#)](Fire_Application_and_Document_Events_Example_CSharp.htm)
[Fire Application and Document Events (VB.NET)](Fire_Application_and_Document_Events_Example_VBNET.htm)
[Fire Application and Document Events (VBA)](Fire_Application_and_Document_Events_Example_VBA.htm)

## Remarks

Applications should perform any cleanup inside this event.

If developing a C++ application, use [dsApplication_DestroyNotify_id](Interop.dsAutomation~Interop.dsAutomation.dsApplicationEvent_id_e.html) to register for this notification.

See [Getting Started](GettingStarted-draftsightapi.html) for more information about C++ interface add-in template callback functions.

## See Also

[_IApplicationEvents_DestroyNotifyEventHandler Members](Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_DestroyNotifyEventHandler.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)

## Availability

DraftSight V1R1
