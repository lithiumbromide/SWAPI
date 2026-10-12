---
title: "GetTransitionPermissions Method (IEdmUserMgr9)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUserMgr9"
member: "GetTransitionPermissions"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr9~GetTransitionPermissions.html"
---

# GetTransitionPermissions Method (IEdmUserMgr9)

Gets the transition permissions for the specified owner and transition.

## Syntax

### Visual Basic

```vb
Sub GetTransitionPermissions( _
   ByVal lOwnerID As System.Integer, _
   ByVal meOwnerType As EdmObjectType, _
   ByVal lTransitionID As System.Integer, _
   ByRef ppoPermissions() As EdmTransitionPermission _
)
```

### C#

```csharp
void GetTransitionPermissions(
   System.int lOwnerID,
   EdmObjectType meOwnerType,
   System.int lTransitionID,
   out EdmTransitionPermission[] ppoPermissions
)
```

### C++/CLI

```cpp
void GetTransitionPermissions(
   System.int lOwnerID,
   EdmObjectType meOwnerType,
   System.int lTransitionID,
   [Out] array<EdmTransitionPermission>^ ppoPermissions
)
```

### Parameters

- `lOwnerID`: ID of the user or group for which to get permissions; 0 to return permissions for all users and groups
- `meOwnerType`: Type of lOwnerID as defined in [EdmObjectType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmObjectType.html); valid only if lOwnerID is not 0
- `lTransitionID`: ID of transition for which to get permissions; 0 to return permissions for all transitions
- `ppoPermissions`: Array of [EdmTransitionPermission](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTransitionPermission.html) structures; one structure for each permission assignment

## Examples

See the [IEdmUserMgr9](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr9.html) examples.

## Remarks

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmUserMgr9 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr9.html)
[IEdmUserMgr9 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr9_members.html)
[IEdmUserMgr9::SetTransitionPermissions Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr9~SetTransitionPermissions.html)

## Availability

SOLIDWORKS PDM Professional 2017
