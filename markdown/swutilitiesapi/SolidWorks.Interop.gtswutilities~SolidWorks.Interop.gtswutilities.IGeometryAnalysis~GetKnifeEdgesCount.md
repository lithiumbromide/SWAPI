---
title: "GetKnifeEdgesCount Method (IGeometryAnalysis)"
project: "SOLIDWORKS Utilities API Help"
interface: "IGeometryAnalysis"
member: "GetKnifeEdgesCount"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IGeometryAnalysis~GetKnifeEdgesCount.html"
---

# GetKnifeEdgesCount Method (IGeometryAnalysis)

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
Dim instance As IGeometryAnalysis
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

## Examples

[Analyze Geometry (VBA)](Analyze_Geometry_VB6.htm)

## Remarks

A sharp edge or knife edge is an edge where the angle between two adjacent faces
is acute.

## See Also

[IGeometryAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IGeometryAnalysis.html)
[IGeometryAnalysis Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IGeometryAnalysis_members.html)

## Availability

SOLIDWORKS Utilities API 2004 FCS
