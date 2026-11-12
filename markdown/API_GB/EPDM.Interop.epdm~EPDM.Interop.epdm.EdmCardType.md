---
title: "EdmCardType Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmCardType"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCardType.html"
---

# EdmCardType Enumeration

Types of data card used in calls to [IEdmVault6::GetCardID](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault6~GetCardID.html).

## Syntax

### Visual Basic

```vb
Public Enum EdmCardType
   Inherits System.Enum
```

### C#

```csharp
public enum EdmCardType : System.Enum
```

### C++/CLI

```cpp
public enum class EdmCardType : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmCard_File | 0 = File data card |
| EdmCard_Folder | 1 = Folder data card |
| EdmCard_Search | 3 = Search card used by the search tool |
| EdmCard_Template | 2 = Template card used by the template manager |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
