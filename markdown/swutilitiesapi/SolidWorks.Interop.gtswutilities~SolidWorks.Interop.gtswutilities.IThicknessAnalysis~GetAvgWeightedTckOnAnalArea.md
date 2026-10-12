---
title: "GetAvgWeightedTckOnAnalArea Method (IThicknessAnalysis)"
project: "SOLIDWORKS Utilities API Help"
interface: "IThicknessAnalysis"
member: "GetAvgWeightedTckOnAnalArea"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetAvgWeightedTckOnAnalArea.html"
---

# GetAvgWeightedTckOnAnalArea Method (IThicknessAnalysis)

Gets the average weighted thickness on the analyzed area.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAvgWeightedTckOnAnalArea( _
   ByRef lErrorcode As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IThicknessAnalysis
Dim lErrorcode As System.Integer
Dim value As System.Double

value = instance.GetAvgWeightedTckOnAnalArea(lErrorcode)
```

### C#

```csharp
System.double GetAvgWeightedTckOnAnalArea(
   out System.int lErrorcode
)
```

### C++/CLI

```cpp
System.double GetAvgWeightedTckOnAnalArea(
   [Out] System.int lErrorcode
)
```

### Parameters

- `lErrorcode`: Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

### Return Value

Average weighted thickness on analyzed area

## VBA Syntax

See [IThicknessAnalysis::GetAvgWeightedTckOnAnalArea](ms-its:swutilitiesapivb6.chm::/swutilities~IThicknessAnalysis~GetAvgWeightedTckOnAnalArea.html).

## Examples

[Run Thickness Analysis (VBA)](Run_Thickness_Analysis_VB6.htm)

## See Also

[IThicknessAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis.html)
[IThicknessAnalysis Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis_members.html)
[IThicknessAnalysis::GetAvgWeightedTckOnAnalArea Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetAvgWeightedTckOnAnalArea.html)
[IThicknessAnalysis::GetMaxTckOnAnalArea Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetMaxTckOnAnalArea.html)
[IThicknessAnalysis::GetMinTckOnAnalArea Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetMinTckOnAnalArea.html)
[IThicknessAnalysis::GetTotalSurfaceAreaAnalyzed Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetTotalSurfaceAreaAnalyzed.html)
[IThicknessAnalysis::GetAvgWeightedTckOnCritArea Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetAvgWeightedTckOnCritArea.html)

## Availability

SOLIDWORKS Utilities API 2006 FCS
