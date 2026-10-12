---
title: "swGlobalBoundingBoxFitOptions_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swGlobalBoundingBoxFitOptions_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGlobalBoundingBoxFitOptions_e.html"
---

# swGlobalBoundingBoxFitOptions_e Enumeration

Global bounding box fit types.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swGlobalBoundingBoxFitOptions_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swGlobalBoundingBoxFitOptions_e
```

### C#

```csharp
public enum swGlobalBoundingBoxFitOptions_e : System.Enum
```

### C++/CLI

```cpp
public enum class swGlobalBoundingBoxFitOptions_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swBoundingBoxType_BestFit | 1 = Orientation of the bounding box is based on the X-Y plane |
| swBoundingBoxType_CustomCoordSys | 3 = Use coordinate system to define bounding box |
| swBoundingBoxType_CustomPlane | 2 = Specify the orientation plane or planar face on which to base the bounding box |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
