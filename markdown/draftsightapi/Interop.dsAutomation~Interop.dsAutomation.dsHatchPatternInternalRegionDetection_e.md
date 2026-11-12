---
title: "dsHatchPatternInternalRegionDetection_e Enumeration"
project: ""
interface: "dsHatchPatternInternalRegionDetection_e"
member: ""
kind: "enum"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.dsHatchPatternInternalRegionDetection_e.html"
---

# dsHatchPatternInternalRegionDetection_e Enumeration

Internal region detection types for hatch patterns.

## Syntax

### Visual Basic

```vb
Public Enum dsHatchPatternInternalRegionDetection_e
   Inherits System.Enum
```

### C#

```csharp
public enum dsHatchPatternInternalRegionDetection_e : System.Enum
```

### JScript

```
public enum dsHatchPatternInternalRegionDetection_e extends System.Enum
```

### Managed Extensions for C++

```
__value public enum dsHatchPatternInternalRegionDetection_e : public System.Enum
```

### C++/CLI

```cpp
public enum class dsHatchPatternInternalRegionDetection_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| dsHatchPatternInternalRegionDetection_Ignore | 3 = Ignore the internal structure and hatch the entire area; hatch lines pass through text, block attributes, and 2D Solids |
| dsHatchPatternInternalRegionDetection_Normal | 1 = Create hatch patterns between alternate areas, starting with the outermost area |
| dsHatchPatternInternalRegionDetection_Outer | 2 = Create hatch patterns only in the outermost areas |

## See Also

[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
