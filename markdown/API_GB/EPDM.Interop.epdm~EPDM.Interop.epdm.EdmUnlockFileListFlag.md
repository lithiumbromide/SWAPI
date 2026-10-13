---
title: "EdmUnlockFileListFlag Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmUnlockFileListFlag"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUnlockFileListFlag.html"
---

# EdmUnlockFileListFlag Enumeration

Flags telling [IEdmBatchUnlock::GetFileList](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock~GetFileList.html) what kind of files to get. [Bitmask](Bitmasks.htm).

## Syntax

### Visual Basic

```vb
Public Enum EdmUnlockFileListFlag
   Inherits System.Enum
```

### C#

```csharp
public enum EdmUnlockFileListFlag : System.Enum
```

### C++/CLI

```cpp
public enum class EdmUnlockFileListFlag : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| Euflf_GetUndoLocked | 2 = Files with their locks undone |
| Euflf_GetUnlocked | 1 = Checked-in files |
| Euflf_GetUnprocessed | 4 = Files not processed by the operation |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
