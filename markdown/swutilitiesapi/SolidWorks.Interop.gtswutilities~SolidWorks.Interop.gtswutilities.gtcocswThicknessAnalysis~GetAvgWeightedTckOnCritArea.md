---
title: "GetAvgWeightedTckOnCritArea Method (gtcocswThicknessAnalysis)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswThicknessAnalysis"
member: "GetAvgWeightedTckOnCritArea"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswThicknessAnalysis~GetAvgWeightedTckOnCritArea.html"
---

# GetAvgWeightedTckOnCritArea Method (gtcocswThicknessAnalysis)

Gets the average weighted thickness on the critical area.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAvgWeightedTckOnCritArea( _
   ByRef lErrorcode As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswThicknessAnalysis
Dim lErrorcode As System.Integer
Dim value As System.Double

value = instance.GetAvgWeightedTckOnCritArea(lErrorcode)
```

### C#

```csharp
System.double GetAvgWeightedTckOnCritArea(
   out System.int lErrorcode
)
```

### C++/CLI

```cpp
System.double GetAvgWeightedTckOnCritArea(
   [Out] System.int lErrorcode
)
```

### Parameters

- `lErrorcode`: Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

### Return Value

Average weighted thickness on the critical area

## VBA Syntax

See [IThicknessAnalysis::GetAvgWeightedTckOnCritArea](ms-its:swutilitiesapivb6.chm::/swutilities~IThicknessAnalysis~GetAvgWeightedTckOnCritArea.html).

## See Also

[gtcocswThicknessAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswThicknessAnalysis.html)
[gtcocswThicknessAnalysis Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswThicknessAnalysis_members.html)

## Availability

SOLIDWORKS Utilities API 2006 FCS
