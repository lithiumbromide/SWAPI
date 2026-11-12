---
title: "swToolBoxPartType_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swToolBoxPartType_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swToolBoxPartType_e.html"
---

# swToolBoxPartType_e Enumeration

Toolbox part types. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swToolBoxPartType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swToolBoxPartType_e
```

### C#

```csharp
public enum swToolBoxPartType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swToolBoxPartType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swNotAToolboxPart | 0x0 = Not a Toolbox part |
| swToolboxCopiedPart | 0x2 = Copied part |
| swToolboxStandardPart | 0x1 = Standard part |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
