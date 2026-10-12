---
title: "EdmUnlockBuildTreeFlags Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmUnlockBuildTreeFlags"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUnlockBuildTreeFlags.html"
---

# EdmUnlockBuildTreeFlags Enumeration

Flags used to control the creation of the check-in file tree created by the [IEdmBatchUnlock](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock.html) interface. [Bitmask](Bitmasks.htm).

## Syntax

### Visual Basic

```vb
Public Enum EdmUnlockBuildTreeFlags
   Inherits System.Enum
```

### C#

```csharp
public enum EdmUnlockBuildTreeFlags : System.Enum
```

### C++/CLI

```cpp
public enum class EdmUnlockBuildTreeFlags : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| Eubtf_ForceUnlock | 32768 = Unlock the file even if it is not modified; use only in combination with Eubtf_MayUnlock |
| Eubtf_IgnoreReferences | 65536 = Ignore the child references at check-in; unlock root items only |
| Eubtf_MayUndoLock | 2 = Support undo file check-out |
| Eubtf_MayUnlock | 1 = Support file check-in |
| Eubtf_MayUnlockWithLatest | 4096 = Check in latest version instead of cached version; use only in combination with Eubtf_MayUnlock |
| Eubtf_MayUnlockWithoutOverwrite | 16384 = Check in without version overwrite; use only in combination with Eubtf_MayUnlock |
| Eubtf_NoCallbackDlgErrors | 256 = Do not pass dialog box errors to the callback |
| Eubtf_NoRemoveLocalCopy | 128 = Do not display the Remove Local Copy column in the dialog box |
| Eubtf_Nothing | 0 = None of the other flags |
| Eubtf_RefreshFileListing | 32 = Refresh the file listing in the File Explorer when the operation completes |
| Eubtf_SearchForDrawings | 512 = Include drawings as sub-parent nodes |
| Eubtf_ShowCloseAfterCheckinOption | 2048 = Display the Reload or Close Files after Check In dropdown on the Check In or Undo Check Out dialog box toolbar; this option permits the user to choose whether to close the files in SOLIDWORKS after the check-in operation has succeeded or reload them in SOLIDWORKS |
| Eubtf_ShowMultipleWarnings | 8192 = Display Multiple Warnings link in warning column of dialog |
| Eubtf_SkipOpenFileChecks | 1024 = Do not check whether files are open in another application |
| Eubtf_UndoLockDefault | 4 = Make undo check-out the default operation |
| Eubtf_Warn_UndoLockModifiedInCb | 16 = Warn the caller of undo check-out of modified files via the callback interface |
| Eubtf_Warn_UndoLockModifiedInDlg | 8 = Show warning icon in the Undo Check Out dialog box for modified files marked for undo check-out |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
