---
title: "swFeatureChamferOption_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swFeatureChamferOption_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFeatureChamferOption_e.html"
---

# swFeatureChamferOption_e Enumeration

Chamfer feature options. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swFeatureChamferOption_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swFeatureChamferOption_e
```

### C#

```csharp
public enum swFeatureChamferOption_e : System.Enum
```

### C++/CLI

```cpp
public enum class swFeatureChamferOption_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swFeatureChamferFlipDirection | 1 or 0x1 |
| swFeatureChamferKeepFeature | 2 or 0x2 |
| swFeatureChamferPropagateFeatToParts | 8 or 0x8 |
| swFeatureChamferTangentPropagation | 4 or 0x4 |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
