---
title: "EdmFolderHistoryFlag Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmFolderHistoryFlag"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmFolderHistoryFlag.html"
---

# EdmFolderHistoryFlag Enumeration

Options for adding folders when calling [IEdmHistory::AddFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory~AddFolder.html). [Bitmask](Bitmasks.htm).

## Syntax

### Visual Basic

```vb
Public Enum EdmFolderHistoryFlag
   Inherits System.Enum
```

### C#

```csharp
public enum EdmFolderHistoryFlag : System.Enum
```

### C++/CLI

```cpp
public enum class EdmFolderHistoryFlag : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| Edmfhf_IncludeFiles | 2 = Add all files in the folder and subfolders |
| Edmfhf_Nothing | 0 = Add the folder |
| Edmfhf_Recursive | 1 = Add subfolders |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
