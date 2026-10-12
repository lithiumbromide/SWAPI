---
title: "SetFolderPermissions Method (IEdmUserMgr7)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUserMgr7"
member: "SetFolderPermissions"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr7~SetFolderPermissions.html"
---

# SetFolderPermissions Method (IEdmUserMgr7)

Sets specified permissions on a specified folder for a specified user or group.

## Syntax

### Visual Basic

```vb
Sub SetFolderPermissions( _
   ByVal poPermissions() As EdmFolderPermission _
)
```

### C#

```csharp
void SetFolderPermissions(
   EdmFolderPermission[] poPermissions
)
```

### C++/CLI

```cpp
void SetFolderPermissions(
   array<EdmFolderPermission>^ poPermissions
)
```

### Parameters

- `poPermissions`: Array of [EdmFolderPermission](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmFolderPermission.html) structures; one structure for each permission assignment

## Examples

See the [IEdmUserMgr7](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr7.html) examples.

## Remarks

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- E_EDM_PERMISSION_DENIED: The logged-in user lacks the [EdmSysPerm](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSysPerm.html).EdmSysPerm_EditUserMgr permission.

## See Also

[IEdmUserMgr7 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr7.html)
[IEdmUserMgr7 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr7_members.html)

## Availability

SOLIDWORKS PDM Professional 2010
