---
title: "dsRichLineJustification_e Enumeration"
project: ""
interface: "dsRichLineJustification_e"
member: ""
kind: "enum"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.dsRichLineJustification_e.html"
---

# dsRichLineJustification_e Enumeration

Justification options for RichLines.

## Syntax

### Visual Basic

```vb
Public Enum dsRichLineJustification_e
   Inherits System.Enum
```

### C#

```csharp
public enum dsRichLineJustification_e : System.Enum
```

### JScript

```
public enum dsRichLineJustification_e extends System.Enum
```

### Managed Extensions for C++

```
__value public enum dsRichLineJustification_e : public System.Enum
```

### C++/CLI

```cpp
public enum class dsRichLineJustification_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| dsRichLineJustification_Bottom | 3 = Draws the RichLine segment above the specified points, with the line element with the most negative offset at the specified vertices |
| dsRichLineJustification_Top | 1 = Draws the RichLine segment below the specified points, with the line element with the most positive offset at the specified vertices |
| dsRichLineJustification_Zero | 2 = Defines a centerline through the segment specified points |

## See Also

[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
