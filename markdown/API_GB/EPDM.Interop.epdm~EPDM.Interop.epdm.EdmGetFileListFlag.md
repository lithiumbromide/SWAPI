---
title: "EdmGetFileListFlag Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmGetFileListFlag"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGetFileListFlag.html"
---

# EdmGetFileListFlag Enumeration

Files to return by [IEdmBatchGet::GetFileList](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet~GetFileList.html). [Bitmask](Bitmasks.htm).

## Syntax

### Visual Basic

```vb
Public Enum EdmGetFileListFlag
   Inherits System.Enum
```

### C#

```csharp
public enum EdmGetFileListFlag : System.Enum
```

### C++/CLI

```cpp
public enum class EdmGetFileListFlag : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| Egflf_GetFailed | 8 = Operation failed |
| Egflf_GetLocked | 2 = Return files checked out by the operation |
| Egflf_GetRetrieved | 1 = Return files retrieved by the operation |
| Egflf_GetUnprocessed | 4 = Return files not processed by the operation |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
