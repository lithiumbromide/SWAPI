---
title: "swFeatureFillSurfaceOptions_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swFeatureFillSurfaceOptions_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFeatureFillSurfaceOptions_e.html"
---

# swFeatureFillSurfaceOptions_e Enumeration

Feature fill surface options. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swFeatureFillSurfaceOptions_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swFeatureFillSurfaceOptions_e
```

### C#

```csharp
public enum swFeatureFillSurfaceOptions_e : System.Enum
```

### C++/CLI

```cpp
public enum class swFeatureFillSurfaceOptions_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swMergeResult | 4 or 0x4; Corresponds to IFillSurfaceFeatureData::Merge |
| swOptimizeSurface | 1 or 0x1; Optimize surface |
| swReverseDirection | 8 or 0x8; Corresponds to IFillSurfaceFeatureData::ReverseDirection |
| swReverseSurface | 16 or 0x10; Corresponds to IFillSurfaceFeatureData::ReverseSurface |
| swTryToFormSolid | 2 or 0x2; Corresponds to IFillSurfaceFeatureData::TryToFormSolid |

## Remarks

Some options might not work because the topology of the surface fill to be created might not permit them. In these cases, the options are ignored.

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
