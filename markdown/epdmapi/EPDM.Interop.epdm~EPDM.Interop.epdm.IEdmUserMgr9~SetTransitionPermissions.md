---
title: "SetTransitionPermissions Method (IEdmUserMgr9)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUserMgr9"
member: "SetTransitionPermissions"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr9~SetTransitionPermissions.html"
---

# SetTransitionPermissions Method (IEdmUserMgr9)

Sets transition permissions.

## Syntax

### Visual Basic

```vb
Sub SetTransitionPermissions( _
   ByVal poPermissions() As EdmTransitionPermission _
)
```

### C#

```csharp
void SetTransitionPermissions(
   EdmTransitionPermission[] poPermissions
)
```

### C++/CLI

```cpp
void SetTransitionPermissions(
   array<EdmTransitionPermission>^ poPermissions
)
```

### Parameters

- `poPermissions`: Array of [EdmTransitionPermission](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTransitionPermission.html) structures; one structure for each permission assignment

## Remarks

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- E_EDM_PERMISSION_DENIED: The logged-in user lacks the [EdmSysPerm](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSysPerm.html).EdmSysPerm_EditUserMgr permission.

## See Also

[IEdmUserMgr9 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr9.html)
[IEdmUserMgr9 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr9_members.html)
[IEdmUserMgr9::GetTransitionPermissions Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr9~GetTransitionPermissions.html)

## Availability

SOLIDWORKS PDM Professional 2017
