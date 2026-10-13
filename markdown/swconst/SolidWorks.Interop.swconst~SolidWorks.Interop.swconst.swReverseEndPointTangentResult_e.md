---
title: "swReverseEndPointTangentResult_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swReverseEndPointTangentResult_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swReverseEndPointTangentResult_e.html"
---

# swReverseEndPointTangentResult_e Enumeration

Result codes for [ISketchManager::ReverseEndPointTangent](ms-its:sldworksapi.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ReverseEndPointTangent.html).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swReverseEndPointTangentResult_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swReverseEndPointTangentResult_e
```

### C#

```csharp
public enum swReverseEndPointTangentResult_e : System.Enum
```

### C++/CLI

```cpp
public enum class swReverseEndPointTangentResult_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swReverseEndPointTangent_ConstraintConflict | 2 = Reversing the end point tangent direction creates a conflict with existing constraints |
| swReverseEndPointTangent_InvalidSelection | 1 = Select a valid end point tangent direction entity |
| swReverseEndPointTangent_Success | 0 |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
