---
title: "GetIntervalCount Method (gtcocswThicknessAnalysis)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswThicknessAnalysis"
member: "GetIntervalCount"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswThicknessAnalysis~GetIntervalCount.html"
---

# GetIntervalCount Method (gtcocswThicknessAnalysis)

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
Dim instance As gtcocswThicknessAnalysis
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

## See Also

[gtcocswThicknessAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswThicknessAnalysis.html)
[gtcocswThicknessAnalysis Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswThicknessAnalysis_members.html)

## Availability

SOLIDWORKS Utilities API 2006 FCS
