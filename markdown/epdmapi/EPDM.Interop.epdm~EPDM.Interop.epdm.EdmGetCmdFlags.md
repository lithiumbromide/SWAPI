---
title: "EdmGetCmdFlags Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmGetCmdFlags"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGetCmdFlags.html"
---

# EdmGetCmdFlags Enumeration

Options for retrieving files from the vault used in calls to

[IEdmBatchGet::CreateTree](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet~CreateTree.html)

.

[Bitmask](Bitmasks.htm)

.

## Syntax

### Visual Basic

```vb
Public Enum EdmGetCmdFlags
   Inherits System.Enum
```

### C#

```csharp
public enum EdmGetCmdFlags : System.Enum
```

### C++/CLI

```cpp
public enum class EdmGetCmdFlags : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| Egcf_AsBuilt | 1 = Use the same versions of referenced files that were used when the referencing file was checked in; if this bit is not set, the latest versions of referenced files are used |
| Egcf_AsBuiltNotDefault | 128 = Use the as-built versions when creating the tree |
| Egcf_ForPreview | 16 = Only retrieve referenced files that are needed by the preview when retrieving the referencing file; skip caching referenced files |
| Egcf_ForViewer | 8192 = Only retrieve referenced files that are needed by the viewer when retrieving the referencing file; skip caching referenced files |
| Egcf_GetLatestRevision | 65536 = Only retrieve latest revision/version |
| Egcf_IncludeAutoCacheFiles | 2048 = Selects the Check Out dialog box Get checkbox for the latest version if the referenced file is not in the local cache |
| Egcf_Lock | 2 = Check out the files instead of just retrieving them |
| Egcf_LockNoLclCopyFiles | 1024 = Locks the local referenced files if a local cache is not present |
| Egcf_LockReferencedFilesToo | 64 = Check out files referenced by the checked-out file |
| Egcf_Nothing | 0 = No options |
| Egcf_RefreshFileListing | 32 = Refresh file listing in File Explorer after files have been checked out |
| Egcf_RollbackTree | 4096 = Provide the ability to roll back files in the dialog |
| Egcf_SingleFileRollback | 16384 = Roll back one file |
| Egcf_SkipExisting | 8 = Do not retrieve files that already exist in the local cache |
| Egcf_SkipLockRefFiles | 512 = Skips checking of lock file references |
| Egcf_SkipOpenFileChecks | 256 = Skips checking whether the file is open in another application |
| Egcf_SkipUnlockedWritable | 4 = Do not retrieve files that are writable and not checked out |
| Egcf_XrefsOpenCheck | 32768 = Check whether cross-reference files are open in another application |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
