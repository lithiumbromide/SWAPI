---
title: "EdmGetOpMsg Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmGetOpMsg"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGetOpMsg.html"
---

# EdmGetOpMsg Enumeration

Log error messages; used in calls to [IEdmGetOpCallback::LogMessage](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetOpCallback~LogMessage.html).

## Syntax

### Visual Basic

```vb
Public Enum EdmGetOpMsg
   Inherits System.Enum
```

### C#

```csharp
public enum EdmGetOpMsg : System.Enum
```

### C++/CLI

```cpp
public enum class EdmGetOpMsg : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| Egom_ErrorRunningPostAddins | 3 = An error occurred running add-ins that implement hooks on EdmCmd_PostGet or EdmCmd_PostLock commands |
| Egom_LockNotificationsError | 1 = Error sending check-out notifications |
| Egom_Undefined | 0 = Undefined message |
| Egom_UndoLockAfterErrorFailed | 2 = The attempt to unlock a file after its check-out failed has failed |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
