---
title: "EdmUnlockStatusFlag Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmUnlockStatusFlag"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUnlockStatusFlag.html"
---

# EdmUnlockStatusFlag Enumeration

Statuses returned by [IEdmBatchUnlock2::GetStatus](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock2~GetStatus.html).

## Syntax

### Visual Basic

```vb
Public Enum EdmUnlockStatusFlag
   Inherits System.Enum
```

### C#

```csharp
public enum EdmUnlockStatusFlag : System.Enum
```

### C++/CLI

```cpp
public enum class EdmUnlockStatusFlag : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| Eusf_CloseAfterCheckinFlag | 1 = Return true if user selects Close File after Check In on the Check In dialog box toolbar, return false if user selects Reload File after Check In |
| Eusf_Nothing | 0 = Do not use |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
