---
title: "dsCommandOptionInt8_e Enumeration"
project: ""
interface: "dsCommandOptionInt8_e"
member: ""
kind: "enum"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.dsCommandOptionInt8_e.html"
---

# dsCommandOptionInt8_e Enumeration

Command options with Int8 values.

## Syntax

### Visual Basic

```vb
Public Enum dsCommandOptionInt8_e
   Inherits System.Enum
```

### C#

```csharp
public enum dsCommandOptionInt8_e : System.Enum
```

### JScript

```
public enum dsCommandOptionInt8_e extends System.Enum
```

### Managed Extensions for C++

```
__value public enum dsCommandOptionInt8_e : public System.Enum
```

### C++/CLI

```cpp
public enum class dsCommandOptionInt8_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| dsCommandOptionInt8_Count | Not used |
| dsCommandOptionInt8_SetDlDmZroDsp | 1 = Tools > Options > Drafting Styles > Dimension > Dual Dimension > Zeroes display: 0 = Include leading zeroes, include trailing zeroes, Hide if 0' , and Hide if 0" 1 = Include leading zeroes, include trailing zeroes, include if 0', and include if 0" 2 = Include leading zeroes, include trailing zeroes, include if 0', and Hide if 0" 3 = Include leading zeroes, include trailing zeroes, Hide if 0' , and include if 0" 4 = Hide leading zeroes , include trailing zeroes, Hide if 0' , and Hide if 0" 5 = Hide leading zeroes , include trailing zeroes, include if 0', and include if 0" 6 = Hide leading zeroes , include trailing zeroes, include if 0', and Hide if 0" 7 = Hide leading zeroes , include trailing zeroes, Hide if 0' , and include if 0" 8 = Include leading zeroes, Hide trailing zeroes , Hide if 0' , and Hide if 0" 9 = Include leading zeroes, Hide trailing zeroes , include if 0', and include if 0" 10 = Include leading zeroes, Hide trailing zeroes , include if 0', and Hide if 0" 11 = Include leading zeroes, Hide trailing zeroes , Hide if 0' , and include if 0" 12 = Hide leading zeroes , Hide trailing zeroes , Hide if 0' , and Hide if 0" 13 = Hide leading zeroes , Hide trailing zeroes , include if 0', and include if 0" 14 = Hide leading zeroes , Hide trailing zeroes , include if 0', and Hide if 0" 15 = Hide leading zeroes , Hide trailing zeroes , Hide if 0' , and include if 0" |
| dsCommandOptionInt8_SetDmTolVJst | 2 = Tools > Options > Drafting Styles > Dimension > Tolerance > Tolerance settings > Vertical text justification: 0 = Bottom 1 = Middle 2 = Top |
| dsCommandOptionInt8_SetTDmDZroDsp | 3 = Tools > Options > Drafting Styles > Dimension > Tolerance > Tolerance settings > Dual dimension > Zeroes display: 0 = Include leading zeroes, include trailing zeroes, Hide if 0' , and Hide if 0" 1 = Include leading zeroes, include trailing zeroes, include if 0', and include if 0" 2 = Include leading zeroes, include trailing zeroes, include if 0', and Hide if 0" 3 = Include leading zeroes, include trailing zeroes, Hide if 0' , and include if 0" 4 = Hide leading zeroes , include trailing zeroes, Hide if 0' , and Hide if 0" 5 = Hide leading zeroes , include trailing zeroes, include if 0', and include if 0" 6 = Hide leading zeroes , include trailing zeroes, include if 0', and Hide if 0" 7 = Hide leading zeroes , include trailing zeroes, Hide if 0' , and include if 0" 8 = Include leading zeroes, Hide trailing zeroes , Hide if 0' , and Hide if 0" 9 = Include leading zeroes, Hide trailing zeroes , include if 0', and include if 0" 10 = Include leading zeroes, Hide trailing zeroes , include if 0', and Hide if 0" 11 = Include leading zeroes, Hide trailing zeroes , Hide if 0' , and include if 0" 12 = Hide leading zeroes , Hide trailing zeroes , Hide if 0' , and Hide if 0" 13 = Hide leading zeroes , Hide trailing zeroes , include if 0', and include if 0" 14 = Hide leading zeroes , Hide trailing zeroes , include if 0', and Hide if 0" 15 = Hide leading zeroes , Hide trailing zeroes , Hide if 0' , and include if 0" |
| dsCommandOptionInt8_SetTDmZroDsp | 4 = Tools > Options > Drafting Styles > Dimension > Tolerance > Tolerance settings > Zeroes display: 0 = Include leading zeroes, include trailing zeroes, Hide if 0' , and Hide if 0" 1 = Include leading zeroes, include trailing zeroes, include if 0', and include if 0" 2 = Include leading zeroes, include trailing zeroes, include if 0', and Hide if 0" 3 = Include leading zeroes, include trailing zeroes, Hide if 0' , and include if 0" 4 = Hide leading zeroes , include trailing zeroes, Hide if 0' , and Hide if 0" 5 = Hide leading zeroes , include trailing zeroes, include if 0', and include if 0" 6 = Hide leading zeroes , include trailing zeroes, include if 0', and Hide if 0" 7 = Hide leading zeroes , include trailing zeroes, Hide if 0' , and include if 0" 8 = Include leading zeroes, Hide trailing zeroes , Hide if 0' , and Hide if 0" 9 = Include leading zeroes, Hide trailing zeroes , include if 0', and include if 0" 10 = Include leading zeroes, Hide trailing zeroes , include if 0', and Hide if 0" 11 = Include leading zeroes, Hide trailing zeroes , Hide if 0' , and include if 0" 12 = Hide leading zeroes , Hide trailing zeroes , Hide if 0' , and Hide if 0" 13 = Hide leading zeroes , Hide trailing zeroes , include if 0', and include if 0" 14 = Hide leading zeroes , Hide trailing zeroes , include if 0', and Hide if 0" 15 = Hide leading zeroes , Hide trailing zeroes , Hide if 0' , and include if 0" |
| dsCommandOptionInt8_Undefined | 0 = Undefined |

## Remarks

The string **Lgcy** in a command option indicates that setting the command option has no effect in DraftSight; however, the value is stored in the DWG file.

In most instances, user-interface command option equivalents are the strings following **dsCommandOptionInt8_**; for example, typing **SetDlDmZroDsp** in the command prompt is equivalent to using **dsCommandOptionInt8_SetDlDmZroDsp** in code.

## See Also

[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IDocument::GetCommandOptionInt8 Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetCommandOptionInt8.html)
[IDocument::SetCommandOptionInt8 Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~SetCommandOptionInt8.html)
