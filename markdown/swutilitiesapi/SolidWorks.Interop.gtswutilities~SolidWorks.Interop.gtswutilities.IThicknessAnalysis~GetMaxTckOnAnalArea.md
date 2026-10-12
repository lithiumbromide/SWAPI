---
title: "GetMaxTckOnAnalArea Method (IThicknessAnalysis)"
project: "SOLIDWORKS Utilities API Help"
interface: "IThicknessAnalysis"
member: "GetMaxTckOnAnalArea"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetMaxTckOnAnalArea.html"
---

# GetMaxTckOnAnalArea Method (IThicknessAnalysis)

Gets the maximum thickness of the analyzed area.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMaxTckOnAnalArea( _
   ByRef lErrorcode As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IThicknessAnalysis
Dim lErrorcode As System.Integer
Dim value As System.Double

value = instance.GetMaxTckOnAnalArea(lErrorcode)
```

### C#

```csharp
System.double GetMaxTckOnAnalArea(
   out System.int lErrorcode
)
```

### C++/CLI

```cpp
System.double GetMaxTckOnAnalArea(
   [Out] System.int lErrorcode
)
```

### Parameters

- `lErrorcode`: Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

### Return Value

Maximum thickness of analyzed area

## VBA Syntax

See [IThicknessAnalysis::GetMaxTckOnAnalArea](ms-its:swutilitiesapivb6.chm::/swutilities~IThicknessAnalysis~GetMaxTckOnAnalArea.html).

## Examples

[Run Thickness Analysis (VBA)](Run_Thickness_Analysis_VB6.htm)

## See Also

[IThicknessAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis.html)
[IThicknessAnalysis Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis_members.html)
[IThicknessAnalysis::GetAvgWeightedTckOnAnalArea Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetAvgWeightedTckOnAnalArea.html)
[IThicknessAnalysis::GetMinTckOnAnalArea Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetMinTckOnAnalArea.html)
[IThicknessAnalysis::GetTotalSurfaceAreaAnalyzed Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetTotalSurfaceAreaAnalyzed.html)

## Availability

SOLIDWORKS Utilities API 2006 FCS
