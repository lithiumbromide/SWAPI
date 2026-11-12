---
title: "EdmTaskFlag Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmTaskFlag"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskFlag.html"
---

# EdmTaskFlag Enumeration

Task add-in flags used in [IEdmTaskProperties::TaskFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties~TaskFlags.html) and [EdmTaskInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskInfo.html). [Bitmask](Bitmasks.htm).

## Syntax

### Visual Basic

```vb
Public Enum EdmTaskFlag
   Inherits System.Enum
```

### C#

```csharp
public enum EdmTaskFlag : System.Enum
```

### C++/CLI

```cpp
public enum class EdmTaskFlag : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmTask_Nothing | 0 = None of the other flags |
| EdmTask_SupportsChangeState | 16 = Task can be launched via a workflow, state, change command |
| EdmTask_SupportsDetails | 4 = Add-in extends the task details dialog box in the task list window in the Administration tool; the add-in will receive a call to its IEdmAddIn5::OnCmd method with the argument EdmCmdType.EdmCmd_TaskDetails when the dialog box is to be extended |
| EdmTask_SupportsInitExec | 2 = Add-in wants to have its IEdmAddIn5::OnCmd method called when the user launches the task; this callback type ( EdmCmdType.EdmCmd_TaskLaunch ) can be used to provide a more sophisticated user interface than one created with the card editor; if this flag is included, then multiple files will be processed by a single task instance; otherwise, each file will be processed by a separate task instance |
| EdmTask_SupportsInitForm | 1 = Add-in supports displaying of a card created with the card editor; the card is used as the user interface when the task is launched, and the values of the card are accessible to the task add-in when it is executed |
| EdmTask_SupportsScheduling | 8 = Task can be scheduled |

## Remarks

The flags indicate what a task add-in is capable of doing.

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
[Programming Tasks](Tasks.htm)
