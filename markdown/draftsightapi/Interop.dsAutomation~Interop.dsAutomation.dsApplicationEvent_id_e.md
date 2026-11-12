---
title: "dsApplicationEvent_id_e Enumeration"
project: ""
interface: "dsApplicationEvent_id_e"
member: ""
kind: "enum"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.dsApplicationEvent_id_e.html"
---

# dsApplicationEvent_id_e Enumeration

Types of DraftSight application events.

## Syntax

### Visual Basic

```vb
Public Enum dsApplicationEvent_id_e
   Inherits System.Enum
```

### C#

```csharp
public enum dsApplicationEvent_id_e : System.Enum
```

### JScript

```
public enum dsApplicationEvent_id_e extends System.Enum
```

### Managed Extensions for C++

```
__value public enum dsApplicationEvent_id_e : public System.Enum
```

### C++/CLI

```cpp
public enum class dsApplicationEvent_id_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| dsApplication_ActiveDocumentChangedNotify_id | 5 = ActiveDocumentChangedNotify |
| dsApplication_ApplicationOptionBoolChangeNotify_id | 9 = ApplicationOptionBoolChangeNotify |
| dsApplication_ApplicationOptionDoubleChangeNotify_id | 12 = ApplicationOptionDoubleChangeNotify |
| dsApplication_ApplicationOptionInt16ChangeNotify_id | 10 = ApplicationOptionInt16ChangeNotify |
| dsApplication_ApplicationOptionInt32ChangeNotify_id | 11 = ApplicationOptionInt32ChangeNotify |
| dsApplication_ApplicationOptionStringChangeNotify_id | 13 = ApplicationOptionStringChangeNotify |
| dsApplication_CommandCancelNotify_id | 8 = CommandCancelNotify |
| dsApplication_CommandPostNotify_id | 7 = CommandPostNotify |
| dsApplication_CommandPreNotify_id | 6 = CommandPreNotify |
| dsApplication_CurrentProfileResetPostNotify_id | 18 = CurrentProfileResetPostNotify |
| dsApplication_CurrentProfileResetPreNotify_id | 17 = CurrentProfileResetPreNotify |
| dsApplication_DestroyNotify_id | 4 = DestroyNotify |
| dsApplication_FileNewNotify_id | 1 = FileNewNotify |
| dsApplication_FileOpenPostNotify_id | 3 = FileOpenPostNotify |
| dsApplication_FileOpenPreNotify_id | 2 = FileOpenPreNotify |
| dsApplication_OnFileProcessedNotify_id | 20 = OnFileProcessedNotify |
| dsApplication_OnIdleNotify_id | 14 = OnIdleNotify |
| dsApplication_PrintPostNotify_id | 16 = PrintPostNotify |
| dsApplication_PrintPreNotify_id | 15 = PrintPreNotify |
| dsApplication_RequestToOpenFileNotify_id | 19 = RequestToOpenFileNotify |

## Remarks

To receive notifications, a DLL application must register for the notifications by object type. This registration must be done for each instance of a particular object.

For example, the file:

- **DsAddinConnection.h**, included in the [DraftSight API COM native C++ interface template](GettingStarted-draftsightapi.html), automatically registers events:

BEGIN_SINK_MAP(CDsAddinConnection)

SINK_ENTRY_EX(IDC_DSAPPLICATIONEVENT, DIID__IApplicationEvents, dsApplication_FileNewNotify_id, OnFileNewNotify)

SINK_ENTRY_EX(IDC_DSAPPLICATIONEVENT, DIID__IApplicationEvents, dsApplication_FileOpenPreNotify_id, OnFileOpenPreNotify)

SINK_ENTRY_EX(IDC_DSAPPLICATIONEVENT, DIID__IApplicationEvents, dsApplication_FileOpenPostNotify_id, OnFileOpenPostNotify)

SINK_ENTRY_EX(IDC_DSAPPLICATIONEVENT, DIID__IApplicationEvents, dsApplication_ActiveDocumentChangedNotify_id, OnActiveDocumentChangedNotify)

END_SINK_MAP()

- **dsAddinConnection.h**, included in the [DraftSight API C++ interface add-in template](GettingStarted-draftsightapi.html), automatically registers and unregisters events:

myApplication(dsApplication_c *dsApp) : m_dsApp(dsApp) {

RegisterApplicationFileNewNotifyHook(m_dsApp);

RegisterApplicationFileOpenPreNotifyHook(m_dsApp);

...

}

~myApplication() {

UnRegisterApplicationFileNewNotifyHook(m_dsApp);

UnRegisterApplicationFileOpenPreNotifyHook(m_dsApp);

...

}

## See Also

[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
