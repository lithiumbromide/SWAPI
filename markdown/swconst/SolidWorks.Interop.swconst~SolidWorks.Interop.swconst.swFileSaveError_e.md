---
title: "swFileSaveError_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swFileSaveError_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFileSaveError_e.html"
---

# swFileSaveError_e Enumeration

File save errors. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swFileSaveError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swFileSaveError_e
```

### C#

```csharp
public enum swFileSaveError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swFileSaveError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swFileLockError | 16 or 0x10 |
| swFileNameContainsAtSign | 8 or 0x8 = File name cannot contain the at symbol (@) |
| swFileNameEmpty | 4 or 0x4 = File name cannot be empty |
| swFileSaveAsBadEDrawingsVersion | 1024 or 0x400 |
| swFileSaveAsDetachedDrawingsNotSupported | 16384 or 0x4000 = Detached drawing save as options is not supported |
| swFileSaveAsDoNotOverwrite | 128 or 0x80 = Do not overwrite an existing file |
| swFileSaveAsInvalidFileExtension | 256 or 0x100 = File name extension does not match the SOLIDWORKS document type |
| swFileSaveAsNameExceedsMaxPathLength | 2048 or 0x800 = File name cannot exceed 255 characters |
| swFileSaveAsNoSelection | 512 or 0x200 = Save the selected bodies in a part document. Valid option for IPartDoc::SaveToFile2 ; however, not a valid option for IModelDocExtension::SaveAs |
| swFileSaveAsNotSupported | 4096 or 0x1000 = Save As operation: is not supported was executed is such a way that the resulting file might not be complete, possibly because SOLIDWORKS is hidden; if the error persists after setting SOLIDWORKS to visible and re-attempting the Save As operation, contact SOLIDWORKS API support . |
| swFileSaveDoNotUpgradeError | 32768 or 0x8000 = Attempt to save a file too many versions behind with "Do Not Upgrade" enabled. |
| swFileSaveFormatNotAvailable | 32 or 0x20 = Save As file type is not valid |
| swFileSaveIncompatibleItemsError | 65536 or 0x10000 = Cannot save to previous version due to incompatible features. |
| swFileSaveRequiresSavingReferences | 8192 or 0x2000 = Saving an assembly with renamed components requires saving the references |
| swFileSaveWithRebuildError | Obsolete = See swFileSaveWarning_e |
| swGenericSaveError | 1 or 0x1 |
| swReadOnlySaveError | 2 or 0x2 |

## Remarks

Not all of these return codes are fatal errors. The return code is a bitmask of different conditions that can occur during the operation, some of which are fatal and some are informational or warnings.

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
