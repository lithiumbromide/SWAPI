---
title: "swCreateSectionViewAtOptions_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swCreateSectionViewAtOptions_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCreateSectionViewAtOptions_e.html"
---

# swCreateSectionViewAtOptions_e Enumeration

Options that affect the section view that is created. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swCreateSectionViewAtOptions_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swCreateSectionViewAtOptions_e
```

### C#

```csharp
public enum swCreateSectionViewAtOptions_e : System.Enum
```

### C++/CLI

```cpp
public enum class swCreateSectionViewAtOptions_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swCreateSectionView_ChangeDirection | 4 or 0x4; If set, then the direction of this section view is switched; if not set, then the direction of this section view is not switched |
| swCreateSectionView_CutSurfaceBodies | 128 or 0x80: If set, then shows only the intersecting line of a surface in a section view |
| swCreateSectionView_DisplaySurfaceCut | 32 or 0x20; If set, then only the surfaces cut by the section line apear in the section view; if not set, then all model surfaces appear in the section view |
| swCreateSectionView_ExcludeFasteners | 64 or 0x40; If set, then fasteners are not included in the section view; if not set, then fasteners are included in the section view |
| swCreateSectionView_NotAligned | 1 or 0x1; If set, then the section does not snap into alignment with the parent view; if not set, then the section snaps into alignment with the parent view |
| swCreateSectionView_OffsetSection | 2 or 0x2; If set, then an aligned section view is created (two lines at an angle); if not set, a normal projection section view is created |
| swCreateSectionView_Partial | 16 or 0x10; If set, then a partial section view is created; if not set, then a complete section view is created |
| swCreateSectionView_ScaleWithModel | 8 or 0x8; If set, then the section view is scaled with the model; if not set, then the section view is not scaled with the model |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
