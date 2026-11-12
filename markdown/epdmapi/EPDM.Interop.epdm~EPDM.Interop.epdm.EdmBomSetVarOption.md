---
title: "EdmBomSetVarOption Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmBomSetVarOption"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomSetVarOption.html"
---

# EdmBomSetVarOption Enumeration

Types of value passed in [IEdmBomCell::SetVar](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomCell~SetVar.html).

## Syntax

### Visual Basic

```vb
Public Enum EdmBomSetVarOption
   Inherits System.Enum
```

### C#

```csharp
public enum EdmBomSetVarOption : System.Enum
```

### C++/CLI

```cpp
public enum class EdmBomSetVarOption : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmBomSetVarOption_Both | 2 = Both computed and edited value |
| EdmBomSetVarOption_Computed | 0 = Computed value |
| EdmBomSetVarOption_Edited | 1 = Edited value |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
