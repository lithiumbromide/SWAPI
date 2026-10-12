---
title: "GetEdgeConvexityFilter Method (IPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "IPowerSelect"
member: "GetEdgeConvexityFilter"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~GetEdgeConvexityFilter.html"
---

# GetEdgeConvexityFilter Method (IPowerSelect)

Gets the Edge convexity filter set in this PowerSelect session.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEdgeConvexityFilter( _
   ByRef bConvex As System.Boolean, _
   ByRef bConcave As System.Boolean, _
   ByRef bIgnoreMixedLoop As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPowerSelect
Dim bConvex As System.Boolean
Dim bConcave As System.Boolean
Dim bIgnoreMixedLoop As System.Boolean
Dim value As System.Integer

value = instance.GetEdgeConvexityFilter(bConvex, bConcave, bIgnoreMixedLoop)
```

### C#

```csharp
System.int GetEdgeConvexityFilter(
   out System.bool bConvex,
   out System.bool bConcave,
   out System.bool bIgnoreMixedLoop
)
```

### C++/CLI

```cpp
System.int GetEdgeConvexityFilter(
   [Out] System.bool bConvex,
   [Out] System.bool bConcave,
   [Out] System.bool bIgnoreMixedLoop
)
```

### Parameters

- `bConvex`: True to get convex edges, false to not
- `bConcave`: True to get concave edges, false to not
- `bIgnoreMixedLoop`: True to ignore loops with convex or concave edges, false to not

### Return Value

Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

## VBA Syntax

See [IPowerSelect::GetEdgeConvexityFilter](ms-its:swutilitiesapivb6.chm::/swutilities~IPowerSelect~GetEdgeConvexityFilter.html).

## See Also

[IPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect.html)
[IPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect_members.html)
[IPowerSelect::SetEdgeConvexityFilter Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~SetEdgeConvexityFilter.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
