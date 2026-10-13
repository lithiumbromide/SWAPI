---
title: "GetMaxDeviationfromTargetThickness Method (IThicknessAnalysis)"
project: "SOLIDWORKS Utilities API Help"
interface: "IThicknessAnalysis"
member: "GetMaxDeviationfromTargetThickness"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetMaxDeviationfromTargetThickness.html"
---

# GetMaxDeviationfromTargetThickness Method (IThicknessAnalysis)

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
Dim instance As IThicknessAnalysis
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

## Examples

[Run Thickness Analysis (VBA)](Run_Thickness_Analysis_VB6.htm)

## See Also

[IThicknessAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis.html)
[IThicknessAnalysis Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis_members.html)
[IThicknessAnalysis::GetAnalysisDetails Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetAnalysisDetails.html)
[IThicknessAnalysis::GetIntervalCount Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetIntervalCount.html)

## Availability

SOLIDWORKS Utilities API 2006 FCS
