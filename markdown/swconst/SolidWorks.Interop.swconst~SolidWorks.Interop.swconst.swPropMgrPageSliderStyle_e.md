---
title: "swPropMgrPageSliderStyle_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swPropMgrPageSliderStyle_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPropMgrPageSliderStyle_e.html"
---

# swPropMgrPageSliderStyle_e Enumeration

PropertyManager page slider styles. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swPropMgrPageSliderStyle_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swPropMgrPageSliderStyle_e
```

### C#

```csharp
public enum swPropMgrPageSliderStyle_e : System.Enum
```

### C++/CLI

```cpp
public enum class swPropMgrPageSliderStyle_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swPropMgrPageSliderStyle_AutoTicks | 2 or 0x2; If set, then tick marks are created based on swPropMgrPageSliderStyle_BottomLeftTicks and swPropMgrPageSliderStyle_TopRightTicks |
| swPropMgrPageSliderStyle_BottomLeftTicks | 4 or 0x4; If set, then tick marks appear at the bottom (horizontal) or left (vertical) of the slider |
| swPropMgrPageSliderStyle_NotifyWhileTracking | 16 or 0x10; If set, then your application is notified when the user is dragging the slider, each time the value changes; if not set, then your application is not notified when the user is dragging the slider, only when the user is done dragging the slider; setting this bit allows your application to react immediately to changes, but it does generate many more callbacks, so it is less efficient |
| swPropMgrPageSliderStyle_TopRightTicks | 8 or 0x8; If set, then tick marks appear at the top (horizontal) or right (vertical) of the slider |
| swPropMgrPageSliderStyle_Vertical | 1 or 0x1; If set, then the slider is oriented vertically; if not set, then the slider is oriented horizontally |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
