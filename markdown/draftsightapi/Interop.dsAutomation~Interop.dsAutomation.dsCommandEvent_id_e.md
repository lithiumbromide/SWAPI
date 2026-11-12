---
title: "dsCommandEvent_id_e Enumeration"
project: ""
interface: "dsCommandEvent_id_e"
member: ""
kind: "enum"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.dsCommandEvent_id_e.html"
---

# dsCommandEvent_id_e Enumeration

Types of command events.

## Syntax

### Visual Basic

```vb
Public Enum dsCommandEvent_id_e
   Inherits System.Enum
```

### C#

```csharp
public enum dsCommandEvent_id_e : System.Enum
```

### JScript

```
public enum dsCommandEvent_id_e extends System.Enum
```

### Managed Extensions for C++

```
__value public enum dsCommandEvent_id_e : public System.Enum
```

### C++/CLI

```cpp
public enum class dsCommandEvent_id_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| dsCommand_ExecuteNotify_id | 1 = ExecuteNotify |

## Remarks

To receive notifications, a DLL application must register for the notifications by object type. This registration must be done for each instance of a particular object.

For example, the file:

- **DsAddinCommand.h**, included in the [DraftSight API COM native C++ interface add-in template](GettingStarted-draftsightapi.html), automatically registers this event:

BEGIN_SINK_MAP(CDsAddinCommand)
SINK_ENTRY_EX(IDC_DSAPPLICATIONEVENT, DIID__ICommandEvents, dsCommand_ExecuteNotify_id, OnExecuteNotify)
END_SINK_MAP()

- **dsAddinConnection.cpp**, included in the [DraftSight API C++ interface add-in template](GettingStarted-draftsightapi.html), automatically registers this event:

RegisterCommandExecuteNotifyHook( pCmd );

## See Also

[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
