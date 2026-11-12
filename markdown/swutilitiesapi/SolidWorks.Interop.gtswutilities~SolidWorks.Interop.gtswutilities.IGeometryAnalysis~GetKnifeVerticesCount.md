---
title: "GetKnifeVerticesCount Method (IGeometryAnalysis)"
project: "SOLIDWORKS Utilities API Help"
interface: "IGeometryAnalysis"
member: "GetKnifeVerticesCount"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IGeometryAnalysis~GetKnifeVerticesCount.html"
---

# GetKnifeVerticesCount Method (IGeometryAnalysis)

Gets the number of knife vertices in the part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetKnifeVerticesCount( _
   ByVal angle As System.Double, _
   ByRef errorcode As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IGeometryAnalysis
Dim angle As System.Double
Dim errorcode As System.Integer
Dim value As System.Integer

value = instance.GetKnifeVerticesCount(angle, errorcode)
```

### C#

```csharp
System.int GetKnifeVerticesCount(
   System.double angle,
   out System.int errorcode
)
```

### C++/CLI

```cpp
System.int GetKnifeVerticesCount(
   System.double angle,
   [Out] System.int errorcode
)
```

### Parameters

- `angle`: Angle to use to determine knife vertices
- `errorcode`: Error as defined by [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

### Return Value

Number of knife vertices

## VBA Syntax

See [IGeometryAnalysis::GetKnifeVerticesCount](ms-its:swutilitiesapivb6.chm::/swutilities~IGeometryAnalysis~GetKnifeVerticesCount.html).

## Examples

[Analyze Geometry (VBA)](Analyze_Geometry_VB6.htm)

## Remarks

If there are two adjacent edges that intersect at an angle smaller than the specified value, then the vertex between the two edges is a knife vertex.

## See Also

[IGeometryAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IGeometryAnalysis.html)
[IGeometryAnalysis Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IGeometryAnalysis_members.html)

## Availability

SOLIDWORKS Utilities API 2004 FCS
