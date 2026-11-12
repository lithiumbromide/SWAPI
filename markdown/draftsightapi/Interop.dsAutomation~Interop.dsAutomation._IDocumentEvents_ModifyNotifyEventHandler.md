---
title: "_IDocumentEvents_ModifyNotifyEventHandler Delegate"
project: ""
interface: "_IDocumentEvents_ModifyNotifyEventHandler"
member: ""
kind: "delegate"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_ModifyNotifyEventHandler.html"
---

# _IDocumentEvents_ModifyNotifyEventHandler Delegate

Notifies an application when a document is marked as dirty (modified since opened and not saved) in the current DraftSight session.

## Syntax

### Visual Basic

```vb
Public Delegate Sub _IDocumentEvents_ModifyNotifyEventHandler()
```

### C#

```csharp
public delegate void _IDocumentEvents_ModifyNotifyEventHandler()
```

### JScript

```
public delegate _IDocumentEvents_ModifyNotifyEventHandler()
```

### Managed Extensions for C++

```
public: __gc __delegate void _IDocumentEvents_ModifyNotifyEventHandler();
```

### C++/CLI

```cpp
public delegate void _IDocumentEvents_ModifyNotifyEventHandler();
```

## Examples

See the following code snippets:

- COM native C++
- [C++](#CPP)

##### COM native C++

**Header file**

//Register the events for the IDocument class

BEGIN_SINK_MAP(CDsAddinDocument)

SINK_ENTRY_EX(IDC_DSAPPLICATIONEVENT, DIID__IDocumentEvents, dsDocument_DestroyNotify_id, OnDestroyNotify)
SINK_ENTRY_EX(IDC_DSAPPLICATIONEVENT, DIID__IDocumentEvents, dsDocument_FileSavePostNotify_id, OnFileSavePostNotify)
SINK_ENTRY_EX(IDC_DSAPPLICATIONEVENT, DIID__IDocumentEvents, dsDocument_ModifyNotify_id, OnModifyNotify)

END_SINK_MAP()

//Declare the callbacks for IDocument class
void __stdcall OnDestroyNotify();
void __stdcall OnFileSavePostNotify();
void __stdcall OnModifyNotify();

**Source file**

void

__stdcall

CDsAddinDocument::OnModifyNotify()

{

//TODO : Add your code here

}

##### C++

**Header file**

class

DSADDINSAMPLE_EXPORT DsAddinDocument :

public dsDocumentEvents_c

{

public

:

DsAddinDocument(dsDocument_c *dsDoc) : m_dsDoc(dsDoc) {

RegisterDocumentDestroyNotifyHook(m_dsDoc);

RegisterDocumentFileSavePostNotifyHook(m_dsDoc);

RegisterDocumentModifyNotifyHook(m_dsDoc);

}

~DsAddinDocument() {

UnRegisterDocumentDestroyNotifyHook(m_dsDoc);

UnRegisterDocumentFileSavePostNotifyHook(m_dsDoc);

UnRegisterDocumentModifyNotifyHook(m_dsDoc);

}

DeclareDocumentDestroyNotifyHook

DeclareDocumentFileSavePostNotifyHook

DeclareDocumentModifyNotifyHook

dsDocument_c* getMyDoc() {

return m_dsDoc;}

bool

DestroyNotify();

bool

FileSavePostNotify();

bool ModifyNotify();

**Source file**

ImplementDocumentDestroyNotifyHook(DsAddinDocument)

ImplementDocumentModifyNotifyHook(DsAddinDocument)

ImplementDocumentFileSavePostNotifyHook(DsAddinDocument)

bool

DsAddinDocument::DestroyNotify()

{

//TODO: Add your code here

return true

;

}

bool

DsAddinDocument::FileSavePostNotify()

{

//TODO: Add your code here

return true

;

}

bool

DsAddinDocument::ModifyNotify()

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

If developing a C++ application, use [dsDocument_ModifyNotify_id](Interop.dsAutomation~Interop.dsAutomation.dsDocumentEvent_id_e.html) to register for this notification.

See [Getting Started](GettingStarted-draftsightapi.html) for more information about C++ interface add-in template callback functions.

## See Also

[_IDocumentEvents_ModifyNotifyEventHandler Members](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_ModifyNotifyEventHandler.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IDocument::IsDirty Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~IsDirty.html)

## Availability

DraftSight V1R1
