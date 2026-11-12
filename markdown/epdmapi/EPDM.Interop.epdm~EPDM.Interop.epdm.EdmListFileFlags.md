---
title: "EdmListFileFlags Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmListFileFlags"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFileFlags.html"
---

# EdmListFileFlags Enumeration

Flags passed to [IEdmBatchListing::AddFile](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing~AddFile.html). [Bitmask](Bitmasks.htm).

## Syntax

### Visual Basic

```vb
Public Enum EdmListFileFlags
   Inherits System.Enum
```

### C#

```csharp
public enum EdmListFileFlags : System.Enum
```

### C++/CLI

```cpp
public enum class EdmListFileFlags : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmList_IsCutListItem | 2 = The file is a cut list item in another file |
| EdmList_IsInternalComponent | 4 = The file is a virtual component in another file |
| EdmList_MayNotReadFile | 1 = The file must not be accessed, even if it is checked out and modified |
| EdmList_Nothing | 0 = Default behavior |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
