---
title: "AddUsers3 Method (IEdmUserMgr10)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUserMgr10"
member: "AddUsers3"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr10~AddUsers3.html"
---

# AddUsers3 Method (IEdmUserMgr10)

Adds the specified users of the specified login type to the vault.

## Syntax

### Visual Basic

```vb
Sub AddUsers3( _
   ByRef ppoUserData As EdmUserData2(), _
   ByVal UserType As EdmUserType _
)
```

### C#

```csharp
void AddUsers3(
   out EdmUserData2[] ppoUserData,
   EdmUserType UserType
)
```

### C++/CLI

```cpp
void AddUsers3(
   [Out] array<EdmUserData2> ppoUserData,
   EdmUserType UserType
)
```

### Parameters

- `ppoUserData`: Array of [EdmUserData2](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserData2.html) structures; one structure for each user
- `UserType`: Login type of users as defined in [EdmUserType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserType.html)

## Examples

See the [IEdmUserMgr10](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr10.html) examples.

## Remarks

This method supersedes [IEdmUserMgr7::AddUsers2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr7~AddUsers2.html) by providing the ability to add users by type to the vault.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmUserMgr10 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr10.html)
[IEdmUserMgr10 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr10_members.html)

## Availability

SOLIDWORKS PDM Professional 2019
