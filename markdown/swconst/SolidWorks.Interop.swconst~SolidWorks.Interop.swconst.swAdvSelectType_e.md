---
title: "swAdvSelectType_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swAdvSelectType_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAdvSelectType_e.html"
---

# swAdvSelectType_e Enumeration

Conditions of criteria for advanced component selection list. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swAdvSelectType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swAdvSelectType_e
```

### C#

```csharp
public enum swAdvSelectType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swAdvSelectType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swAdvSelectType_And | 1 or 0x1 |
| swAdvSelectType_Contains | 16 or 0x10 |
| swAdvSelectType_Does_Not_Interferes_With | 128 or 0x80 |
| swAdvSelectType_Equals | 4096 or 0x1000 |
| swAdvSelectType_Greater_Than | 256 or 0x100 |
| swAdvSelectType_Greater_Than_OR_Equal | 1024 or 0x400 |
| swAdvSelectType_Interferes_With | 64 or 0x40 |
| swAdvSelectType_Is_Ccontained_By | 32 or 0x20 |
| swAdvSelectType_Is_Exactly | 4 or 0x4 |
| swAdvSelectType_Is_No | 32768 or 0x8000 |
| swAdvSelectType_Is_Not | 8 or 0x8 |
| swAdvSelectType_Is_Not_Equal | 8192 or 0x2000 |
| swAdvSelectType_Is_Yes | 16384 or 0x4000 |
| swAdvSelectType_Less_Than | 512 or 0x200 |
| swAdvSelectType_Less_Than_OR_Equal | 2048 or 0x800 |
| swAdvSelectType_Or | 2 or 0x2 |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
