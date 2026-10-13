---
title: "EdmTaskStatus Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmTaskStatus"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskStatus.html"
---

# EdmTaskStatus Enumeration

Task add-in statuses.

## Syntax

### Visual Basic

```vb
Public Enum EdmTaskStatus
   Inherits System.Enum
```

### C#

```csharp
public enum EdmTaskStatus : System.Enum
```

### C++/CLI

```cpp
public enum class EdmTaskStatus : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmTaskStat_CancelPending | 6 = Cancel clicked, but the host computer hasn't noticed it yet |
| EdmTaskStat_DoneCancelled | 8 = Task terminated through canceling |
| EdmTaskStat_DoneFailed | 9 = Task completed with errors |
| EdmTaskStat_DoneOK | 7 = Task completed successfully |
| EdmTaskStat_ResumePending | 11 = Resume clicked after task was suspended, but the host server hasn't noticed it yet |
| EdmTaskStat_Retrying | 4 = Execution has failed at least once, but the framework is trying to execute the add-in again |
| EdmTaskStat_Running | 3 = Task add-in is running on the host computer |
| EdmTaskStat_Starting | 2 = Task starting on the host computer |
| EdmTaskStat_Suspended | 5 = Task suspended by the user |
| EdmTaskStat_SuspensionPending | 10 = Suspend clicked, but the task add-in hasn't noticed it yet |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
[IEdmTaskInstance::GetStatus Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance~GetStatus.html)
[IEdmTaskInstance::SetStatus Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance~SetStatus.html)
