---
title: "_IApplicationEvents_ActiveDocumentChangedNotifyEventHandler Delegate"
project: ""
interface: "_IApplicationEvents_ActiveDocumentChangedNotifyEventHandler"
member: ""
kind: "delegate"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_ActiveDocumentChangedNotifyEventHandler.html"
---

# _IApplicationEvents_ActiveDocumentChangedNotifyEventHandler Delegate

Post-notifies an application when the active window has changed.

## Syntax

### Visual Basic

```vb
Public Delegate Sub _IApplicationEvents_ActiveDocumentChangedNotifyEventHandler()
```

### C#

```csharp
public delegate void _IApplicationEvents_ActiveDocumentChangedNotifyEventHandler()
```

### JScript

```
public delegate _IApplicationEvents_ActiveDocumentChangedNotifyEventHandler()
```

### Managed Extensions for C++

```
public: __gc __delegate void _IApplicationEvents_ActiveDocumentChangedNotifyEventHandler();
```

### C++/CLI

```cpp
public delegate void _IApplicationEvents_ActiveDocumentChangedNotifyEventHandler();
```

## Examples

##### COM native C++

**Header file**

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

**Source file**

void __stdcall CDsAddinConnection::OnActiveDocumentChangedNotify()
{

// TODO: Add your code here

}

[Back to top](#exampleBookmark)

## Examples

[Fire Application and Document Events (C#)](Fire_Application_and_Document_Events_Example_CSharp.htm)
[Fire Application and Document Events (VB.NET)](Fire_Application_and_Document_Events_Example_VBNET.htm)
[Fire Application and Document Events (VBA)](Fire_Application_and_Document_Events_Example_VBA.htm)

## Remarks

This event is only sent when the active window in the DraftSight session actually changes to a new active window. For example, if the DraftSight application closes a non-active document, then there is no need to activate a new window.

Window activations are not guaranteed during the shutdown of the DraftSight application.

If developing a C++ application, use [dsApplication_ActiveDocumentChangedNotify_id](Interop.dsAutomation~Interop.dsAutomation.dsApplicationEvent_id_e.html) to register for this notification.

See [Getting Started](GettingStarted-draftsightapi.html) for more information about C++ interface add-in template callback functions.

## See Also

[_IApplicationEvents_ActiveDocumentChangedNotifyEventHandler Members](Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_ActiveDocumentChangedNotifyEventHandler.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)

## Availability

DraftSight V1R1
