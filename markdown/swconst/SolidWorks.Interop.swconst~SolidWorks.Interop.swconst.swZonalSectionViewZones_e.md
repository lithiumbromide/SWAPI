---
title: "swZonalSectionViewZones_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swZonalSectionViewZones_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swZonalSectionViewZones_e.html"
---

# swZonalSectionViewZones_e Enumeration

Intersection zones for section views. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm)

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swZonalSectionViewZones_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swZonalSectionViewZones_e
```

### C#

```csharp
public enum swZonalSectionViewZones_e : System.Enum
```

### C++/CLI

```cpp
public enum class swZonalSectionViewZones_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swZonalSectionViewZones_swZonalSectionViewZone_1 | 1 or 0x1 |
| swZonalSectionViewZones_swZonalSectionViewZone_2 | 2 or 0x2 |
| swZonalSectionViewZones_swZonalSectionViewZone_3 | 4 or 0x4 |
| swZonalSectionViewZones_swZonalSectionViewZone_4 | 8 or 0x8 |
| swZonalSectionViewZones_swZonalSectionViewZone_5 | 16 or 0x10 |
| swZonalSectionViewZones_swZonalSectionViewZone_6 | 32 or 0x20 |
| swZonalSectionViewZones_swZonalSectionViewZone_7 | 64 or 0x40 |
| swZonalSectionViewZones_swZonalSectionViewZone_8 | 128 or 0x80 |

## Remarks

Descriptions of the intersection zones in relation to the number of sectioning planes appear in [ISectionViewData::SectionedZones](ms-its:sldworksapi.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SectionedZones.html).

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
