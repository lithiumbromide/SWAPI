---
title: "swBalloonItemNumbersOrder_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swBalloonItemNumbersOrder_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBalloonItemNumbersOrder_e.html"
---

# swBalloonItemNumbersOrder_e Enumeration

Balloon item ordering options. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swBalloonItemNumbersOrder_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swBalloonItemNumbersOrder_e
```

### C#

```csharp
public enum swBalloonItemNumbersOrder_e : System.Enum
```

### C++/CLI

```cpp
public enum class swBalloonItemNumbersOrder_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swBalloonItemNumbers_DoNotChangeItemNumbers | 0x1 or 1 |
| swBalloonItemNumbers_FollowAssemblyOrder | 0x2 or 2 |
| swBalloonItemNumbers_NotApplicable | -1 |
| swBalloonItemNumbers_OrderSequentially | 0x4 or 4 |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
