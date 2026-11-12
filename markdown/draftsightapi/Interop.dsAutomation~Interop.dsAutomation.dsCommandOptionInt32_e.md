---
title: "dsCommandOptionInt32_e Enumeration"
project: ""
interface: "dsCommandOptionInt32_e"
member: ""
kind: "enum"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.dsCommandOptionInt32_e.html"
---

# dsCommandOptionInt32_e Enumeration

Obsolete. Superseded by [dsApplicationOptionInt32_e](Interop.dsAutomation~Interop.dsAutomation.dsApplicationOptionInt32_e.html).

## Syntax

### Visual Basic

```vb
Public Enum dsCommandOptionInt32_e
   Inherits System.Enum
```

### C#

```csharp
public enum dsCommandOptionInt32_e : System.Enum
```

### JScript

```
public enum dsCommandOptionInt32_e extends System.Enum
```

### Managed Extensions for C++

```
__value public enum dsCommandOptionInt32_e : public System.Enum
```

### C++/CLI

```cpp
public enum class dsCommandOptionInt32_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| dsCommandOptionInt32_Count | Obsolete. Superseded by dsApplicationOptionInt32_e . |
| dsCommandOptionInt32_EnblClkDrg | Obsolete. Superseded by dsApplicationOptionInt32_e . |
| dsCommandOptionInt32_EnblEntSelAuto | Obsolete. Superseded by dsApplicationOptionInt32_e . |
| dsCommandOptionInt32_SetCmdPrmtLvl | Obsolete. Superseded by dsApplicationOptionInt32_e . |
| dsCommandOptionInt32_SetCrdInptMode | Obsolete. Superseded by dsApplicationOptionInt32_e . |
| dsCommandOptionInt32_SetEntSelAdd | Obsolete. Superseded by dsApplicationOptionInt32_e . |
| dsCommandOptionInt32_SetSvTm | Obsolete. Superseded by dsApplicationOptionInt32_e . |
| dsCommandOptionInt32_Undefined | Obsolete. Superseded by dsApplicationOptionInt32_e . |

## Remarks

The string **Lgcy** in a command option indicates that setting the command option has no effect in DraftSight; however, the value is stored in the DWG file.

In most instances, user-interface command option equivalents are the strings following **dsCommandOptionInt32_**; for example, typing **EnblClkDrg** in the command prompt is equivalent to using **dsCommandOptionInt32_EnblClkDrg** in code.

## See Also

[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IDocument::GetCommandOptionInt32 Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetCommandOptionInt32.html)
[IDocument::SetCommandOptionInt32 Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~SetCommandOptionInt32.html)
