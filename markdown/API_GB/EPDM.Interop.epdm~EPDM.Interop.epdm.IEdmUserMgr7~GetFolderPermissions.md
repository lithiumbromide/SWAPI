---
title: "GetFolderPermissions Method (IEdmUserMgr7)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUserMgr7"
member: "GetFolderPermissions"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr7~GetFolderPermissions.html"
---

# GetFolderPermissions Method (IEdmUserMgr7)

Gets the permissions set on the specified folder for the specified user or group.

## Syntax

### Visual Basic

```vb
Sub GetFolderPermissions( _
   ByVal lOwnerID As System.Integer, _
   ByVal meOwnerType As EdmObjectType, _
   ByVal lFolderID As System.Integer, _
   ByVal lEdmGetPermFlags As System.Integer, _
   ByRef ppoPermissions As EdmFolderPermission() _
)
```

### C#

```csharp
void GetFolderPermissions(
   System.int lOwnerID,
   EdmObjectType meOwnerType,
   System.int lFolderID,
   System.int lEdmGetPermFlags,
   out EdmFolderPermission[] ppoPermissions
)
```

### C++/CLI

```cpp
void GetFolderPermissions(
   System.int lOwnerID,
   EdmObjectType meOwnerType,
   System.int lFolderID,
   System.int lEdmGetPermFlags,
   [Out] array<EdmFolderPermission> ppoPermissions
)
```

### Parameters

- `lOwnerID`: ID of the user or group for which to get permissions; 0 to return permissions for all users and groups
- `meOwnerType`: Type of lOwnerID as defined in [EdmObjectType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmObjectType.html)
- `lFolderID`: ID of folder for which to get permissions
- `lEdmGetPermFlags`: Combination of [EdmGetPermFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGetPermFlag.html) bits (see **Remarks**)
- `ppoPermissions`: Array of [EdmFolderPermission](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmFolderPermission.html) structures; one structure for each permission

## Examples

See the [IEdmUserMgr7](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr7.html) examples.

## Remarks

This method returns not only permissions explicitly set on a folder, but also permissions inherited from parent folders, depending on the combination of EdmGetPermFlag bits in lEdmGetPermFlags.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmUserMgr7 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr7.html)
[IEdmUserMgr7 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr7_members.html)

## Availability

SOLIDWORKS PDM Professional 2010
