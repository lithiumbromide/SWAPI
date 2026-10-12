---
title: "swRoutingComponentGroupingOption_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swRoutingComponentGroupingOption_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRoutingComponentGroupingOption_e.html"
---

# swRoutingComponentGroupingOption_e Enumeration

Routing components grouping options. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swRoutingComponentGroupingOption_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swRoutingComponentGroupingOption_e
```

### C#

```csharp
public enum swRoutingComponentGroupingOption_e : System.Enum
```

### C++/CLI

```cpp
public enum class swRoutingComponentGroupingOption_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swDisplayUnitsInBOM | 4 or 0x4 |
| swGroupPipesOrTubesWithTheSameDiameterAndSchedule | 2 or 0x2 |
| swRoutingGroupSpoolComponents | 8 or 0x8 |
| swShowOnlyRoutingComponentsInBOM | 1 or 0x1 |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
