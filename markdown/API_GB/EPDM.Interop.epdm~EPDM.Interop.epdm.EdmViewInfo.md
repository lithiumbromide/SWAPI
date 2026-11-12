---
title: "EdmViewInfo Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmViewInfo"
member: ""
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmViewInfo.html"
---

# EdmViewInfo Structure

Contains information about a file vault view.

## Syntax

### Visual Basic

```vb
Public Structure EdmViewInfo
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmViewInfo : System.ValueType
```

### C++/CLI

```cpp
public value class EdmViewInfo : public System.ValueType
```

## Examples

struct EdmViewInfo{
string [mbsVaultName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmViewInfo~mbsVaultName.html);
string [mbsViewID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmViewInfo~mbsViewID.html);
string [mbsVaultID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmViewInfo~mbsVaultID.html);
string [mbsPath](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmViewInfo~mbsPath.html);
short [mbLoggedIn](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmViewInfo~mbLoggedIn.html);
};

## Examples

[Destroy Deleted Files in Vault (C#)](Destroy_Deleted_Files_in_Vault_Example_CSharp.htm)
[Destroy Deleted Files in Vault (VB.NET)](Destroy_Deleted_Files_in_Vault_Example_VBNET.htm)
[Add Items (C#)](Add_Items_Example_CSharp.htm)
[Add Items (VB.NET)](Add_Items_Example_VBNET.htm)

## Remarks

This structure is returned by [IEdmVault8::GetVaultViews](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault8~GetVaultViews.html).

## See Also

[EdmViewInfo Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmViewInfo_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

Version 6.4 of SOLIDWORKS PDM Professional
