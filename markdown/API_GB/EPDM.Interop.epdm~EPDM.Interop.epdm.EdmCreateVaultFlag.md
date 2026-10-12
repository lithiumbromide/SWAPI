---
title: "EdmCreateVaultFlag Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmCreateVaultFlag"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCreateVaultFlag.html"
---

# EdmCreateVaultFlag Enumeration

Options for creating new vaults used in calls to [IEdmVault11::CreateNewVault](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11~CreateNewVault.html).

## Syntax

### Visual Basic

```vb
Public Enum EdmCreateVaultFlag
   Inherits System.Enum
```

### C#

```csharp
public enum EdmCreateVaultFlag : System.Enum
```

### C++/CLI

```cpp
public enum class EdmCreateVaultFlag : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmCreateVault_Nothing | 0 = Default behavior; specify a password for the Admin user |
| EdmCreateVault_UseDefaultAdminPassword | 1 = Use the default Admin password that is stored on the archive server |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
