---
title: "EdmMBoxResult Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmMBoxResult"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmMBoxResult.html"
---

# EdmMBoxResult Enumeration

Types of clicked button returned by [IEdmVault5::MsgBox](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~MsgBox.html).

## Syntax

### Visual Basic

```vb
Public Enum EdmMBoxResult
   Inherits System.Enum
```

### C#

```csharp
public enum EdmMBoxResult : System.Enum
```

### C++/CLI

```cpp
public enum class EdmMBoxResult : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmMbr_Abort | 3 = User clicked Abort |
| EdmMbr_Cancel | 2 = User clicked Cancel or Close in the caption |
| EdmMbr_Ignore | 5 = User clicked Ignore |
| EdmMbr_No | 7 = User clicked No |
| EdmMbr_NoAll | 10 = User clicked No to All |
| EdmMbr_OK | 1 = User clicked OK |
| EdmMbr_OkAll | 8 = User clicked OK to All |
| EdmMbr_Retry | 4 = User clicked Retry |
| EdmMbr_Yes | 6 = User clicked Yes |
| EdmMbr_YesAll | 9 = User clicked Yes to All |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
