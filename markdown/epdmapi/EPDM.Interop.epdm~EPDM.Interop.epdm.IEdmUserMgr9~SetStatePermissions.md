---
title: "SetStatePermissions Method (IEdmUserMgr9)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUserMgr9"
member: "SetStatePermissions"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr9~SetStatePermissions.html"
---

# SetStatePermissions Method (IEdmUserMgr9)

Sets state permissions.

## Syntax

### Visual Basic

```vb
Sub SetStatePermissions( _
   ByVal poPermissions() As EdmStatePermission _
)
```

### C#

```csharp
void SetStatePermissions(
   EdmStatePermission[] poPermissions
)
```

### C++/CLI

```cpp
void SetStatePermissions(
   array<EdmStatePermission>^ poPermissions
)
```

### Parameters

- `poPermissions`: Array of [EdmStatePermission](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmStatePermission.html) structures; one structure for each permission assignment

## Remarks

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- E_EDM_PERMISSION_DENIED: The logged-in user lacks the [EdmSysPerm](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSysPerm.html).EdmSysPerm_EditUserMgr permission.

## See Also

[IEdmUserMgr9 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr9.html)
[IEdmUserMgr9 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr9_members.html)
[IEdmUserMgr9::GetStatePermissions Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr9~GetStatePermissions.html)

## Availability

SOLIDWORKS PDM Professional 2017
