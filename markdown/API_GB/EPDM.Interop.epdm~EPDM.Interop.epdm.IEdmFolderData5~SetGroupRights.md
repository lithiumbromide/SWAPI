---
title: "SetGroupRights Method (IEdmFolderData5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFolderData5"
member: "SetGroupRights"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolderData5~SetGroupRights.html"
---

# SetGroupRights Method (IEdmFolderData5)

Sets the specified permissions for the specified user group.

## Syntax

### Visual Basic

```vb
Sub SetGroupRights( _
   ByVal lGroupID As System.Integer, _
   ByVal lEdmRightFlags As System.Integer _
)
```

### C#

```csharp
void SetGroupRights(
   System.int lGroupID,
   System.int lEdmRightFlags
)
```

### C++/CLI

```cpp
void SetGroupRights(
   System.int lGroupID,
   System.int lEdmRightFlags
)
```

### Parameters

- `lGroupID`: ID of user group for which to set permissions
- `lEdmRightFlags`: Combination of [EdmRightFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRightFlags.html) bits

## Examples

See the [IEdmFolderData5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolderData5.html) examples.

## Remarks

Retrieve user groups using [IEdmUserMgr5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5.html).

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmFolderData5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolderData5.html)
[IEdmFolderData5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolderData5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
