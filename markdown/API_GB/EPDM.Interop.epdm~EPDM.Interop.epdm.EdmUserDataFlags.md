---
title: "EdmUserDataFlags Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmUserDataFlags"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserDataFlags.html"
---

# EdmUserDataFlags Enumeration

Flags used in [EdmUserData](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserData.html)'s mlFlags field when adding users with [IEdmUserMgr6::AddUsers](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr6~AddUsers.html).

## Syntax

### Visual Basic

```vb
Public Enum EdmUserDataFlags
   Inherits System.Enum
```

### C#

```csharp
public enum EdmUserDataFlags : System.Enum
```

### C++/CLI

```cpp
public enum class EdmUserDataFlags : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| Edmudf_CopySettings | 4 = Copy the settings from the user with EdmUserData.mlUserID |
| Edmudf_ForceAdd | 2 = Add this user even if other users in the array sent to IEdmUserMgr7::AddUsers2 cannot be added |
| Edmudf_GetInterface | 1 = Return the IEdmUser6 interface in the structure |
| Edmudf_Nothing | 0 = None of the other flags |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
