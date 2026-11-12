---
title: "swSlicingTypes_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swSlicingTypes_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSlicingTypes_e.html"
---

# swSlicingTypes_e Enumeration

Types of slicing. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swSlicingTypes_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swSlicingTypes_e
```

### C#

```csharp
public enum swSlicingTypes_e : System.Enum
```

### C++/CLI

```cpp
public enum class swSlicingTypes_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swSlicingTypes_Circle | 4 = Creates a circle whose diameter equals the average of the length and width of the rectangle that encloses all the sketch entities; circle is located at the intersection of the source geometry and the slicing plane |
| swSlicingTypes_Exact | 2 = Creates an exact intersection of the mesh BREP body and graphics body resulting in a polyline; set only if swSlicingTypes_Intersection is also set; not valid with swSlicingTypes_Circle and swSlicingTypes_Rectangle |
| swSlicingTypes_Intersection | 1 = For SOLIDWORKS BREP geometry, the slicing is identical to what is generated using the Intersection Curve tool; for mesh BREP and graphics bodies, sketches generated cannot be modified |
| swSlicingTypes_None | 0 |
| swSlicingTypes_Rectangle | 8 = Creates a rectangle that encloses all the sketch entities and is located at the intersection of the source geometry and the slicing plane |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
