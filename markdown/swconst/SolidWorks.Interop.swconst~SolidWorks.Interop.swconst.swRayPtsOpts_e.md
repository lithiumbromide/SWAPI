---
title: "swRayPtsOpts_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swRayPtsOpts_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRayPtsOpts_e.html"
---

# swRayPtsOpts_e Enumeration

Ray points options. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swRayPtsOpts_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swRayPtsOpts_e
```

### C#

```csharp
public enum swRayPtsOpts_e : System.Enum
```

### C++/CLI

```cpp
public enum class swRayPtsOpts_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swRayPtsOptsENTRY_EXIT | 4 or 0x4; Output requested of whether ray was entering or exiting body when it hit |
| swRayPtsOptsNORMALS | 1 or 0x1; Output of normals requested |
| swRayPtsOptsTOPOLS | 2 or 0x2; Output of entities hit requested |
| swRayPtsOptsUNBLOCK | 8 or 0x8; Allow the system to respond while waiting |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
