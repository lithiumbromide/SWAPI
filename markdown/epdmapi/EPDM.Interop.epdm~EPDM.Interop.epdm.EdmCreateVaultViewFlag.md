---
title: "EdmCreateVaultViewFlag Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmCreateVaultViewFlag"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCreateVaultViewFlag.html"
---

# EdmCreateVaultViewFlag Enumeration

Options for creating vault views used in calls to [IEdmVault11::CreateNewVaultView](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11~CreateNewVaultView.html).

## Syntax

### Visual Basic

```vb
Public Enum EdmCreateVaultViewFlag
   Inherits System.Enum
```

### C#

```csharp
public enum EdmCreateVaultViewFlag : System.Enum
```

### C++/CLI

```cpp
public enum class EdmCreateVaultViewFlag : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmCreateVaultView_Nothing | 0 = Default behavior; the view is created only for the currently logged in Windows user |
| EdmCreateVaultView_SharedView | 1 = The view is accessible to all Windows users on this computer |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
