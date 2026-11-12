---
title: "EdmBomFlag Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmBomFlag"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomFlag.html"
---

# EdmBomFlag Enumeration

Bill of Materials options used in calls to [IEdmFile7::GetComputedBOM](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile7~GetComputedBOM.html). [Bitmask](Bitmasks.htm).

## Syntax

### Visual Basic

```vb
Public Enum EdmBomFlag
   Inherits System.Enum
```

### C#

```csharp
public enum EdmBomFlag : System.Enum
```

### C++/CLI

```cpp
public enum class EdmBomFlag : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmBf_AsBuilt | 1 = Include as-built referenced files, i.e., the versions which were present in the cache when the parent file was checked in |
| EdmBf_ShowSelected | 2 = Include the selected file in the Bill of Materials; if this flag is not set, only its children are included |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
