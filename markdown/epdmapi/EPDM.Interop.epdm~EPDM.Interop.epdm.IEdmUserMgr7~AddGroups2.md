---
title: "AddGroups2 Method (IEdmUserMgr7)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUserMgr7"
member: "AddGroups2"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr7~AddGroups2.html"
---

# AddGroups2 Method (IEdmUserMgr7)

Adds the specified user groups to the vault.

## Syntax

### Visual Basic

```vb
Sub AddGroups2( _
   ByRef ppoGroupData() As EdmGroupData2 _
)
```

### C#

```csharp
void AddGroups2(
   out EdmGroupData2[] ppoGroupData
)
```

### C++/CLI

```cpp
void AddGroups2(
   [Out] array<EdmGroupData2>^ ppoGroupData
)
```

### Parameters

- `ppoGroupData`: Array of [EdmGroupData2](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupData2.html) structures; one structure for each group

## Examples

[Vault Utilities (VB.NET)](Vault_Utilities_Example_VBNET.htm)
[Vault Utilities (C#)](Vault_Utilities_Example_CSharp.htm)

## Remarks

This method supersedes [IEdmUserMgr6::AddGroups](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr6~AddGroups.html) by providing the ability to specify permissions for added groups.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmUserMgr7 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr7.html)
[IEdmUserMgr7 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr7_members.html)

## Availability

SOLIDWORKS PDM Professional 2010
