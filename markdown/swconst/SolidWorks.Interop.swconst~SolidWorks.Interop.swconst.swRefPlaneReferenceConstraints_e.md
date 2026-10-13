---
title: "swRefPlaneReferenceConstraints_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swRefPlaneReferenceConstraints_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRefPlaneReferenceConstraints_e.html"
---

# swRefPlaneReferenceConstraints_e Enumeration

Reference plane constraints. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swRefPlaneReferenceConstraints_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swRefPlaneReferenceConstraints_e
```

### C#

```csharp
public enum swRefPlaneReferenceConstraints_e : System.Enum
```

### C++/CLI

```cpp
public enum class swRefPlaneReferenceConstraints_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swRefPlaneReferenceConstraint_Angle | 16 or 0x10 |
| swRefPlaneReferenceConstraint_Coincident | 4 or 0x4 |
| swRefPlaneReferenceConstraint_Distance | 8 or 0x8 |
| swRefPlaneReferenceConstraint_MidPlane | 128 or 0x80 |
| swRefPlaneReferenceConstraint_OptionFlip | 256 or 0x100 |
| swRefPlaneReferenceConstraint_OptionOriginOnCurve | 512 or 0x200 |
| swRefPlaneReferenceConstraint_OptionProjectAlongSketchNormal | 2056 or 0x800 |
| swRefPlaneReferenceConstraint_OptionProjectToNearestLocation | 1028 or 0x400 |
| swRefPlaneReferenceConstraint_OptionReferenceFlip | 8192 or 0x2000 |
| swRefPlaneReferenceConstraint_Parallel | 1 or 0x1 |
| swRefPlaneReferenceConstraint_ParallelToScreen | 4096 or 0x1000 |
| swRefPlaneReferenceConstraint_Perpendicular | 2 or 0x2 |
| swRefPlaneReferenceConstraint_Project | 64 or 0x40 |
| swRefPlaneReferenceConstraint_Tangent | 32 or 0x20 |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
