---
title: "swAutodimEntities_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swAutodimEntities_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAutodimEntities_e.html"
---

# swAutodimEntities_e Enumeration

Entities to dimension [ISketch::AutoDimension2](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~AutoDimension2.html) and [IDrawingDoc::AutoDimension](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~Solidworks.Interop.sldworks.IDrawingDoc~AutoDimension.html).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swAutodimEntities_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swAutodimEntities_e
```

### C#

```csharp
public enum swAutodimEntities_e : System.Enum
```

### C++/CLI

```cpp
public enum class swAutodimEntities_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swAutodimEntitiesAll | 1 = Autodimensions all of the supported entities in the sketch |
| swAutodimEntitiesBasedOnPreselect | 0 = SOLIDWORKS to figure out what to do based on the selected supported entities marked with swAutodimMarkEntities . If any exist, then autodimension them, just like swAutodimEntitiesSelected. If none exist, then autodimension all supported entities, just like swAutodimEntitiesAll |
| swAutodimEntitiesSelected | 2 = Autodimensions selected supported entities marked with swAutodimMarkEntities . If none exist, then autodimensions all supported entities, just like swAutodimEntitiesAll |

## Remarks

Supported entities are lines, points, vertices, faces, sketch entities, center lines, and center marks.

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
