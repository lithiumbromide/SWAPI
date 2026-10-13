---
title: "AddUsers Method (IEdmUserMgr6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUserMgr6"
member: "AddUsers"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr6~AddUsers.html"
---

# AddUsers Method (IEdmUserMgr6)

Obsolete. Superseded by [IEdmUserMgr7::AddUsers2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr7~AddUsers2.html).

## Syntax

### Visual Basic

```vb
Sub AddUsers( _
   ByRef ppoUserData As EdmUserData() _
)
```

### C#

```csharp
void AddUsers(
   out EdmUserData[] ppoUserData
)
```

### C++/CLI

```cpp
void AddUsers(
   [Out] array<EdmUserData> ppoUserData
)
```

### Parameters

- `ppoUserData`: Array of [EdmUserData](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserData.html) structures; one structure for each user

## Remarks

This method is superseded by [IEdmUserMgr7::AddUsers2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr7~AddUsers2.html) which allows you to specify system permissions.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmUserMgr6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr6.html)
[IEdmUserMgr6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr6_members.html)

## Availability

SOLIDWORKS PDM Professional 2007
