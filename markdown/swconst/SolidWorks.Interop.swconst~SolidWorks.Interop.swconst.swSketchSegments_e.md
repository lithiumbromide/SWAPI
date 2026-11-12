---
title: "swSketchSegments_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swSketchSegments_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSketchSegments_e.html"
---

# swSketchSegments_e Enumeration

Types of [ISketchSegment](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html) objects.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swSketchSegments_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swSketchSegments_e
```

### C#

```csharp
public enum swSketchSegments_e : System.Enum
```

### C++/CLI

```cpp
public enum class swSketchSegments_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swSketchARC | 1 |
| swSketchELLIPSE | 2 |
| swSketchLINE | 0 |
| swSketchPARABOLA | 5 |
| swSketchSPLINE | 3 |
| swSketchTEXT | 4 |

## Remarks

Based on these types, you can obtain the appropriate derived class (that is, [ISketchLine](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchLine.html), [ISketchArc](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchArc.html), and so on) and call the appropriate derived class functions.

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
