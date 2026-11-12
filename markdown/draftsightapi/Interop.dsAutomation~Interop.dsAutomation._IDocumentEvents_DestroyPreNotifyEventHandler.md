---
title: "_IDocumentEvents_DestroyPreNotifyEventHandler Delegate"
project: ""
interface: "_IDocumentEvents_DestroyPreNotifyEventHandler"
member: ""
kind: "delegate"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_DestroyPreNotifyEventHandler.html"
---

# _IDocumentEvents_DestroyPreNotifyEventHandler Delegate

Pre-notifies an application when a document is about to close.

## Syntax

### Visual Basic

```vb
Public Delegate Sub _IDocumentEvents_DestroyPreNotifyEventHandler()
```

### C#

```csharp
public delegate void _IDocumentEvents_DestroyPreNotifyEventHandler()
```

### JScript

```
public delegate _IDocumentEvents_DestroyPreNotifyEventHandler()
```

### Managed Extensions for C++

```
public: __gc __delegate void _IDocumentEvents_DestroyPreNotifyEventHandler();
```

### C++/CLI

```cpp
public delegate void _IDocumentEvents_DestroyPreNotifyEventHandler();
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
SINK_ENTRY_EX(IDC_DSAPPLICATIONEVENT, DIID__IDocumentEvents, dsDocument_DestroyPreNotify_id, OnDestroyPreNotify)
SINK_ENTRY_EX(IDC_DSAPPLICATIONEVENT, DIID__IDocumentEvents, dsDocument_FileSavePostNotify_id, OnFileSavePostNotify)
SINK_ENTRY_EX(IDC_DSAPPLICATIONEVENT, DIID__IDocumentEvents, dsDocument_ModifyNotify_id, OnModifyNotify)

END_SINK_MAP()

//Declare the callbacks for IDocument class
void __stdcall OnDestroyNotify();
void __stdcall OnDestroyPreNotify();
void __stdcall OnFileSavePostNotify();
void __stdcall OnModifyNotify();

**Source file**

void

__stdcall CDsAddinDocument::OnDestroyPreNotify()

{

// TODO: Add your code here

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
RegisterDocumentDestroyPreNotifyHook(m_dsDoc);

RegisterDocumentFileSavePostNotifyHook(m_dsDoc);

RegisterDocumentModifyNotifyHook(m_dsDoc);

}

~DsAddinDocument() {

UnRegisterDocumentDestroyNotifyHook(m_dsDoc);
UnRegisterDocumentDestroyPreNotifyHook(m_dsDoc);

UnRegisterDocumentFileSavePostNotifyHook(m_dsDoc);

UnRegisterDocumentModifyNotifyHook(m_dsDoc);

}

DeclareDocumentDestroyNotifyHook
DeclareDocumentDestroyPreNotifyHook

DeclareDocumentFileSavePostNotifyHook

DeclareDocumentModifyNotifyHook

dsDocument_c* getMyDoc() {

return m_dsDoc;}

bool DestroyNotify();

bool DestroyPreNotify();

bool FileSavePostNotify();

bool ModifyNotify();

**Source file**

ImplementDocumentDestroyNotifyHook(DsAddinDocument)
ImplementDocumentDestroyPreNotifyHook(DsAddinDocument)

ImplementDocumentModifyNotifyHook(DsAddinDocument)

ImplementDocumentFileSavePostNotifyHook(DsAddinDocument)

bool

DsAddinDocument::DestroyNotify()

{

//TODO: Add your code here

return true

;

}

bool DsAddinDocument::DestroyPreNotify()

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

## Remarks

If developing a C++ application, use [dsDocument_DestroyPreNotify_id](Interop.dsAutomation~Interop.dsAutomation.dsDocumentEvent_id_e.html) to register for this notification.

See [Getting Started](GettingStarted-draftsightapi.html) for more information about C++ interface add-in template callback functions.

## See Also

[_IDocumentEvents_DestroyPreNotifyEventHandler Members](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_DestroyPreNotifyEventHandler.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IDocument Event DestroyNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_DestroyNotifyEventHandler.html)

## Availability

DraftSight V1R4.0
