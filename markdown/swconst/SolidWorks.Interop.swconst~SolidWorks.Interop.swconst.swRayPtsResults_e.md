---
title: "swRayPtsResults_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swRayPtsResults_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRayPtsResults_e.html"
---

# swRayPtsResults_e Enumeration

Types of intersections and whether the rays are entering or exiting the body when they hit. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swRayPtsResults_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swRayPtsResults_e
```

### C#

```csharp
public enum swRayPtsResults_e : System.Enum
```

### C++/CLI

```cpp
public enum class swRayPtsResults_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swRayPtsResultsEDGE | 4 or 0x4; Edge hit |
| swRayPtsResultsENTER | 16 or 0x10; Ray was entering body when it hit (optionally appears when swRayPtsOptsENTRY_EXIT is specified in the options argument to IModelDoc2::RayIntersections ) |
| swRayPtsResultsEXIT | 32 or 0x20; Ray was exiting body when it hit (optionally appears when swRayPtsOptsENTRY_EXIT is specified in the options argument to IModelDoc2::RayIntersections ) |
| swRayPtsResultsFACE | 1 or 0x1; Simple face hit |
| swRayPtsResultsSILHOUETTE | 2 or 0x2; Grazing face hit |
| swRayPtsResultsUnknown | 0 or 0x0; Unknown |
| swRayPtsResultsVERTEX | 8 or 0x8; Vertex hit |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
