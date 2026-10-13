---
title: "EdmAddFlag Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmAddFlag"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddFlag.html"
---

# EdmAddFlag Enumeration

Options for adding a file to a folder to the vault, copying a file or folder within the vault, or copying/moving a tree of files and folders. [Bitmask](Bitmasks.htm).

## Syntax

### Visual Basic

```vb
Public Enum EdmAddFlag
   Inherits System.Enum
```

### C#

```csharp
public enum EdmAddFlag : System.Enum
```

### C++/CLI

```cpp
public enum class EdmAddFlag : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmAdd_DeleteSource | 64 = Delete the source file once it has been added to the vault |
| EdmAdd_DoNotCopy | 512 = Do not physically copy the file during the add operations because the file has already been copied |
| EdmAdd_DontAddCorrupt | 2 = Refuse to add corrupt files; IEdmFolder5::AddFile returns the error code E_EDM_INVALID_FILE |
| EdmAdd_ForceGenerateSerialNumbers | 128 = Force regeneration of serial numbers when values already exist; if this flag is not set, SOLIDWORKS PDM Professional will only generate values that are missing in the file |
| EdmAdd_GetInterface | 256 = Return the file interface; only works with IEdmBatchAdd |
| EdmAdd_KeepExistingSerialNumbers | 4 = Do not replace existing serial numbers with new ones; SOLIDWORKS PDM Professional still creates serial numbers for empty fields; if this flag is not set, SOLIDWORKS PDM Professional writes over existing serial numbers with new ones |
| EdmAdd_Refresh | 1 = Make all file listings in File Explorer and Open/Save As dialog boxes refresh so that the new file is displayed |
| EdmAdd_Simple | 0 = Add the file |
| EdmAdd_UniqueVarClearDuplicate | 16 = Clear duplicated unique constrained variables instead of failing |
| EdmAdd_UniqueVarDelayCheck | 32 = Delay the unique variable check until the next check-in |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
