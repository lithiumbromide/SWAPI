---
title: "dsDocumentEvent_id_e Enumeration"
project: ""
interface: "dsDocumentEvent_id_e"
member: ""
kind: "enum"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.dsDocumentEvent_id_e.html"
---

# dsDocumentEvent_id_e Enumeration

Types of document events.

## Syntax

### Visual Basic

```vb
Public Enum dsDocumentEvent_id_e
   Inherits System.Enum
```

### C#

```csharp
public enum dsDocumentEvent_id_e : System.Enum
```

### JScript

```
public enum dsDocumentEvent_id_e extends System.Enum
```

### Managed Extensions for C++

```
__value public enum dsDocumentEvent_id_e : public System.Enum
```

### C++/CLI

```cpp
public enum class dsDocumentEvent_id_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| dsDocument_ActiveSheetChangeNotify_id | 15 = ActiveSheetChangeNotify |
| dsDocument_CommandOptionBoolChangeNotify_id | 11 = CommandOptionBoolChangeNotify |
| dsDocument_CommandOptionDoubleChangeNotify_id | 16 = CommandOptionDoubleChangeNotify |
| dsDocument_CommandOptionInt16ChangeNotify_id | 9 = CommandOptionInt16ChangeNotify |
| dsDocument_CommandOptionInt32ChangeNotify_id | 10 = CommandOptionInt32ChangeNotify |
| dsDocument_CommandOptionInt8ChangeNotify_id | 8 = CommandOptionInt8ChangeNotify |
| dsDocument_CommandOptionPoint2DChangeNotify_id | 13 = CommandOptionPoint2DChangeNotify |
| dsDocument_CommandOptionPoint3DChangeNotify_id | 14 = CommandOptionPoint3DChangeNotify |
| dsDocument_CommandOptionStringChangeNotify_id | 12 = CommandOptionStringChangeNotify |
| dsDocument_DestroyNotify_id | 1 = DestroyNotify |
| dsDocument_DestroyPreNotify_id | 17 = DestroyPreNotify |
| dsDocument_DragNotify_id | 20 = DragNotify |
| dsDocument_DropNotify_id | 21 = DropNotify |
| dsDocument_FileSavePostNotify_id | 3 = Obsolete |
| dsDocument_FileSavePostNotify2_id | 18 = FileSavePostNotify2 |
| dsDocument_FileSavePreNotify_id | 2 = FileSavePreNotify |
| dsDocument_FileXRefNotification_id | 19 = FileXRefNotification |
| dsDocument_ModifyNotify_id | 4 = ModifyNotify |
| dsDocument_ObjectAppendNotify_id | 7 = ObjectAppendNotify |
| dsDocument_ObjectEraseNotify_id | 6 = ObjectEraseNotify |
| dsDocument_ObjectModifyNotify_id | 5 = ObjectModfiyNotify |

## Remarks

To receive notifications, a DLL application must register for the notifications by object type. This registration must be done for each instance of a particular object.

For example, the file:

- **DsAddinDocument.h**, included in the [DraftSight API COM native C++ interface add-in template](GettingStarted-draftsightapi.html), automatically registers these events:

BEGIN_SINK_MAP(CDsAddinDocument)
SINK_ENTRY_EX( IDC_DSAPPLICATIONEVENT, DIID__IDocumentEvents, dsDocument_DestroyNotify_id, OnDestroyNotify )
SINK_ENTRY_EX( IDC_DSAPPLICATIONEVENT, DIID__IDocumentEvents, dsDocument_FileSavePostNotify_id, OnFileSavePostNotify )
SINK_ENTRY_EX( IDC_DSAPPLICATIONEVENT, DIID__IDocumentEvents, dsDocument_ModifyNotify_id, OnModifyNotify )
END_SINK_MAP()

- **dsAddinDocument.h**, included in the [DraftSight API C++ interface add-in template](GettingStarted-draftsightapi.html), automatically registers and unregisters these events:

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

## See Also

[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
