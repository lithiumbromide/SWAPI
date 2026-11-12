---
title: "GetDiscontinuousFacesCount Method (gtcocswGeometryAnalysis)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswGeometryAnalysis"
member: "GetDiscontinuousFacesCount"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswGeometryAnalysis~GetDiscontinuousFacesCount.html"
---

# GetDiscontinuousFacesCount Method (gtcocswGeometryAnalysis)

Gets the number of discontinuous faces in the part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDiscontinuousFacesCount( _
   ByRef errorcode As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswGeometryAnalysis
Dim errorcode As System.Integer
Dim value As System.Integer

value = instance.GetDiscontinuousFacesCount(errorcode)
```

### C#

```csharp
System.int GetDiscontinuousFacesCount(
   out System.int errorcode
)
```

### C++/CLI

```cpp
System.int GetDiscontinuousFacesCount(
   [Out] System.int errorcode
)
```

### Parameters

- `errorcode`: Error as defined by [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

### Return Value

Number of discontinuous faces

## VBA Syntax

See [IGeometryAnalysis::GetDiscontinuousFacesCount](ms-its:swutilitiesapivb6.chm::/swutilities~IGeometryAnalysis~GetDiscontinuousFacesCount.html).

## See Also

[gtcocswGeometryAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswGeometryAnalysis.html)
[gtcocswGeometryAnalysis Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswGeometryAnalysis_members.html)

## Availability

SOLIDWORKS Utilities API 2004 FCS
