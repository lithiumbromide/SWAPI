---
title: "swSweptFlangeError_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swSweptFlangeError_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSweptFlangeError_e.html"
---

# swSweptFlangeError_e Enumeration

Swept flange creation errors. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swSweptFlangeError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swSweptFlangeError_e
```

### C#

```csharp
public enum swSweptFlangeError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swSweptFlangeError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swSweptFlangeError_InvalidPath | 2 |
| swSweptFlangeError_InvalidProfile | 1 |
| swSweptFlangeError_InvalidSheetMetalParameters | 8 = ISweptFlangeFeatureData::UseMaterialSheetMetalParameters and ISweptFlangeFeatuareData::UseGaugeTable cannot both be set to true |
| swSweptFlangeError_None | 0 |
| swSweptFlangeError_SelfIntersectingGeometry | 4 |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
