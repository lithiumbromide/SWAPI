---
title: "GetMinTckOnAnalArea Method (IThicknessAnalysis)"
project: "SOLIDWORKS Utilities API Help"
interface: "IThicknessAnalysis"
member: "GetMinTckOnAnalArea"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetMinTckOnAnalArea.html"
---

# GetMinTckOnAnalArea Method (IThicknessAnalysis)

Gets the minimum thickness of the analyzed area.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMinTckOnAnalArea( _
   ByRef lErrorcode As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IThicknessAnalysis
Dim lErrorcode As System.Integer
Dim value As System.Double

value = instance.GetMinTckOnAnalArea(lErrorcode)
```

### C#

```csharp
System.double GetMinTckOnAnalArea(
   out System.int lErrorcode
)
```

### C++/CLI

```cpp
System.double GetMinTckOnAnalArea(
   [Out] System.int lErrorcode
)
```

### Parameters

- `lErrorcode`: Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

### Return Value

Minimum thickness of analyzed area

## VBA Syntax

See [IThicknessAnalysis::GetMinTckOnAnalArea](ms-its:swutilitiesapivb6.chm::/swutilities~IThicknessAnalysis~GetMinTckOnAnalArea.html).

## Examples

[Run Thickness Analysis (VBA)](Run_Thickness_Analysis_VB6.htm)

## See Also

[IThicknessAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis.html)
[IThicknessAnalysis Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis_members.html)
[IThicknessAnalysis::GetAvgWeightedTckOnAnalArea Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetAvgWeightedTckOnAnalArea.html)
[IThicknessAnalysis::GetMaxTckOnAnalArea Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetMaxTckOnAnalArea.html)
[IThicknessAnalysis::GetTotalSurfaceAreaAnalyzed Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetTotalSurfaceAreaAnalyzed.html)

## Availability

SOLIDWORKS Utilities API 2006 FCS
