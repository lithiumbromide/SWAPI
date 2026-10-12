---
title: "swSketchFullyDefineRelationType_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swSketchFullyDefineRelationType_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSketchFullyDefineRelationType_e.html"
---

# swSketchFullyDefineRelationType_e Enumeration

Fully defined sketch relations. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swSketchFullyDefineRelationType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swSketchFullyDefineRelationType_e
```

### C#

```csharp
public enum swSketchFullyDefineRelationType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swSketchFullyDefineRelationType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swSketchFullyDefineRelationType_Coincident | 512 or 0x200 |
| swSketchFullyDefineRelationType_Colinear | 32 or 0x20 |
| swSketchFullyDefineRelationType_Concentric | 64 or 0x40 |
| swSketchFullyDefineRelationType_Equal | 1 or 0x1 |
| swSketchFullyDefineRelationType_Horizontal | 2 or 0x2 |
| swSketchFullyDefineRelationType_Midpoint | 256 or 0x100 |
| swSketchFullyDefineRelationType_Parallel | 128 or 0x80 |
| swSketchFullyDefineRelationType_Perpendicular | 16 or 0x10 |
| swSketchFullyDefineRelationType_Tangent | 8 or 0x8 |
| swSketchFullyDefineRelationType_Vertical | 4 or 0x4 |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
