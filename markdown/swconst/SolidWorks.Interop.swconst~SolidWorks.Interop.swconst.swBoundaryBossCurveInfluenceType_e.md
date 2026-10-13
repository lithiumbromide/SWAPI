---
title: "swBoundaryBossCurveInfluenceType_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swBoundaryBossCurveInfluenceType_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBoundaryBossCurveInfluenceType_e.html"
---

# swBoundaryBossCurveInfluenceType_e Enumeration

Boundary feature curve influence types. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swBoundaryBossCurveInfluenceType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swBoundaryBossCurveInfluenceType_e
```

### C#

```csharp
public enum swBoundaryBossCurveInfluenceType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swBoundaryBossCurveInfluenceType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swBoundaryBossCurve_GlobalInfluence | 32 or 0x20 |
| swBoundaryBossCurve_LinearInfluence | 144 or 0x90 |
| swBoundaryBossCurve_ToEdgeInfluence | 64 or 0x40 |
| swBoundaryBossCurve_ToNextCurveInfluence | 0 or 0x0 |
| swBoundaryBossCurve_ToNextSharpInfluence | 16 or 0x10 |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
