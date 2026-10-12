---
title: "GetTotalSurfaceAreaAnalyzed Method (IThicknessAnalysis)"
project: "SOLIDWORKS Utilities API Help"
interface: "IThicknessAnalysis"
member: "GetTotalSurfaceAreaAnalyzed"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetTotalSurfaceAreaAnalyzed.html"
---

# GetTotalSurfaceAreaAnalyzed Method (IThicknessAnalysis)

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
Dim instance As IThicknessAnalysis
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

## Examples

[Run Thickness Analysis (VBA)](Run_Thickness_Analysis_VB6.htm)

## See Also

[IThicknessAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis.html)
[IThicknessAnalysis Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis_members.html)
[IThicknessAnalysis::GetAvgWeightedTckOnAnalArea Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetAvgWeightedTckOnAnalArea.html)
[IThicknessAnalysis::GetMaxTckOnAnalArea Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetMaxTckOnAnalArea.html)
[IThicknessAnalysis::GetMinTckOnAnalArea Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetMinTckOnAnalArea.html)

## Availability

SOLIDWORKS Utilities API 2006 FCS
