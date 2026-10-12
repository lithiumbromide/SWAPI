---
title: "EdmUnlockFlag Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmUnlockFlag"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUnlockFlag.html"
---

# EdmUnlockFlag Enumeration

Flags used in [IEdmFile5::UnlockFile](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~UnlockFile.html) to control the behavior of the check-in operation. [Bitmask](Bitmasks.htm).

## Syntax

### Visual Basic

```vb
Public Enum EdmUnlockFlag
   Inherits System.Enum
```

### C#

```csharp
public enum EdmUnlockFlag : System.Enum
```

### C++/CLI

```cpp
public enum class EdmUnlockFlag : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmUnlock_FailOnBlockingWarnings | 512 = Fail only for blocking warnings |
| EdmUnlock_FailOnRegenerationNeed | 16 = Fail if the file needs to be regenerated in the CAD program NOTE : Only files resaved in SOLIDWORKS 2009 or later can trigger this flag |
| EdmUnlock_ForceUnlock | 256 = Unlock the file even if it is not modified |
| EdmUnlock_IgnoreCorruptFile | 4 = Ignore files with file formats unrecognized by SOLIDWORKS PDM Professional; without this flag, SOLIDWORKS PDM Professional returns E_EDM_INVALID_FILE if it encounters a corrupt file or a file containing a newer format than SOLIDWORKS PDM Professional can handle |
| EdmUnlock_IgnoreReferences | 128 = Silently unlock parent files without their references |
| EdmUnlock_IgnoreRefsNotLockedByCaller | 32 = Ignore references not locked by caller |
| EdmUnlock_IgnoreRefsOutsideVault | 8 = Ignore references to files outside the vault |
| EdmUnlock_KeepLocked | 1 = Keep the file checked out after creating the new version in the archive |
| EdmUnlock_OverwriteLatestVersion | 64 = Do not create a new version; overwrite the last version of the file with new changes |
| EdmUnlock_RemoveLocalCopy | 2 = Remove the local copy of the file from the hard disk after the file has been checked in |
| EdmUnlock_Simple | 0 = Check in the file using default behavior |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
