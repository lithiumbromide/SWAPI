---
title: "EdmChangeStateFileListFlag Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmChangeStateFileListFlag"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmChangeStateFileListFlag.html"
---

# EdmChangeStateFileListFlag Enumeration

Options for returning files when making calls to [IEdmBatchChangeState::GetFileList](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState~GetFileList.html). [Bitmask](Bitmasks.htm).

## Syntax

### Visual Basic

```vb
Public Enum EdmChangeStateFileListFlag
   Inherits System.Enum
```

### C#

```csharp
public enum EdmChangeStateFileListFlag : System.Enum
```

### C++/CLI

```cpp
public enum class EdmChangeStateFileListFlag : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| Ecsflf_GetActionUpdated | 4 = Return files that were updated by an action that set a variable value |
| Ecsflf_GetChanged | 1 = Return files that had their state changed |
| Ecsflf_GetUnprocessed | 2 = Return files that did not have their state changed |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
