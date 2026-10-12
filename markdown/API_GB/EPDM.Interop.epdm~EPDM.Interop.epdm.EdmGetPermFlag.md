---
title: "EdmGetPermFlag Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmGetPermFlag"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGetPermFlag.html"
---

# EdmGetPermFlag Enumeration

Options for returning folder permissions used in calls to [IEdmUserMgr7::GetFolderPermissions](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr7~GetFolderPermissions.html).

## Syntax

### Visual Basic

```vb
Public Enum EdmGetPermFlag
   Inherits System.Enum
```

### C#

```csharp
public enum EdmGetPermFlag : System.Enum
```

### C++/CLI

```cpp
public enum class EdmGetPermFlag : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmGetPerm_Nothing | 0 = Default behavior; return all inherited permissions, not just those explicitly set on a folder |
| EdmGetPerm_OnlyExplicitlySet | 1 = Return only permissions explicitly set on folders |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
