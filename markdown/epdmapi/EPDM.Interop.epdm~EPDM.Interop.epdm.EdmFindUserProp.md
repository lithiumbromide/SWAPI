---
title: "EdmFindUserProp Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmFindUserProp"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmFindUserProp.html"
---

# EdmFindUserProp Enumeration

Properties to get or set when calling [IEdmFindUser::GetPropt](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFindUser~GetPropt.html) and [IEdmFindUser::SetPropt](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFindUser~SetPropt.html).

## Syntax

### Visual Basic

```vb
Public Enum EdmFindUserProp
   Inherits System.Enum
```

### C#

```csharp
public enum EdmFindUserProp : System.Enum
```

### C++/CLI

```cpp
public enum class EdmFindUserProp : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| Edmfup_Email | 3 = User's email address |
| Edmfup_FullName | 1 = User's full name |
| Edmfup_Initials | 2 = User's initials |
| Edmfup_LoginName | 0 = User's login name |
| Edmfup_UserData | 4 = User's custom data |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
