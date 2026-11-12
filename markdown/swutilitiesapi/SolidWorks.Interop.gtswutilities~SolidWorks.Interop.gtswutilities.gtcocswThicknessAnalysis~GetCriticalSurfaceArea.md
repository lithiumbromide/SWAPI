---
title: "GetCriticalSurfaceArea Method (gtcocswThicknessAnalysis)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswThicknessAnalysis"
member: "GetCriticalSurfaceArea"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswThicknessAnalysis~GetCriticalSurfaceArea.html"
---

# GetCriticalSurfaceArea Method (gtcocswThicknessAnalysis)

Gets the critical surface area.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCriticalSurfaceArea( _
   ByRef lErrorcode As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswThicknessAnalysis
Dim lErrorcode As System.Integer
Dim value As System.Double

value = instance.GetCriticalSurfaceArea(lErrorcode)
```

### C#

```csharp
System.double GetCriticalSurfaceArea(
   out System.int lErrorcode
)
```

### C++/CLI

```cpp
System.double GetCriticalSurfaceArea(
   [Out] System.int lErrorcode
)
```

### Parameters

- `lErrorcode`: Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

### Return Value

Critical surface area

## VBA Syntax

See [IThicknessAnalysis::GetCriticalSurfaceArea](ms-its:swutilitiesapivb6.chm::/swutilities~IThicknessAnalysis~GetCriticalSurfaceArea.html).

## See Also

[gtcocswThicknessAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswThicknessAnalysis.html)
[gtcocswThicknessAnalysis Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswThicknessAnalysis_members.html)

## Availability

SOLIDWORKS Utilities API 2006 FCS
