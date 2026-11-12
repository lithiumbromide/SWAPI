---
title: "GetMaxDeviationfromTargetThickness Method (gtcocswThicknessAnalysis)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswThicknessAnalysis"
member: "GetMaxDeviationfromTargetThickness"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswThicknessAnalysis~GetMaxDeviationfromTargetThickness.html"
---

# GetMaxDeviationfromTargetThickness Method (gtcocswThicknessAnalysis)

Gets the maximum deviation from the target thickness.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMaxDeviationfromTargetThickness( _
   ByRef lErrorcode As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswThicknessAnalysis
Dim lErrorcode As System.Integer
Dim value As System.Double

value = instance.GetMaxDeviationfromTargetThickness(lErrorcode)
```

### C#

```csharp
System.double GetMaxDeviationfromTargetThickness(
   out System.int lErrorcode
)
```

### C++/CLI

```cpp
System.double GetMaxDeviationfromTargetThickness(
   [Out] System.int lErrorcode
)
```

### Parameters

- `lErrorcode`: Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

### Return Value

Maximum deviation from the target thickness

## VBA Syntax

See [IThicknessAnalysis::GetMaxDeviationfromTargetThickness](ms-its:swutilitiesapivb6.chm::/swutilities~IThicknessAnalysis~GetMaxDeviationfromTargetThickness.html).

## See Also

[gtcocswThicknessAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswThicknessAnalysis.html)
[gtcocswThicknessAnalysis Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswThicknessAnalysis_members.html)

## Availability

SOLIDWORKS Utilities API 2006 FCS
