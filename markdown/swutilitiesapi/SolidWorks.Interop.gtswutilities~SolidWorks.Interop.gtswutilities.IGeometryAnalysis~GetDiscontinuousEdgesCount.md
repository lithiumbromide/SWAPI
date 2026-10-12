---
title: "GetDiscontinuousEdgesCount Method (IGeometryAnalysis)"
project: "SOLIDWORKS Utilities API Help"
interface: "IGeometryAnalysis"
member: "GetDiscontinuousEdgesCount"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IGeometryAnalysis~GetDiscontinuousEdgesCount.html"
---

# GetDiscontinuousEdgesCount Method (IGeometryAnalysis)

Gets the number of discontinuous edges in the part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDiscontinuousEdgesCount( _
   ByRef errorcode As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IGeometryAnalysis
Dim errorcode As System.Integer
Dim value As System.Integer

value = instance.GetDiscontinuousEdgesCount(errorcode)
```

### C#

```csharp
System.int GetDiscontinuousEdgesCount(
   out System.int errorcode
)
```

### C++/CLI

```cpp
System.int GetDiscontinuousEdgesCount(
   [Out] System.int errorcode
)
```

### Parameters

- `errorcode`: Error as defined by [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

### Return Value

Number of discontinuous edges

## VBA Syntax

See [IGeometryAnalysis::GetDiscontinuousEdgesCount](ms-its:swutilitiesapivb6.chm::/swutilities~IGeometryAnalysis~GetDiscontinuousEdgesCount.html).

## Examples

[Analyze Geometry (VBA)](Analyze_Geometry_VB6.htm)

## Remarks

All edges in the part where the underlying curve geometry has position or tangent discontinuity are discontinuous edges.

## See Also

[IGeometryAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IGeometryAnalysis.html)
[IGeometryAnalysis Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IGeometryAnalysis_members.html)

## Availability

SOLIDWORKS Utilities API 2004 FCS
