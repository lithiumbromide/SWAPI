---
title: "GetSmallFacesCount Method (gtcocswGeometryAnalysis)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswGeometryAnalysis"
member: "GetSmallFacesCount"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswGeometryAnalysis~GetSmallFacesCount.html"
---

# GetSmallFacesCount Method (gtcocswGeometryAnalysis)

Gets the number of small faces on the part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSmallFacesCount( _
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

value = instance.GetSmallFacesCount(length, errorcode)
```

### C#

```csharp
System.int GetSmallFacesCount(
   System.double length,
   out System.int errorcode
)
```

### C++/CLI

```cpp
System.int GetSmallFacesCount(
   System.double length,
   [Out] System.int errorcode
)
```

### Parameters

- `length`: Length to use to detect small faces
- `errorcode`: Error as defined by [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

### Return Value

Number of small faces

## VBA Syntax

See [IGeometryAnalysis::GetSmallFacesCount](ms-its:swutilitiesapivb6.chm::/swutilities~IGeometryAnalysis~GetSmallFacesCount.html).

## Remarks

Small faces are faces with all edges shorter than a specified length.

## See Also

[gtcocswGeometryAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswGeometryAnalysis.html)
[gtcocswGeometryAnalysis Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswGeometryAnalysis_members.html)

## Availability

SOLIDWORKS Utilities API 2004 FCS
