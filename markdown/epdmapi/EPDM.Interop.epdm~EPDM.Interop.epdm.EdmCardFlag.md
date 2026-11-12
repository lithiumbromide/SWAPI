---
title: "EdmCardFlag Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmCardFlag"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCardFlag.html"
---

# EdmCardFlag Enumeration

Options for file data card behavior used in [EdmCmdData](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdData.html); use these flags to tell SOLIDWORKS PDM Professional what to do when [IEdmAddIn5::OnCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~OnCmd.html) returns.

## Syntax

### Visual Basic

```vb
Public Enum EdmCardFlag
   Inherits System.Enum
```

### C#

```csharp
public enum EdmCardFlag : System.Enum
```

### C++/CLI

```cpp
public enum class EdmCardFlag : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmCF_CloseDlgCancel | 2 = Close dialog and do not save changes |
| EdmCF_CloseDlgOK | 1 = Close dialog and save changes |
| EdmCF_Nothing | 0 = Do nothing |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
