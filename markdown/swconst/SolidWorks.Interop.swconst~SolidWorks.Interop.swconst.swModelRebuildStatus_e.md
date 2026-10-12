---
title: "swModelRebuildStatus_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swModelRebuildStatus_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swModelRebuildStatus_e.html"
---

# swModelRebuildStatus_e Enumeration

Rebuild status of model. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swModelRebuildStatus_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swModelRebuildStatus_e
```

### C#

```csharp
public enum swModelRebuildStatus_e : System.Enum
```

### C++/CLI

```cpp
public enum class swModelRebuildStatus_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swModelRebuildStatus_FrozenFeatureNeedsRebuild | 2 |
| swModelRebuildStatus_FullyRebuilt | 0 or FALSE |
| swModelRebuildStatus_NonFrozenFeatureNeedsRebuild | 1 or TRUE |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
