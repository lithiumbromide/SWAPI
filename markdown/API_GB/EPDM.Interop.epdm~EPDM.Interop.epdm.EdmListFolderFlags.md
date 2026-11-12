---
title: "EdmListFolderFlags Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmListFolderFlags"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFolderFlags.html"
---

# EdmListFolderFlags Enumeration

Flags used in calls to [IEdmBatchListing::AddFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing~AddFolder.html) to tell how to add the folder to the list.

## Syntax

### Visual Basic

```vb
Public Enum EdmListFolderFlags
   Inherits System.Enum
```

### C#

```csharp
public enum EdmListFolderFlags : System.Enum
```

### C++/CLI

```cpp
public enum class EdmListFolderFlags : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmListFolder_Nothing | 0 = None of the other values |
| EdmListFolder_Recursive | 1 = Add the files inside the folder instead of adding the folder itself to the list; the files in any subfolders are added recursively |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
