---
title: "EdmRefItemType Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmRefItemType"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRefItemType.html"
---

# EdmRefItemType Enumeration

Items to return from [IEdmRefItemContainer::GetItems](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRefItemContainer~GetItems.html).

## Syntax

### Visual Basic

```vb
Public Enum EdmRefItemType
   Inherits System.Enum
```

### C#

```csharp
public enum EdmRefItemType : System.Enum
```

### C++/CLI

```cpp
public enum class EdmRefItemType : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| Edmrit_All | 2 = Return all items in the container (recursively) |
| Edmrit_Roots | 1 = Return only root items in the container |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
