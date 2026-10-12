---
title: "GetStatePermissions Method (IEdmUserMgr9)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUserMgr9"
member: "GetStatePermissions"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr9~GetStatePermissions.html"
---

# GetStatePermissions Method (IEdmUserMgr9)

Gets the state permissions for the specified owner and state.

## Syntax

### Visual Basic

```vb
Sub GetStatePermissions( _
   ByVal lOwnerID As System.Integer, _
   ByVal meOwnerType As EdmObjectType, _
   ByVal lStateID As System.Integer, _
   ByRef ppoPermissions() As EdmStatePermission _
)
```

### C#

```csharp
void GetStatePermissions(
   System.int lOwnerID,
   EdmObjectType meOwnerType,
   System.int lStateID,
   out EdmStatePermission[] ppoPermissions
)
```

### C++/CLI

```cpp
void GetStatePermissions(
   System.int lOwnerID,
   EdmObjectType meOwnerType,
   System.int lStateID,
   [Out] array<EdmStatePermission>^ ppoPermissions
)
```

### Parameters

- `lOwnerID`: ID of the user or group for which to get permissions; 0 to return permissions for all users and groups
- `meOwnerType`: Type of lOwnerID as defined in [EdmObjectType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmObjectType.html); valid only if lOwnerID is not 0
- `lStateID`: ID of state for which to get permissions; 0 to return permissions for all states
- `ppoPermissions`: Array of [EdmStatePermission](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmStatePermission.html) structures; one structure for each permission assignment

## Examples

See the [IEdmUserMgr9](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr9.html) examples.

## Remarks

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmUserMgr9 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr9.html)
[IEdmUserMgr9 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr9_members.html)
[IEdmUserMgr9::SetStatePermissions Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr9~SetStatePermissions.html)

## Availability

SOLIDWORKS PDM Professional 2017
