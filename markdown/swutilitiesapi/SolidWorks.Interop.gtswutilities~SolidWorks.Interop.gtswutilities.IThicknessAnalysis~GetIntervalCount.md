---
title: "GetIntervalCount Method (IThicknessAnalysis)"
project: "SOLIDWORKS Utilities API Help"
interface: "IThicknessAnalysis"
member: "GetIntervalCount"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetIntervalCount.html"
---

# GetIntervalCount Method (IThicknessAnalysis)

Gets the number of intervals in the thickness color scale.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetIntervalCount( _
   ByRef lErrorcode As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IThicknessAnalysis
Dim lErrorcode As System.Integer
Dim value As System.Integer

value = instance.GetIntervalCount(lErrorcode)
```

### C#

```csharp
System.int GetIntervalCount(
   out System.int lErrorcode
)
```

### C++/CLI

```cpp
System.int GetIntervalCount(
   [Out] System.int lErrorcode
)
```

### Parameters

- `lErrorcode`: Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

### Return Value

Number of intervals in the thickness color scale

## VBA Syntax

See [IThicknessAnalysis::GetIntervalCount](ms-its:swutilitiesapivb6.chm::/swutilities~IThicknessAnalysis~GetIntervalCount.html).

## Examples

[Run Thickness Analysis (VBA)](Run_Thickness_Analysis_VB6.htm)

## See Also

[IThicknessAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis.html)
[IThicknessAnalysis Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis_members.html)
[IThicknessAnalysis::GetAnalysisDetails Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetAnalysisDetails.html)
[IThicknessAnalysis::GetMaxDeviationfromTargetThickness Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetMaxDeviationfromTargetThickness.html)

## Availability

SOLIDWORKS Utilities API 2006 FCS
