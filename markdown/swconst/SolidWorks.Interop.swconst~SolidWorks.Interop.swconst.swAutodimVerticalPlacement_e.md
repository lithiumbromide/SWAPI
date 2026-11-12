---
title: "swAutodimVerticalPlacement_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swAutodimVerticalPlacement_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAutodimVerticalPlacement_e.html"
---

# swAutodimVerticalPlacement_e Enumeration

Placements of the vertical dimensions created by [ISketch::AutoDimension2](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~AutoDimension2.html) and [IDrawingDoc::AutoDimension](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~Solidworks.Interop.sldworks.IDrawingDoc~AutoDimension.html).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swAutodimVerticalPlacement_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swAutodimVerticalPlacement_e
```

### C#

```csharp
public enum swAutodimVerticalPlacement_e : System.Enum
```

### C++/CLI

```cpp
public enum class swAutodimVerticalPlacement_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swAutodimVerticalPlacementLeft | -1 = Place the vertical dimensions left of the sketch |
| swAutodimVerticalPlacementRight | 1 = Place the vertical dimensions right of the sketch |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
