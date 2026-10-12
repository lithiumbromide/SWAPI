---
title: "GetShortEdgesCount Method (gtcocswGeometryAnalysis)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswGeometryAnalysis"
member: "GetShortEdgesCount"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswGeometryAnalysis~GetShortEdgesCount.html"
---

# GetShortEdgesCount Method (gtcocswGeometryAnalysis)

Gets the number of edges shorter than the specified length on the part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetShortEdgesCount( _
   ByVal length As System.Double, _
   ByRef errorcode As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswGeometryAnalysis
Dim length As System.Double
Dim errorcode As System.Integer
Dim value As System.Integer

value = instance.GetShortEdgesCount(length, errorcode)
```

### C#

```csharp
System.int GetShortEdgesCount(
   System.double length,
   out System.int errorcode
)
```

### C++/CLI

```cpp
System.int GetShortEdgesCount(
   System.double length,
   [Out] System.int errorcode
)
```

### Parameters

- `length`: Length to use to which to compare the edges
- `errorcode`: Error as defined by [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

### Return Value

Number of small edges

## VBA Syntax

See [IGeometryAnalysis::GetShortEdgesCount](ms-its:swutilitiesapivb6.chm::/swutilities~IGeometryAnalysis~GetShortEdgesCount.html).

## See Also

[gtcocswGeometryAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswGeometryAnalysis.html)
[gtcocswGeometryAnalysis Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswGeometryAnalysis_members.html)

## Availability

SOLIDWORKS Utilities API 2004 FCS
