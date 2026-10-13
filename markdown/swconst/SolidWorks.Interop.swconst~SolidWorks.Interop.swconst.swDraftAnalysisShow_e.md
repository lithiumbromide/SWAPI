---
title: "swDraftAnalysisShow_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swDraftAnalysisShow_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDraftAnalysisShow_e.html"
---

# swDraftAnalysisShow_e Enumeration

Show draft analsyis options. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swDraftAnalysisShow_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swDraftAnalysisShow_e
```

### C#

```csharp
public enum swDraftAnalysisShow_e : System.Enum
```

### C++/CLI

```cpp
public enum class swDraftAnalysisShow_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swDraftAnalysisShowDraftRequired | 4 or 0x4 |
| swDraftAnalysisShowNegative | 2 or 0x2 |
| swDraftAnalysisShowNegativeSteep | 32 or 0x20 |
| swDraftAnalysisShowPositive | 1 or 0x1 |
| swDraftAnalysisShowPositiveSteep | 16 or 0x10 |
| swDraftAnalysisShowStraddle | 8 or 0x8 |
| swDraftAnalysisShowSurface | 64 or 0x40 |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
