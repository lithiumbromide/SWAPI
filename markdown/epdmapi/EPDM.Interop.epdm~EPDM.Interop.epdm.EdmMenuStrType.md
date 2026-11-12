---
title: "EdmMenuStrType Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmMenuStrType"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmMenuStrType.html"
---

# EdmMenuStrType Enumeration

Types of arguments sent to [IEdmMenu5::GetString](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMenu5~GetString.html) to specify which string to return.

## Syntax

### Visual Basic

```vb
Public Enum EdmMenuStrType
   Inherits System.Enum
```

### C#

```csharp
public enum EdmMenuStrType : System.Enum
```

### C++/CLI

```cpp
public enum class EdmMenuStrType : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| MenuStr_MenuStr | 1 = The menu item string |
| MenuStr_StatusBar | 2 = The help string to show in the status bar |
| MenuStr_Tooltip | 3 = The ToolTip help string to show when the mouse cursor is over the command's toolbar button |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
