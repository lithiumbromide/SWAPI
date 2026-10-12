---
title: "GetFirstLoggedInUserPosition Method (IEdmUserMgr5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUserMgr5"
member: "GetFirstLoggedInUserPosition"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5~GetFirstLoggedInUserPosition.html"
---

# GetFirstLoggedInUserPosition Method (IEdmUserMgr5)

Starts an enumeration of the users that are logged in to the specified vaults.

## Syntax

### Visual Basic

```vb
Function GetFirstLoggedInUserPosition( _
   ByVal bsVaultNames As System.String _
) As IEdmPos5
```

### C#

```csharp
IEdmPos5 GetFirstLoggedInUserPosition(
   System.string bsVaultNames
)
```

### C++/CLI

```cpp
IEdmPos5^ GetFirstLoggedInUserPosition(
   System.String^ bsVaultNames
)
```

### Parameters

- `bsVaultNames`: Optional newline-separated list of the names of the vaults for which to enumerate logged-in users; "" to enumerate users that are logged in to the current vault only

### Return Value

[IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the first logged-in user in the enumeration

## Examples

[Create New Vault (VB.NET)](Create_New_Vault_Example_VBNET.htm)
[Create New Vault (C#)](Create_New_Vault_Example_CSharp.htm)

## Remarks

After calling this method, pass the returned position of the first logged-in user to [IEdmUserMgr5::GetNextLoggedInUser](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5~GetNextLoggedInUser.html) to get the first logged-in user in this list. Then call IEdmUserMgr5::GetNextLoggedInUser repeatedly to get the rest of the users that are logged in to the vault.

C++ users not using smart-pointer wrapper functions must release the returned interface, IEdmPos5.

Call [IEdmUserMgr5::GetLoggedInUser](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5~GetNextLoggedInUser.html) to only get the [user](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser5.html) who is currently running this program in the [vault](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5.html).

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmUserMgr5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5.html)
[IEdmUserMgr5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
