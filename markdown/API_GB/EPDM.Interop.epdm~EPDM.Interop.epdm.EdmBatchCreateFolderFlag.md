---
title: "EdmBatchCreateFolderFlag Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmBatchCreateFolderFlag"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBatchCreateFolderFlag.html"
---

# EdmBatchCreateFolderFlag Enumeration

Flags used by [IEdmBatchAddFolders::Create](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAddFolders~Create.html).

## Syntax

### Visual Basic

```vb
Public Enum EdmBatchCreateFolderFlag
   Inherits System.Enum
```

### C#

```csharp
public enum EdmBatchCreateFolderFlag : System.Enum
```

### C++/CLI

```cpp
public enum class EdmBatchCreateFolderFlag : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| Ebcf_Nothing | 0 = Default behavior |
| Ebcf_RenameExistingRoots | 1 = If this flag is specified, and one of the folders added with IEdmBatchAddFolders::AddFolder already exists in the file vault, the folder is added and renamed to "Copy of Xxxx", where "Xxxx" is the original name. If this flag is not set, the original folder is returned. |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
