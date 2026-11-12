---
title: "EdmFolderInfoFlag Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmFolderInfoFlag"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmFolderInfoFlag.html"
---

# EdmFolderInfoFlag Enumeration

Return codes in [EdmFolderInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmFolderInfo.html) which is returned from [IEdmBatchAddFolders::Create](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAddFolders~Create.html).

## Syntax

### Visual Basic

```vb
Public Enum EdmFolderInfoFlag
   Inherits System.Enum
```

### C#

```csharp
public enum EdmFolderInfoFlag : System.Enum
```

### C++/CLI

```cpp
public enum class EdmFolderInfoFlag : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| Eff_AlreadyExisted | 1 = Folder already existed in the vault; EdmFolderInfo structure contains information about the existing folder |
| Eff_Nothing | 0 = Folder was successfully added |
| Eff_PermissionDenied | 2 = Folder could not be added due to lack of permissions |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
