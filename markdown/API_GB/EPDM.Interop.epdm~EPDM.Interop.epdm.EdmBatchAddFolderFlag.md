---
title: "EdmBatchAddFolderFlag Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmBatchAddFolderFlag"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBatchAddFolderFlag.html"
---

# EdmBatchAddFolderFlag Enumeration

Flags used by [IEdmBatchAddFolders::AddFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAddFolders~AddFolder.html) to specify the behavior of the added folder.

## Syntax

### Visual Basic

```vb
Public Enum EdmBatchAddFolderFlag
   Inherits System.Enum
```

### C#

```csharp
public enum EdmBatchAddFolderFlag : System.Enum
```

### C++/CLI

```cpp
public enum class EdmBatchAddFolderFlag : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| Ebaff_DisableRefresh | 2 = Disable the automatic refresh of folder listings in File Explorer |
| Ebaff_GetInterface | 1 = Return IEdmFolder6 for the folder in the EdmFolderInfo structure that is returned by IEdmBatchAddFolders::Create |
| Ebaff_Nothing | 0 = Standard behavior |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
