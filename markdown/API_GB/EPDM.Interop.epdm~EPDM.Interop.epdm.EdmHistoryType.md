---
title: "EdmHistoryType Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmHistoryType"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryType.html"
---

# EdmHistoryType Enumeration

Types of history record; used by the [IEdmHistory](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory.html) interface. [Bitmask](Bitmasks.htm).

## Syntax

### Visual Basic

```vb
Public Enum EdmHistoryType
   Inherits System.Enum
```

### C#

```csharp
public enum EdmHistoryType : System.Enum
```

### C++/CLI

```cpp
public enum class EdmHistoryType : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| Edmhist_ColdStoreRestore | 262144 = A file was restored from cold storage |
| Edmhist_FileBranch | 4194304 |
| Edmhist_FileBranchMerge | 8388608 |
| Edmhist_FileColdStore | 1024 = A file was moved to the cold storage |
| Edmhist_FileDelete | 16 = A file was deleted to the bit bucket |
| Edmhist_FileLabel | 128 = A label was applied to a file |
| Edmhist_FileMove | 4 = A file was moved |
| Edmhist_FileParallelState | 61708864 |
| Edmhist_FilePendingState | 33554432 |
| Edmhist_FileRename | 2 = A file was renamed |
| Edmhist_FileRevision | 512 = A revision was set on the file |
| Edmhist_FileRollback | 8 = A file was rolled back |
| Edmhist_FileShare | 1 = A file was shared |
| Edmhist_FileState | 256 = The file’s workflow state was changed |
| Edmhist_FileUndelete | 32 = A file was recovered from the bit bucket |
| Edmhist_FileUndoLock | 2097152 |
| Edmhist_FileVerFreeVar | 524288 = File version-free variables were updated |
| Edmhist_FileVersion | 64 = A file was checked in, producing a new version |
| Edmhist_FileVersionOverwrite | 16777216 |
| Edmhist_FolderCardData | 131072 = A folder’s properties were edited |
| Edmhist_FolderCreate | 8192 = A folder was created |
| Edmhist_FolderDelete | 2048 = A folder was deleted to the bit bucket |
| Edmhist_FolderLabel | 65536 = A label was applied to a folder |
| Edmhist_FolderMove | 32768 = A folder was moved |
| Edmhist_FolderRename | 16384 = A folder was renamed |
| Edmhist_FolderUndelete | 4096 = A folder was recovered from the bit bucket |
| Edmhist_FolderVerFreeVar | 1048576 = Folder version-free variables were updated |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
