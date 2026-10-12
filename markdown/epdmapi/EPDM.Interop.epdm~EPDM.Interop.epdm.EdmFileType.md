---
title: "EdmFileType Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmFileType"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmFileType.html"
---

# EdmFileType Enumeration

Types of SOLIDWORKS PDM Professional file; used in calls to [IEdmFile8::FileType](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile8~FileType.html).

## Syntax

### Visual Basic

```vb
Public Enum EdmFileType
   Inherits System.Enum
```

### C#

```csharp
public enum EdmFileType : System.Enum
```

### C++/CLI

```cpp
public enum class EdmFileType : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| Edmft_CutListItem | 5 = SOLIDWORKS cut list item |
| Edmft_InternalComponent | 2 = A SOLIDWORKS internal part or assembly |
| Edmft_Item | 4 = IEdmItem |
| Edmft_Normal | 1 = File system file |
| Edmft_Nothing | 0 = Error |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
