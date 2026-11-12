---
title: "swAutodimHorizontalPlacement_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swAutodimHorizontalPlacement_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAutodimHorizontalPlacement_e.html"
---

# swAutodimHorizontalPlacement_e Enumeration

Placements for the horizontal dimensions created by [ISketch::AutoDimension2](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~AutoDimension2.html) and [IDrawingDoc::AutoDimension](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~Solidworks.Interop.sldworks.IDrawingDoc~AutoDimension.html).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swAutodimHorizontalPlacement_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swAutodimHorizontalPlacement_e
```

### C#

```csharp
public enum swAutodimHorizontalPlacement_e : System.Enum
```

### C++/CLI

```cpp
public enum class swAutodimHorizontalPlacement_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swAutodimHorizontalPlacementAbove | 1 = Place the horizontal dimensions above the sketch. |
| swAutodimHorizontalPlacementBelow | -1 = Place the horizontal dimensions below the sketch. |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
