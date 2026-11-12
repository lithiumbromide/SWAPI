---
title: "EdmResolveReason Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmResolveReason"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmResolveReason.html"
---

# EdmResolveReason Enumeration

Types of flags, which contain the reason for the function call, to pass to your implementation of [IEdmCallback6::Resolve](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback6~Resolve.html). [Bitmask](Bitmasks.htm).

## Syntax

### Visual Basic

```vb
Public Enum EdmResolveReason
   Inherits System.Enum
```

### C#

```csharp
public enum EdmResolveReason : System.Enum
```

### C++/CLI

```cpp
public enum class EdmResolveReason : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| Edmrr_DstExists | 1 = Destination file name is already used in the folder |
| Edmrr_DstExistsGlobal | 64 = Destination file name is already used in the vault |
| Edmrr_FolderExists | 32 = Folder with the same name exists |
| Edmrr_LockedByYouHere | 2 = Destination (existing) file is checked out by the logged-in user |
| Edmrr_SameAsSource | 4 = Source file and the destination file are the same |
| Edmrr_SerialNumber | 16 = Source file contains serial number values |
| Edmrr_UniqueValues | 8 = Source file contains unique, constrained, variable values that must be cleared on copy |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
