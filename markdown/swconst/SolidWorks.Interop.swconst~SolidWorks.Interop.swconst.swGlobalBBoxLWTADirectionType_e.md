---
title: "swGlobalBBoxLWTADirectionType_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swGlobalBBoxLWTADirectionType_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGlobalBBoxLWTADirectionType_e.html"
---

# swGlobalBBoxLWTADirectionType_e Enumeration

Length, width, and thickness directions for a rectangular bounding box and axis directions for a cylindrical bounding box.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swGlobalBBoxLWTADirectionType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swGlobalBBoxLWTADirectionType_e
```

### C#

```csharp
public enum swGlobalBBoxLWTADirectionType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swGlobalBBoxLWTADirectionType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swBBox_AxisDir_X | 7 = Axis direction is the X direction of the coordinate system |
| swBBox_AxisDir_Y | 8 = Axis direction is the Y direction of the coordinate system |
| swBBox_AxisDir_Z | 9 = Axis direction is the Z direction of the coordinate system |
| swBBox_LWTADir_Unspecified | 0 = Length, width, thickness, and axis directions are not fixed. Length is the longest and thickness is the shortest direction |
| swBBox_LWTDir_XYZ | 1 = LWT directions map to XYZ coordinates |
| swBBox_LWTDir_XZY | 6 = LWT directions map to XZY coordinates |
| swBBox_LWTDir_YXZ | 2 = LWT directions map to YXZ coordinates |
| swBBox_LWTDir_YZX | 3 = LWT directions map to YZX coordinates |
| swBBox_LWTDir_ZXY | 5 = LWT directions map to ZXY coordinates |
| swBBox_LWTDir_ZYX | 4 = LWT directions map to ZYX coordinates |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
