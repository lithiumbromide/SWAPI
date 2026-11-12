---
title: "SetThicknessAnalysisBody Method (IThicknessAnalysis)"
project: "SOLIDWORKS Utilities API Help"
interface: "IThicknessAnalysis"
member: "SetThicknessAnalysisBody"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~SetThicknessAnalysisBody.html"
---

# SetThicknessAnalysisBody Method (IThicknessAnalysis)

Sets the SOLIDWORKS body in a multibody part to use in the thickness analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetThicknessAnalysisBody( _
   ByVal lpBody2 As Body2 _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IThicknessAnalysis
Dim lpBody2 As Body2
Dim value As System.Integer

value = instance.SetThicknessAnalysisBody(lpBody2)
```

### C#

```csharp
System.int SetThicknessAnalysisBody(
   Body2 lpBody2
)
```

### C++/CLI

```cpp
System.int SetThicknessAnalysisBody(
   Body2^ lpBody2
)
```

### Parameters

- `lpBody2`: SOLIDWORKS body

### Return Value

Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

## VBA Syntax

See [IThicknessAnalysis::SetThicknessAnalysisBody](ms-its:swutilitiesapivb6.chm::/swutilities~IThicknessAnalysis~SetThicknessAnalysisBody.html).

## Remarks

You do not need to use this method if the part is made up of a single solid body.

Use [IThicknessAnalysis::GetThicknessAnalysisBody](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IThicknessAnalysis~GetThicknessAnalysisBody.html) to get the body selected for the thickness analysis.

[IThicknessAnalysis::RunThickAnalysis2](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IThicknessAnalysis~RunThickAnalysis2.html) and [IThicknessAnalysis::RunThinAnalysis2](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IThicknessAnalysis~RunThinAnalysis.html) fail if a body is not set in a multibody part.

## See Also

[IThicknessAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis.html)
[IThicknessAnalysis Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis_members.html)

## Availability

SOLIDWORKS Utilities API 2006 FCS
