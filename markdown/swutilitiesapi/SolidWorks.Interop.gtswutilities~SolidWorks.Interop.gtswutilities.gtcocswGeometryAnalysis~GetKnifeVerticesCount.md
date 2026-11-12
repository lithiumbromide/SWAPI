---
title: "GetKnifeVerticesCount Method (gtcocswGeometryAnalysis)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswGeometryAnalysis"
member: "GetKnifeVerticesCount"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswGeometryAnalysis~GetKnifeVerticesCount.html"
---

# GetKnifeVerticesCount Method (gtcocswGeometryAnalysis)

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
Dim instance As gtcocswGeometryAnalysis
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

## Remarks

If there are two adjacent edges that intersect at an angle smaller than the specified value, then the vertex between the two edges is a knife vertex.

## See Also

[gtcocswGeometryAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswGeometryAnalysis.html)
[gtcocswGeometryAnalysis Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswGeometryAnalysis_members.html)

## Availability

SOLIDWORKS Utilities API 2004 FCS
