---
title: "EdmClientType Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmClientType"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmClientType.html"
---

# EdmClientType Enumeration

Types of SOLIDWORKS PDM Professional client; used in calls to [IEdmVault8::ClientType](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault8~ClientType.html).

## Syntax

### Visual Basic

```vb
Public Enum EdmClientType
   Inherits System.Enum
```

### C#

```csharp
public enum EdmClientType : System.Enum
```

### C++/CLI

```cpp
public enum class EdmClientType : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| Edmct_ConisioLight | 2 = SOLIDWORKS PDM Professional Viewer |
| Edmct_ConisioLT | 4 = LT (Version 5.3 and older) |
| Edmct_ConisioProf | 0 = SOLIDWORKS PDM Professional Editor |
| Edmct_ConisioStd | 1 = SOLIDWORKS PDM Professional Contributor |
| Edmct_ConisioWeb | 3 = SOLIDWORKS PDM Professional Web |
| Edmct_None | -1 = No SOLIDWORKS PDM Professional client is installed |
| Edmct_Reserved | Do not use |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
