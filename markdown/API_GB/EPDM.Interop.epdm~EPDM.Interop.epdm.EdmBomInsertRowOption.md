---
title: "EdmBomInsertRowOption Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmBomInsertRowOption"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomInsertRowOption.html"
---

# EdmBomInsertRowOption Enumeration

Bill of Materials row insertion options for [IEdmBomView2::InsertRow](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomView2~InsertRow.html).

## Syntax

### Visual Basic

```vb
Public Enum EdmBomInsertRowOption
   Inherits System.Enum
```

### C#

```csharp
public enum EdmBomInsertRowOption : System.Enum
```

### C++/CLI

```cpp
public enum class EdmBomInsertRowOption : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmBomInsertRowOption_AboveRow | 0 = Insert the new row above the specified row |
| EdmBomInsertRowOption_AsChild | 2 = Insert the new row as a child of the specified row |
| EdmBomInsertRowOption_BelowRow | 1 = Insert the new row below the specified row |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
