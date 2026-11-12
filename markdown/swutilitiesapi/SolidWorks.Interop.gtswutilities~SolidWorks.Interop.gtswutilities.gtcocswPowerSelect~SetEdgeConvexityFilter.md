---
title: "SetEdgeConvexityFilter Method (gtcocswPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswPowerSelect"
member: "SetEdgeConvexityFilter"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect~SetEdgeConvexityFilter.html"
---

# SetEdgeConvexityFilter Method (gtcocswPowerSelect)

Sets the Edge convexity filter for this PowerSelect session.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetEdgeConvexityFilter( _
   ByVal bConvex As System.Boolean, _
   ByVal bConcave As System.Boolean, _
   ByVal bIgnoreMixedLoop As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswPowerSelect
Dim bConvex As System.Boolean
Dim bConcave As System.Boolean
Dim bIgnoreMixedLoop As System.Boolean
Dim value As System.Integer

value = instance.SetEdgeConvexityFilter(bConvex, bConcave, bIgnoreMixedLoop)
```

### C#

```csharp
System.int SetEdgeConvexityFilter(
   System.bool bConvex,
   System.bool bConcave,
   System.bool bIgnoreMixedLoop
)
```

### C++/CLI

```cpp
System.int SetEdgeConvexityFilter(
   System.bool bConvex,
   System.bool bConcave,
   System.bool bIgnoreMixedLoop
)
```

### Parameters

- `bConvex`: True to get convex edges, false to not
- `bConcave`: True to get concave edges, false to not
- `bIgnoreMixedLoop`: True to ignore loops with convex or concave edges, false to not

### Return Value

Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

## VBA Syntax

See [IPowerSelect::SetEdgeConvexityFilter](ms-its:swutilitiesapivb6.chm::/swutilities~IPowerSelect~SetEdgeConvexityFilter.html).

## See Also

[gtcocswPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect.html)
[gtcocswPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect_members.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
