---
title: "SetUserRights Method (IEdmFolderData5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFolderData5"
member: "SetUserRights"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolderData5~SetUserRights.html"
---

# SetUserRights Method (IEdmFolderData5)

Sets the specified permissions for the specified user.

## Syntax

### Visual Basic

```vb
Sub SetUserRights( _
   ByVal lUserID As System.Integer, _
   ByVal lEdmRightFlags As System.Integer _
)
```

### C#

```csharp
void SetUserRights(
   System.int lUserID,
   System.int lEdmRightFlags
)
```

### C++/CLI

```cpp
void SetUserRights(
   System.int lUserID,
   System.int lEdmRightFlags
)
```

### Parameters

- `lUserID`: ID of user for which to set permissions
- `lEdmRightFlags`: Combination of [EdmRightFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRightFlags.html) bits

## Examples

See the [IEdmFolderData5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolderData5.html) examples.

## Remarks

Retrieve users using [IEdmUserMgr5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5.html).

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmFolderData5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolderData5.html)
[IEdmFolderData5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolderData5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
