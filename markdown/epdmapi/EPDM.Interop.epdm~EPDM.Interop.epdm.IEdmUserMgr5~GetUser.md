---
title: "GetUser Method (IEdmUserMgr5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUserMgr5"
member: "GetUser"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5~GetUser.html"
---

# GetUser Method (IEdmUserMgr5)

Gets a user with the specified name or ID.

## Syntax

### Visual Basic

```vb
Function GetUser( _
   ByRef poIdOrName As System.Object _
) As IEdmUser5
```

### C#

```csharp
IEdmUser5 GetUser(
   ref System.object poIdOrName
)
```

### C++/CLI

```cpp
IEdmUser5^ GetUser(
   System.Object^% poIdOrName
)
```

### Parameters

- `poIdOrName`: Id or name of user to get

### Return Value

[IEdmUser5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser5.html)

## Examples

[Add Folder (VB.NET)](Add_Folder_Example_VBNET.htm)
[Add Folder (C#)](Add_Folder_Example_CSharp.htm)

## Remarks

C++ users must release the returned interface, IEdmUser5.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- S_FALSE: The poIdOrName argument contains an unknown user name. ppoRetUser contains null when this happens in C++.
- E_EDM_INVALID_ID: The poIdOrName argument contains an invalid ID.
- E_EDM_DATABASE_ACCESS: Returned only for invalid IDs in SOLIDWORKS PDM Professional 5.2.

## See Also

[IEdmUserMgr5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5.html)
[IEdmUserMgr5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
