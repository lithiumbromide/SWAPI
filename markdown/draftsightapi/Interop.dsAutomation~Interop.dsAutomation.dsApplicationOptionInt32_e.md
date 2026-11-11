---
title: "dsApplicationOptionInt32_e Enumeration"
project: ""
interface: "dsApplicationOptionInt32_e"
member: ""
kind: "enum"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.dsApplicationOptionInt32_e.html"
---

# dsApplicationOptionInt32_e Enumeration

Application options with Int32 values.

## Syntax

### Visual Basic

```vb
Public Enum dsApplicationOptionInt32_e
   Inherits System.Enum
```

### C#

```csharp
public enum dsApplicationOptionInt32_e : System.Enum
```

### JScript

```
public enum dsApplicationOptionInt32_e extends System.Enum
```

### Managed Extensions for C++

```
__value public enum dsApplicationOptionInt32_e : public System.Enum
```

### C++/CLI

```cpp
public enum class dsApplicationOptionInt32_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| dsApplicationOptionInt32_Count | Not used |
| dsApplicationOptionInt32_EnblClkDrg | 1 = Tools > Options > User Preferences > Mouse Options > Options > Enable Click and drag: 0 = Disabled 1 = Enabled |
| dsApplicationOptionInt32_EnblEntSelAuto | 2 = Tools > Options > User Preferences > Drafting Options > Entity Selection > Selection Settings > Automatic window/cross selection: 0 = Disabled 1 = Enabled |
| dsApplicationOptionInt32_SetCmdPrmtLvl | 3 = Sets the number of prompts to display in the command window; range 0-5, where 0 is the least restrictive and displays the most number of prompts (default) and 5 is the most restrictive and displays the least number of prompts |
| dsApplicationOptionInt32_SetCrdInptMode | 4 = Sets the number of prompts to display in the command window; range 0-5, where 0 is the least restrictive and displays the most number of prompts (default) and 5 is the most restrictive and displays the least number of prompts |
| dsApplicationOptionInt32_SetEntSelAdd | 5 = Set how entities are added to the selection set: 0 = Selected entities replace any previously selected entities in the selection set 1 = Selected entities added to current selection set |
| dsApplicationOptionInt32_SetSvTm | 6 = Tools > Options > System Options > Auto-save & Backup > Auto-save/backups > Save document every nn minutes |
| dsApplicationOptionInt32_Undefined | 0 = Undefined |

## Remarks

## See Also

[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
