---
title: "swRepairSketchOption_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swRepairSketchOption_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRepairSketchOption_e.html"
---

# swRepairSketchOption_e Enumeration

Options for repairing sketches. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swRepairSketchOption_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swRepairSketchOption_e
```

### C#

```csharp
public enum swRepairSketchOption_e : System.Enum
```

### C++/CLI

```cpp
public enum class swRepairSketchOption_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swRepairSketchBreakIntersection | 8 = Break intersection |
| swRepairSketchCleanup | 0 = Clean up |
| swRepairSketchCloseGaps | 4 = Close gaps |
| swRepairSketchMergeSegment | 2 = Merge segment |
| swRepairSketchZeroSegment | 1 = Zero segment |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
