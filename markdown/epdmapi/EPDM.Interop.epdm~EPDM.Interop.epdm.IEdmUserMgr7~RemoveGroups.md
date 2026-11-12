---
title: "RemoveGroups Method (IEdmUserMgr7)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUserMgr7"
member: "RemoveGroups"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr7~RemoveGroups.html"
---

# RemoveGroups Method (IEdmUserMgr7)

Removes the specified groups from the vault.

## Syntax

### Visual Basic

```vb
Sub RemoveGroups( _
   ByVal poGroupIDs() As System.Integer _
)
```

### C#

```csharp
void RemoveGroups(
   System.int[] poGroupIDs
)
```

### C++/CLI

```cpp
void RemoveGroups(
   System.array<int>^ poGroupIDs
)
```

### Parameters

- `poGroupIDs`: Array of IDs of the groups to remove (see **Remarks**)

## Examples

[Vault Utilities (VB.NET)](Vault_Utilities_Example_VBNET.htm)
[Vault Utilities (C#)](Vault_Utilities_Example_CSharp.htm)

## Remarks

If you specify an ID in poGroupIDs that does not exist, it is ignored.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- E_EDM_PERMISSION_DENIED: The logged-in user lacks the [EdmSysPerm](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSysPerm.html).EdmSysPerm_EditUserMgr permission.

## See Also

[IEdmUserMgr7 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr7.html)
[IEdmUserMgr7 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr7_members.html)

## Availability

SOLIDWORKS PDM Professional 2010
