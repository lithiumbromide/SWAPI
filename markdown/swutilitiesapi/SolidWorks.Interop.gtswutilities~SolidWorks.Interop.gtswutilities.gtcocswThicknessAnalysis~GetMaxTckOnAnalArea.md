---
title: "GetMaxTckOnAnalArea Method (gtcocswThicknessAnalysis)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswThicknessAnalysis"
member: "GetMaxTckOnAnalArea"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswThicknessAnalysis~GetMaxTckOnAnalArea.html"
---

# GetMaxTckOnAnalArea Method (gtcocswThicknessAnalysis)

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
Dim instance As gtcocswThicknessAnalysis
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

## See Also

[gtcocswThicknessAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswThicknessAnalysis.html)
[gtcocswThicknessAnalysis Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswThicknessAnalysis_members.html)

## Availability

SOLIDWORKS Utilities API 2006 FCS
