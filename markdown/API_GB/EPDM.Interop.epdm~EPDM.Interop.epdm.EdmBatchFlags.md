---
title: "EdmBatchFlags Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmBatchFlags"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBatchFlags.html"
---

# EdmBatchFlags Enumeration

Flags used in [IEdmBatchUpdate::SetVar](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate~SetVar.html) and [IEdmBatchUpdate2::SetFolderVar](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate2~SetFolderVar.html) to control the behavior of [IEdmBatchUpdate](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate.html) and [IEdmBatchUpdate2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate2.html). [Bitmask](Bitmasks.htm).

## Syntax

### Visual Basic

```vb
Public Enum EdmBatchFlags
   Inherits System.Enum
```

### C#

```csharp
public enum EdmBatchFlags : System.Enum
```

### C++/CLI

```cpp
public enum class EdmBatchFlags : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmBatch_AllConfigs | 1 = Ignore the configuration argument and update the variable value in all configurations |
| EdmBatch_Nothing | 0 = Normal operation |
| EdmBatch_RefreshPreview | 2 = Reload data card |
| EdmBatch_UpdateVarIfNotPartOfCard | 4 = Update all variables, even those that are not visible in this data card |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
