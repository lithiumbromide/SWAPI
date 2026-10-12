---
title: "EdmRefType Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmRefType"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRefType.html"
---

# EdmRefType Enumeration

Types of references to return from [IEdmRefItem::GetRefs](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRefItem~GetRefs.html).

## Syntax

### Visual Basic

```vb
Public Enum EdmRefType
   Inherits System.Enum
```

### C#

```csharp
public enum EdmRefType : System.Enum
```

### C++/CLI

```cpp
public enum class EdmRefType : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| Edmrt_Children | 1 = Return normal file references |
| Edmrt_SubParents | 2 = Return sub-parents, which are parent files displayed as blue children in the reference dialog box; drawing files for some CAD formats are displayed this way |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
