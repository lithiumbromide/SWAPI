---
title: "swAutodimMark_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swAutodimMark_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAutodimMark_e.html"
---

# swAutodimMark_e Enumeration

Selection mark values. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swAutodimMark_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swAutodimMark_e
```

### C#

```csharp
public enum swAutodimMark_e : System.Enum
```

### C++/CLI

```cpp
public enum class swAutodimMark_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swAutodimMarkEntities | 1 or 0x1; Sketch entities to autodimension when swAutodimEntitiesSelected is passed as the entitiesToDimension argument to ISketch::AutoDimension2 |
| swAutodimMarkHorizontalDatum | 2 or 0x2; Sketch entities to autodimension when swAutodimEntitiesSelected is passed as the entitiesToDimension argument to ISketch::AutoDimension2 |
| swAutodimMarkOriginDatum | 8 or 0x8; Unique datum for the origin dimension scheme. Datum must be either a sketch point or a vertical sketch line. |
| swAutodimMarkVerticalDatum | 4 or 0x4; Unique datum for the horizontal dimension scheme; datum must be either a sketch point or a vertical sketch line |

## Remarks

These values are passed by [IModelDocExtension::SelectByID2](ms-its:sldworksapi.chm::/Solidworks.Interop.sldworks~Solidworks.Interop.sldworks.IModelDocExtension~SelectByID2.html).

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
