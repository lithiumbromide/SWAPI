---
title: "GetKnifeEdgesCount Method (gtcocswGeometryAnalysis)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswGeometryAnalysis"
member: "GetKnifeEdgesCount"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswGeometryAnalysis~GetKnifeEdgesCount.html"
---

# GetKnifeEdgesCount Method (gtcocswGeometryAnalysis)

Gets the number of knife edges in the part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetKnifeEdgesCount( _
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

value = instance.GetKnifeEdgesCount(angle, errorcode)
```

### C#

```csharp
System.int GetKnifeEdgesCount(
   System.double angle,
   out System.int errorcode
)
```

### C++/CLI

```cpp
System.int GetKnifeEdgesCount(
   System.double angle,
   [Out] System.int errorcode
)
```

### Parameters

- `angle`: Angle to use to determine the knife edges
- `errorcode`: Error as defined by [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

### Return Value

Number of knife edges

## VBA Syntax

See [IGeometryAnalysis::GetKnifeEdgesCount](ms-its:swutilitiesapivb6.chm::/swutilities~IGeometryAnalysis~GetKnifeEdgesCount.html).

## Remarks

A sharp edge or knife edge is an edge where the angle between two adjacent faces
is acute.

## See Also

[gtcocswGeometryAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswGeometryAnalysis.html)
[gtcocswGeometryAnalysis Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswGeometryAnalysis_members.html)

## Availability

SOLIDWORKS Utilities API 2004 FCS
