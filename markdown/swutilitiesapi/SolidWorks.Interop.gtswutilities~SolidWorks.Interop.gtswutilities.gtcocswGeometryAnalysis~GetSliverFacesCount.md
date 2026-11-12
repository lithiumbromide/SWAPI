---
title: "GetSliverFacesCount Method (gtcocswGeometryAnalysis)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswGeometryAnalysis"
member: "GetSliverFacesCount"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswGeometryAnalysis~GetSliverFacesCount.html"
---

# GetSliverFacesCount Method (gtcocswGeometryAnalysis)

Gets the number of sliver faces in the part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSliverFacesCount( _
   ByVal width As System.Double, _
   ByRef errorcode As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswGeometryAnalysis
Dim width As System.Double
Dim errorcode As System.Integer
Dim value As System.Integer

value = instance.GetSliverFacesCount(width, errorcode)
```

### C#

```csharp
System.int GetSliverFacesCount(
   System.double width,
   out System.int errorcode
)
```

### C++/CLI

```cpp
System.int GetSliverFacesCount(
   System.double width,
   [Out] System.int errorcode
)
```

### Parameters

- `width`: Width to use to detect sliver faces
- `errorcode`: Error as defined by [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

### Return Value

Number of sliver faces

## VBA Syntax

See [IGeometryAnalysis::GetSliverFacesCount](ms-its:swutilitiesapivb6.chm::/swutilities~IGeometryAnalysis~GetSliverFacesCount.html).

## Remarks

Sliver faces are faces with a high aspect ratio (the ratio of length to width). A face is a sliver face if its area is less than the limiting area W*((P/2)-W), where W is the specified width and P is the face perimeter.

## See Also

[gtcocswGeometryAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswGeometryAnalysis.html)
[gtcocswGeometryAnalysis Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswGeometryAnalysis_members.html)

## Availability

SOLIDWORKS Utilities API 2004 FCS
