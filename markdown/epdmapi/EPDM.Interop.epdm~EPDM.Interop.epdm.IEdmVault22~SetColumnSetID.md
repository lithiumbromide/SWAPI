---
title: "SetColumnSetID Method (IEdmVault22)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault22"
member: "SetColumnSetID"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault22~SetColumnSetID.html"
---

# SetColumnSetID Method (IEdmVault22)

Sets the specified column set ID in the user's registry.

## Syntax

### Visual Basic

```vb
Sub SetColumnSetID( _
   ByVal mlColumnSetID As System.Integer _
)
```

### C#

```csharp
void SetColumnSetID(
   System.int mlColumnSetID
)
```

### C++/CLI

```cpp
void SetColumnSetID(
   System.int mlColumnSetID
)
```

### Parameters

- `mlColumnSetID`: ID of column set to register

## Examples

See the [IEdmVault22](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault22.html) example

## Remarks

Before calling this method, use [IEdmVault22::GetColumnSets](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault22~GetColumnSets.html) to obtain all valid column set IDs for the currently logged-in user of this vault.

This method stores the column set ID at the following location in the registry:

`User_Computer\HKEY_CURRENT_USER\SOFTWARE\SolidWorks\Applications\PDMWorks Enterprise\CTDMListView\ColumnSet\vault_name\user_name`

After calling this method, call [IEdmVault22::GetCurrentColumnSet](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault22~GetCurrentColumnSet.html) to verify the current column set was changed.

## See Also

[IEdmVault22 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault22.html)
[IEdmVault22 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault22_members.html)

## Availability

SOLIDWORKS PDM Professional 2024
