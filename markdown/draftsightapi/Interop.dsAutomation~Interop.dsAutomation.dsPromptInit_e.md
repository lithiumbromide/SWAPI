---
title: "dsPromptInit_e Enumeration"
project: ""
interface: "dsPromptInit_e"
member: ""
kind: "enum"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.dsPromptInit_e.html"
---

# dsPromptInit_e Enumeration

Types of input initializers. [Bitmask](Bitmasks.htm).

## Syntax

### Visual Basic

```vb
Public Enum dsPromptInit_e
   Inherits System.Enum
```

### C#

```csharp
public enum dsPromptInit_e : System.Enum
```

### JScript

```
public enum dsPromptInit_e extends System.Enum
```

### Managed Extensions for C++

```
__value public enum dsPromptInit_e : public System.Enum
```

### C++/CLI

```cpp
public enum class dsPromptInit_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| dsPromptInit_2D | 64 or 0x040: Z coordinate ignored |
| dsPromptInit_Button | 256 or 0x100: Keywords are displayed on the Options toolbar |
| dsPromptInit_Dash | 32 or 0x020: Not used |
| dsPromptInit_GetZ | 16 or 0x010: Return Z coordinate |
| dsPromptInit_NoButton | 512 or 0x200: Keywords are not displayed on the Options toolbar |
| dsPromptInit_NoDefault | 1024 or 0x400: Default value not used |
| dsPromptInit_NoLim | 8 or 0x008: Not used |
| dsPromptInit_NoNeg | 4 or 0x004: Negative input value not accepted |
| dsPromptInit_NoNull | 1 or 0x001: Null input not accepted |
| dsPromptInit_NoZero | 2 or 0x002: 0 not accepted |
| dsPromptInit_Other | 128 or 0x080: Any keyboard input accepted |
| dsPromptInit_UsePromptExplanation | 2048 or 0x800: Use text set by ICommandMessage::PromptExplanation for prompt |

## See Also

[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
