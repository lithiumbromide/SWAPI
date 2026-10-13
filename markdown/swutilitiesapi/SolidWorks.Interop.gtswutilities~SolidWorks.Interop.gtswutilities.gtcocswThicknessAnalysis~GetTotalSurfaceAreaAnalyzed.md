---
title: "GetTotalSurfaceAreaAnalyzed Method (gtcocswThicknessAnalysis)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswThicknessAnalysis"
member: "GetTotalSurfaceAreaAnalyzed"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswThicknessAnalysis~GetTotalSurfaceAreaAnalyzed.html"
---

# GetTotalSurfaceAreaAnalyzed Method (gtcocswThicknessAnalysis)

Gets the total surface area analyzed.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTotalSurfaceAreaAnalyzed( _
   ByRef lErrorcode As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswThicknessAnalysis
Dim lErrorcode As System.Integer
Dim value As System.Double

value = instance.GetTotalSurfaceAreaAnalyzed(lErrorcode)
```

### C#

```csharp
System.double GetTotalSurfaceAreaAnalyzed(
   out System.int lErrorcode
)
```

### C++/CLI

```cpp
System.double GetTotalSurfaceAreaAnalyzed(
   [Out] System.int lErrorcode
)
```

### Parameters

- `lErrorcode`: Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

### Return Value

Total surface area analyzed

## VBA Syntax

See [IThicknessAnalysis::GetTotalSurfaceAreaAnalyzed](ms-its:swutilitiesapivb6.chm::/swutilities~IThicknessAnalysis~GetTotalSurfaceAreaAnalyzed.html).

## See Also

[gtcocswThicknessAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswThicknessAnalysis.html)
[gtcocswThicknessAnalysis Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswThicknessAnalysis_members.html)

## Availability

SOLIDWORKS Utilities API 2006 FCS
