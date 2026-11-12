---
title: "EdmBrowseForFolderFlag Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmBrowseForFolderFlag"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBrowseForFolderFlag.html"
---

# EdmBrowseForFolderFlag Enumeration

Browse options used in calls to [IEdmVault11::BrowseForFolder2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11~BrowseForFolder2.html).

## Syntax

### Visual Basic

```vb
Public Enum EdmBrowseForFolderFlag
   Inherits System.Enum
```

### C#

```csharp
public enum EdmBrowseForFolderFlag : System.Enum
```

### C++/CLI

```cpp
public enum class EdmBrowseForFolderFlag : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmBwsFld_ExclFileFolders | 1 = Do not permit browsing in file folders |
| EdmBwsFld_ExclItemFolders | 2 = Do not permit browsing in item folders |
| EdmBwsFld_None | 0 = Default behavior; permit browsing in both item and file folders |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
