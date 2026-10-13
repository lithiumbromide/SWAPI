---
title: "swRebuildOptions_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swRebuildOptions_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRebuildOptions_e.html"
---

# swRebuildOptions_e Enumeration

Rebuild options. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swRebuildOptions_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swRebuildOptions_e
```

### C#

```csharp
public enum swRebuildOptions_e : System.Enum
```

### C++/CLI

```cpp
public enum class swRebuildOptions_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swCurrentSheetDisp | 8 or 0x8; Drawing only; only rebuilds the display of the views on the current drawing sheet |
| swForceRebuildAll | 2 or 0x2; Assembly or drawing; Forces a rebuild of all geometry |
| swRebuildAll | 1 or 0x1; Assembly or drawing; rebuilds geometry that has not been regenerated |
| swUpdateDirtyOnly | 16 or 0x10; Drawing only; only rebuilds drawing views that are dirty when OR'd with swCurrentSheetDisp option |
| swUpdateMates | 4 or 0x4; Assembly only; only rebuilds mates, which is much faster than rebuilding the geometry. Especially useful for IComponent2::Transform2 |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
