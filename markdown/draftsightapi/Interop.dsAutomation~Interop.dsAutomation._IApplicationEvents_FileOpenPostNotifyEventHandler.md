---
title: "_IApplicationEvents_FileOpenPostNotifyEventHandler Delegate"
project: ""
interface: "_IApplicationEvents_FileOpenPostNotifyEventHandler"
member: ""
kind: "delegate"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_FileOpenPostNotifyEventHandler.html"
---

# _IApplicationEvents_FileOpenPostNotifyEventHandler Delegate

Post-notifies an application when a file has been opened.

## Syntax

### Visual Basic

```vb
Public Delegate Sub _IApplicationEvents_FileOpenPostNotifyEventHandler( _
   ByVal Document As Document _
)
```

### C#

```csharp
public delegate void _IApplicationEvents_FileOpenPostNotifyEventHandler(
   Document Document
)
```

### JScript

```
public delegate _IApplicationEvents_FileOpenPostNotifyEventHandler(
   Document : Document
)
```

### Managed Extensions for C++

```
public: __gc __delegate void _IApplicationEvents_FileOpenPostNotifyEventHandler(
   Document* Document
)
```

### C++/CLI

```cpp
public delegate void _IApplicationEvents_FileOpenPostNotifyEventHandler(
   Document^ Document
)
```

### Parameters

- `Document`: New [document](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)

## Examples

See the following code snippets:

- COM native C++
- [C++](#CPP)

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

void

__stdcall

CDsAddinConnection::OnFileOpenPostNotify(IDocument* Doc)

{

//TODO: Add your implementation code here

}

##### C++

**Header file**

class DSADDINSAMPLE_EXPORT myApplication :

public dsApplicationEvents_c, public dsCommandEvents_c

public

:

myApplication(dsApplication_c *dsApp) : m_dsApp(dsApp) {

RegisterApplicationFileNewNotifyHook(m_dsApp);

RegisterApplicationFileOpenPreNotifyHook(m_dsApp);

RegisterApplicationFileOpenPostNotifyHook(m_dsApp);

}

~myApplication() {

UnRegisterApplicationFileNewNotifyHook(m_dsApp);

UnRegisterApplicationFileOpenPreNotifyHook(m_dsApp);

UnRegisterApplicationFileOpenPostNotifyHook(m_dsApp);

}

DeclareApplicationFileNewNotifyHook

DeclareApplicationFileOpenPreNotifyHook

DeclareApplicationFileOpenPostNotifyHook

bool

FileNewNotify(dsDocument_c * docIn);

bool

FileOpenPreNotify(dsString fileName, dsDocumentOpenOption_e Option);

bool FileOpenPostNotify(dsDocument_c* docIn);

**Source file**

ImplementApplicationFileNewNotifyHook(myApplication)

ImplementApplicationFileOpenPreNotifyHook(myApplication)

ImplementApplicationFileOpenPostNotifyHook(myApplication)

bool

myApplication::FileNewNotify(dsDocument_c* docIn)

{

//TODO: Add your code here

return true

;

}

bool

myApplication::FileOpenPreNotify(dsString fileName, dsDocumentOpenOption_e Option)

{

//TODO: Add your code here

return true

;

}

bool

myApplication::FileOpenPostNotify(dsDocument_c *docIn)

{

//TODO: Add your code here

return true

;

}

[Back to top](#exampleBookmark)

## Examples

[Fire Application and Document Events (C#)](Fire_Application_and_Document_Events_Example_CSharp.htm)
[Fire Application and Document Events (VB.NET)](Fire_Application_and_Document_Events_Example_VBNET.htm)
[Fire Application and Document Events (VBA)](Fire_Application_and_Document_Events_Example_VBA.htm)

## Remarks

This is the last event fired before control returns to the user. This event indicates that methods that modify the file can be called.

If developing a C++ application, use [dsApplication_FileOpenPostNotify_id](Interop.dsAutomation~Interop.dsAutomation.dsApplicationEvent_id_e.html) to register for this notification.

See [Getting Started](GettingStarted-draftsightapi.html) for more information about C++ interface add-in template callback functions.

## See Also

[_IApplicationEvents_FileOpenPostNotifyEventHandler Members](Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_FileOpenPostNotifyEventHandler.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IApplication Event FileOpenPreNotify](Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_FileOpenPreNotifyEventHandler.html)

## Availability

DraftSight V1R1
