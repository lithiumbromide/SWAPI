---
title: "GetAvgWeightedTckOnAnalArea Method (gtcocswThicknessAnalysis)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswThicknessAnalysis"
member: "GetAvgWeightedTckOnAnalArea"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswThicknessAnalysis~GetAvgWeightedTckOnAnalArea.html"
---

# GetAvgWeightedTckOnAnalArea Method (gtcocswThicknessAnalysis)

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
Dim instance As gtcocswThicknessAnalysis
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

## See Also

[gtcocswThicknessAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswThicknessAnalysis.html)
[gtcocswThicknessAnalysis Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswThicknessAnalysis_members.html)

## Availability

SOLIDWORKS Utilities API 2006 FCS
