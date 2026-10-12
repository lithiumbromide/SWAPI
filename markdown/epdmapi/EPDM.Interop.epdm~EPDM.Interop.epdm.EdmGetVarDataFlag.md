---
title: "EdmGetVarDataFlag Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmGetVarDataFlag"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGetVarDataFlag.html"
---

# EdmGetVarDataFlag Enumeration

Options specified in [EdmGetVarData](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGetVarData.html) to describe a file. [Bitmask](Bitmasks.htm).

## Syntax

### Visual Basic

```vb
Public Enum EdmGetVarDataFlag
   Inherits System.Enum
```

### C#

```csharp
public enum EdmGetVarDataFlag : System.Enum
```

### C++/CLI

```cpp
public enum class EdmGetVarDataFlag : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| Edmgvdf_MayUpdate | 1 = The file's card may be updated by the logged-in user |
| Edmgvdf_Nothing | 0 = No updates |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
