---
title: "swMotionStudyType_e Enumeration"
project: "SOLIDWORKS Motion Study API Help"
interface: "swMotionStudyType_e"
member: ""
kind: "enum"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.swMotionStudyType_e.html"
---

# swMotionStudyType_e Enumeration

Motion study types. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swMotionStudyType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swMotionStudyType_e
```

### C#

```csharp
public enum swMotionStudyType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swMotionStudyType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swMotionStudyTypeAssembly | 1 or 0x1 = Animation; D-cubed solver is used to do presentation animation only; no simulation is performed, so no results or plots are available; gravity, contact, springs, and forces cannot be used; mass and inertia values have no effect on the animation |
| swMotionStudyTypeCosmosMotion | 4 or 0x4 = Motion Analysis; ADAMS (MSC.Software) solver is used to return accurate results; you must load the SOLIDWORKS Motion add-in with a SOLIDWORKS premium license to use this option |
| swMotionStudyTypeLegacyCosmosMotion | 8 or 0x8 = Legacy COSMOSMotion; in SOLIDWORKS 2007 and earlier, motion analysis was provided through the COSMOSMotion add-in; this option is available if either the COSMOSMotion add-in is loaded or you open an older model that was created using that add-in; models with legacy COSMOSMotion data can be opened but not edited |
| swMotionStudyTypeNewCosmosMotion | 16 or 0x10 |
| swMotionStudyTypePhysicalSimulation | 2 or 0x2 = Basic Motion; NVIDIA phys-x solver is used to perform fast and approximate dynamic analysis; quickly returns results that look realistic at the cost of accuracy |

## See Also

[SolidWorks.Interop.swmotionstudy Namespace](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy_namespace.html)
