---
title: "GetDiscontinuousFacesCount Method (IGeometryAnalysis)"
project: "SOLIDWORKS Utilities API Help"
interface: "IGeometryAnalysis"
member: "GetDiscontinuousFacesCount"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IGeometryAnalysis~GetDiscontinuousFacesCount.html"
---

# GetDiscontinuousFacesCount Method (IGeometryAnalysis)

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
Dim instance As IGeometryAnalysis
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

## Examples

[Analyze Geometry (VBA)](Analyze_Geometry_VB6.htm)

## See Also

[IGeometryAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IGeometryAnalysis.html)
[IGeometryAnalysis Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IGeometryAnalysis_members.html)

## Availability

SOLIDWORKS Utilities API 2004 FCS
