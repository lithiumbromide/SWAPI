---
title: "GetSmallFacesCount Method (IGeometryAnalysis)"
project: "SOLIDWORKS Utilities API Help"
interface: "IGeometryAnalysis"
member: "GetSmallFacesCount"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IGeometryAnalysis~GetSmallFacesCount.html"
---

# GetSmallFacesCount Method (IGeometryAnalysis)

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
Dim instance As IGeometryAnalysis
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

## Examples

[Analyze Geometry (VBA)](Analyze_Geometry_VB6.htm)

## Remarks

Small faces are faces with all edges shorter than a specified length.

## See Also

[IGeometryAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IGeometryAnalysis.html)
[IGeometryAnalysis Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IGeometryAnalysis_members.html)

## Availability

SOLIDWORKS Utilities API 2004 FCS
