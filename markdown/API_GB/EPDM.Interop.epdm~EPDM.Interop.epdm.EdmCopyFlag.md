---
title: "EdmCopyFlag Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmCopyFlag"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCopyFlag.html"
---

# EdmCopyFlag Enumeration

Options for copying files when making calls to [IEdmFolder5::CopyFile](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~CopyFile.html). [Bitmask](Bitmasks.htm).

## Syntax

### Visual Basic

```vb
Public Enum EdmCopyFlag
   Inherits System.Enum
```

### C#

```csharp
public enum EdmCopyFlag : System.Enum
```

### C++/CLI

```cpp
public enum class EdmCopyFlag : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmCpy_NewSerialNumbers | 1 = Generate missing serial numbers; regenerate existing serial numbers |
| EdmCpy_Simple | 0 = Copy the file |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
