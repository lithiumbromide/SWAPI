---
title: "EdmDefValComp Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmDefValComp"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmDefValComp.html"
---

# EdmDefValComp Enumeration

Return options when calling [IEdmCardViewCallback6::GetDefaultValueComponent](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardViewCallback6~GetDefaultValueComponent.html).

## Syntax

### Visual Basic

```vb
Public Enum EdmDefValComp
   Inherits System.Enum
```

### C#

```csharp
public enum EdmDefValComp : System.Enum
```

### C++/CLI

```cpp
public enum class EdmDefValComp : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmDvc_FileID | 1 = Return the ID of the file |
| EdmDvc_FilePath | 3 = Return the file's complete path |
| EdmDvc_FolderID | 2 = Return the ID of the file's parent folder |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
