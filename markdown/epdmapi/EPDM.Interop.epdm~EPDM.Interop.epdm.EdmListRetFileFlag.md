---
title: "EdmListRetFileFlag Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmListRetFileFlag"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListRetFileFlag.html"
---

# EdmListRetFileFlag Enumeration

Flags returned in an [IEdmBatchListing](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing.html) column if you specify column type [EdmCol_EdmListRetFileFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmColType.html).

## Syntax

### Visual Basic

```vb
Public Enum EdmListRetFileFlag
   Inherits System.Enum
```

### C#

```csharp
public enum EdmListRetFileFlag : System.Enum
```

### C++/CLI

```cpp
public enum class EdmListRetFileFlag : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmLstRet_Drawing | 1 = It is a backwards drawing reference (i.e., it displayed as blue links in Enterprise's command dialog boxes) |
| EdmLstRet_InternalComponent | 2 = Internal SOLIDWORKS part, cut list, etc.; i.e., it is not a physical file |
| EdmLstRet_Nothing | 0 = It is an ordinary system file |
| EdmLstRet_ToolboxPart | 4 = This is a part file from the Toolbox library |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
[IEdmBatchListing2::CreateListEx Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing2~CreateListEx.html)
